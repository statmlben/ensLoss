import numpy as np
import pandas as pd
from torch import einsum
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

# main class

class TabMLP(nn.Module):
    def __init__(self, input_shape=12, H=128, D=1):
        super(TabMLP, self).__init__()
        self.H = H
        self.D = D
        self.layer_1 = nn.Linear(input_shape, H) 
        self.layer_2 = nn.Linear(H, H)
        self.layer_3 = nn.Linear(H, H)
        self.layer_out = nn.Linear(H, 1)
        self.relu = nn.ReLU()
        self.batchnorm1 = nn.BatchNorm1d(H)
        self.batchnorm2 = nn.BatchNorm1d(H)
        self.batchnorm3 = nn.BatchNorm1d(H)

    def forward(self, inputs):
        x = self.relu(self.layer_1(inputs))
        x = self.batchnorm1(x)
        if self.D > 1:
            x = self.relu(self.layer_2(x))
            x = self.batchnorm2(x)
        if self.D > 2:
            x = self.relu(self.layer_3(x))
            x = self.batchnorm3(x)
        # x = self.dropout(x)
        x = self.layer_out(x)
        return x

class TabMLP1(nn.Module):
    def __init__(self, input_shape=12, H=128):
        super(TabMLP3, self).__init__()
        self.H = H
        self.D = 5
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
    def __init__(self, input_shape=12, H=128):
        super(TabMLP3, self).__init__()
        self.H = H
        self.D = 5
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
    def __init__(self, input_shape=12, H=128):
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

