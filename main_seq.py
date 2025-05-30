"""ensLoss with sequential training"""

# Authors: Ben Dai 
# License: MIT License

## basics
import numpy as np
import pandas as pd
import random
import torch
from itertools import combinations

## dataloader
from loader import openml_data, img_data
from torch.utils.data import DataLoader

## models
import img_models

## Train
from train import Trainer, Trainer_seq

## args; print config, figure, out
import argparse
import pprint
import sys
from base import pairwise_ttest, line

## log to wandb
import wandb

def main(config, filename='PCam', n_trials=5, wandb_log=False):

    ## wandb log
    if wandb_log:
        wandb.init(project="ensLoss-seq", name=filename+'-'+config['model']['net'])

    ## Reproducibility
    torch.manual_seed(0)
    random.seed(0)
    np.random.seed(0)

    Acc = {'trial': [], 'loss': [], 'test_acc': [], 'test_auc': []}
    path_={'method': [], 'loss': [], 'epoch': [], 'train_acc': [], 'test_acc': []}

    for h in range(n_trials):

        train_data, test_data = img_data(name=filename)

        train_loader = DataLoader(dataset=train_data, batch_size=config['batch_size'], shuffle=True)
        test_loader = DataLoader(dataset=test_data, batch_size=32)

        ## get some random training data
        # dataiter = iter(train_loader)
        # X_batch, y_batch = next(dataiter)

        ## ensLoss ##
        # if 'ensLoss' in config['loss_list']:
        #     model = getattr(img_models, config['model']['net'])(num_classes=1)
        #     model.to(config['device'])

        #     if h==0:
        #         ## print the model in the first trial
        #         print(model)

        #     print('\n-- TRAIN ensLoss --\n')
            
        #     trainer_ = Trainer(model=model, loss='ensLoss', period=config['ensLoss_per_epochs'],
        #                         config=config, device=config['device'], 
        #                         train_loader=train_loader, val_loader=test_loader)
        #     path_, acc_test, auc_test = trainer_.train(path_)
        #     Acc['trial'].append(h)
        #     Acc['loss'].append('ensLoss')
        #     Acc['test_acc'].append(acc_test)
        #     Acc['test_auc'].append(auc_test)

        # BCE loss ##
        if 'BCE' in config['loss_list']:
            print('\n-- TRAIN BCE --\n')
            model = getattr(img_models, config['model']['net'])(num_classes=1)
            model.to(config['device'])
            
            ## Stage 1 train: BCE loss
            trainer_ = Trainer(model=model, loss='BCELoss',
                                config=config, device=config['device'],
                                train_loader=train_loader, val_loader=test_loader)

            path_, acc_test, auc_test = trainer_.train(path_)
            torch.save(model.state_dict(), './save/seq/seq_model.pt')
            model.load_state_dict(torch.load('./save/seq/seq_model.pt', weights_only=True))

            ## Stage 2 train: ensloss
            trainer_seq = Trainer_seq(model=model, loss='ensLoss',
                                config=config, device=config['device'],
                                train_loader=train_loader, val_loader=test_loader)
            
            path_, acc_test, auc_test = trainer_seq.train(path_)
            path_['method'].extend(['BCE+ensLoss']*int((config['trainer']['epochs'] + config['trainer']['seq_epochs']) / config['trainer']['val_per_epochs']))

            Acc['trial'].append(h)
            Acc['loss'].append('BCE+ensLoss')
            Acc['test_acc'].append(acc_test)
            Acc['test_auc'].append(auc_test)

    #     # Hinge loss ##
    #     if 'Hinge' in config['loss_list']:
    #         print('\n-- TRAIN Hinge --\n')
    #         model = getattr(img_models, config['model']['net'])(num_classes=1)
    #         model.to(config['device'])

    #         trainer_ = Trainer_seq(model=model, loss='Hinge', 
    #                             config=config, device=config['device'],
    #                             train_loader=train_loader, val_loader=test_loader)
    #         path_, acc_test, auc_test = trainer_.train(path_)
    #         Acc['trial'].append(h)
    #         Acc['loss'].append('Hinge+ensLoss')
    #         Acc['test_acc'].append(acc_test)
    #         Acc['test_auc'].append(auc_test)

    # path_ = pd.DataFrame(path_)
    # Acc = pd.DataFrame(Acc)
    
    # # Plot
    # mean_pd = path_.groupby(['epoch', 'loss'], as_index=False).mean()
    # mean_pd = mean_pd.melt(id_vars=['epoch', 'loss'], var_name='type', value_name='mean')
    # std_pd = path_.groupby(['epoch', 'loss'], as_index=False).std()
    # std_pd = std_pd.melt(id_vars=['epoch', 'loss'], var_name='type', value_name='std')

    # std_pd['std'] = std_pd['std'] / np.sqrt(n_trials)

    # path_stat = pd.merge(mean_pd, std_pd, on=['epoch', 'loss', 'type'], suffixes=("", ""))

    # fig = line(
    #     data_frame = path_stat,
    #     x = 'epoch',
    #     y = 'mean',
    #     error_y = 'std',
    #     error_y_mode = 'band',
    #     color = 'loss',
    #     line_dash='type',
    #     line_dash_map={'test_acc': 'solid', 'train_acc': 'dot'},
    #     title = f'Ave Test Acc in Epochs',
    # )
    # # fig.show()

    # # Hypothesis Testing
    # try:
    #     p_less = pairwise_ttest(df=Acc, val_col='test_acc', group_col='loss', alternative='less').round(5)
    #     p_less = p_less[p_less['B'] == 'ensLoss']

    #     p_greater = pairwise_ttest(df=Acc, val_col='test_acc', group_col='loss', alternative='greater').round(5)
    #     p_greater = p_greater[p_greater['B'] == 'ensLoss']

    #     p_less_auc = pairwise_ttest(df=Acc, val_col='test_auc', group_col='loss', alternative='less').round(5)
    #     p_less_auc = p_less_auc[p_less_auc['B'] == 'ensLoss']

    #     p_greater_auc = pairwise_ttest(df=Acc, val_col='test_auc', group_col='loss', alternative='greater').round(5)
    #     p_greater_auc = p_greater_auc[p_greater_auc['B'] == 'ensLoss']
    # except:
    #     pass

    # res_acc = Acc.groupby('loss').agg({'test_acc': ['mean', 'std']})
    # res_acc[('test_acc', 'std')] /= np.sqrt(n_trials)
    # res_acc = res_acc.T.round(4)

    # res_auc = Acc.groupby('loss').agg({'test_auc': ['mean', 'std']})
    # res_auc[('test_auc', 'std')] /= np.sqrt(n_trials)
    # res_auc = res_auc.T.round(4)

    # ## Save outcome
    # orig_stdout = sys.stdout
    # out_file = open('out_seq.txt', 'a+')
    # sys.stdout = out_file

    # print('\n#### %s - model: %s ####\n' %(filename, config['model']['net']))
    # # print('\n Step Size: %s \n' %config['optimizer'])
    # print('\n-- CONFIG --\n')
    # pprint.pprint(config, width=1)

    # print('\n-- Performance --\n')
    # print((res_acc.round(4)).to_markdown())
    # print('\n')
    # print((res_auc.round(4)).to_markdown())

    # print('\n-- Testing --\n')
    # print(p_less.round(4).to_markdown())
    # print('\n')
    # print(p_greater.round(4).to_markdown())

    # print(p_less_auc.round(4).to_markdown())
    # print('\n')
    # print(p_greater_auc.round(4).to_markdown())

    # if wandb_log:
    #     wandb.log({"test_acc_curve": fig,
    #                "perf": Acc.groupby('loss')['test_acc'].agg(['mean', 'std']),
    #                "path": path_,
    #                "perf_table": Acc,
    #                "p_less": p_less,
    #                "p_greater": p_greater,
    #                "p_less_auc": p_less_auc,
    #                "p_greater_auc": p_greater_auc,
    #                })
    #     wandb.finish()

    # out_file.close()
    # sys.stdout = orig_stdout

