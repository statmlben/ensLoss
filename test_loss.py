"""Test different tails of Hinge loss in simulated data"""

# Authors: Ben Dai <bendai@cuhk.edu.hk>
# License: MIT License

## basics
import numpy as np
import pandas as pd
import random
import torch

## dataloader
from loader import openml_data, img_data, sim_data
from torch.utils.data import DataLoader

## models
import img_models
import models

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
        'dataset' : "sim",
        'model': {'net': 'ResNet18'},
        # 'model': {'net': 'TabMLP5'},
        'save_model': False,
        'batch_size': 64,
        'trainer': {'epochs': 500, 'val_per_epochs': 2},
        'optimizer': {'lr': 1e-3, 
                      'type': 'SGD', 
                      'lr_scheduler': 'CosineAnnealingLR', 
                      'args': {'T_max': 300}},
        'device': torch.device("cuda:0" if torch.cuda.is_available() else "cpu")}

## Reproducibility
for loss_name in ['Hinge', 'Exp_Hinge', 'Inv_Hinge', 'Inv_Log_Hinge', 'Log_Hinge']:
    for h in range(5):

        torch.manual_seed(h)
        random.seed(h)
        np.random.seed(h)

        # path_={'loss': [], 'epoch': [], 'train_loss': [], 'train_acc': [], 'test_loss': [], 'test_acc': []}
        path_={'loss': [], 'epoch': [], 'train_loss': [], 'train_acc': []}

        ## Simluate data
        # train_data, test_data = sim_data(n=5000, d=200, random_state=0)
        train_data, test_data = img_data(name='CIFAR')

        train_loader = DataLoader(dataset=train_data, batch_size=config['batch_size'], shuffle=True)
        test_loader = DataLoader(dataset=test_data, batch_size=32)

        ## Define Model
        # model = getattr(models, config['model']['net'])(input_shape=200, H=256)
        model = getattr(img_models, config['model']['net'])(num_classes=1)
        model.to(config['device'])

        print(model)

        print('\n-- TRAIN Hinge Loss with Different Tails --\n')

        ## Setting
        device = config['device']
        optimizer = getattr(torch.optim, config['optimizer']['type'])(model.parameters(), lr=config['optimizer']['lr'], momentum=0.9, weight_decay=5e-4)
        scheduler = getattr(torch.optim.lr_scheduler, config['optimizer']['lr_scheduler'])(optimizer, **config['optimizer']['args'])

        # loss_ = getattr(losses, 'sqrt_Hinge')()
        loss_ = getattr(losses, loss_name)()

        for e in range(1, config['trainer']['epochs']+1):

            epoch_loss_train = []
            epoch_acc_train = 0

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
                    
                    tbar.set_description('TRAIN ({}) SGD({}) LR({:.2E}) | Loss: {:.3f} Acc: {:.3f}'.format(
                            e, loss_name, optimizer.param_groups[0]["lr"], np.mean(epoch_loss_train), epoch_acc_train))

            path_['epoch'].append(e)
            path_['loss'].append(loss_name)
            path_['train_loss'].append(np.mean(epoch_loss_train))
            path_['train_acc'].append(epoch_acc_train)
            # path_['test_loss'].append(np.mean(epoch_loss_val))
            # path_['test_acc'].append(epoch_acc_val)


        # EVALUATION
        # print('\n###### EVALUATION ######')
        # epoch_loss_val = []
        # epoch_acc_val = 0
        # epoch_auc_val = 0

        # model.eval()
        # with torch.no_grad():
        #     acc_metric = BinaryAccuracy()
        #     tbar = tqdm(test_loader, ncols=120)
        #     for batch_idx, (X_batch, y_batch) in enumerate(tbar):

        #         X_batch, y_batch = X_batch.to(device), y_batch.to(device)
        #         y_pred = model(X_batch)
                
        #         loss_val = loss_(y_pred, y_batch.unsqueeze(1).float())
        #         acc_metric.update(1.0*(y_pred > 0).flatten(), y_batch)
                
        #         epoch_loss_val.append(loss_val.item())
        #         epoch_acc_val = acc_metric.compute().item()

        #         tbar.set_description('VALID ({}) SGD({}) | Loss: {:.3f} Acc: {:.3f}'.format(
        #                 e, loss_name, np.mean(epoch_loss_val), epoch_acc_val))

        df = pd.DataFrame(path_)
        df.to_csv('./expt/test_loss_CIFAR.csv', mode='a', header=False, index=False)