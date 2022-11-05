import numpy as np
import pandas as pd

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score


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