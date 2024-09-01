"""
CNN for text data

Credict: https://github.com/zachAlbus/pyTorch-text-classification/blob/master/Zhang/model.py
"""

import torch
from torch import nn
from transformers import AutoTokenizer
from torch.autograd import Variable

class CNN(nn.Module):
    def __init__(self, embedding_dim=300, hidden_dim=128, output_dim=1):
        self.use_gpu = torch.cuda.is_available()
        self.hidden_dim = hidden_dim
        super(CNN, self).__init__()
        self.tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
        self.embedding = nn.Embedding(len(self.tokenizer), embedding_dim)


        self.conv1 = nn.Sequential(
            nn.Conv1d(1, 256, kernel_size=7, stride=1),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=3, stride=3)
        )

        self.conv2 = nn.Sequential(
            nn.Conv1d(256, 256, kernel_size=7, stride=1),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=3, stride=3)
        )

        self.conv3 = nn.Sequential(
            nn.Conv1d(256, 256, kernel_size=3, stride=1),
            nn.ReLU()
        )

        self.conv4 = nn.Sequential(
            nn.Conv1d(256, 256, kernel_size=3, stride=1),
            nn.ReLU()
        )

        self.conv5 = nn.Sequential(
            nn.Conv1d(256, 256, kernel_size=3, stride=1),
            nn.ReLU()
        )

        self.conv6 = nn.Sequential(
            nn.Conv1d(256, 256, kernel_size=3, stride=1),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=3, stride=3)
        )

        self.fc = nn.Linear(256, output_dim)

    def forward(self, batch_seqs, batch_seq_masks=None, batch_seq_segments=None):
        x = self.embedding(batch_seqs) # batch x sen_len x emb_size
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.conv5(x)
        x = self.conv6(x)
        # collapse
        x = x.view(x.size(0), -1)
        out = self.fc(x)
        return out
