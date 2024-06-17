"""ensLoss in text datasets"""

# Authors: Ben Dai <bendai@cuhk.edu.hk>
# License: MIT License

## basics
import numpy as np
import pandas as pd
import random
import torch
from itertools import combinations

## dataloader
from loader import openml_data, img_data, text_data
from torch.utils.data import DataLoader

## models
import text_models

## Train
from train import Trainer

## args; print config, figure, out
import argparse
import pprint
import sys
from base import pairwise_ttest, line

## log to wandb
import wandb

def main(config, filename='SST2', n_trials=5, wandb_log=False):

    ## wandb log
    if wandb_log:
        wandb.init(project="ensLoss-txt", name=filename+'-'+config['model']['net'])

    ## Reproducibility
    torch.manual_seed(0)
    random.seed(0)
    np.random.seed(0)

    Acc = {'trial': [], 'loss': [], 'test_acc': [], 'test_auc': []}
    path_={'loss': [], 'epoch': [], 'train_loss': [], 'train_acc': [], 'test_acc': []}

    for h in range(n_trials):

        train_loader, test_loader = text_data(name='SST2', batch=config['batch_size'])

        ## ensLoss ##
        model = getattr(img_models, config['model']['net'])(num_classes=1)
        model.to(config['device'])

        if h==0:
            ## print the model in the first trial
            print(model)

        print('\n-- TRAIN ensLoss --\n')
        
        trainer_ = Trainer(model=model, loss='ensLoss', 
                            config=config, device=config['device'],
                            train_loader=train_loader, val_loader=test_loader)
        path_, acc_test, auc_test = trainer_.train(path_)
        Acc['trial'].append(h)
        Acc['loss'].append('ensLoss')
        Acc['test_acc'].append(acc_test)
        Acc['test_auc'].append(auc_test)

        ## BCE loss ##
        print('\n-- TRAIN BCE --\n')
        model = getattr(img_models, config['model']['net'])(num_classes=1)
        model.to(config['device'])

        trainer_ = Trainer(model=model, loss='BCELoss',
                            config=config, device=config['device'],
                            train_loader=train_loader, val_loader=test_loader)
        path_, acc_test, auc_test = trainer_.train(path_)
        Acc['trial'].append(h)
        Acc['loss'].append('BCE')
        Acc['test_acc'].append(acc_test)
        Acc['test_auc'].append(auc_test)

        ## Hinge loss ##
        print('\n-- TRAIN Hinge --\n')
        model = getattr(img_models, config['model']['net'])(num_classes=1)
        model.to(config['device'])

        trainer_ = Trainer(model=model, loss='Hinge', 
                            config=config, device=config['device'],
                            train_loader=train_loader, val_loader=test_loader)
        path_, acc_test, auc_test = trainer_.train(path_)
        Acc['trial'].append(h)
        Acc['loss'].append('Hinge')
        Acc['test_acc'].append(acc_test)
        Acc['test_auc'].append(auc_test)

        ## EXP loss ##
        print('\n-- TRAIN EXP --\n')
        model = getattr(img_models, config['model']['net'])(num_classes=1)
        model.to(config['device'])

        trainer_ = Trainer(model=model, loss='EXP', 
                            config=config, device=config['device'],
                            train_loader=train_loader, val_loader=test_loader)
        path_, acc_test, auc_test = trainer_.train(path_)
        Acc['trial'].append(h)
        Acc['loss'].append('EXP')
        Acc['test_acc'].append(acc_test)
        Acc['test_auc'].append(auc_test)

    path_ = pd.DataFrame(path_)
    Acc = pd.DataFrame(Acc)
    
    # Plot
    path_ = path_.drop('train_loss', axis=1)
    mean_pd = path_.groupby(['epoch', 'loss'], as_index=False).mean()
    mean_pd = mean_pd.melt(id_vars=['epoch', 'loss'], var_name='type', value_name='mean')
    std_pd = path_.groupby(['epoch', 'loss'], as_index=False).std()
    std_pd = std_pd.melt(id_vars=['epoch', 'loss'], var_name='type', value_name='std')

    std_pd['std'] = std_pd['std'] / np.sqrt(n_trials)

    path_stat = pd.merge(mean_pd, std_pd, on=['epoch', 'loss', 'type'], suffixes=("", ""))

    fig = line(
        data_frame = path_stat,
        x = 'epoch',
        y = 'mean',
        error_y = 'std',
        error_y_mode = 'band',
        color = 'loss',
        line_dash='type',
        line_dash_map={'test_acc': 'solid', 'train_acc': 'dot'},
        title = f'Ave Test Acc in Epochs',
    )
    # fig.show()

    # Hypothesis Testing    
    p_less = pairwise_ttest(df=Acc, val_col='test_acc', group_col='loss', alternative='less').round(5)
    p_less = p_less[p_less['B'] == 'ensLoss']

    p_greater = pairwise_ttest(df=Acc, val_col='test_acc', group_col='loss', alternative='greater').round(5)
    p_greater = p_greater[p_greater['B'] == 'ensLoss']

    res_acc = Acc.groupby('loss').agg({'test_acc': ['mean', 'std']})
    res_acc[('test_acc', 'std')] /= np.sqrt(n_trials)
    res_acc = res_acc.T.round(4)

    res_auc = Acc.groupby('loss').agg({'test_auc': ['mean', 'std']})
    res_auc[('test_auc', 'std')] /= np.sqrt(n_trials)
    res_auc = res_auc.T.round(4)

    ## Save outcome
    orig_stdout = sys.stdout
    out_file = open('out_text.txt', 'a+')
    sys.stdout = out_file

    print('\n#### %s - model: %s ####\n' %(filename, config['model']['net']))
    # print('\n Step Size: %s \n' %config['optimizer'])
    print('\n-- CONFIG --\n')
    pprint.pprint(config, width=1)

    print('\n-- Performance --\n')
    print((res_acc.round(4)).to_markdown())
    print('\n')
    print((res_auc.round(4)).to_markdown())

    print('\n-- Testing --\n')
    print(p_less.round(4).to_markdown())
    print('\n')
    print(p_greater.round(4).to_markdown())

    if wandb_log:
        wandb.log({"test_acc_curve": fig,
                   "perf": Acc.groupby('loss', as_index=False)['test_acc'].agg(['mean', 'std']),
                   "path": path_,
                   "perf_table": Acc,
                   "p_less": p_less,
                   "p_greater": p_greater,
                   })
        wandb.finish()
        
    sys.stdout.close()

