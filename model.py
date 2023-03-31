import numpy as np
import pandas as pd

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torchvision import datasets, models, transforms


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
        # self.layer_1 = nn.Linear(input_shape, int(input_shape/2)) 
        # self.layer_2 = nn.Linear(int(input_shape/2), int(input_shape/4))
        # self.layer_3 = nn.Linear(int(input_shape/4), int(input_shape/8))
        # self.layer_out = nn.Linear(int(input_shape/(2**D)), 1)
        # self.relu = nn.ReLU()
        # # self.dropout = nn.Dropout(p=0.1)
        # self.batchnorm1 = nn.BatchNorm1d(int(input_shape/2))
        # self.batchnorm2 = nn.BatchNorm1d(int(input_shape/4))
        # self.batchnorm3 = nn.BatchNorm1d(int(input_shape/8))

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

class MHIST_CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 32, 3)
        self.conv2 = nn.Conv2d(32, 64, 3)
        self.conv3 = nn.Conv2d(64, 128, 3)
        self.pool = nn.MaxPool2d(2, 2)

        self.fc1 = nn.Linear(86528, 1024)
        self.fc2 = nn.Linear(1024, 512)
        self.fc3 = nn.Linear(512, 1)

    def forward(self, x):
        ## 224x224
        x = self.pool(F.relu(self.conv1(x))) # out_shape= 32x111x111
        x = self.pool(F.relu(self.conv2(x))) # out_shape= 64x54x54
        x = self.pool(F.relu(self.conv3(x))) # out_shape= 128x26x26

        x = torch.flatten(x, 1) # out_shape=86528
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

def MHIST_resnet18(weight=None):
    model = models.resnet18(weights='DEFAULT')
    num_features = model.fc.in_features     
    model.fc = nn.Linear(num_features, 1)   #(num_of_class == 1)
    return model