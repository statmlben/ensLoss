import numpy as np
import pandas as pd
import random
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

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

## spine dataset
def spine_data(random_state=0):
    filename='./dataset/biodeg.csv'
    df = pd.read_csv(filename)
    df = df.iloc[:, :-1]

    encode_map = {'Abnormal': 1, 'Normal': 0}
    df['Class_att'].replace(encode_map, inplace=True)
    df['Class_att'] = df['Class_att'].astype('float')

    X = df.iloc[:, 0:-1]
    y = df.iloc[:, -1]
    X = X.values
    y = y.values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=random_state)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    train_data = TrainData(torch.FloatTensor(X_train), torch.FloatTensor(y_train))
    test_data = TrainData(torch.FloatTensor(X_test), torch.FloatTensor(y_test))
    return train_data, test_data

## sonar dataset
def sonar_data(random_state=0):
    filename='./dataset/sonar_csv.csv'
    df = pd.read_csv(filename)

    encode_map = {'Rock': 1, 'Mine': 0}
    df['Class'].replace(encode_map, inplace=True)
    df['Class'] = df['Class'].astype('float')

    X = df.iloc[:, 0:-1]
    y = df.iloc[:, -1]
    X = X.values
    y = y.values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=random_state)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    train_data = TrainData(torch.FloatTensor(X_train), torch.FloatTensor(y_train))
    test_data = TrainData(torch.FloatTensor(X_test), torch.FloatTensor(y_test))
    return train_data, test_data

## qsar-biodeg dataset
def biodeg_data(random_state=0):
    filename='./dataset/biodeg.csv'
    df = pd.read_csv(filename, sep=";", header=None)

    encode_map = {'RB': 1, 'NRB': 0}
    df[41].replace(encode_map, inplace=True)
    df[41] = df[41].astype('float')

    X = df.iloc[:, 0:-1]
    y = df.iloc[:, -1]
    X = X.values
    y = y.values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=random_state)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    train_data = TrainData(torch.FloatTensor(X_train), torch.FloatTensor(y_train))
    test_data = TrainData(torch.FloatTensor(X_test), torch.FloatTensor(y_test))
    return train_data, test_data