if __name__=='__main__':
    # PARSE THE ARGS
    parser = argparse.ArgumentParser(description='eLOTO Training')
    parser.add_argument('-B', '--batch', default=128, type=int,
                           help='batch size of the training set')
    parser.add_argument('-e', '--epoch', default=200, type=int,
                           help='number of epochs to train')
    parser.add_argument('-F', '--filename', default="CIFAR", type=str,
                           help='filename of the dataset')
    parser.add_argument('-N', '--net', default="ResNet50", type=str,
                           help='the neural net of the classification')
    parser.add_argument('-R', '--n_trials', default=5, type=int,
                           help='number of trials for the experiments')
    parser.add_argument('--log', default=True, action=argparse.BooleanOptionalAction,
                           help='if save the training process in wandb')
    args = parser.parse_args()

    config = {
            'dataset' : args.filename,
            'model': {'net': 'ResNet50'},
            'save_model': True,
            'batch_size': args.batch,
            'trainer': {'epochs': args.epoch, 'val_per_epochs': 5},
            'optimizer': {'lr': 1e-3, 'type': 'SGD', 
                          'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': args.epoch}},
            'device': torch.device("cuda:0" if torch.cuda.is_available() else "cpu")}

    filename = args.filename
    n_trials = args.n_trials
    wandb_log = args.log
    config['model']['net'] = args.net

    ## for a binary classification dataset
    main(config=config, filename=filename, n_trials=n_trials, wandb_log=wandb_log)

## text dataset
# SST2
# https://github.com/Doragd/Text-Classification-PyTorch
# https://pytorch.org/text/main/tutorials/sst2_classification_non_distributed.html

# IMDB
# https://github.com/JustinCharbonneau/IMDB-Sentiment-Benchmark


# python main_image.py -B=128 -e=100 -F="SST2" -R=5 --log