import numpy as np
import pandas as pd

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from scipy.stats import ttest_ind, ttest_1samp
from itertools import combinations, permutations

import plotly.express as px
import plotly.graph_objs as go

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

def line(error_y_mode=None, **kwargs):
    """Extension of `plotly.express.line` to use error bands."""
    ERROR_MODES = {'bar','band','bars','bands',None}
    if error_y_mode not in ERROR_MODES:
        raise ValueError(f"'error_y_mode' must be one of {ERROR_MODES}, received {repr(error_y_mode)}.")
    if error_y_mode in {'bar','bars',None}:
        fig = px.line(**kwargs)
    elif error_y_mode in {'band','bands'}:
        if 'error_y' not in kwargs:
            raise ValueError(f"If you provide argument 'error_y_mode' you must also provide 'error_y'.")
        figure_with_error_bars = px.line(**kwargs)
        fig = px.line(**{arg: val for arg,val in kwargs.items() if arg != 'error_y'})
        for data in figure_with_error_bars.data:
            x = list(data['x'])
            y_upper = list(data['y'] + data['error_y']['array'])
            y_lower = list(data['y'] - data['error_y']['array'] if data['error_y']['arrayminus'] is None else data['y'] - data['error_y']['arrayminus'])
            color = f"rgba({tuple(int(data['line']['color'].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))},.3)".replace('((','(').replace('),',',').replace(' ','')
            fig.add_trace(
                go.Scatter(
                    x = x+x[::-1],
                    y = y_upper+y_lower[::-1],
                    fill = 'toself',
                    fillcolor = color,
                    line = dict(
                        color = 'rgba(255,255,255,0)'
                    ),
                    hoverinfo = "skip",
                    showlegend = False,
                    legendgroup = data['legendgroup'],
                    xaxis = data['xaxis'],
                    yaxis = data['yaxis'],
                )
            )
        # Reorder data as said here: https://stackoverflow.com/a/66854398/8849755
        reordered_data = []
        for i in range(int(len(fig.data)/2)):
            reordered_data.append(fig.data[i+int(len(fig.data)/2)])
            reordered_data.append(fig.data[i])
        fig.data = tuple(reordered_data)
    return fig