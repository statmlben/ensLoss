"""Test different tails of Hinge loss in CIFAR"""

# Authors: Ben Dai <bendai@cuhk.edu.hk>
# License: MIT License

## basics
import numpy as np
import pandas as pd
import random
import torch

## dataloader
from loader import openml_data, img_data
from torch.utils.data import DataLoader

## models
import img_models

## Train
from train import Trainer

## args; print config, figure, out
import argparse
import pprint
from plot import line
import sys

## log to wandb
import wandb

## train libs
from tqdm import tqdm
import losses
from torcheval.metrics import BinaryAccuracy, BinaryAUROC

## config setting
config = {
        'dataset' : "CIFAR",
        'model': {'net': 'ResNet50'},
        'save_model': False,
        'batch_size': 128,
        'trainer': {'epochs': 50, 'val_per_epochs': 5},
        'optimizer': {'lr': 1e-3, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 50}},
        'device': torch.device("cuda:0" if torch.cuda.is_available() else "cpu")}

filename = "CIFAR"

## Reproducibility
torch.manual_seed(0)
random.seed(0)
np.random.seed(0)

path_={'loss': [], 'epoch': [], 'train_loss': [], 'train_acc': [], 'mag': []}

train_data, test_data = img_data(name=filename)

train_loader = DataLoader(dataset=train_data, batch_size=config['batch_size'], shuffle=True)
test_loader = DataLoader(dataset=test_data, batch_size=32)

## Define Model
model = getattr(img_models, config['model']['net'])(num_classes=1)
model.to(config['device'])

print(model)

print('\n-- TRAIN Hinge Loss with Different Tails --\n')

## Setting
device = config['device']
optimizer = getattr(torch.optim, config['optimizer']['type'])(model.parameters(), lr=config['optimizer']['lr'], momentum=0.9, weight_decay=5e-4)
scheduler = getattr(torch.optim.lr_scheduler, config['optimizer']['lr_scheduler'])(optimizer, **config['optimizer']['args'])


loss_name = 'log_Hinge'
# loss_ = getattr(losses, 'sqrt_Hinge')()
loss_ = getattr(losses, loss_name)()
for e in range(1, config['trainer']['epochs']+1):

    epoch_loss_train = []
    epoch_acc_train = 0
    epoch_mag = []

    model.train()
    
    acc_metric = BinaryAccuracy()
    tbar = tqdm(train_loader, ncols=120)

    for batch_idx, (X_batch, y_batch) in enumerate(tbar):
        y_batch = y_batch.float()
        X_batch, y_batch = X_batch.to(device), y_batch.to(device)
        
        optimizer.zero_grad()
        y_pred = model(X_batch)
        loss = loss_(y_pred, y_batch.unsqueeze(1).float())
        acc_metric.update(1.0*(y_pred > 0).flatten(), y_batch)
        # acc = binary_acc(y_pred, y_batch.unsqueeze(1))
        
        loss.backward()
        optimizer.step()
        
        epoch_loss_train.append(loss.item())
        # epoch_acc_train += acc.item()
        epoch_acc_train = acc_metric.compute().item()
        epoch_mag.append(abs(y_pred.detach()).mean().item())
        
        tbar.set_description('TRAIN ({}) SGD({}) LR({:.2E}) | MAG: {:.3f} Loss: {:.3f} Acc: {:.3f}'.format(
                e, loss_name, optimizer.param_groups[0]["lr"], np.mean(epoch_mag), np.mean(epoch_loss_train), epoch_acc_train))

    path_['loss'].append(loss_name)
    path_['epoch'].append(e)
    path_['train_loss'].append(np.mean(epoch_loss_train))
    path_['train_acc'].append(epoch_acc_train)
    path_['mag'].append(np.mean(epoch_mag))

df = pd.DataFrame(path_)

## Image dataset
# CIFAR10: https://www.cs.toronto.edu/~kriz/cifar.html
# PCam: https://github.com/basveeling/pcam

# python test_loss.py -B=128 -e=100 -F="CIFAR" -R=5 --no-log