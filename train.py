""" eloto:  """

# Authors: Ben Dai <bendai@cuhk.edu.hk>
# License: MIT License

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm
from metric import binary_acc
import pandas as pd
import losses
from torchmetrics.classification import BinaryAUROC
import numpy as np
from skopt import Optimizer

def get_instance(module, name, config, *args):
    # GET THE CORRESPONDING CLASS / FCT 
    return getattr(module, config[name]['type'])(*args, **config[name]['args'])

class Trainer(object):

    def __init__(self, model, loss, config, device, train_loader, val_loader=None):
        self.model = model
        self.loss = loss
        self.device = config['device']
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.config = config

    def train(self, path_={'loss': [], 'epoch': [], 'train_loss': [], 'train_acc': [], 'test_acc': []}):
        
        config = self.config

        loss_ = getattr(losses, self.loss)()
        optimizer = getattr(torch.optim, config['optimizer']['type'])(self.model.parameters(), lr=config['optimizer']['lr'], momentum=0.9, weight_decay=5e-4)
        scheduler = getattr(torch.optim.lr_scheduler, config['optimizer']['lr_scheduler'])(optimizer, **config['optimizer']['args'])
        
        # opt = Optimizer([(0.0, 10.0)], "GP", 
        #                 n_initial_points=5, 
        #                 acq_optimizer="sampling")

        for e in range(1, config['trainer']['epochs']+1):

            ## set loss function parameter
            if (e%10 ==0) and (self.loss=='COTO'):
                if np.random.randn() > 0.:
                    loss_.lam = np.random.rand()
                else:
                    loss_.lam = 1.0 / np.random.rand()

                    
            #     now_acc_train = epoch_acc_train/len(self.train_loader)
            #     opt.tell([loss_.lam], -now_acc_train)
                
            #     next_lam = opt.ask()[0]
            #     loss_.lam = next_lam

            epoch_loss_train = 0
            epoch_acc_train = 0

            self.model.train()
            
            tbar = tqdm(self.train_loader, ncols=120)
            for batch_idx, (X_batch, y_batch) in enumerate(tbar):
                y_batch = y_batch.float()
                X_batch, y_batch = X_batch.to(self.device), y_batch.to(self.device)
                
                optimizer.zero_grad()
                y_pred = self.model(X_batch)
                loss = loss_(y_pred, y_batch.unsqueeze(1).float())
                acc = binary_acc(y_pred, y_batch.unsqueeze(1))
                
                loss.backward()
                if self.loss=='EXP':
                    torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1.0)
                optimizer.step()
            # target * y_pred.flatten()
                
                # epoch_loss_train += loss.item()
                epoch_acc_train += acc.item()
                
                tbar.set_description('TRAIN ({}) SGD({}) LR({:.2E}) | Acc: {:.3f}'.format(
                        e, self.loss, optimizer.param_groups[0]["lr"], epoch_acc_train/(batch_idx+1)))
            
            scheduler.step()

            # EVALUATION
            if e%(config['trainer']['val_per_epochs'])==0:
                print('\n###### EVALUATION ######')
                epoch_loss_val = 0
                epoch_acc_val = 0

                self.model.eval()
                with torch.no_grad():
                    tbar = tqdm(self.val_loader, ncols=120)
                    for batch_idx, (X_batch, y_batch) in enumerate(tbar):

                        X_batch, y_batch = X_batch.to(self.device), y_batch.to(self.device)
                        y_pred = self.model(X_batch)
                        acc = binary_acc(y_pred, y_batch.unsqueeze(1))
                        
                        # epoch_loss_valid += loss.item()
                        epoch_acc_val += acc.item()
                    
                        tbar.set_description('VALID ({}) SGD({}) | Acc: {:.3f}'.format(
                                e, self.loss, epoch_acc_val/(batch_idx+1)))

                print('\n')
                path_['epoch'].append(e)
                path_['loss'].append(self.loss)
                path_['train_loss'].append(epoch_loss_train/len(self.train_loader))
                path_['train_acc'].append(epoch_acc_train/len(self.train_loader))
                path_['test_acc'].append(epoch_acc_val/len(self.val_loader))

                # if self.loss=='COTO':
                #     # now_acc_train = epoch_acc_train/len(self.train_loader)
                #     now_acc_valid = epoch_acc_val/len(self.val_loader)
                #     opt.tell([loss_.lam], 1.0-now_acc_valid)
                    
                #     next_lam = opt.ask()[0]
                #     loss_.lam = next_lam

        return path_, epoch_acc_val/len(self.val_loader)
