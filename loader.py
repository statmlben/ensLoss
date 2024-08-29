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
from torchtext.datasets import SST2, IMDB
from torchtext.vocab import Vectors, GloVe, CharNGram, FastText
import torchtext
## lib used for image transform argumentation
import glob
from os.path import exists
import copy
from tqdm import tqdm
from torchvision import transforms
from PIL import Image

## lib used for text transform
import torchtext.transforms as T
from torch.hub import load_state_dict_from_url
import transformers

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
def img_data(name='CIFAR35', aug=False):
    if 'CIFAR' in name:
        # classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
        # CIFAR35 = CIFAR2 (cat-dog) -> 3 (cat) vs 5 (dog)
        
        binary_class_list = [int(name[-2]), int(name[-1])]
        if aug:
            transform = transforms.Compose(
                        [
                        transforms.RandomCrop(32, padding=4),
                        transforms.RandomHorizontalFlip(),
                        transforms.ToTensor(),
                        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
        else:
            transform = transforms.Compose(
                        [
                        # transforms.ToPILImage(),
                        transforms.ToTensor(),
                        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])            

        trainset = torchvision.datasets.CIFAR10(root='./dataset', train=True,
                                        download=False, transform=transform)
        train_index = [i for i, t in enumerate(trainset.targets) if (t in binary_class_list)]
        train_data = torch.utils.data.Subset(trainset, train_index)

        testset = torchvision.datasets.CIFAR10(root='./dataset', train=False,
                                       download=False, transform=transform)
        test_index = [i for i, t in enumerate(testset.targets) if (t in binary_class_list)]
        test_data = torch.utils.data.Subset(testset, test_index)
        
        encode_map = {int(name[-2]): 0, int(name[-1]): 1}
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

    elif 'FER' in name:
        binary_class_list = [int(name[-2]), int(name[-1])]
        transform = transforms.Compose(
            [
            # transforms.ToPILImage(),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

        train_data = torchvision.datasets.FER2013(root='./dataset', split="train", transform=transform)
        train_index = [i for i, t in enumerate(train_data.targets) if (t in binary_class_list)]
        train_data = torch.utils.data.Subset(trainset, train_index)
        
        test_data = torchvision.datasets.FER2013(root='./dataset', split="val",
                                       download=False, transform=transform)
        
    else:
        raise Exception("Sorry, no dataset provided.") 
    return train_data, test_data

# Transform the raw dataset using non-batched API (i.e apply transformation line by line)
# def text_data(name='SST2', batch_size=128):
#     train_datapipe = IMDB(split="train")
#     test_datapipe = IMDB(split="test")

#     train_loader = DataLoader(train_datapipe, 
#                                  shuffle=True, batch_size=batch_size, 
#                                  collate_fn=collate_batch)
#     test_loader = DataLoader(test_datapipe, 
#                                  batch_size=batch_size,
#                                  collate_fn=collate_batch)
#     return train_loader, test_loader

# def collate_batch(batch):
#     ids, types, masks, label_list = [], [], [], []

#     tokenizer = transformers.AlbertTokenizer.from_pretrained("albert-base-v2", do_lower_case=True)
#     max_input_length = 50

#     for text, label in batch:
#         tokenized = tokenizer(text,
#                               padding="max_length", max_length=max_input_length,
#                               truncation=True, return_tensors="pt")
#         ids.append(tokenized['input_ids'])
#         types.append(tokenized['token_type_ids'])
#         masks.append(tokenized['attention_mask'])
#         label_list.append(label)

#     input_data = {
#         "input_ids": torch.squeeze(torch.stack(ids)),
#         "token_type_ids": torch.squeeze(torch.stack(types)),
#         "attention_mask": torch.squeeze(torch.stack(masks))
#     }
#     label_list = torch.tensor(label_list, dtype=torch.int64)
#     return input_data, label_list

def text_data(tokenizer, name='SST2', max_seq_len=50):
    data_path = "./dataset/SST2/"
    train_df = pd.read_csv(os.path.join(data_path,"train.tsv"),sep='\t')
    test_df = pd.read_csv(os.path.join(data_path,"dev.tsv"),sep='\t')
    train_data = DataPrecessForSentence(tokenizer, train_df, max_seq_len = max_seq_len)
    test_data = DataPrecessForSentence(tokenizer, test_df, max_seq_len = max_seq_len)

    return train_data, test_data

class DataPrecessForSentence(Dataset):
    """
    Encoding sentences

    Created on Mon Nov  2 14:24:49 2020

    @author: Jiang Yuxin
    https://github.com/YJiangcm/SST-2-sentiment-analysis/blob/master/data_sst2.py
    """
    
    def __init__(self, bert_tokenizer, df, max_seq_len = 50):
        super(DataPrecessForSentence, self).__init__()
        self.bert_tokenizer = bert_tokenizer
        self.max_seq_len = max_seq_len
        self.input_ids, self.attention_mask, self.token_type_ids, self.labels = self.get_input(df)
        
    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return self.input_ids[idx], self.attention_mask[idx], self.token_type_ids[idx], self.labels[idx]
        
    # Convert dataframe to tensor
    def get_input(self, df):
        sentences = df['sentence'].values
        labels = df['label'].values
        
        # tokenizer
        tokens_seq = list(map(self.bert_tokenizer.tokenize, sentences)) # list of shape [sentence_len, token_len]
        
        # Get fixed-length sequence and its mask
        result = list(map(self.trunate_and_pad, tokens_seq))
        
        input_ids = [i[0] for i in result]
        attention_mask = [i[1] for i in result]
        token_type_ids = [i[2] for i in result]
        
        return (
               torch.Tensor(input_ids).type(torch.long), 
               torch.Tensor(attention_mask).type(torch.long),
               torch.Tensor(token_type_ids).type(torch.long), 
               torch.Tensor(labels).type(torch.long)
               )
    
    def trunate_and_pad(self, tokens_seq):
        
        # Concat '[CLS]' at the beginning
        tokens_seq = ['[CLS]'] + tokens_seq     
        # Truncate sequences of which the lengths exceed the max_seq_len
        if len(tokens_seq) > self.max_seq_len:
            tokens_seq = tokens_seq[0 : self.max_seq_len]           
        # Generate padding
        padding = [0] * (self.max_seq_len - len(tokens_seq))       
        # Convert tokens_seq to token_ids
        input_ids = self.bert_tokenizer.convert_tokens_to_ids(tokens_seq)
        input_ids += padding   
        # Create attention_mask
        attention_mask = [1] * len(tokens_seq) + padding     
        # Create token_type_ids
        token_type_ids = [0] * (self.max_seq_len)
        
        assert len(input_ids) == self.max_seq_len
        assert len(attention_mask) == self.max_seq_len
        assert len(token_type_ids) == self.max_seq_len
        
        return input_ids, attention_mask, token_type_ids
