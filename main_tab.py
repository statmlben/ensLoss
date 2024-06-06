""" ensLoss in tabular datasets"""

# Authors: Ben Dai <bendai@cuhk.edu.hk>
# License: MIT License

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

from loader import TrainData, TestData, openml_data
from base import evaluate, pairwise_ttest
from sklearn.model_selection import KFold
import scipy
from train import Trainer
import plotly.express as px
import plotly as ply

import pingouin as pg
from scipy import stats
import argparse
import wandb
import plotly.graph_objs as go
from plot import line
import sys

## tab models
import tab_models

def main(config, data_id=43969, n_trials=2, wandb_log=True):

    ## wandb log
    if wandb_log:
        wandb.init(project="ensLoss", name=str(data_id)+'-'+config['model']['net'])

    ## Reproducibility
    torch.manual_seed(0)
    random.seed(0)
    np.random.seed(0)

    Acc = {'trial': [], 'loss': [], 'test_acc': [], 'test_auc': []}
    path_={'loss': [], 'epoch': [], 'train_loss': [], 'train_acc': [], 'test_acc': []}

    for h in range(n_trials):

        train_data, test_data = openml_data(data_id=data_id, random_state=h)
        input_shape = train_data.X_data.shape[1]

        train_loader = DataLoader(dataset=train_data, batch_size=config['batch_size'], shuffle=True)
        test_loader = DataLoader(dataset=test_data, batch_size=32)

        ## ensLoss ##
        print('\n-- TRAIN ensLoss --\n')
        model = getattr(models, config['model']['net'])(input_shape=input_shape, **config['model']['args'])
        model.to(config['device'])
        print(model)
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
        model = getattr(models, config['model']['net'])(input_shape=input_shape, **config['model']['args'])
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
        model = getattr(models, config['model']['net'])(input_shape=input_shape, **config['model']['args'])
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
        model = getattr(models, config['model']['net'])(input_shape=input_shape, **config['model']['args'])
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
    out_file = open('out_img.txt', 'a+')
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
    parser.add_argument('-e', '--epoch', default=500, type=int,
                           help='number of epochs to train')
    parser.add_argument('-ID', '--data_id', default=43969, type=int,
                           help='data_id of the dataset')
    parser.add_argument('-R', '--n_trials', default=5, type=int,
                           help='number of trials for the experiments')
    parser.add_argument('--log', default=True, action=argparse.BooleanOptionalAction,
                           help='if save the training process in wandb')
    args = parser.parse_args()

    config = {
            'dataset' : args.data_id,
            'model': {'net': 'TabMLP5', 'args': {'H': 64}},
            'batch_size': args.batch,
            'trainer': {'epochs': args.epoch, 'val_per_epochs': 10}, 
            # 'optimizer': {'lr': 1e-4, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 1./3, 'total_iters': 1}},
            'optimizer': {'lr': 1e-4, 'type': 'SGD', 'weight_decay': 5e-5, 
                          'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': args.epoch}},
            'device': torch.device("cuda:0" if torch.cuda.is_available() else "cpu")}

    data_id = args.data_id
    n_trials = args.n_trials
    wandb_log = args.log

    main(config=config, data_id=data_id, n_trials=n_trials, wandb_log=wandb_log)

# Tabular data learning benchmark (MLP:1e-4)
# electricity (45.3k x 9): 44120 (bad)
# house_16H (13.5k x 17): 44123 (good)
# phoneme (3.17k x 6): 43973 (fair)
# MiniBooNE (72998, 50): 44128 (good)
# MagicTelescope (13376, 10): 44125 (good)
# higgs (98k x 29): 23512 (slightly good)
# eye_movements (7.61k x 24): 44157 (slightly good)
# jannis (57.6k x 55): 45021 (slightly good)
# credit (16.7k x 11): 45024 (good)
# california (20.6k x 9): 45025 (good)

# Tabular data learning benchmark (MLP5:1e-5)
# electricity (45.3k x 9): 44120 (good)
# house_16H (13.5k x 17): 44123 (good)
# phoneme (3.17k x 6): 43973 (fair)
# MiniBooNE (72998, 50): 44128 (good)
# MagicTelescope (13376, 10): 44125 (fair)
# higgs (98k x 29): 23512 (good)
# eye_movements (7.61k x 24): 44157 (fair)
# jannis (57.6k x 55): 45021 (good)
# credit (16.7k x 11): 45024 (good)
# california (20.6k x 9): 45025 (good)

# Tabular data learning benchmark (1e-5)
# electricity (45.3k x 9): 44120 (bad)
# house_16H (13.5k x 17): 44123 (good)
# phoneme (3.17k x 6): 43973 (fair)
# MiniBooNE (72998, 50): 44128 (fair - good)
# MagicTelescope (13376, 10): 44125 (good)
# higgs (98k x 29): 23512 (good)
# eye_movements (7.61k x 24): 44157 (fair, potential good)
# jannis (57.6k x 55): 45021 (good)
# credit (16.7k x 11): 45024 (good)
# california (20.6k x 9): 45025 (good)

