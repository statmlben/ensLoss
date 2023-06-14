""" COTO in tabular datasets"""

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
from model import BinaryClassification
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
from tab_transformer_pytorch import TabTransformer


def main(config, D, H, data_id=43969, n_trials=2, wandb_log=True):

    ## wandb log
    if wandb_log:
        wandb.init(project="COTO", name=str(data_id)+'-'+str(D)+'-'+str(H))

    ## Reproducibility
    torch.manual_seed(0)
    random.seed(0)
    np.random.seed(0)

    Acc = {'trial': [], 'loss': [], 'test_acc': []}
    path_={'loss': [], 'epoch': [], 'train_loss': [], 'train_acc': [], 'test_acc': []}

    for h in range(n_trials):

        train_data, test_data = openml_data(data_id=data_id, random_state=h)
        input_shape = train_data.X_data.shape[1]

        train_loader = DataLoader(dataset=train_data, batch_size=config['batch_size'], shuffle=True)
        test_loader = DataLoader(dataset=test_data, batch_size=32)

        ## COTO ##
        print('\n-- TRAIN COTO --\n')
        model = BinaryClassification(input_shape=input_shape, H=H, D=D)
        model.to(config['device'])

        trainer_ = Trainer(model=model, loss='COTO', 
                            config=config, device=config['device'],
                            train_loader=train_loader, val_loader=test_loader)
        path_, acc_test = trainer_.train(path_)
        Acc['trial'].append(h)
        Acc['loss'].append('COTO')
        Acc['test_acc'].append(acc_test)

        ## BCE loss ##
        print('\n-- TRAIN BCE --\n')
        model = BinaryClassification(input_shape=input_shape, H=H, D=D)
        model.to(config['device'])

        trainer_ = Trainer(model=model, loss='BCELoss', 
                            config=config, device=config['device'],
                            train_loader=train_loader, val_loader=test_loader)
        path_, acc_test = trainer_.train(path_)
        Acc['trial'].append(h)
        Acc['loss'].append('BCE')
        Acc['test_acc'].append(acc_test)

        ## Hinge loss ##
        print('\n-- TRAIN Hinge --\n')
        model = BinaryClassification(input_shape=input_shape, H=H, D=D)
        model.to(config['device'])

        trainer_ = Trainer(model=model, loss='Hinge', 
                            config=config, device=config['device'],
                            train_loader=train_loader, val_loader=test_loader)
        path_, acc_test = trainer_.train(path_)
        Acc['trial'].append(h)
        Acc['loss'].append('Hinge')
        Acc['test_acc'].append(acc_test)

        ## EXP loss ##
        print('\n-- TRAIN EXP --\n')
        model = BinaryClassification(input_shape=input_shape, H=H, D=D)
        model.to(config['device'])

        trainer_ = Trainer(model=model, loss='EXP', 
                            config=config, device=config['device'],
                            train_loader=train_loader, val_loader=test_loader)
        path_, acc_test = trainer_.train(path_)
        Acc['trial'].append(h)
        Acc['loss'].append('EXP')
        Acc['test_acc'].append(acc_test)

    path_ = pd.DataFrame(path_)
    path_.to_csv('path_D{}_H{}_Batch{}.csv'.format(D,H,config['batch_size']), index=False)
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
    # p_less = pg.pairwise_tests(dv='test_acc', within='loss', data=Acc, subject='trial',
    #                 alternative='less').round(5)
    # p_less = p_less[['A', 'B', 'p-unc', 'alternative']]
    # p_less = p_less[p_less['B'] == 'COTO']

    p_less = pairwise_ttest(df=Acc, val_col='test_acc', group_col='loss', alternative='less').round(5)
    p_less = p_less[p_less['B'] == 'COTO']

    # p_greater = pg.pairwise_tests(dv='test_acc', within='loss', data=Acc, subject='trial',
    #                 alternative='greater').round(5)
    # p_greater = p_greater[['A', 'B', 'p-unc', 'alternative']]
    # p_greater = p_greater[p_greater['B'] == 'COTO']

    p_greater = pairwise_ttest(df=Acc, val_col='test_acc', group_col='loss', alternative='greater').round(5)
    p_greater = p_greater[p_greater['B'] == 'COTO']

    res = Acc.groupby('loss').agg({'test_acc': ['mean', 'std']})
    res[('test_acc', 'std')] /= np.sqrt(n_trials)
    res = res.T.round(4)

    ## Save outcome
    orig_stdout = sys.stdout
    out_file = open('out.txt', 'a+')
    sys.stdout = out_file

    print('\n#### %d - D: %d, H: %d ####\n' %(data_id, D, H))

    print('\n Step Size: %s \n' %config['optimizer'])

    print('\n-- Performance --\n')
    print((res.round(4)).to_markdown())

    print('\n-- Testing --\n')
    print(p_less.round(4).to_markdown())
    print(p_greater.round(4).to_markdown())

    out = '| ({}, {}) | mean(std) | {}({}) | {}({}) | {}({}) |'.format(H, D, 
                                                            res['BCE'][0], res['BCE'][1], 
                                                            res['Hinge'][0], res['Hinge'][1],
                                                            res['COTO'][0], res['COTO'][1])
    p_pair = '|          | p_value   | {}        | {}        | ---            |'.format(p_less[p_less['A']=='BCE']['pvalue'].values[0], 
                                        p_less[p_less['A']=='Hinge']['pvalue'].values[0])
    print('\n-- Result --\n')
    print(out)
    print(p_pair)
    if wandb_log:
        wandb.log({"test_acc_curve": fig,
                   "path": path_,
                   "perf_table": Acc,
                   "p_less": p_less,
                   "p_greater": p_greater,
                   })
        wandb.finish()
    
    sys.stdout = orig_stdout
    out_file.close()

