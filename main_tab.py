""" ensLoss in tabular datasets"""

# Authors: Ben Dai <bendai@cuhk.edu.hk>
# License: MIT License

## basics
import numpy as np
import pandas as pd
import seaborn as sns
import random

## dataloader
import torch
from torch.utils.data import Dataset, DataLoader
from loader import TrainData, TestData, openml_data

## train
from train import Trainer

## result
from base import pairwise_ttest, line

## args; print config, figure, out
import argparse
import wandb
import sys
import pprint

## tab models
import tab_models

def main(config, data_id=43969, n_trials=5, wandb_log=True):

    ## wandb log
    if wandb_log:
        wandb.init(project="ensLoss-tab", name=str(data_id)+'-'+config['model']['net'])

    ## Reproducibility
    torch.manual_seed(0)
    random.seed(0)
    np.random.seed(0)

    Acc = {'trial': [], 'loss': [], 'test_acc': [], 'test_auc': []}
    path_={'loss': [], 'epoch': [], 'train_acc': [], 'test_acc': []}

    for h in range(n_trials):

        train_data, test_data = openml_data(data_id=data_id, random_state=h)
        input_shape = train_data.X_data.shape[1]

        train_loader = DataLoader(dataset=train_data, batch_size=config['batch_size'], shuffle=True)
        test_loader = DataLoader(dataset=test_data, batch_size=32)

        ## ensLoss ##
        print('\n-- TRAIN ensLoss --\n')
        model = getattr(tab_models, config['model']['net'])(input_shape=input_shape, **config['model']['args'])
        model.to(config['device'])
        print(model)
        trainer_ = Trainer(model=model, loss='ensLoss', period=config['ensLoss_per_epochs'],
                            config=config, device=config['device'],
                            train_loader=train_loader, val_loader=test_loader)
        path_, acc_test, auc_test = trainer_.train(path_)
        Acc['trial'].append(h)
        Acc['loss'].append('ensLoss')
        Acc['test_acc'].append(acc_test)
        Acc['test_auc'].append(auc_test)

        ## BCE loss ##
        print('\n-- TRAIN BCE --\n')
        model = getattr(tab_models, config['model']['net'])(input_shape=input_shape, **config['model']['args'])
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
        model = getattr(tab_models, config['model']['net'])(input_shape=input_shape, **config['model']['args'])
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
        model = getattr(tab_models, config['model']['net'])(input_shape=input_shape, **config['model']['args'])
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
    out_file = open('out_tab.txt', 'a+')
    sys.stdout = out_file

    print('\n#### Data ID: %s - model: %s ####\n' %(data_id, config['model']['net']))
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
                   "perf": Acc.groupby('loss')['test_acc'].agg(['mean', 'std']),
                   "path": path_,
                   "perf_table": Acc,
                   "p_less": p_less,
                   "p_greater": p_greater,
                   "p_less_auc": p_less_auc,
                   "p_greater_auc": p_greater_auc,
                   })
        wandb.finish()

    out_file.close()
    sys.stdout = orig_stdout

if __name__=='__main__':
    # PARSE THE ARGS
    parser = argparse.ArgumentParser(description='ensLoss Training')
    # parser.add_argument('-D', '--depth', default=1, type=int,
    #                     help='depth of the neural network')
    # parser.add_argument('-H', '--width', default=128, type=int,
    #                        help='width of the neural network')
    parser.add_argument('-B', '--batch', default=128, type=int,
                           help='batch size of the training set')
    parser.add_argument('-e', '--epoch', default=300, type=int,
                           help='number of epochs to train')
    parser.add_argument('-ID', '--data_id', default=43969, type=int,
                           help='data_id of the dataset')
    parser.add_argument('-N', '--net', default="TabMLP3", type=str,
                           help='the neural net of the classification')
    parser.add_argument('-R', '--n_trials', default=5, type=int,
                           help='number of trials for the experiments')
    parser.add_argument('--log', default=True, action=argparse.BooleanOptionalAction,
                           help='if save the training process in wandb')
    args = parser.parse_args()

    config = {
            'dataset' : args.data_id,
            'model': {'net': args.net, 'args': {}},
            'batch_size': args.batch,
            'save_model': False,
            'ensLoss_per_epochs': -1,
            'trainer': {'epochs': args.epoch, 'val_per_epochs': 10}, 
            'optimizer': {'lr': 1e-4, 'type': 'SGD', 'weight_decay': 5e-6, 
                          'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': args.epoch}},
            'device': torch.device("cuda:0" if torch.cuda.is_available() else "cpu")}

    data_id = args.data_id
    n_trials = args.n_trials
    wandb_log = args.log

    main(config=config, data_id=data_id, n_trials=n_trials, wandb_log=wandb_log)

# python main_tab.py -B=128 -e=300 -ID=1142 -N='TabMLP1' -R=5 --no-log

## experiment on Aug 14
# Bioresponse: 4134
# guillermo: 41159
# riccardo: 41161
# hiva_agnostic: 1039
# christine: 41142

## OVA Datasets
# OVA_Breast: 1128
# OVA_Uterus: 1138
# OVA_Ovary: 1166
# OVA_Kidney: 1134
# OVA_Lung: 1130
# OVA_Omentum: 1139
# OVA_Colon: 1161
# OVA_Endometrium: 1142
# OVA_Prostate: 1146