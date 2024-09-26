import numpy as np
import pandas as pd
from torch import einsum
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

# main class
class TabMLP1(nn.Module):
    def __init__(self, input_shape=12, H=1024):
        super(TabMLP1, self).__init__()
        self.H = H
        self.D = 1
        self.layer_1 = nn.Linear(input_shape, H)
        self.batchnorm1 = nn.BatchNorm1d(H)

        self.layer_out = nn.Linear(H, 1)
        self.relu = nn.ReLU()

    def forward(self, inputs):
        x = self.relu(self.layer_1(inputs))
        x = self.batchnorm1(x)
        x = self.layer_out(x)
        return x

class TabMLP3(nn.Module):
    def __init__(self, input_shape=12, H=1024):
        super(TabMLP3, self).__init__()
        self.H = H
        self.D = 3
        self.layer_1 = nn.Linear(input_shape, H)
        self.layer_2 = nn.Linear(H, H)
        self.layer_3 = nn.Linear(H, H)

        self.batchnorm1 = nn.BatchNorm1d(H)
        self.batchnorm2 = nn.BatchNorm1d(H)
        self.batchnorm3 = nn.BatchNorm1d(H)

        self.layer_out = nn.Linear(H, 1)
        self.relu = nn.ReLU()

    def forward(self, inputs):
        x = self.relu(self.layer_1(inputs))
        x = self.batchnorm1(x)
        x = self.relu(self.layer_2(x))
        x = self.batchnorm2(x)
        x = self.relu(self.layer_3(x))
        x = self.batchnorm3(x)
        x = self.layer_out(x)
        return x

class TabMLP5(nn.Module):
    def __init__(self, input_shape=12, H=1024):
        super(TabMLP5, self).__init__()
        self.H = H
        self.D = 5
        self.layer_1 = nn.Linear(input_shape, H)
        self.layer_2 = nn.Linear(H, H)
        self.layer_3 = nn.Linear(H, H)
        self.layer_4 = nn.Linear(H, H)
        self.layer_5 = nn.Linear(H, H)

        self.batchnorm1 = nn.BatchNorm1d(H)
        self.batchnorm2 = nn.BatchNorm1d(H)
        self.batchnorm3 = nn.BatchNorm1d(H)
        self.batchnorm4 = nn.BatchNorm1d(H)
        self.batchnorm5 = nn.BatchNorm1d(H)

        self.layer_out = nn.Linear(H, 1)
        self.relu = nn.ReLU()

    def forward(self, inputs):
        x = self.relu(self.layer_1(inputs))
        x = self.batchnorm1(x)
        x = self.relu(self.layer_2(x))
        x = self.batchnorm2(x)
        x = self.relu(self.layer_3(x))
        x = self.batchnorm3(x)
        x = self.relu(self.layer_4(x))
        x = self.batchnorm4(x)
        x = self.relu(self.layer_5(x))
        x = self.batchnorm5(x)
        x = self.layer_out(x)
        return x

def make_normalization(normalization:str, input_dim:int):
    '''utility function to return the normlaiation layer'''
    return {'batchnorm': nn.BatchNorm1d, 'layernorm': nn.LayerNorm}[
        normalization
    ](input_dim)

class ResNetBlock(nn.Module):
    def __init__(
        self, 
        input_dim:int, 
        normalization:str,
        hidden_factor:float=2, hidden_dropout:float = 0.1, 
        residual_dropout:float = 0.05
    ):
        super().__init__()
        # hidden size
        d_hidden = int(hidden_factor *  input_dim)
        
        self.ff = nn.Sequential(
            # make_normalization(normalization, input_dim),
            nn.Linear(input_dim, d_hidden),
            nn.ReLU(),
            nn.Dropout(hidden_dropout), # first dropout
            nn.Linear(d_hidden, input_dim),
            nn.Dropout(residual_dropout)
        )
        
    def forward(self, x:torch.Tensor) -> torch.Tensor:
        return x + self.ff(x)

class ResNet(nn.Module):
    """
    ResNet for Tabular data.

    Credit: https://www.kaggle.com/code/syerramilli/ps3e24-pytorch-tabular-resnet
    """
    def __init__(self, input_shape:int, params:dict={}, verbose=False):
        super(ResNet, self).__init__()
        self.params = params
        self.input_shape = input_shape
        self.verbose = []
                
        n_hidden = params.get('n_hidden', 3)
        layer_size = params.get('layer_size', 1024)
        normalization = params.get('normalization', 'layernorm')
        hidden_factor = params.get('hidden_factor', 2.)
        hidden_dropout = params.get('hidden_dropout', 0.1)
        residual_dropout = params.get('residual_dropout', 0.05)
        
        self.ff = nn.Sequential(
            nn.Linear(input_shape, layer_size)
        )
        for _ in range(n_hidden):
            self.ff.append(ResNetBlock(layer_size, normalization, hidden_factor, hidden_dropout, residual_dropout))
        
        # output layer
        self.prediction = nn.Sequential(
            make_normalization(normalization, layer_size),
            nn.ReLU(),
            nn.Linear(layer_size, 1),
            # nn.Sigmoid()
        )
        
    def forward(self, x:torch.Tensor) -> torch.Tensor:
        return self.prediction(self.ff(x))


def ResNet3(input_shape:int):
    return ResNet(input_shape=input_shape, params={'n_hidden': 3})

def ResNet5(input_shape:int):
    return ResNet(input_shape=input_shape, params={'n_hidden': 5})

def ResNet7(input_shape:int):
    return ResNet(input_shape=input_shape, params={'n_hidden': 7})

def ResNet10(input_shape:int):
    return ResNet(input_shape=input_shape, params={'n_hidden': 10})

def ResNet20(input_shape:int):
    return ResNet(input_shape=input_shape, params={'n_hidden': 20})

def ResNet30(input_shape:int):
    return ResNet(input_shape=input_shape, params={'n_hidden': 30})