if __name__=='__main__':
    # PARSE THE ARGS
    parser = argparse.ArgumentParser(description='ensLoss sequential Training')
    parser.add_argument('-B', '--batch', default=128, type=int,
                           help='batch size of the training set')
    parser.add_argument('-e', '--epoch', default=50, type=int,
                           help='number of epochs to train')
    parser.add_argument('-F', '--filename', default="CIFAR", type=str,
                           help='filename of the dataset')
    parser.add_argument('-N', '--net', default="ResNet50", type=str,
                           help='the neural net of the classification')
    parser.add_argument('-SE', '--seq_epoch', default=100, type=int,
                           help='number of ens epochs to train')
    parser.add_argument('-R', '--n_trials', default=5, type=int,    
                           help='number of trials for the experiments')
    parser.add_argument('--log', default=True, action=argparse.BooleanOptionalAction,
                           help='if save the training process in wandb')
    args = parser.parse_args()

    config = {
            'loss_list': ['BCE', 'Hinge'],
            'dataset' : args.filename,
            'model': {'net': args.net},
            'save_model': False,
            'batch_size': args.batch,
            'ensLoss_per_epochs': -1,
            'trainer': {'epochs': args.epoch, 'seq_epochs': args.seq_epoch, 'val_per_epochs': 5},
            'optimizer': {'lr': 1e-3, 'type': 'SGD', 'weight_decay': 5e-4, 
                          'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': args.epoch+args.seq_epoch}},
            'device': torch.device("cuda:0" if torch.cuda.is_available() else "cpu")}

    filename = args.filename
    n_trials = args.n_trials
    wandb_log = args.log

    if filename == 'CIFAR':
        ## for a multi-class classification dataset
        ## Currently, we only support experiments that are based on the CIFAR10 dataset.
        for (u,v) in combinations(range(10), 2):
            filename_tmp = filename+str(u)+str(v)
            main(config=config, filename=filename_tmp, n_trials=n_trials, wandb_log=wandb_log)
    
    else:
        ## for a binary classification dataset
        main(config=config, filename=filename, n_trials=n_trials, wandb_log=wandb_log)

## Image dataset
# CIFAR10: https://www.cs.toronto.edu/~kriz/cifar.html
# PCam: https://github.com/basveeling/pcam

# python main_seq.py -B=128 -e=100 -F="PCam" -R=5 --log
# python main_seq.py -B=128 -e=200 -F="CIFAR35" -N="VGG16" -R=1 --no-log