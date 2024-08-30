
#### SST2 - model: BiLSTM ####


-- CONFIG --

{'batch_size': 64,
 'dataset': 'SST2',
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'net': 'BiLSTM',
           'pretrain': 'albert-base-v2'},
 'optimizer': {'args': {'T_max': 150},
               'lr': 2e-05,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'AdamW',
               'weight_decay': 1e-05},
 'save_model': False,
 'trainer': {'epochs': 150,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7929 | 0.7892 |  0.7835 |    0.8005 |
| ('test_acc', 'std')  | 0.0061 | 0.0043 |  0.0052 |    0.0024 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8486 | 0.8381 |  0.8518 |    0.8631 |
| ('test_auc', 'std')  | 0.0035 | 0.0081 |  0.0043 |    0.0036 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.1181 | -1.3926 | less          |
|  6 | Hinge | ensLoss |   0.0121 | -3.5338 | less          |
|  9 | EXP   | ensLoss |   0.0658 | -1.8916 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.8819 | -1.3926 | greater       |
|  6 | Hinge | ensLoss |   0.9879 | -3.5338 | greater       |
|  9 | EXP   | ensLoss |   0.9342 | -1.8916 | greater       |

#### SST2 - model: BiLSTM ####


-- CONFIG --

{'batch_size': 64,
 'dataset': 'SST2',
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'net': 'BiLSTM',
           'pretrain': 'albert-base-v2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 2e-05,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'AdamW',
               'weight_decay': 1e-05},
 'save_model': False,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7819 | 0.7739 |  0.7805 |    0.7857 |
| ('test_acc', 'std')  | 0.0029 | 0.0015 |  0.0037 |    0.0034 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8481 | 0.8415 |  0.837  |    0.8593 |
| ('test_auc', 'std')  | 0.0032 | 0.0024 |  0.0035 |    0.0025 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.1858 | -0.9405 | less          |
|  6 | Hinge | ensLoss |   0.0617 | -1.7002 | less          |
|  9 | EXP   | ensLoss |   0.0067 | -3.0684 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.8142 | -0.9405 | greater       |
|  6 | Hinge | ensLoss |   0.9383 | -1.7002 | greater       |
|  9 | EXP   | ensLoss |   0.9933 | -3.0684 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0063 | -3.1058 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -5.8331 | less          |
|  9 | EXP   | ensLoss |   0.0009 | -4.3433 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9937 | -3.1058 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -5.8331 | greater       |
|  9 | EXP   | ensLoss |   0.9991 | -4.3433 | greater       |

#### SST2 - model: LSTM ####


-- CONFIG --

{'batch_size': 64,
 'dataset': 'SST2',
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'net': 'LSTM',
           'pretrain': 'albert-base-v2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 2e-05,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'AdamW',
               'weight_decay': 1e-05},
 'save_model': False,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7836 | 0.7808 |  0.7787 |    0.7735 |
| ('test_acc', 'std')  | 0.0018 | 0.0023 |  0.0043 |    0.004  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8436 | 0.8416 |  0.8119 |    0.8305 |
| ('test_auc', 'std')  | 0.0018 | 0.0026 |  0.0041 |    0.004  |

-- Testing --

|    | A     | B       |   pvalue |   stat | alternative   |
|---:|:------|:--------|---------:|-------:|:--------------|
|  3 | BCE   | ensLoss |   0.976  | 2.2878 | less          |
|  6 | Hinge | ensLoss |   0.7912 | 0.8497 | less          |
|  9 | EXP   | ensLoss |   0.9564 | 1.9196 | less          |


|    | A     | B       |   pvalue |   stat | alternative   |
|---:|:------|:--------|---------:|-------:|:--------------|
|  3 | BCE   | ensLoss |   0.024  | 2.2878 | greater       |
|  6 | Hinge | ensLoss |   0.2088 | 0.8497 | greater       |
|  9 | EXP   | ensLoss |   0.0436 | 1.9196 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9836 |  2.5184 | less          |
|  6 | Hinge | ensLoss |   0.0063 | -3.1083 | less          |
|  9 | EXP   | ensLoss |   0.9869 |  2.6574 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0164 |  2.5184 | greater       |
|  6 | Hinge | ensLoss |   0.9937 | -3.1083 | greater       |
|  9 | EXP   | ensLoss |   0.0131 |  2.6574 | greater       |

#### SST2 - model: BiLSTM ####


-- CONFIG --

{'batch_size': 64,
 'dataset': 'SST2',
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'net': 'BiLSTM'},
 'optimizer': {'args': {'T_max': 100},
               'lr': 2e-05,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'AdamW',
               'weight_decay': 1e-05},
 'save_model': False,
 'trainer': {'epochs': 100,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7992 | 0.8079 |  0.7924 |    0.8069 |
| ('test_acc', 'std')  | 0.0022 | 0.0019 |  0.0052 |    0.0032 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.878  | 0.8863 |  0.8706 |    0.8715 |
| ('test_auc', 'std')  | 0.0021 | 0.0013 |  0.0047 |    0.0028 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0415 | -1.9504 | less          |
|  6 | Hinge | ensLoss |   0.0024 | -3.7023 | less          |
|  9 | EXP   | ensLoss |   0.6194 |  0.3133 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9585 | -1.9504 | greater       |
|  6 | Hinge | ensLoss |   0.9976 | -3.7023 | greater       |
|  9 | EXP   | ensLoss |   0.3806 |  0.3133 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9359 |  1.6753 | less          |
|  6 | Hinge | ensLoss |   0.4446 | -0.1434 | less          |
|  9 | EXP   | ensLoss |   0.9993 |  4.5112 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0641 |  1.6753 | greater       |
|  6 | Hinge | ensLoss |   0.5554 | -0.1434 | greater       |
|  9 | EXP   | ensLoss |   0.0007 |  4.5112 | greater       |
