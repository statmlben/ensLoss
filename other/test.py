# import numpy as np

# def BC_inv(z, lam=0):
#     if lam == 0.:
#         return np.exp(z)
#     else:
#         diff = 1. + lam*z
#         return (np.where(diff > 0.0, diff, 0.0))**(1.0/lam)

# x = np.random.randn(1000)
# z = BC_inv(x, lam=0.0)

# import matplotlib.pyplot as plt

# plt.hist(z)
# plt.show()

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

import torchvision.transforms as transforms
from torchvision import datasets, models, transforms

config = {
        'model': {'net': 'ResNet18', 'args': {}},
        'batch_size': 256,
        'trainer': {'epochs': 200, 'val_per_epochs': 10}, 
        'optimizer': {'lr': 1e-3, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}},
        'device': torch.device("cuda:0" if torch.cuda.is_available() else "cpu")}

## Reproducibility
torch.manual_seed(0)
random.seed(0)
np.random.seed(0)

## image tranform
transform = transforms.Compose(
            [
            # transforms.ToPILImage(),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

Acc = {'trial': [], 'loss': [], 'test_acc': []}
path_={'loss': [], 'epoch': [], 'train_loss': [], 'train_acc': [], 'test_acc': []}


train_data, test_data = img_data(transform=transform, name='CIFAR')
input_shape = (3, 224, 224)

train_loader = DataLoader(dataset=train_data, batch_size=config['batch_size'], shuffle=True)
test_loader = DataLoader(dataset=test_data, batch_size=32)

## get some random training data
# dataiter = iter(train_loader)
# images, labels = next(dataiter)

## eLOTO ##
print('\n-- TRAIN eLOTO --\n')
model = getattr(img_models, config['model']['net'])(num_classes=1, **config['model']['args'])
model.to(config['device'])

trainer_ = Trainer(model=model, loss='COTO', 
                    config=config, device=config['device'],
                    train_loader=train_loader, val_loader=test_loader)
path_, acc_test = trainer_.train(path_)
Acc['trial'].append(h)
Acc['loss'].append('eLOTO')
Acc['test_acc'].append(acc_test)

## BCE loss ##
print('\n-- TRAIN BCE --\n')
model = getattr(img_models, config['model']['net'])(num_classes=1, **config['model']['args'])
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
model = getattr(img_models, config['model']['net'])(num_classes=1, **config['model']['args'])
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
model = getattr(img_models, config['model']['net'])(num_classes=1, **config['model']['args'])
model.to(config['device'])

trainer_ = Trainer(model=model, loss='EXP', 
                    config=config, device=config['device'],
                    train_loader=train_loader, val_loader=test_loader)
path_, acc_test = trainer_.train(path_)
Acc['trial'].append(h)
Acc['loss'].append('EXP')
Acc['test_acc'].append(acc_test)


