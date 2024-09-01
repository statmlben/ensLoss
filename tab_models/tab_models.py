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
                
        n_hidden = params.get('n_hidden', 2)
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

class conbr_block(nn.Module):
    def __init__(self, in_layer, out_layer, kernel_size, stride, dilation):
        super(conbr_block, self).__init__()

        self.conv1 = nn.Conv1d(in_layer, out_layer, kernel_size=kernel_size, stride=stride, dilation = dilation, padding = 3, bias=True)
        self.bn = nn.BatchNorm1d(out_layer)
        self.relu = nn.ReLU()
    
    def forward(self,x):
        x = self.conv1(x)
        x = self.bn(x)
        out = self.relu(x)
        
        return out       

class se_block(nn.Module):
    def __init__(self,in_layer, out_layer):
        super(se_block, self).__init__()
        
        self.conv1 = nn.Conv1d(in_layer, out_layer//8, kernel_size=1, padding=0)
        self.conv2 = nn.Conv1d(out_layer//8, in_layer, kernel_size=1, padding=0)
        self.fc = nn.Linear(1,out_layer//8)
        self.fc2 = nn.Linear(out_layer//8,out_layer)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()
    
    def forward(self,x):

        x_se = nn.functional.adaptive_avg_pool1d(x,1)
        x_se = self.conv1(x_se)
        x_se = self.relu(x_se)
        x_se = self.conv2(x_se)
        x_se = self.sigmoid(x_se)
        
        x_out = torch.add(x, x_se)
        return x_out

class re_block(nn.Module):
    def __init__(self, in_layer, out_layer, kernel_size, dilation):
        super(re_block, self).__init__()
        
        self.cbr1 = conbr_block(in_layer,out_layer, kernel_size, 1, dilation)
        self.cbr2 = conbr_block(out_layer,out_layer, kernel_size, 1, dilation)
        self.seblock = se_block(out_layer, out_layer)
    
    def forward(self,x):

        x_re = self.cbr1(x)
        x_re = self.cbr2(x_re)
        x_re = self.seblock(x_re)
        x_out = torch.add(x, x_re)
        return x_out          

class UNET_1D(nn.Module):
    """
    UNET for Tabular data.

    Credit: https://www.kaggle.com/code/syerramilli/ps3e24-pytorch-tabular-resnet
    """
    def __init__(self ,input_dim,layer_n,kernel_size,depth):
        super(UNET_1D, self).__init__()
        self.input_dim = input_dim
        self.layer_n = layer_n
        self.kernel_size = kernel_size
        self.depth = depth
        
        self.AvgPool1D1 = nn.AvgPool1d(input_dim, stride=5)
        self.AvgPool1D2 = nn.AvgPool1d(input_dim, stride=25)
        self.AvgPool1D3 = nn.AvgPool1d(input_dim, stride=125)
        
        self.layer1 = self.down_layer(self.input_dim, self.layer_n, self.kernel_size,1, 2)
        self.layer2 = self.down_layer(self.layer_n, int(self.layer_n*2), self.kernel_size,5, 2)
        self.layer3 = self.down_layer(int(self.layer_n*2)+int(self.input_dim), int(self.layer_n*3), self.kernel_size,5, 2)
        self.layer4 = self.down_layer(int(self.layer_n*3)+int(self.input_dim), int(self.layer_n*4), self.kernel_size,5, 2)
        self.layer5 = self.down_layer(int(self.layer_n*4)+int(self.input_dim), int(self.layer_n*5), self.kernel_size,4, 2)

        self.cbr_up1 = conbr_block(int(self.layer_n*7), int(self.layer_n*3), self.kernel_size, 1, 1)
        self.cbr_up2 = conbr_block(int(self.layer_n*5), int(self.layer_n*2), self.kernel_size, 1, 1)
        self.cbr_up3 = conbr_block(int(self.layer_n*3), self.layer_n, self.kernel_size, 1, 1)
        self.upsample = nn.Upsample(scale_factor=5, mode='nearest')
        self.upsample1 = nn.Upsample(scale_factor=5, mode='nearest')
        
        self.outcov = nn.Conv1d(self.layer_n, 11, kernel_size=self.kernel_size, stride=1,padding = 3)
    
        
    def down_layer(self, input_layer, out_layer, kernel, stride, depth):
        block = []
        block.append(conbr_block(input_layer, out_layer, kernel, stride, 1))
        for i in range(depth):
            block.append(re_block(out_layer,out_layer,kernel,1))
        return nn.Sequential(*block)
            
    def forward(self, x):
        
        pool_x1 = self.AvgPool1D1(x)
        pool_x2 = self.AvgPool1D2(x)
        pool_x3 = self.AvgPool1D3(x)
        
        #############Encoder#####################
        
        out_0 = self.layer1(x)
        out_1 = self.layer2(out_0)
        
        x = torch.cat([out_1,pool_x1],1)
        out_2 = self.layer3(x)
        
        x = torch.cat([out_2,pool_x2],1)
        x = self.layer4(x)
        
        #############Decoder####################
        
        up = self.upsample1(x)
        up = torch.cat([up,out_2],1)
        up = self.cbr_up1(up)
        
        up = self.upsample(up)
        up = torch.cat([up,out_1],1)
        up = self.cbr_up2(up)
        
        up = self.upsample(up)
        up = torch.cat([up,out_0],1)
        up = self.cbr_up3(up)
        
        out = self.outcov(up)
        
        #out = nn.functional.softmax(out,dim=2)
        
        return out

def UNet3(input_shape:int):
    return UNET_1D(input_dim=1, layer_n=128, kernel_size=7, depth=3)
