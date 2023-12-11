"""eloto in image datasets"""

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

from loader import TrainData, TestData, openml_data, img_data
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
import models
from img_models import ResNet18
import img_models
import Image_Classification_PyTorch

import torchvision.transforms as transforms
from torchvision import datasets, models, transforms

def main(config, filename='CIFAR', n_trials=5, wandb_log=False):

    ## wandb log
    if wandb_log:
        wandb.init(project="COTO", name=filename+config['model']['net'])

    ## Reproducibility
    torch.manual_seed(0)
    random.seed(0)
    np.random.seed(0)

    Acc = {'trial': [], 'loss': [], 'test_acc': [], 'test_auc': []}
    path_={'loss': [], 'epoch': [], 'train_loss': [], 'train_acc': [], 'test_acc': []}

    for h in range(n_trials):

        train_data, test_data = img_data(name=filename)

        train_loader = DataLoader(dataset=train_data, batch_size=config['batch_size'], shuffle=True)
        test_loader = DataLoader(dataset=test_data, batch_size=32)

        ## get some random training data
        # dataiter = iter(train_loader)
        # X_batch, y_batch = next(dataiter)

        ## eLOTO ##
        print('\n-- TRAIN eLOTO --\n')
        model = getattr(img_models, config['model']['net'])(num_classes=1, **config['model']['args'])
        model.to(config['device'])
        print(model)
        
        trainer_ = Trainer(model=model, loss='COTO', 
                            config=config, device=config['device'],
                            train_loader=train_loader, val_loader=test_loader)
        path_, acc_test, auc_test = trainer_.train(path_)
        Acc['trial'].append(h)
        Acc['loss'].append('COTO')
        Acc['test_acc'].append(acc_test)
        Acc['test_auc'].append(auc_test)

        ## BCE loss ##
        print('\n-- TRAIN BCE --\n')
        model = getattr(img_models, config['model']['net'])(num_classes=1, **config['model']['args'])
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
        model = getattr(img_models, config['model']['net'])(num_classes=1, **config['model']['args'])
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
        model = getattr(img_models, config['model']['net'])(num_classes=1, **config['model']['args'])
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
    # path_.to_csv('path_D{}_H{}_Batch{}.csv'.format(D,H,config['batch_size']), index=False)
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
    p_less = p_less[p_less['B'] == 'COTO']

    p_greater = pairwise_ttest(df=Acc, val_col='test_acc', group_col='loss', alternative='greater').round(5)
    p_greater = p_greater[p_greater['B'] == 'COTO']

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
    print('\n Step Size: %s \n' %config['optimizer'])

    print('\n-- Performance --\n')
    print((res_acc.round(4)).to_markdown())
    print('\n')
    print((res_auc.round(4)).to_markdown())

    print('\n-- Testing --\n')
    print(p_less.round(4).to_markdown())
    print('\n')
    print(p_greater.round(4).to_markdown())

    out = '| ({}) | mean(std) | {}({}) | {}({}) | {}({}) |'.format( config['model']['net'],
                                                            res_acc['BCE'][0], res_acc['BCE'][1], 
                                                            res_acc['Hinge'][0], res_acc['Hinge'][1],
                                                            res_acc['COTO'][0], res_acc['COTO'][1])
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

if __name__=='__main__':
    # PARSE THE ARGS
    parser = argparse.ArgumentParser(description='eLOTO Training')
    parser.add_argument('-B', '--batch', default=128, type=int,
                           help='batch size of the training set')
    parser.add_argument('-e', '--epoch', default=200, type=int,
                           help='number of epochs to train')
    parser.add_argument('-F', '--filename', default="CIFAR", type=str,
                           help='filename of the dataset')
    parser.add_argument('-R', '--n_trials', default=5, type=int,
                           help='number of trials for the experiments')
    parser.add_argument('--log', default=True, action=argparse.BooleanOptionalAction,
                           help='if save the training process in wandb')
    args = parser.parse_args()

    config = {
            'dataset' : args.filename,
            # 'model': {'net': 'VGG', 'args': {'vgg_name': 'VGG19'}},
            'model': {'net': 'ResNet50', 'args': {}},
            'batch_size': args.batch,
            'trainer': {'epochs': args.epoch, 'val_per_epochs': 10}, 
            'optimizer': {'lr': 1e-3, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}},
            'device': torch.device("cuda:0" if torch.cuda.is_available() else "cpu")}

    filename = args.filename
    n_trials = args.n_trials
    wandb_log = args.log

    main(config=config, filename=filename, n_trials=n_trials, wandb_log=wandb_log)

## Image dataset
# Age and gender prediction: https://talhassner.github.io/home/projects/Adience/Adience-data.html
# PCam: https://github.com/basveeling/pcam
# MHIST: https://bmirds.github.io/MHIST/
