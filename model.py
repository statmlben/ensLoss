import numpy as np
import pandas as pd

import torch
import torch.nn as nn
import torch.optim as optim

class BinaryClassification(nn.Module):
    def __init__(self, input_shape=12, H=128, D=1):
        super(BinaryClassification, self).__init__()        # Number of input features is 12.
        self.H = H
        self.D = D
        self.layer_1 = nn.Linear(input_shape, H) 
        self.layer_2 = nn.Linear(H, H)
        self.layer_3 = nn.Linear(H, H)
        self.layer_out = nn.Linear(H, 1)
        self.relu = nn.ReLU()
        # self.dropout = nn.Dropout(p=0.1)
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