"""ensLoss + reg methods in image datasets"""

# Authors: Ben Dai <bendai@cuhk.edu.hk>
# License: MIT License

## basics
import numpy as np
import pandas as pd
import random
import torch
from itertools import combinations

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
from base import pairwise_ttest, append_dropout

## log to wandb
import wandb

def main(config, filename='PCam', n_trials=5, wandb_log=False):

    ## wandb log
    if wandb_log:
        wandb.init(project="ensLoss", name='Reg'+'-'+filename+'-'+config['model']['net'])

    ## Reproducibility
    torch.manual_seed(0)
    random.seed(0)
    np.random.seed(0)

    Acc = {'trial': [], 'loss': [], 'test_acc': [], 'test_auc': []}
    path_={'loss': [], 'epoch': [], 'train_loss': [], 'train_acc': [], 'test_acc': []}

    for h in range(n_trials):

        train_data, test_data = img_data(name=filename, aug=config['dataAug'])

        train_loader = DataLoader(dataset=train_data, batch_size=config['batch_size'], shuffle=True)
        test_loader = DataLoader(dataset=test_data, batch_size=32)

        ## get some random training data
        # dataiter = iter(train_loader)
        # X_batch, y_batch = next(dataiter)

        ## ensLoss ##
        model = getattr(img_models, config['model']['net'])(num_classes=1, 
                                                            dropout_rate=config['model']['dropout_rate'])
        model.to(config['device'])

        if h==0:
            ## print the model in the first trial
            print(model)

        print('\n-- TRAIN ensLoss --\n')
        
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
        model = getattr(img_models, config['model']['net'])(num_classes=1, 
                                                            dropout_rate=config['model']['dropout_rate'])
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
        model = getattr(img_models, config['model']['net'])(num_classes=1, 
                                                            dropout_rate=config['model']['dropout_rate'])
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
        model = getattr(img_models, config['model']['net'])(num_classes=1, 
                                                            dropout_rate=config['model']['dropout_rate'])
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
    
    res_acc = Acc.groupby('loss').agg({'test_acc': ['mean', 'std']})
    res_acc[('test_acc', 'std')] /= np.sqrt(n_trials)
    res_acc = res_acc.T.round(4)

    res_auc = Acc.groupby('loss').agg({'test_auc': ['mean', 'std']})
    res_auc[('test_auc', 'std')] /= np.sqrt(n_trials)
    res_auc = res_auc.T.round(4)

    ## Save outcome
    orig_stdout = sys.stdout
    out_file = open('out_reg.txt', 'a+')
    sys.stdout = out_file

    print('\n#### %s - model: %s ####\n' %(filename, config['model']['net']))
    # print('\n Step Size: %s \n' %config['optimizer'])
    print('\n-- CONFIG --\n')
    pprint.pprint(config, width=1)

    print('\n-- Performance --\n')
    print((res_acc.round(4)).to_markdown())
    print('\n')
    print((res_auc.round(4)).to_markdown())

    if wandb_log:
        wandb.log({"perf": Acc.groupby('loss')['test_acc'].agg(['mean', 'std']),
                   "path": path_,
                   "perf_table": Acc,
                   })
        wandb.finish()

    out_file.close()
    sys.stdout = orig_stdout

if __name__=='__main__':
    # PARSE THE ARGS
    parser = argparse.ArgumentParser(description='ensLoss Training')
    parser.add_argument('-B', '--batch', default=128, type=int,
                           help='batch size of the training set')
    parser.add_argument('-e', '--epoch', default=200, type=int,
                           help='number of epochs to train')
    parser.add_argument('-F', '--filename', default="CIFAR", type=str,
                           help='filename of the dataset')
    parser.add_argument('-N', '--net', default="ResNet50", type=str,
                           help='the neural net of the classification')
    parser.add_argument('-WD', '--weight_decay', default=5e-4, type=float,
                           help='the strength of the weight decay of SGD')
    parser.add_argument('-dr', '--dropout_rate', default=0.0, type=float,
                           help='the dropout rate of ResNet50')
    parser.add_argument('-R', '--n_trials', default=5, type=int,
                           help='number of trials for the experiments')
    parser.add_argument('--aug', default=True, action=argparse.BooleanOptionalAction,
                           help='if data augmentation of CIFAR datasets')
    parser.add_argument('--log', default=True, action=argparse.BooleanOptionalAction,
                           help='if save the training process in wandb')
    args = parser.parse_args()

    config = {
            'dataset' : args.filename,
            'dataAug': args.aug,
            'model': {'net': args.net, 'dropout_rate': args.dropout_rate},
            'save_model': False,
            'batch_size': args.batch,
            'trainer': {'epochs': args.epoch, 'val_per_epochs': 5},
            'optimizer': {'lr': 1e-3, 'type': 'SGD', 'weight_decay': args.weight_decay, 
                          'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': args.epoch}},
            'device': torch.device("cuda:0" if torch.cuda.is_available() else "cpu")}

    filename = args.filename
    n_trials = args.n_trials
    wandb_log = args.log

    if filename == 'CIFAR':
        ## for a multi-class classification dataset
        ## Currently, we only support experiments that are based on the CIFAR10 dataset.
        for (u,v) in combinations(range(10), 2):
            filename_tmp = filename+str(u)+str(v)
            main(config=config, filename=filename_tmp, n_trials=n_trials, wandb_log=wandb_log)
    
    else:
        ## for a binary classification dataset
        main(config=config, filename=filename, n_trials=n_trials, wandb_log=wandb_log)

## Image dataset
# CIFAR10: https://www.cs.toronto.edu/~kriz/cifar.html
# PCam: https://github.com/basveeling/pcam

# example bash: 
# python reg_image.py -F="CIFAR35" -R=5 -dr=0.1 -WD=0.0 --no-log --no-aug
