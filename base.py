import numpy as np
import pandas as pd

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from scipy.stats import ttest_ind, ttest_1samp
from itertools import combinations, permutations

def evaluate(model, loader, y_test, device):
    y_pred_list = []
    model.eval()

    with torch.no_grad():
        for X_batch in loader:
            X_batch = X_batch.to(device)
            y_test_pred = model(X_batch)
            y_test_pred = torch.sigmoid(y_test_pred)
            y_pred_tag = torch.round(y_test_pred)
            y_pred_list.extend(y_pred_tag.cpu().numpy())

    y_pred_list = np.array(y_pred_list).flatten()
    acc = accuracy_score(y_test, y_pred_list)
    return acc, y_pred_list


def pairwise_ttest(df, val_col, group_col, subject='trial', alternative='less'):
    res = {'A': [], 'B':[], 'pvalue': [], 'stat': [], 'alternative': []}
    group_lst = df[group_col].unique()
    perm = permutations(group_lst, 2)
    for g1, g2 in perm:
        diff = df[df[group_col] == g1].set_index(subject)[val_col] - df[df[group_col] == g2].set_index(subject)[val_col]
        test_res = ttest_1samp(diff, popmean=0.0, alternative=alternative)
        res['A'].append(g1)
        res['B'].append(g2)
        res['pvalue'].append(test_res.pvalue)
        res['alternative'].append(alternative)
        res['stat'].append(test_res.statistic)
    res = pd.DataFrame(res)
    return res

# Credict: https://discuss.pytorch.org/t/where-and-how-to-add-dropout-in-resnet18/12869/3
def append_dropout(model, rate=0.2):
    for name, module in model.named_children():
        if len(list(module.children())) > 0:
            print(name)
            print(module)
            append_dropout(module)
        if isinstance(module, nn.ReLU):
            print('Dropout layer: %s' %name)
            new = nn.Sequential(module, nn.Dropout2d(p=rate, inplace=True))
            setattr(model, name, new)