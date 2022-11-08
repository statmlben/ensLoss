## implementation for "Lower Back Pain Symptoms Dataset"

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

from loader import TrainData, TestData, spine_data, sonar_data, openml_data
from model import BinaryClassification
from base import evaluate
from sklearn.model_selection import KFold
import scipy
from train import Trainer

import seaborn as sns
import pingouin as pg
from scipy import stats
import argparse

def main(config, D, H, n_trials=15):

    ## Reproducibility
    torch.manual_seed(1024)
    random.seed(1024)
    np.random.seed(1024)

    Acc = {'trial': [], 'loss': [], 'test_acc': []}
    path_={'loss': [], 'epoch': [], 'train_loss': [], 'train_acc': [], 'valid_acc': []}

    for h in range(n_trials):

        # train_data, test_data = spine_data(random_state=h)
        # train_data, test_data = sonar_data(random_state=h)
        train_data, test_data = openml_data(name='sylva_prior', random_state=h)
        input_shape = train_data.X_data.shape[1]

        train_loader = DataLoader(dataset=train_data, batch_size=config['batch_size'], shuffle=True)
        test_loader = DataLoader(dataset=test_data, batch_size=32)

        ## eLOTO ##
        model = BinaryClassification(input_shape=input_shape, H=H, D=D)
        model.to(config['device'])

        trainer_ = Trainer(model=model, loss='eLOTO', 
                            config=config, device=config['device'],
                            train_loader=train_loader, val_loader=test_loader)
        path_, acc_test = trainer_.train(path_)
        Acc['trial'].append(h)
        Acc['loss'].append('eLOTO')
        Acc['test_acc'].append(acc_test)

        ## BCE loss ##
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
        model = BinaryClassification(input_shape=input_shape, H=H, D=D)
        model.to(config['device'])

        trainer_ = Trainer(model=model, loss='Hinge', 
                            config=config, device=config['device'],
                            train_loader=train_loader, val_loader=test_loader)
        path_, acc_test = trainer_.train(path_)
        Acc['trial'].append(h)
        Acc['loss'].append('Hinge')
        Acc['test_acc'].append(acc_test)

    path_ = pd.DataFrame(path_)
    Acc = pd.DataFrame(Acc)

    sns.set()
    ## Variance should be reduced to var / n_trials
    qt = 1 - 2*(1 - scipy.stats.norm.cdf(1.96/np.sqrt(n_trials)))
    sns.lineplot(data=path_, x='epoch', y='valid_acc', hue='loss', ci=int(100*qt))
    plt.show()

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

    print('#### D: %d, H: %d ####' %(D, H))

    print('\n-- Performance --\n')
    print((res.round(4)).to_markdown())

    print('\n-- Testing --\n')
    print(p_less.round(4).to_markdown())
    print(p_greater.round(4).to_markdown())

    out = '| ({}, {}) | mean(std) | {}({}) | {}({}) | {}({}) |'.format(H, D, res['BCE'][0], res['BCE'][1], 
                                                            res['Hinge'][0], res['Hinge'][1],
                                                            res['eLOTO'][0], res['eLOTO'][1])
    p_pair = '|          | p_value   | {}        | {}        | ---            |'.format(p_less[p_less['A']=='BCE']['p-unc'].values[0], 
                                        p_less[p_less['A']=='Hinge']['p-unc'].values[0])
    print('\n-- Result --\n')
    print(out)
    print(p_pair)



if __name__=='__main__':
    # PARSE THE ARGS
    parser = argparse.ArgumentParser(description='eLOTO Training')
    parser.add_argument('-D', '--depth', default=1, type=int,
                        help='depth of the neural network')
    parser.add_argument('-H', '--width', default=128, type=int,
                           help='width of the neural network')
    args = parser.parse_args()

    config = { 'batch_size': 64,
            'trainer': {'epochs': 2000, 'val_per_epochs': 20}, 
            'optimizer': {'lr': 1e-5, 'type': 'Adam', 'lr_scheduler': 'LinearLR'},
            'device': torch.device("cuda:0" if torch.cuda.is_available() else "cpu")}

    H, D = args.width, args.depth

    main(config=config, D=D, H=H)