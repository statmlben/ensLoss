# -*- coding: utf-8 -*-
"""
Transformers models for text data
"""

import torch
from torch import nn
from transformers import (
    BertForSequenceClassification, 
    AlbertForSequenceClassification, 
    XLNetForSequenceClassification, 
    RobertaForSequenceClassification, 
    AutoTokenizer
)
from torch.autograd import Variable

class AlbertModel(nn.Module):
    def __init__(self, requires_grad = True):
        super(AlbertModel, self).__init__()
        self.albert = AlbertForSequenceClassification.from_pretrained('albert-base-v2')
        self.tokenizer = AutoTokenizer.from_pretrained('albert-base-v2', do_lower_case=True)
        self.requires_grad = requires_grad
        self.device = torch.device("cuda")
        self.out = nn.Linear(2, 1)

        for param in self.albert.parameters():
            param.requires_grad = True  # Each parameter requires gradient

    def forward(self, batch_seqs, batch_seq_masks, batch_seq_segments):
        # sequence_output, pooled_output = self.albert(input_ids = batch_seqs, attention_mask = batch_seq_masks, 
        #                                              token_type_ids=batch_seq_segments)
        logits = self.albert(input_ids = batch_seqs, attention_mask = batch_seq_masks, 
                              token_type_ids=batch_seq_segments).logits
        logits = self.out(logits)
        return logits
        
class BertModel(nn.Module):
    def __init__(self, requires_grad = True):
        super(BertModel, self).__init__()
        self.bert = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels = 1)
        self.tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
        self.requires_grad = requires_grad
        self.device = torch.device("cuda")
        for param in self.bert.parameters():
            param.requires_grad = requires_grad  # Each parameter requires gradient

    def forward(self, batch_seqs, batch_seq_masks, batch_seq_segments):
        logits = self.bert(input_ids = batch_seqs, attention_mask = batch_seq_masks, 
                              token_type_ids=batch_seq_segments).logits
        return logits
        
class RobertModel(nn.Module):
    def __init__(self, requires_grad = True):
        super(RobertModel, self).__init__()
        self.bert = RobertaForSequenceClassification.from_pretrained('roberta-base', num_labels = 1)
        self.tokenizer = AutoTokenizer.from_pretrained('roberta-base', do_lower_case=True)
        self.requires_grad = requires_grad
        self.device = torch.device("cuda")
        for param in self.bert.parameters():
            param.requires_grad = requires_grad  # Each parameter requires gradient

    def forward(self, batch_seqs, batch_seq_masks, batch_seq_segments):
        logits = self.bert(input_ids = batch_seqs, attention_mask = batch_seq_masks, 
                              token_type_ids=batch_seq_segments).logits
        return logits
        
    
    
class XlnetModel(nn.Module):
    def __init__(self, requires_grad = True):
        super(XlnetModel, self).__init__()
        self.xlnet = XLNetForSequenceClassification.from_pretrained('xlnet-large-cased', num_labels = 2)
        self.tokenizer = AutoTokenizer.from_pretrained('xlnet-large-cased', do_lower_case=True)
        self.requires_grad = requires_grad
        self.device = torch.device("cuda")
        for param in self.xlnet.parameters():
            param.requires_grad = requires_grad  # Each parameter requires gradient

    def forward(self, batch_seqs, batch_seq_masks, batch_seq_segments, labels):
        loss, logits = self.xlnet(input_ids = batch_seqs, attention_mask = batch_seq_masks, 
                              token_type_ids=batch_seq_segments, labels = labels)[:2]
        probabilities = nn.functional.softmax(logits, dim=-1)
        return loss, logits, probabilities
