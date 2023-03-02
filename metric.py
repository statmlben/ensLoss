import numpy as np
import pandas as pd

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, roc_auc_score

def binary_acc(y_pred, y_test):
    y_pred_tag = torch.round(torch.sigmoid(y_pred))

    correct_results_sum = (y_pred_tag == y_test).sum().float()
    acc = correct_results_sum/y_test.shape[0]
    # acc = torch.round(acc * 100)
    return acc

def binary_auc(y_pred, y_test):
    return roc_auc_score(y_test, torch.sigmoid(y_pred))