"""ensLoss in text datasets"""

# Authors: Ben Dai 
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
from train import Trainer, Trainer_txt

## args; print config, figure, out
import argparse
import pprint
import sys
from base import pairwise_ttest, line

## log to wandb
import wandb

## text models
import transformers

def main(config, filename='SST2', n_trials=5, wandb_log=False):

    ## wandb log
    if wandb_log:
        wandb.init(project="ensLoss-txt", name=filename+'-'+config['model']['net'])

    ## Reproducibility
    torch.manual_seed(0)
    random.seed(0)
    np.random.seed(0)

    Acc = {'trial': [], 'loss': [], 'test_acc': [], 'test_auc': []}
    path_={'loss': [], 'epoch': [], 'train_acc': [], 'test_acc': []}

    for h in range(n_trials):

        model = getattr(text_models, config['model']['net'])()
        model.to(config['device'])

        train_data, test_data = text_data(name='SST2', tokenizer=model.tokenizer)
        train_loader = DataLoader(train_data, shuffle=True, batch_size=config['batch_size'])
        test_loader = DataLoader(test_data, shuffle=False, batch_size=config['batch_size'])
        ## get some random training data
        # dataiter = iter(train_loader)
        # X_batch, y_batch = next(dataiter)

        ## ensLoss ##        
        print('\n-- TRAIN ensLoss --\n')
        
        if h==0:
            ## print the model in the first trial
            print(model)
        
        trainer_ = Trainer_txt(model=model, loss='ensLoss', 
                            config=config, device=config['device'],
                            train_loader=train_loader, val_loader=test_loader)
        path_, acc_test, auc_test = trainer_.train(path_)
        Acc['trial'].append(h)
        Acc['loss'].append('ensLoss')
        Acc['test_acc'].append(acc_test)
        Acc['test_auc'].append(auc_test)

        ## BCE loss ##
        print('\n-- TRAIN BCE --\n')
        model = getattr(text_models, config['model']['net'])()
        # model = getattr(img_models, config['model']['net'])(num_classes=1)
        model.to(config['device'])

        trainer_ = Trainer_txt(model=model, loss='BCELoss',
                            config=config, device=config['device'],
                            train_loader=train_loader, val_loader=test_loader)
        path_, acc_test, auc_test = trainer_.train(path_)
        Acc['trial'].append(h)
        Acc['loss'].append('BCE')
        Acc['test_acc'].append(acc_test)
        Acc['test_auc'].append(auc_test)

        # BCE+ensLoss loss ##
        # print('\n-- TRAIN BCE + ensLoss --\n')
        # model = getattr(text_models, config['model']['net'])()
        # # model = getattr(img_models, config['model']['net'])(num_classes=1)
        # model.to(config['device'])

        # trainer_ = Trainer_txt(model=model, loss='BCELoss',
        #                     config=config, device=config['device'],
        #                     train_loader=train_loader, val_loader=test_loader, 
        #                     seq_epoch=int(config['trainer']['epochs']*0.6))
        
        # path_, acc_test, auc_test = trainer_.train(path_)
        # Acc['trial'].append(h)
        # Acc['loss'].append('BCE+ensLoss')
        # Acc['test_acc'].append(acc_test)
        # Acc['test_auc'].append(auc_test)

        ## Hinge loss ##
        print('\n-- TRAIN Hinge --\n')
        model = getattr(text_models, config['model']['net'])()
        # model = getattr(transformers, config['model']['net']).from_pretrained(config['model']['pretrain'], 
        #                                                                     num_labels=1, 
        #                                                                     return_dict=True)
        model.to(config['device'])

        trainer_ = Trainer_txt(model=model, loss='Hinge', 
                            config=config, device=config['device'],
                            train_loader=train_loader, val_loader=test_loader)
        path_, acc_test, auc_test = trainer_.train(path_)
        Acc['trial'].append(h)
        Acc['loss'].append('Hinge')
        Acc['test_acc'].append(acc_test)
        Acc['test_auc'].append(auc_test)

        # ## Hinge + ensLoss loss ##
        # print('\n-- TRAIN Hinge + ensLoss --\n')
        # model = getattr(text_models, config['model']['net'])()
        # model.to(config['device'])

        # trainer_ = Trainer_txt(model=model, loss='Hinge', 
        #                     config=config, device=config['device'],
        #                     train_loader=train_loader, val_loader=test_loader,
        #                     seq_epoch=int(config['trainer']['epochs']*0.6))
        # path_, acc_test, auc_test = trainer_.train(path_)
        # Acc['trial'].append(h)
        # Acc['loss'].append('Hinge+ensLoss')
        # Acc['test_acc'].append(acc_test)
        # Acc['test_auc'].append(auc_test)

        ## EXP loss ##
        print('\n-- TRAIN EXP --\n')
        model = getattr(text_models, config['model']['net'])()
        model.to(config['device'])

        trainer_ = Trainer_txt(model=model, loss='EXP', 
                            config=config, device=config['device'],
                            train_loader=train_loader, val_loader=test_loader)
        path_, acc_test, auc_test = trainer_.train(path_)
        Acc['trial'].append(h)
        Acc['loss'].append('EXP')
        Acc['test_acc'].append(acc_test)
        Acc['test_auc'].append(auc_test)

        # ## EXP+ensLoss loss ##
        # print('\n-- TRAIN EXP+ensLoss --\n')
        # model = getattr(text_models, config['model']['net'])()
        # model.to(config['device'])

        # trainer_ = Trainer_txt(model=model, loss='EXP', 
        #                     config=config, device=config['device'],
        #                     train_loader=train_loader, val_loader=test_loader,
        #                     seq_epoch=int(config['trainer']['epochs']*0.6))
        # path_, acc_test, auc_test = trainer_.train(path_)
        # Acc['trial'].append(h)
        # Acc['loss'].append('EXP+ensLoss')
        # Acc['test_acc'].append(acc_test)
        # Acc['test_auc'].append(auc_test)

    path_ = pd.DataFrame(path_)
    Acc = pd.DataFrame(Acc)
    
    # Plot
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

    p_less_auc = pairwise_ttest(df=Acc, val_col='test_auc', group_col='loss', alternative='less').round(5)
    p_less_auc = p_less_auc[p_less_auc['B'] == 'ensLoss']

    p_greater_auc = pairwise_ttest(df=Acc, val_col='test_auc', group_col='loss', alternative='greater').round(5)
    p_greater_auc = p_greater_auc[p_greater_auc['B'] == 'ensLoss']

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

    print(p_less_auc.round(4).to_markdown())
    print('\n')
    print(p_greater_auc.round(4).to_markdown())

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
    parser = argparse.ArgumentParser(description='ensLoss Training')
    parser.add_argument('-B', '--batch', default=32, type=int,
                           help='batch size of the training set')
    parser.add_argument('-e', '--epoch', default=50, type=int,
                           help='number of epochs to train')
    parser.add_argument('-F', '--filename', default="SST2", type=str,
                           help='filename of the dataset')
    parser.add_argument('-N', '--net', default="AlbertModel", type=str,
                           help='the transformer model of the text classification')
    # parser.add_argument('-PT', '--pretrain', default="albert-base-v1", type=str,
    #                        help='the pre-trained models for transformer')
    parser.add_argument('-R', '--n_trials', default=5, type=int,
                           help='number of trials for the experiments')
    parser.add_argument('--log', default=True, action=argparse.BooleanOptionalAction,
                           help='if save the training process in wandb')
    args = parser.parse_args()

    config = {
            'dataset' : args.filename,
            'model': {'net': 'BiLSTM'},
            'save_model': False,
            'batch_size': args.batch,
            'ensLoss_per_epochs': -1,
            'trainer': {'epochs': args.epoch, 'val_per_epochs': 5},
            'optimizer': {'lr': 2e-5, 'type': 'AdamW', 'weight_decay': 1e-5,
                          'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': args.epoch}},
            'device': torch.device("cuda:0" if torch.cuda.is_available() else "cpu")}

    filename = args.filename
    n_trials = args.n_trials
    wandb_log = args.log
    config['model']['net'] = args.net
    # config['model']['pretrain'] = args.pretrain

    ## for a binary classification dataset
    main(config=config, filename=filename, n_trials=n_trials, wandb_log=wandb_log)

## text dataset
# SST2
# https://github.com/Doragd/Text-Classification-PyTorch
# https://pytorch.org/text/main/tutorials/sst2_classification_non_distributed.html

# python main_text.py -e=50 -B=32 -N="BiLSTM" -F="SST2" -R=5 --no-log

## Candidate Models and Pretrain
# BertForSequenceClassification + bert-base-uncased
# AlbertForSequenceClassification + albert-base-v2
# FlaubertForSequenceClassification + flaubert/flaubert_small_cased

## References
## pre-train models: https://huggingface.co/transformers/v3.3.1/pretrained_models.html
## pytorch-sentiment-classification  https://github.com/clairett/pytorch-sentiment-classification
## other small models: https://github.com/FreedomIntelligence/TextClassificationBenchmark
## more models: https://github.com/shayneobrien/sentiment-classification/tree/master/src
## GLUE benchmark: 
## https://openreview.net/pdf?id=rJ4km2R5t7
## https://gluebenchmark.com/leaderboard
