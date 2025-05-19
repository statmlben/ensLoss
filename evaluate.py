""" ensLoss: test.py"""

# Authors: Ben Dai 
# License: MIT License

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm
import pandas as pd
import losses
import numpy as np
from torcheval.metrics import BinaryAccuracy, BinaryAUROC
import os
import time

class Tester(object):
    def __init__(self, model, device, test_loader):
        self.model = model
        self.device = device
        self.test_loader = test_loader

    def test(self):

        print('\n###### TEST ######')
        epoch_acc_val = 0
        epoch_auc_val = 0

        self.model.eval()

        with torch.no_grad():
            acc_metric = BinaryAccuracy()
            auc_metric = BinaryAUROC()

            tbar = tqdm(self.test_loader, ncols=120)
                        
            for batch_idx, (X_batch, y_batch) in enumerate(tbar):
                X_batch, y_batch = X_batch.to(self.device), y_batch.to(self.device)
                y_pred = self.model(X_batch)
                
                acc_metric.update(1.0*(y_pred > 0).flatten(), y_batch)
                auc_metric.update(y_pred.flatten(), y_batch)
                
                epoch_acc_val = acc_metric.compute().item()
                epoch_auc_val = auc_metric.compute().item()

                tbar.set_description('TEST | Acc: {:.3f}; AUC: {:.3f}'.format(
                        epoch_acc_val, epoch_auc_val))

        return epoch_acc_val, epoch_auc_val


class Tester_bag(object):
    def __init__(self, model_bag, device, test_loader, strategy='average'):
        self.model_bag = model_bag
        self.device = device
        self.test_loader = test_loader
        self.num_bag = len(model_bag)
        self.strategy = strategy

    def test(self):

        print('\n###### TEST ######')
        epoch_acc_val = 0
        epoch_auc_val = 0

        for i in range(self.num_bag):
            self.model_bag[i].eval()

        with torch.no_grad():
            acc_metric = BinaryAccuracy()
            auc_metric = BinaryAUROC()

            tbar = tqdm(self.test_loader, ncols=120)
                        
            for batch_idx, (X_batch, y_batch) in enumerate(tbar):
                X_batch, y_batch = X_batch.to(self.device), y_batch.to(self.device)
                
                y_pred_bag = torch.stack([model(X_batch) for model in self.model_bag], dim=0)
                if self.strategy == 'average':
                    y_pred = torch.mean(y_pred_bag, dim=0)
                elif self.strategy == 'voting':
                    y_pred_bag = torch.sign(y_pred_bag)
                    y_pred, _ = torch.mode(y_pred_bag, dim=0)
                else:
                    raise ValueError('Unknown strategy: {}'.format(self.strategy))
            
                acc_metric.update(1.0*(y_pred > 0).flatten(), y_batch)
                auc_metric.update(y_pred.flatten(), y_batch)
                
                epoch_acc_val = acc_metric.compute().item()
                epoch_auc_val = auc_metric.compute().item()

                tbar.set_description('TEST | Acc: {:.3f}; AUC: {:.3f}'.format(
                        epoch_acc_val, epoch_auc_val))

        return epoch_acc_val, epoch_auc_val