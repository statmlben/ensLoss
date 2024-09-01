# -*- coding: utf-8 -*-
"""
(Bi)LSTM for text data

Credict: https://github.com/zachAlbus/pyTorch-text-classification/blob/master/Zhang/model.py
"""

import torch
from torch import nn
from transformers import (
    BertForSequenceClassification, 
    AlbertForSequenceClassification, 
    XLNetForSequenceClassification, 
    RobertaForSequenceClassification, 
    BertTokenizer
)
from torch.autograd import Variable

class LSTM(nn.Module):
    def __init__(self, embedding_dim=300, hidden_dim=1000, lstm_layers=2, fc_dim=512, output_dim=1):
        self.use_gpu = torch.cuda.is_available()
        self.hidden_dim = hidden_dim
        self.batch_size = 64
        self.lstm_layers = lstm_layers
        super(LSTM, self).__init__()
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
        self.embedding = nn.Embedding(len(self.tokenizer), embedding_dim)
        self.lstm = nn.LSTM(
            embedding_dim,
            hidden_dim,
            num_layers=lstm_layers,
        )
        self.fc = nn.Linear(hidden_dim, fc_dim)
        self.classifier = nn.Linear(fc_dim, output_dim)
        self.hidden = self.init_hidden()
        self.relu = nn.ReLU()

    def init_hidden(self, batch_size=None):
        if batch_size is None:
            batch_size= self.batch_size
        
        if self.use_gpu:
            h0 = Variable(torch.zeros(self.lstm_layers, batch_size, self.hidden_dim).cuda())
            c0 = Variable(torch.zeros(self.lstm_layers, batch_size, self.hidden_dim).cuda())
        else:
            h0 = Variable(torch.zeros(self.lstm_layers, batch_size, self.hidden_dim))
            c0 = Variable(torch.zeros(self.lstm_layers,batch_size, self.hidden_dim))
        return (h0, c0)

    def forward(self, batch_seqs, batch_seq_masks=None, batch_seq_segments=None):
        x = self.embedding(batch_seqs) # batch x sen_len x emb_size
        x = x.permute(1,0,2) # sen_len x batch x emb_size
        self.hidden= self.init_hidden(batch_seqs.size()[0]) #1x64x128
        x, _ = self.lstm(x, self.hidden)
        ## reduce by mean
        x = x.permute(1,0,2)
        x = torch.amax(x, 1)
        ## connect to fc
        x = self.relu(self.fc(x))
        out = self.classifier(x)
        return out

class BiLSTM(nn.Module):
    def __init__(self, embedding_dim=300, hidden_dim=500, lstm_layers=2, fc_dim=512, output_dim=1):
        self.use_gpu = torch.cuda.is_available()
        self.hidden_dim = hidden_dim
        self.batch_size = 64
        self.lstm_layers = lstm_layers
        super(BiLSTM, self).__init__()
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
        self.embedding = nn.Embedding(len(self.tokenizer), embedding_dim)
        self.lstm = nn.LSTM(
            embedding_dim,
            hidden_dim // 2,
            num_layers=lstm_layers,
            bidirectional = True
        )
        self.fc = nn.Linear(hidden_dim, fc_dim)
        self.classifier = nn.Linear(fc_dim, output_dim)
        self.hidden = self.init_hidden()
        self.relu = nn.ReLU()

    def init_hidden(self, batch_size=None):
        if batch_size is None:
            batch_size= self.batch_size
        
        if self.use_gpu:
            h0 = Variable(torch.zeros(2*self.lstm_layers, batch_size, self.hidden_dim // 2).cuda())
            c0 = Variable(torch.zeros(2*self.lstm_layers, batch_size, self.hidden_dim // 2).cuda())
        else:
            h0 = Variable(torch.zeros(2*self.lstm_layers, batch_size, self.hidden_dim // 2))
            c0 = Variable(torch.zeros(2*self.lstm_layers, batch_size, self.hidden_dim // 2))
        return (h0, c0)

    def forward(self, batch_seqs, batch_seq_masks=None, batch_seq_segments=None):
        x = self.embedding(batch_seqs) # batch x sen_len x emb_size
        x = x.permute(1,0,2) # sen_len x batch x emb_size
        self.hidden= self.init_hidden(batch_seqs.size()[0]) #1x64x128
        x, _ = self.lstm(x, self.hidden)
        ## reduce by mean
        x = x.permute(1,0,2)
        x = torch.amax(x, 1)
        ## connect to fc
        x = self.relu(self.fc(x))
        out = self.classifier(x)
        return out
