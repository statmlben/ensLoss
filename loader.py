import numpy as np
import pandas as pd
import random
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from scipy.io.arff import loadarff 
from sklearn.datasets import fetch_openml
import os
from torchvision.io import read_image
import torchvision

## lib used for argumentation
import glob
from os.path import exists
import copy
from tqdm import tqdm
from torchvision import transforms
from PIL import Image
# from albumentations import Normalize, Compose, Rotate, CenterCrop, HorizontalFlip, RandomScale, Flip, Resize, ShiftScaleRotate, \
#     RandomCrop, IAAAdditiveGaussianNoise, ElasticTransform, HueSaturationValue, LongestMaxSize, RandomBrightnessContrast, Blur
# from albumentations.pytorch import ToTensorV2

## Reproducibility
torch.manual_seed(1024)
random.seed(1024)
np.random.seed(1024)

## train data
class TrainData(Dataset):
    def __init__(self, X_data, y_data):
        self.X_data = X_data
        self.y_data = y_data

    def __getitem__(self, index):
        return self.X_data[index], self.y_data[index]
        
    def __len__ (self):
        return len(self.X_data)

## test data
class TestData(Dataset):
    def __init__(self, X_data):
        self.X_data = X_data
        
    def __getitem__(self, index):
        return self.X_data[index]
        
    def __len__ (self):
        return len(self.X_data)

## Tabular data in openml
def openml_data(random_state=0, data_id=43969):
    dataset = fetch_openml(data_id=data_id)
    target_set = list(set(dataset.target))
    #if condition returns True, then nothing happens:
    assert len(target_set) == 2, "Only binary classification is considered."

    encode_map = {target_set[0]: 0, target_set[1]: 1}

    if data_id == 42395:
        del dataset.data['ID_code']
    X = dataset.data
    y = dataset.target
    y.replace(encode_map, inplace=True)
    
    y = y.loc[~pd.isnull(X).any(axis=1)]
    X = X.loc[~pd.isnull(X).any(axis=1)]
    
    X = X.values
    y = y.values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=random_state)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    train_data = TrainData(torch.FloatTensor(X_train), torch.FloatTensor(y_train))
    test_data = TrainData(torch.FloatTensor(X_test), torch.FloatTensor(y_test))
    return train_data, test_data

## Simulated dataset
def sim_data(n=3000, d=200, random_state=0):
    X = torch.randn(n, d)
    beta = torch.ones(d)
    score = torch.matmul(torch.relu(X), beta)
    score = (score - torch.mean(score)) / torch.std(score) * 2
    score = torch.clamp(score, max=5)
    score = torch.clamp(score, min=-5)

    prob = torch.sigmoid(score)

    y = torch.bernoulli(prob)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=random_state)
    
    train_data = TrainData(torch.FloatTensor(X_train), torch.FloatTensor(y_train))
    test_data = TrainData(torch.FloatTensor(X_test), torch.FloatTensor(y_test))
    return train_data, test_data

## image dataset
def img_data(name='CIFAR'):
    if name == 'CIFAR':
        # ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
        # 3 (cat) vs 5 (dog)
        # 2 (bird) vs 4 (deer)
        # 1 (automobile) vs 9 (truck)
            ## image tranform

        # transform_train = transforms.Compose([
        #     transforms.RandomCrop(32, padding=4),
        #     transforms.RandomHorizontalFlip(),
        #     transforms.ToTensor(),
        #     transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
        # ])

        # transform_test = transforms.Compose([
        #     transforms.ToTensor(),
        #     transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
        # ])

        transform = transforms.Compose(
                    [
                    # transforms.ToPILImage(),
                    transforms.ToTensor(),
                    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

        binary_class_list = [3, 5]
        trainset = torchvision.datasets.CIFAR10(root='./dataset', train=True,
                                        download=False, transform=transform)
        train_index = [i for i, t in enumerate(trainset.targets) if (t in binary_class_list)]
        train_data = torch.utils.data.Subset(trainset, train_index)

        testset = torchvision.datasets.CIFAR10(root='./dataset', train=False,
                                       download=False, transform=transform)
        test_index = [i for i, t in enumerate(testset.targets) if (t in binary_class_list)]
        test_data = torch.utils.data.Subset(testset, test_index)
        # print(set(train_data.dataset.targets))
        encode_map = {3: 0, 5: 1}
        train_data.dataset.targets = list(map(encode_map.get, train_data.dataset.targets))
        test_data.dataset.targets = list(map(encode_map.get, test_data.dataset.targets))

    elif name == 'PCam':
        
        transform = transforms.Compose(
            [
            # transforms.ToPILImage(),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])    

        train_data = torchvision.datasets.PCAM(root='./dataset', split="train",
                                download=True, transform=transform)
        test_data = torchvision.datasets.PCAM(root='./dataset', split="test",
                                       download=True, transform=transform)
        pass
    else:
        raise Exception("Sorry, no dataset provided.") 
    return train_data, test_data
