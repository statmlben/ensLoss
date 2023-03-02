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
from model import BinaryClassification, MHIST_CNN, MHIST_resnet18
from base import evaluate
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
import torchvision.transforms as transforms
from torchvision import datasets, models, transforms

def main(config, filename='MHIST', n_trials=2, wandb_log=False):

    ## wandb log
    if wandb_log:
        wandb.init(project="COTO", name=filename+str(D)+'-'+str(H))

    ## image tranform
    transform = transforms.Compose(
                [transforms.ToPILImage(),
                transforms.ToTensor(),
                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    Acc = {'trial': [], 'loss': [], 'test_acc': []}
    path_={'loss': [], 'epoch': [], 'train_loss': [], 'train_acc': [], 'test_acc': []}

    for h in range(n_trials):

        ## Reproducibility
        torch.manual_seed(h)
        random.seed(h)
        np.random.seed(h)

        train_data, test_data = img_data(transform=transform, name=filename)
        input_shape = (3, 224, 224)

        train_loader = DataLoader(dataset=train_data, batch_size=config['batch_size'], shuffle=True)
        test_loader = DataLoader(dataset=test_data, batch_size=32)

        ## eLOTO ##
        # print('\n-- TRAIN eLOTO --\n')
        # model = MHIST_CNN()
        # model.to(config['device'])

        # trainer_ = Trainer(model=model, loss='eLOTO', 
        #                     config=config, device=config['device'],
        #                     train_loader=train_loader, val_loader=test_loader)
        # path_, acc_test = trainer_.train(path_)
        # Acc['trial'].append(h)
        # Acc['loss'].append('eLOTO')
        # Acc['test_acc'].append(acc_test)

        ## BCE loss ##
        print('\n-- TRAIN BCE --\n')
        # model = MHIST_CNN()
        model = MHIST_resnet18()

        model.to(config['device'])

        trainer_ = Trainer(model=model, loss='BCELoss',
                            config=config, device=config['device'],
                            train_loader=train_loader, val_loader=test_loader)
        path_, acc_test = trainer_.train(path_)
        Acc['trial'].append(h)
        Acc['loss'].append('BCE')
        Acc['test_acc'].append(acc_test)

        ## Hinge loss ##
        # print('\n-- TRAIN Hinge --\n')
        # model = MHIST_CNN()
        # model.to(config['device'])

        # trainer_ = Trainer(model=model, loss='Hinge', 
        #                     config=config, device=config['device'],
        #                     train_loader=train_loader, val_loader=test_loader)
        # path_, acc_test = trainer_.train(path_)
        # Acc['trial'].append(h)
        # Acc['loss'].append('Hinge')
        # Acc['test_acc'].append(acc_test)

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
    p_less = pg.pairwise_tests(dv='test_acc', within='loss', data=Acc, subject='trial',
                    alternative='less').round(5)
    p_less = p_less[['A', 'B', 'p-unc', 'alternative']]
    p_less = p_less[p_less['B'] == 'eLOTO']

    p_greater = pg.pairwise_tests(dv='test_acc', within='loss', data=Acc, subject='trial',
                    alternative='greater').round(5)
    p_greater = p_greater[['A', 'B', 'p-unc', 'alternative']]
    p_greater = p_greater[p_greater['B'] == 'eLOTO']

    res = Acc.groupby('loss').agg({'test_acc': ['mean', 'std']})
    res[('test_acc', 'std')] /= np.sqrt(n_trials)
    res = res.T.round(4)

    # print('#### D: %d, H: %d ####' %(D, H))

    print('\n-- Performance --\n')
    print((res.round(4)).to_markdown())

    print('\n-- Testing --\n')
    print(p_less.round(4).to_markdown())
    print(p_greater.round(4).to_markdown())

    out = '| mean(std) | {}({}) | {}({}) | {}({}) |'.format(res['BCE'][0], res['BCE'][1], 
                                                            res['Hinge'][0], res['Hinge'][1],
                                                            res['eLOTO'][0], res['eLOTO'][1])
    p_pair = '|          | p_value   | {}        | {}        | ---            |'.format(p_less[p_less['A']=='BCE']['p-unc'].values[0], 
                                        p_less[p_less['A']=='Hinge']['p-unc'].values[0])
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
    parser.add_argument('-B', '--batch', default=32, type=int,
                           help='batch size of the training set')
    parser.add_argument('-e', '--epoch', default=100, type=int,
                           help='number of epochs to train')
    parser.add_argument('-f', '--filename', default='MHIST', type=str,
                           help='filename of the dataset')
    args = parser.parse_args()

    config = { 'batch_size': args.batch,
            'trainer': {'epochs': args.epoch, 'val_per_epochs': 10},
            'optimizer': {'lr': 1e-3, 'type': 'Adam', 'lr_scheduler': 'StepLR', 'step_size':5, 'gamma':0.91}, #please change the argument if you use other LR
            'device': torch.device("cuda:0" if torch.cuda.is_available() else "cpu")}

    filename = args.filename

    main(config=config, filename=filename)

## Tabular dataset
# philippine
# sylva_prior
# SantanderCustomerSatisfaction

## Image dataset
# Age and gender prediction: https://talhassner.github.io/home/projects/Adience/Adience-data.html
# PCam: https://github.com/basveeling/pcam
# MHIST: https://bmirds.github.io/MHIST/