if __name__=='__main__':
    # PARSE THE ARGS
    parser = argparse.ArgumentParser(description='COTO Training')
    parser.add_argument('-D', '--depth', default=1, type=int,
                        help='depth of the neural network')
    parser.add_argument('-H', '--width', default=128, type=int,
                           help='width of the neural network')
    parser.add_argument('-B', '--batch', default=256, type=int,
                           help='batch size of the training set')
    parser.add_argument('-e', '--epoch', default=500, type=int,
                           help='number of epochs to train')
    parser.add_argument('-ID', '--data_id', default=43969, type=int,
                           help='data_id of the dataset')
    parser.add_argument('-R', '--n_trials', default=20, type=int,
                           help='number of trials for the experiments')
    parser.add_argument('-L', '--log', default=False, type=bool,
                           help='if save the training process in wandb')
    args = parser.parse_args()

    config = { 'batch_size': args.batch,
            'trainer': {'epochs': args.epoch, 'val_per_epochs': 10}, 
            # 'optimizer': {'lr': 1e-4, 'type': 'Adam', 'lr_scheduler': 'StepLR', 'args': {'step_size':30, 'gamma': .5}}, #please change the argument if you use other LR
            # 'optimizer': {'lr': 1e-5, 'type': 'Adam', 'lr_scheduler': 'CyclicLR', 'args': {'base_lr': 1e-5, 'max_lr': 1e-4, 'step_size_up': 10, 'mode': "triangular2", 'cycle_momentum': False}},
            'optimizer': {'lr': 1e-5, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 1./3, 'total_iters': 1}},
            # 'optimizer': {'lr': 1e-4, 'type': 'Adam', 'lr_scheduler': 'LinearLR', 'args': {'start_factor': 0.1, 'total_iters': 100}},
            'device': torch.device("cuda:0" if torch.cuda.is_available() else "cpu")}

    H, D = args.width, args.depth
    data_id = args.data_id
    n_trials = args.n_trials
    wandb_log = args.log

    main(config=config, D=D, H=H, data_id=data_id, n_trials=n_trials, wandb_log=wandb_log)

## Tabular dataset
# philippine: 41145
# SantanderCustomerSatisfaction: 42395

## Open Performance Benchmark on Tabular Data
# heloc (10k x 23): 45023
# higgs (98k x 29): 23512
# california (20.6k x 9): 45025


# Tabular data learning benchmark
# electricity (45.3k x 9): 44120
# house_16H (13.5k x 17): 44123
# phoneme (3.17k x 6): 43973
# MiniBooNE (72998, 50): 44128
# MagicTelescope (13376, 10): 44125
# higgs (98k x 29): 23512
# eye_movements (7.61 x 24): 44157
# jannis (57.6k x 55): 45021
# credit (16.7k x 11): 45024
# california (20.6k x 9): 45025

## Image dataset
# CIFAR2: 
# PCam: https://github.com/basveeling/pcam
# MHIST: https://bmirds.github.io/MHIST/
