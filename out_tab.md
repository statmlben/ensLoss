
#### Data ID: 4134 - model: TabMLP3 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 4134,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP3'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7821 | 0.7758 |  0.7602 |    0.7782 |
| ('test_acc', 'std')  | 0.0043 | 0.0032 |  0.0043 |    0.0026 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8497 | 0.8478 |  0.8284 |    0.8521 |
| ('test_auc', 'std')  | 0.0038 | 0.0033 |  0.0035 |    0.0029 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9274 |  1.5949 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -6.1798 | less          |
|  9 | EXP   | ensLoss |   0.1858 | -0.9401 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0726 |  1.5949 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -6.1798 | greater       |
|  9 | EXP   | ensLoss |   0.8142 | -0.9401 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.1212 | -1.2515 | less          |
|  6 | Hinge | ensLoss |   0      | -8.518  | less          |
|  9 | EXP   | ensLoss |   0.0404 | -1.9672 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.8788 | -1.2515 | greater       |
|  6 | Hinge | ensLoss |   1      | -8.518  | greater       |
|  9 | EXP   | ensLoss |   0.9596 | -1.9672 | greater       |

#### Data ID: 4134 - model: TabMLP5 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 4134,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP5'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7684 | 0.7749 |  0.7603 |    0.7718 |
| ('test_acc', 'std')  | 0.0042 | 0.0046 |  0.0021 |    0.0037 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8436 | 0.8439 |  0.8285 |    0.8463 |
| ('test_auc', 'std')  | 0.0038 | 0.004  |  0.0031 |    0.0034 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0738 | -1.5845 | less          |
|  6 | Hinge | ensLoss |   0.0036 | -3.4547 | less          |
|  9 | EXP   | ensLoss |   0.8851 |  1.2881 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9262 | -1.5845 | greater       |
|  6 | Hinge | ensLoss |   0.9964 | -3.4547 | greater       |
|  9 | EXP   | ensLoss |   0.1149 |  1.2881 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0909 | -1.4467 | less          |
|  6 | Hinge | ensLoss |   0      | -8.726  | less          |
|  9 | EXP   | ensLoss |   0.1462 | -1.1185 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9091 | -1.4467 | greater       |
|  6 | Hinge | ensLoss |   1      | -8.726  | greater       |
|  9 | EXP   | ensLoss |   0.8538 | -1.1185 | greater       |

#### Data ID: 41159 - model: TabMLP3 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 41159,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP3'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7287 | 0.7323 |  0.7276 |    0.769  |
| ('test_acc', 'std')  | 0.0023 | 0.0016 |  0.0025 |    0.0021 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.7983 | 0.8006 |  0.7902 |    0.8367 |
| ('test_auc', 'std')  | 0.0019 | 0.0014 |  0.0024 |    0.0016 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -36.7354 | less          |
|  6 | Hinge | ensLoss |        0 | -23.8639 | less          |
|  9 | EXP   | ensLoss |        0 | -21.4107 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -36.7354 | greater       |
|  6 | Hinge | ensLoss |        1 | -23.8639 | greater       |
|  9 | EXP   | ensLoss |        1 | -21.4107 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -62.6589 | less          |
|  6 | Hinge | ensLoss |        0 | -37.1153 | less          |
|  9 | EXP   | ensLoss |        0 | -37.3288 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -62.6589 | greater       |
|  6 | Hinge | ensLoss |        1 | -37.1153 | greater       |
|  9 | EXP   | ensLoss |        1 | -37.3288 | greater       |

#### Data ID: 41159 - model: TabMLP5 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 41159,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP5'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7035 | 0.7026 |  0.6967 |    0.7534 |
| ('test_acc', 'std')  | 0.0014 | 0.0021 |  0.002  |    0.0025 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.7694 | 0.7674 |  0.7537 |    0.8196 |
| ('test_auc', 'std')  | 0.0018 | 0.0023 |  0.0018 |    0.0022 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -22.966  | less          |
|  6 | Hinge | ensLoss |        0 | -21.939  | less          |
|  9 | EXP   | ensLoss |        0 | -20.2573 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -22.966  | greater       |
|  6 | Hinge | ensLoss |        1 | -21.939  | greater       |
|  9 | EXP   | ensLoss |        1 | -20.2573 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -43.0595 | less          |
|  6 | Hinge | ensLoss |        0 | -29.3081 | less          |
|  9 | EXP   | ensLoss |        0 | -37.1328 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -43.0595 | greater       |
|  6 | Hinge | ensLoss |        1 | -29.3081 | greater       |
|  9 | EXP   | ensLoss |        1 | -37.1328 | greater       |

#### Data ID: 41161 - model: TabMLP3 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 41161,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP3'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9853 | 0.9849 |  0.9888 |    0.991  |
| ('test_acc', 'std')  | 0.0005 | 0.001  |  0.0007 |    0.0004 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9967 | 0.9964 |  0.9967 |    0.9974 |
| ('test_auc', 'std')  | 0.0002 | 0.0002 |  0.0002 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -10.9001 | less          |
|  6 | Hinge | ensLoss |   0.0026 |  -3.663  | less          |
|  9 | EXP   | ensLoss |   0.0002 |  -5.3949 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -10.9001 | greater       |
|  6 | Hinge | ensLoss |   0.9974 |  -3.663  | greater       |
|  9 | EXP   | ensLoss |   0.9998 |  -5.3949 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 |  -5.7651 | less          |
|  6 | Hinge | ensLoss |   0      |  -6.5652 | less          |
|  9 | EXP   | ensLoss |   0      | -10.1751 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 |  -5.7651 | greater       |
|  6 | Hinge | ensLoss |   1      |  -6.5652 | greater       |
|  9 | EXP   | ensLoss |   1      | -10.1751 | greater       |

#### Data ID: 41161 - model: TabMLP5 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 41161,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP5'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9868 | 0.9869 |  0.9862 |    0.9914 |
| ('test_acc', 'std')  | 0.0007 | 0.0004 |  0.0007 |    0.0007 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9963 | 0.9961 |  0.9954 |    0.9969 |
| ('test_auc', 'std')  | 0.0002 | 0.0003 |  0.0002 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -10.304  | less          |
|  6 | Hinge | ensLoss |   0.0002 |  -5.3634 | less          |
|  9 | EXP   | ensLoss |   0      |  -7.1876 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -10.304  | greater       |
|  6 | Hinge | ensLoss |   0.9998 |  -5.3634 | greater       |
|  9 | EXP   | ensLoss |   1      |  -7.1876 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0009 | -4.3632 | less          |
|  6 | Hinge | ensLoss |   0      | -7.1437 | less          |
|  9 | EXP   | ensLoss |   0      | -7.2756 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9991 | -4.3632 | greater       |
|  6 | Hinge | ensLoss |   1      | -7.1437 | greater       |
|  9 | EXP   | ensLoss |   1      | -7.2756 | greater       |

#### Data ID: 1039 - model: TabMLP3 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1039,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP3'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9381 | 0.9443 |  0.9589 |    0.9368 |
| ('test_acc', 'std')  | 0.0027 | 0.0026 |  0.0016 |    0.0018 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.763  | 0.7439 |  0.7035 |    0.7471 |
| ('test_auc', 'std')  | 0.0102 | 0.0139 |  0.0103 |    0.0129 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.6975 |  0.5359 | less          |
|  6 | Hinge | ensLoss |   1      | 13.2484 | less          |
|  9 | EXP   | ensLoss |   0.9989 |  4.2274 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.3025 |  0.5359 | greater       |
|  6 | Hinge | ensLoss |   0      | 13.2484 | greater       |
|  9 | EXP   | ensLoss |   0.0011 |  4.2274 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.8572 |  1.1353 | less          |
|  6 | Hinge | ensLoss |   0.0062 | -3.1196 | less          |
|  9 | EXP   | ensLoss |   0.4208 | -0.2058 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.1428 |  1.1353 | greater       |
|  6 | Hinge | ensLoss |   0.9938 | -3.1196 | greater       |
|  9 | EXP   | ensLoss |   0.5792 | -0.2058 | greater       |

#### Data ID: 1039 - model: TabMLP5 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1039,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP5'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9102 | 0.9165 |  0.9555 |    0.9061 |
| ('test_acc', 'std')  | 0.0027 | 0.0041 |  0.0017 |    0.0047 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.7511 | 0.7553 |  0.7134 |    0.7597 |
| ('test_auc', 'std')  | 0.007  | 0.0086 |  0.0105 |    0.0115 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.7571 |  0.7268 | less          |
|  6 | Hinge | ensLoss |   1      | 11.5897 | less          |
|  9 | EXP   | ensLoss |   0.9968 |  3.534  | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.2429 |  0.7268 | greater       |
|  6 | Hinge | ensLoss |   0      | 11.5897 | greater       |
|  9 | EXP   | ensLoss |   0.0032 |  3.534  | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.2436 | -0.7246 | less          |
|  6 | Hinge | ensLoss |   0.0071 | -3.0331 | less          |
|  9 | EXP   | ensLoss |   0.3769 | -0.3234 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.7564 | -0.7246 | greater       |
|  6 | Hinge | ensLoss |   0.9929 | -3.0331 | greater       |
|  9 | EXP   | ensLoss |   0.6231 | -0.3234 | greater       |

#### Data ID: 41142 - model: TabMLP3 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 41142,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP3'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7054 | 0.7051 |  0.6774 |    0.7078 |
| ('test_acc', 'std')  | 0.0035 | 0.0023 |  0.003  |    0.003  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.7702 | 0.7708 |  0.7383 |    0.7738 |
| ('test_auc', 'std')  | 0.0033 | 0.0028 |  0.0047 |    0.0029 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.2754 |  -0.6197 | less          |
|  6 | Hinge | ensLoss |   0      | -16.8192 | less          |
|  9 | EXP   | ensLoss |   0.2055 |  -0.8621 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.7246 |  -0.6197 | greater       |
|  6 | Hinge | ensLoss |   1      | -16.8192 | greater       |
|  9 | EXP   | ensLoss |   0.7945 |  -0.8621 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.1495 |  -1.102  | less          |
|  6 | Hinge | ensLoss |   0      | -15.224  | less          |
|  9 | EXP   | ensLoss |   0.174  |  -0.9902 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.8505 |  -1.102  | greater       |
|  6 | Hinge | ensLoss |   1      | -15.224  | greater       |
|  9 | EXP   | ensLoss |   0.826  |  -0.9902 | greater       |

#### Data ID: 41142 - model: TabMLP5 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 41142,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP5'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.6962 | 0.6942 |  0.6748 |    0.6994 |
| ('test_acc', 'std')  | 0.0034 | 0.0041 |  0.0023 |    0.0029 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.7605 | 0.758  |  0.7355 |    0.7647 |
| ('test_auc', 'std')  | 0.0034 | 0.0037 |  0.0019 |    0.0029 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.1466 | -1.1161 | less          |
|  6 | Hinge | ensLoss |   0      | -7.7608 | less          |
|  9 | EXP   | ensLoss |   0.1853 | -0.9425 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.8534 | -1.1161 | greater       |
|  6 | Hinge | ensLoss |   1      | -7.7608 | greater       |
|  9 | EXP   | ensLoss |   0.8147 | -0.9425 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0271 |  -2.2118 | less          |
|  6 | Hinge | ensLoss |   0      | -13.3135 | less          |
|  9 | EXP   | ensLoss |   0.045  |  -1.8986 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9729 |  -2.2118 | greater       |
|  6 | Hinge | ensLoss |   1      | -13.3135 | greater       |
|  9 | EXP   | ensLoss |   0.955  |  -1.8986 | greater       |

#### Data ID: 1128 - model: TabMLP3 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1128,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP3'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9543 | 0.9502 |  0.9427 |    0.9552 |
| ('test_acc', 'std')  | 0.0032 | 0.005  |  0.0035 |    0.0039 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9694 | 0.9668 |  0.9643 |    0.9705 |
| ('test_auc', 'std')  | 0.0032 | 0.0028 |  0.0041 |    0.0031 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.3463 | -0.4082 | less          |
|  6 | Hinge | ensLoss |   0.0013 | -4.1058 | less          |
|  9 | EXP   | ensLoss |   0.0236 | -2.2987 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.6537 | -0.4082 | greater       |
|  6 | Hinge | ensLoss |   0.9987 | -4.1058 | greater       |
|  9 | EXP   | ensLoss |   0.9764 | -2.2987 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.3175 | -0.4913 | less          |
|  6 | Hinge | ensLoss |   0.0413 | -1.9524 | less          |
|  9 | EXP   | ensLoss |   0.0619 | -1.6978 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.6825 | -0.4913 | greater       |
|  6 | Hinge | ensLoss |   0.9587 | -1.9524 | greater       |
|  9 | EXP   | ensLoss |   0.9381 | -1.6978 | greater       |

#### Data ID: 1128 - model: TabMLP5 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1128,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP5'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9427 | 0.9438 |  0.9261 |    0.9545 |
| ('test_acc', 'std')  | 0.0042 | 0.0044 |  0.0055 |    0.0041 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9664 | 0.9672 |  0.9601 |    0.9703 |
| ('test_auc', 'std')  | 0.0035 | 0.0031 |  0.0037 |    0.0026 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -6.7082 | less          |
|  6 | Hinge | ensLoss |   0      | -8.3373 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -5.5902 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -6.7082 | greater       |
|  6 | Hinge | ensLoss |   1      | -8.3373 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -5.5902 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.062  | -1.6967 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -5.3162 | less          |
|  9 | EXP   | ensLoss |   0.0483 | -1.855  | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.938  | -1.6967 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -5.3162 | greater       |
|  9 | EXP   | ensLoss |   0.9517 | -1.855  | greater       |

#### Data ID: 1138 - model: TabMLP3 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1138,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP3'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8317 | 0.8306 |  0.8468 |    0.8569 |
| ('test_acc', 'std')  | 0.0054 | 0.0057 |  0.007  |    0.0046 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9372 | 0.9358 |  0.9351 |    0.9412 |
| ('test_auc', 'std')  | 0.0059 | 0.0072 |  0.0063 |    0.0045 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -5.6198 | less          |
|  6 | Hinge | ensLoss |   0.0235 | -2.2992 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -5.274  | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -5.6198 | greater       |
|  6 | Hinge | ensLoss |   0.9765 | -2.2992 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -5.274  | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.1855 | -0.9416 | less          |
|  6 | Hinge | ensLoss |   0.0594 | -1.7242 | less          |
|  9 | EXP   | ensLoss |   0.108  | -1.3305 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.8145 | -0.9416 | greater       |
|  6 | Hinge | ensLoss |   0.9406 | -1.7242 | greater       |
|  9 | EXP   | ensLoss |   0.892  | -1.3305 | greater       |

#### Data ID: 1138 - model: TabMLP5 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1138,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP5'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8054 | 0.8209 |  0.8422 |    0.8668 |
| ('test_acc', 'std')  | 0.0049 | 0.0047 |  0.0055 |    0.0052 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.932  | 0.9341 |  0.9276 |    0.9342 |
| ('test_auc', 'std')  | 0.0042 | 0.0065 |  0.0072 |    0.0057 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -9.3595 | less          |
|  6 | Hinge | ensLoss |   0.0003 | -5.201  | less          |
|  9 | EXP   | ensLoss |   0      | -9.8122 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -9.3595 | greater       |
|  6 | Hinge | ensLoss |   0.9997 | -5.201  | greater       |
|  9 | EXP   | ensLoss |   1      | -9.8122 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.2904 | -0.5728 | less          |
|  6 | Hinge | ensLoss |   0.0282 | -2.1889 | less          |
|  9 | EXP   | ensLoss |   0.4894 | -0.0273 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.7096 | -0.5728 | greater       |
|  6 | Hinge | ensLoss |   0.9718 | -2.1889 | greater       |
|  9 | EXP   | ensLoss |   0.5106 | -0.0273 | greater       |

#### Data ID: 1166 - model: TabMLP3 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1166,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP3'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8489 | 0.8502 |  0.8545 |    0.8817 |
| ('test_acc', 'std')  | 0.0074 | 0.0072 |  0.0066 |    0.0048 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9358 | 0.9355 |  0.9302 |    0.9416 |
| ('test_auc', 'std')  | 0.0034 | 0.0049 |  0.0045 |    0.0037 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -6.7856 | less          |
|  6 | Hinge | ensLoss |        0 | -6.6367 | less          |
|  9 | EXP   | ensLoss |        0 | -7.6901 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -6.7856 | greater       |
|  6 | Hinge | ensLoss |        1 | -6.6367 | greater       |
|  9 | EXP   | ensLoss |        1 | -7.6901 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0063 | -3.1072 | less          |
|  6 | Hinge | ensLoss |   0.003  | -3.5734 | less          |
|  9 | EXP   | ensLoss |   0.0761 | -1.5645 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9937 | -3.1072 | greater       |
|  6 | Hinge | ensLoss |   0.997  | -3.5734 | greater       |
|  9 | EXP   | ensLoss |   0.9239 | -1.5645 | greater       |

#### Data ID: 1166 - model: TabMLP5 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1166,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP5'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8183 | 0.8282 |  0.8276 |    0.8716 |
| ('test_acc', 'std')  | 0.0053 | 0.0069 |  0.0053 |    0.0044 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9261 | 0.9285 |  0.9161 |    0.9394 |
| ('test_auc', 'std')  | 0.0031 | 0.0053 |  0.0054 |    0.0037 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -11.0449 | less          |
|  6 | Hinge | ensLoss |        0 |  -8.3562 | less          |
|  9 | EXP   | ensLoss |        0 |  -8.7318 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -11.0449 | greater       |
|  6 | Hinge | ensLoss |        1 |  -8.3562 | greater       |
|  9 | EXP   | ensLoss |        1 |  -8.7318 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 | -5.1906 | less          |
|  6 | Hinge | ensLoss |   0      | -8.0954 | less          |
|  9 | EXP   | ensLoss |   0.0026 | -3.6747 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 | -5.1906 | greater       |
|  6 | Hinge | ensLoss |   1      | -8.0954 | greater       |
|  9 | EXP   | ensLoss |   0.9974 | -3.6747 | greater       |

#### Data ID: 1134 - model: TabMLP3 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1134,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP3'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9817 | 0.9797 |  0.9778 |    0.9819 |
| ('test_acc', 'std')  | 0.0014 | 0.0024 |  0.0027 |    0.0017 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9903 | 0.9937 |  0.9862 |    0.9956 |
| ('test_auc', 'std')  | 0.0032 | 0.0022 |  0.0032 |    0.0017 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.4537 | -0.1196 | less          |
|  6 | Hinge | ensLoss |   0.062  | -1.6964 | less          |
|  9 | EXP   | ensLoss |   0.1104 | -1.3156 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.5463 | -0.1196 | greater       |
|  6 | Hinge | ensLoss |   0.938  | -1.6964 | greater       |
|  9 | EXP   | ensLoss |   0.8896 | -1.3156 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0179 | -2.4665 | less          |
|  6 | Hinge | ensLoss |   0.0008 | -4.4358 | less          |
|  9 | EXP   | ensLoss |   0.0368 | -2.0248 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9821 | -2.4665 | greater       |
|  6 | Hinge | ensLoss |   0.9992 | -4.4358 | greater       |
|  9 | EXP   | ensLoss |   0.9632 | -2.0248 | greater       |

#### Data ID: 1134 - model: TabMLP5 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1134,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP5'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9759 | 0.9772 |  0.9647 |    0.9806 |
| ('test_acc', 'std')  | 0.0026 | 0.0021 |  0.003  |    0.0015 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9924 | 0.9892 |  0.9819 |    0.9916 |
| ('test_auc', 'std')  | 0.0022 | 0.0052 |  0.0044 |    0.0031 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0072 | -3.0251 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -6.5069 | less          |
|  9 | EXP   | ensLoss |   0.0096 | -2.8483 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9928 | -3.0251 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -6.5069 | greater       |
|  9 | EXP   | ensLoss |   0.9904 | -2.8483 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.6342 |  0.3538 | less          |
|  6 | Hinge | ensLoss |   0.0028 | -3.6237 | less          |
|  9 | EXP   | ensLoss |   0.2115 | -0.8392 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.3658 |  0.3538 | greater       |
|  6 | Hinge | ensLoss |   0.9972 | -3.6237 | greater       |
|  9 | EXP   | ensLoss |   0.7885 | -0.8392 | greater       |

#### Data ID: 1130 - model: TabMLP3 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1130,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP3'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9112 | 0.9091 |  0.9108 |    0.9306 |
| ('test_acc', 'std')  | 0.0042 | 0.005  |  0.0042 |    0.003  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9542 | 0.9555 |  0.9545 |     0.963 |
| ('test_auc', 'std')  | 0.008  | 0.0043 |  0.0084 |     0.005 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0006 | -4.6719 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -5.4807 | less          |
|  9 | EXP   | ensLoss |   0.0006 | -4.6852 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9994 | -4.6719 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -5.4807 | greater       |
|  9 | EXP   | ensLoss |   0.9994 | -4.6852 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0242 | -2.2816 | less          |
|  6 | Hinge | ensLoss |   0.047  | -1.8721 | less          |
|  9 | EXP   | ensLoss |   0.0213 | -2.3592 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9758 | -2.2816 | greater       |
|  6 | Hinge | ensLoss |   0.953  | -1.8721 | greater       |
|  9 | EXP   | ensLoss |   0.9787 | -2.3592 | greater       |

#### Data ID: 1130 - model: TabMLP5 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1130,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP5'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8817 | 0.8931 |  0.8976 |    0.93   |
| ('test_acc', 'std')  | 0.0054 | 0.0075 |  0.0049 |    0.0042 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.954  | 0.9585 |  0.9483 |    0.9569 |
| ('test_auc', 'std')  | 0.0042 | 0.0057 |  0.0058 |    0.0062 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -8.3326 | less          |
|  6 | Hinge | ensLoss |   0      | -7.2808 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -6.4586 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -8.3326 | greater       |
|  6 | Hinge | ensLoss |   1      | -7.2808 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -6.4586 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.2635 | -0.6579 | less          |
|  6 | Hinge | ensLoss |   0.1435 | -1.1318 | less          |
|  9 | EXP   | ensLoss |   0.6464 |  0.3879 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.7365 | -0.6579 | greater       |
|  6 | Hinge | ensLoss |   0.8565 | -1.1318 | greater       |
|  9 | EXP   | ensLoss |   0.3535 |  0.3879 | greater       |

#### Data ID: 1139 - model: TabMLP3 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1139,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP3'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.778  | 0.772  |  0.8024 |    0.7955 |
| ('test_acc', 'std')  | 0.0066 | 0.0046 |  0.0082 |    0.0088 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9084 | 0.9092 |   0.904 |    0.9125 |
| ('test_auc', 'std')  | 0.0082 | 0.0097 |   0.01  |    0.0092 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0588 | -1.7309 | less          |
|  6 | Hinge | ensLoss |   0.8395 |  1.0502 | less          |
|  9 | EXP   | ensLoss |   0.0044 | -3.3359 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9412 | -1.7309 | greater       |
|  6 | Hinge | ensLoss |   0.1605 |  1.0502 | greater       |
|  9 | EXP   | ensLoss |   0.9956 | -3.3359 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.3192 | -0.4861 | less          |
|  6 | Hinge | ensLoss |   0.1324 | -1.189  | less          |
|  9 | EXP   | ensLoss |   0.2108 | -0.842  | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.6808 | -0.4861 | greater       |
|  6 | Hinge | ensLoss |   0.8676 | -1.189  | greater       |
|  9 | EXP   | ensLoss |   0.7892 | -0.842  | greater       |

#### Data ID: 1139 - model: TabMLP5 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1139,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP5'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7142 | 0.7491 |  0.7925 |    0.82   |
| ('test_acc', 'std')  | 0.0112 | 0.0058 |  0.0069 |    0.0063 |


|                      |   BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.901 | 0.9065 |  0.8849 |    0.9116 |
| ('test_auc', 'std')  | 0.009 | 0.0074 |  0.0114 |    0.0081 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -9.7876 | less          |
|  6 | Hinge | ensLoss |   0.0034 | -3.4886 | less          |
|  9 | EXP   | ensLoss |   0      | -8.194  | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -9.7876 | greater       |
|  6 | Hinge | ensLoss |   0.9966 | -3.4886 | greater       |
|  9 | EXP   | ensLoss |   1      | -8.194  | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0508 | -1.8227 | less          |
|  6 | Hinge | ensLoss |   0.0053 | -3.2164 | less          |
|  9 | EXP   | ensLoss |   0.2211 | -0.8039 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9492 | -1.8227 | greater       |
|  6 | Hinge | ensLoss |   0.9947 | -3.2164 | greater       |
|  9 | EXP   | ensLoss |   0.7789 | -0.8039 | greater       |

#### Data ID: 1161 - model: TabMLP3 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1161,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP3'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9586 | 0.9569 |  0.9556 |    0.9631 |
| ('test_acc', 'std')  | 0.0026 | 0.0025 |  0.0027 |    0.0022 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9556 | 0.9594 |  0.9496 |    0.9654 |
| ('test_auc', 'std')  | 0.0046 | 0.005  |  0.0051 |    0.0044 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0155 | -2.5529 | less          |
|  6 | Hinge | ensLoss |   0.0038 | -3.4156 | less          |
|  9 | EXP   | ensLoss |   0.0019 | -3.8562 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9845 | -2.5529 | greater       |
|  6 | Hinge | ensLoss |   0.9962 | -3.4156 | greater       |
|  9 | EXP   | ensLoss |   0.9981 | -3.8562 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0022 | -3.7874 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -5.7174 | less          |
|  9 | EXP   | ensLoss |   0.0336 | -2.0814 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9978 | -3.7874 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -5.7174 | greater       |
|  9 | EXP   | ensLoss |   0.9664 | -2.0814 | greater       |

#### Data ID: 1161 - model: TabMLP5 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1161,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP5'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9573 | 0.9573 |  0.9515 |    0.9627 |
| ('test_acc', 'std')  | 0.0027 | 0.0028 |  0.0025 |    0.002  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9536 | 0.9554 |  0.9496 |    0.9632 |
| ('test_auc', 'std')  | 0.0047 | 0.0046 |  0.005  |    0.0059 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0005 | -4.7916 | less          |
|  6 | Hinge | ensLoss |   0      | -7.471  | less          |
|  9 | EXP   | ensLoss |   0.0006 | -4.6072 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9995 | -4.7916 | greater       |
|  6 | Hinge | ensLoss |   1      | -7.471  | greater       |
|  9 | EXP   | ensLoss |   0.9994 | -4.6072 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0026 | -3.6517 | less          |
|  6 | Hinge | ensLoss |   0.0067 | -3.0655 | less          |
|  9 | EXP   | ensLoss |   0.0074 | -3.0052 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9974 | -3.6517 | greater       |
|  6 | Hinge | ensLoss |   0.9933 | -3.0655 | greater       |
|  9 | EXP   | ensLoss |   0.9926 | -3.0052 | greater       |

#### Data ID: 1142 - model: TabMLP3 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1142,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP3'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7808 | 0.7843 |  0.8239 |    0.7981 |
| ('test_acc', 'std')  | 0.0073 | 0.0055 |  0.0034 |    0.0061 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9344 | 0.9372 |  0.938  |    0.9293 |
| ('test_auc', 'std')  | 0.0103 | 0.0105 |  0.0081 |    0.0125 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0192 | -2.4244 | less          |
|  6 | Hinge | ensLoss |   0.9998 |  5.5682 | less          |
|  9 | EXP   | ensLoss |   0.0755 | -1.5696 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9808 | -2.4244 | greater       |
|  6 | Hinge | ensLoss |   0.0002 |  5.5682 | greater       |
|  9 | EXP   | ensLoss |   0.9245 | -1.5696 | greater       |
|    | A     | B       |   pvalue |   stat | alternative   |
|---:|:------|:--------|---------:|-------:|:--------------|
|  3 | BCE   | ensLoss |   0.7269 | 0.627  | less          |
|  6 | Hinge | ensLoss |   0.8441 | 1.0714 | less          |
|  9 | EXP   | ensLoss |   0.9059 | 1.4237 | less          |


|    | A     | B       |   pvalue |   stat | alternative   |
|---:|:------|:--------|---------:|-------:|:--------------|
|  3 | BCE   | ensLoss |   0.2731 | 0.627  | greater       |
|  6 | Hinge | ensLoss |   0.1559 | 1.0714 | greater       |
|  9 | EXP   | ensLoss |   0.0941 | 1.4237 | greater       |

#### Data ID: 1142 - model: TabMLP5 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1142,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP5'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7166 | 0.7433 |  0.8168 |    0.8319 |
| ('test_acc', 'std')  | 0.012  | 0.0055 |  0.0059 |    0.0064 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9226 | 0.9251 |  0.9155 |    0.9252 |
| ('test_auc', 'std')  | 0.0082 | 0.011  |  0.0134 |    0.0101 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -12.8565 | less          |
|  6 | Hinge | ensLoss |   0.0016 |  -3.9973 | less          |
|  9 | EXP   | ensLoss |   0      | -12.631  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -12.8565 | greater       |
|  6 | Hinge | ensLoss |   0.9984 |  -3.9973 | greater       |
|  9 | EXP   | ensLoss |   1      | -12.631  | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.3219 | -0.4784 | less          |
|  6 | Hinge | ensLoss |   0.1466 | -1.1161 | less          |
|  9 | EXP   | ensLoss |   0.4914 | -0.0223 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.6781 | -0.4784 | greater       |
|  6 | Hinge | ensLoss |   0.8534 | -1.1161 | greater       |
|  9 | EXP   | ensLoss |   0.5087 | -0.0223 | greater       |

#### Data ID: 1146 - model: TabMLP3 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1146,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP3'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9793 | 0.9793 |  0.9843 |    0.9823 |
| ('test_acc', 'std')  | 0.0027 | 0.0027 |  0.0018 |    0.0025 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9895 | 0.9797 |  0.9825 |    0.9881 |
| ('test_auc', 'std')  | 0.0047 | 0.0065 |  0.0065 |    0.0046 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.178  | -0.9728 | less          |
|  6 | Hinge | ensLoss |   0.7282 |  0.6313 | less          |
|  9 | EXP   | ensLoss |   0.1504 | -1.0977 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.822  | -0.9728 | greater       |
|  6 | Hinge | ensLoss |   0.2718 |  0.6313 | greater       |
|  9 | EXP   | ensLoss |   0.8496 | -1.0977 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.6001 |  0.2613 | less          |
|  6 | Hinge | ensLoss |   0.2216 | -0.8021 | less          |
|  9 | EXP   | ensLoss |   0.0812 | -1.5214 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.3999 |  0.2613 | greater       |
|  6 | Hinge | ensLoss |   0.7784 | -0.8021 | greater       |
|  9 | EXP   | ensLoss |   0.9188 | -1.5214 | greater       |

#### Data ID: 1146 - model: TabMLP5 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1146,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP5'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9739 | 0.9696 |  0.9722 |    0.9793 |
| ('test_acc', 'std')  | 0.0016 | 0.0024 |  0.0027 |    0.0019 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9796 | 0.9808 |  0.977  |     0.98  |
| ('test_auc', 'std')  | 0.0059 | 0.0067 |  0.0067 |     0.006 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0134 | -2.6434 | less          |
|  6 | Hinge | ensLoss |   0.015  | -2.5725 | less          |
|  9 | EXP   | ensLoss |   0.0046 | -3.3085 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9866 | -2.6434 | greater       |
|  6 | Hinge | ensLoss |   0.985  | -2.5725 | greater       |
|  9 | EXP   | ensLoss |   0.9954 | -3.3085 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.4495 | -0.1306 | less          |
|  6 | Hinge | ensLoss |   0.2426 | -0.7279 | less          |
|  9 | EXP   | ensLoss |   0.5982 |  0.2561 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.5505 | -0.1306 | greater       |
|  6 | Hinge | ensLoss |   0.7574 | -0.7279 | greater       |
|  9 | EXP   | ensLoss |   0.4018 |  0.2561 | greater       |

#### Data ID: 4134 - model: TabMLP1 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 4134,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP1'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7786 | 0.7773 |  0.7736 |    0.7822 |
| ('test_acc', 'std')  | 0.0032 | 0.0032 |  0.0031 |    0.0042 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8504 | 0.8435 |  0.8342 |    0.8531 |
| ('test_auc', 'std')  | 0.0032 | 0.0035 |  0.0039 |    0.0031 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0717 | -1.6028 | less          |
|  6 | Hinge | ensLoss |   0.0013 | -4.1232 | less          |
|  9 | EXP   | ensLoss |   0.0818 | -1.517  | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9283 | -1.6028 | greater       |
|  6 | Hinge | ensLoss |   0.9987 | -4.1232 | greater       |
|  9 | EXP   | ensLoss |   0.9182 | -1.517  | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0586 | -1.733  | less          |
|  6 | Hinge | ensLoss |   0      | -9.8723 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -5.7044 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9414 | -1.733  | greater       |
|  6 | Hinge | ensLoss |   1      | -9.8723 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -5.7044 | greater       |

#### Data ID: 41159 - model: TabMLP1 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 41159,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP1'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7454 | 0.7551 |  0.7545 |    0.7602 |
| ('test_acc', 'std')  | 0.0015 | 0.0018 |  0.0022 |    0.0016 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8112 | 0.8212 |  0.8188 |    0.8276 |
| ('test_auc', 'std')  | 0.0016 | 0.0017 |  0.0021 |    0.0017 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -16.1008 | less          |
|  6 | Hinge | ensLoss |   0.0018 |  -3.9185 | less          |
|  9 | EXP   | ensLoss |   0.0043 |  -3.3477 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -16.1008 | greater       |
|  6 | Hinge | ensLoss |   0.9982 |  -3.9185 | greater       |
|  9 | EXP   | ensLoss |   0.9957 |  -3.3477 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -40.9211 | less          |
|  6 | Hinge | ensLoss |        0 |  -9.0313 | less          |
|  9 | EXP   | ensLoss |        0 |  -9.7046 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -40.9211 | greater       |
|  6 | Hinge | ensLoss |        1 |  -9.0313 | greater       |
|  9 | EXP   | ensLoss |        1 |  -9.7046 | greater       |

#### Data ID: 41161 - model: TabMLP1 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 41161,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP1'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9915 | 0.9912 |  0.9923 |    0.9895 |
| ('test_acc', 'std')  | 0.0005 | 0.0004 |  0.0003 |    0.0006 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9972 | 0.9971 |  0.9974 |    0.9973 |
| ('test_auc', 'std')  | 0.0002 | 0.0002 |  0.0002 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |   stat | alternative   |
|---:|:------|:--------|---------:|-------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | 5.6266 | less          |
|  6 | Hinge | ensLoss |   0.9999 | 6.408  | less          |
|  9 | EXP   | ensLoss |   0.9998 | 5.6979 | less          |


|    | A     | B       |   pvalue |   stat | alternative   |
|---:|:------|:--------|---------:|-------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | 5.6266 | greater       |
|  6 | Hinge | ensLoss |   0.0001 | 6.408  | greater       |
|  9 | EXP   | ensLoss |   0.0001 | 5.6979 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0038 | -3.419  | less          |
|  6 | Hinge | ensLoss |   0.9903 |  2.8405 | less          |
|  9 | EXP   | ensLoss |   0      | -6.9544 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9962 | -3.419  | greater       |
|  6 | Hinge | ensLoss |   0.0097 |  2.8405 | greater       |
|  9 | EXP   | ensLoss |   1      | -6.9544 | greater       |

#### Data ID: 1039 - model: TabMLP1 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1039,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP1'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9593 | 0.9635 |  0.9638 |    0.9646 |
| ('test_acc', 'std')  | 0.0016 | 0.0016 |  0.0013 |    0.0016 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.7502 | 0.7364 |  0.7116 |    0.7484 |
| ('test_auc', 'std')  | 0.01   | 0.0087 |  0.0108 |    0.0137 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0008 | -4.4275 | less          |
|  6 | Hinge | ensLoss |   0.163  | -1.0389 | less          |
|  9 | EXP   | ensLoss |   0.1691 | -1.0115 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9992 | -4.4275 | greater       |
|  6 | Hinge | ensLoss |   0.837  | -1.0389 | greater       |
|  9 | EXP   | ensLoss |   0.8309 | -1.0115 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.5726 |  0.1882 | less          |
|  6 | Hinge | ensLoss |   0.0017 | -3.9431 | less          |
|  9 | EXP   | ensLoss |   0.1921 | -0.9149 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.4274 |  0.1882 | greater       |
|  6 | Hinge | ensLoss |   0.9983 | -3.9431 | greater       |
|  9 | EXP   | ensLoss |   0.8079 | -0.9149 | greater       |

#### Data ID: 41142 - model: TabMLP1 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 41142,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP1'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7089 | 0.7019 |  0.6759 |    0.7125 |
| ('test_acc', 'std')  | 0.004  | 0.0026 |  0.0031 |    0.0037 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.7775 | 0.7705 |  0.7408 |    0.7813 |
| ('test_auc', 'std')  | 0.0033 | 0.0028 |  0.0033 |    0.0029 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0357 |  -2.0426 | less          |
|  6 | Hinge | ensLoss |   0      | -14.0394 | less          |
|  9 | EXP   | ensLoss |   0.0009 |  -4.34   | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9643 |  -2.0426 | greater       |
|  6 | Hinge | ensLoss |   1      | -14.0394 | greater       |
|  9 | EXP   | ensLoss |   0.9991 |  -4.34   | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0139 |  -2.6192 | less          |
|  6 | Hinge | ensLoss |   0      | -19.9048 | less          |
|  9 | EXP   | ensLoss |   0.0001 |  -5.7764 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9861 |  -2.6192 | greater       |
|  6 | Hinge | ensLoss |   1      | -19.9048 | greater       |
|  9 | EXP   | ensLoss |   0.9999 |  -5.7764 | greater       |

#### Data ID: 1128 - model: TabMLP1 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1128,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP1'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.955  | 0.955  |  0.9558 |    0.9586 |
| ('test_acc', 'std')  | 0.0033 | 0.0044 |  0.0023 |    0.0037 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9655 | 0.9671 |  0.9628 |    0.9678 |
| ('test_auc', 'std')  | 0.0037 | 0.0043 |  0.0039 |    0.0035 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0336 | -2.0803 | less          |
|  6 | Hinge | ensLoss |   0.1573 | -1.065  | less          |
|  9 | EXP   | ensLoss |   0.0412 | -1.9543 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9664 | -2.0803 | greater       |
|  6 | Hinge | ensLoss |   0.8427 | -1.065  | greater       |
|  9 | EXP   | ensLoss |   0.9588 | -1.9543 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0151 | -2.569  | less          |
|  6 | Hinge | ensLoss |   0.0075 | -2.9977 | less          |
|  9 | EXP   | ensLoss |   0.2527 | -0.6938 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9849 | -2.569  | greater       |
|  6 | Hinge | ensLoss |   0.9925 | -2.9977 | greater       |
|  9 | EXP   | ensLoss |   0.7473 | -0.6938 | greater       |

#### Data ID: 1138 - model: TabMLP1 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1138,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP1'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8483 | 0.8599 |  0.8657 |    0.8513 |
| ('test_acc', 'std')  | 0.0049 | 0.0066 |  0.008  |    0.0057 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9362 | 0.9357 |  0.9299 |    0.9384 |
| ('test_auc', 'std')  | 0.0054 | 0.0048 |  0.0064 |    0.0045 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.1109 | -1.3125 | less          |
|  6 | Hinge | ensLoss |   0.9798 |  2.392  | less          |
|  9 | EXP   | ensLoss |   0.9655 |  2.0641 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.8891 | -1.3125 | greater       |
|  6 | Hinge | ensLoss |   0.0202 |  2.392  | greater       |
|  9 | EXP   | ensLoss |   0.0345 |  2.0641 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.2606 | -0.6676 | less          |
|  6 | Hinge | ensLoss |   0.0143 | -2.6024 | less          |
|  9 | EXP   | ensLoss |   0.0568 | -1.7523 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.7394 | -0.6676 | greater       |
|  6 | Hinge | ensLoss |   0.9857 | -2.6024 | greater       |
|  9 | EXP   | ensLoss |   0.9432 | -1.7523 | greater       |

#### Data ID: 1166 - model: TabMLP1 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1166,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP1'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |   BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.861 | 0.8737 |  0.8819 |    0.8802 |
| ('test_acc', 'std')  | 0.005 | 0.0059 |  0.007  |    0.005  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.936  | 0.9402 |  0.9303 |    0.9377 |
| ('test_auc', 'std')  | 0.0051 | 0.0032 |  0.0054 |    0.0035 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 | -5.2273 | less          |
|  6 | Hinge | ensLoss |   0.6467 |  0.3885 | less          |
|  9 | EXP   | ensLoss |   0.0101 | -2.818  | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 | -5.2273 | greater       |
|  6 | Hinge | ensLoss |   0.3533 |  0.3885 | greater       |
|  9 | EXP   | ensLoss |   0.9899 | -2.818  | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.2946 | -0.5599 | less          |
|  6 | Hinge | ensLoss |   0.0347 | -2.061  | less          |
|  9 | EXP   | ensLoss |   0.8039 |  0.8987 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.7054 | -0.5599 | greater       |
|  6 | Hinge | ensLoss |   0.9653 | -2.061  | greater       |
|  9 | EXP   | ensLoss |   0.1961 |  0.8987 | greater       |

#### Data ID: 1134 - model: TabMLP1 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1134,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP1'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9843 | 0.9832 |  0.9812 |    0.9866 |
| ('test_acc', 'std')  | 0.0018 | 0.0017 |  0.0023 |    0.0021 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9905 | 0.9909 |  0.9863 |    0.9934 |
| ('test_auc', 'std')  | 0.0026 | 0.0028 |  0.0034 |    0.0028 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0286 | -2.1807 | less          |
|  6 | Hinge | ensLoss |   0.0093 | -2.8656 | less          |
|  9 | EXP   | ensLoss |   0.0327 | -2.0969 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9714 | -2.1807 | greater       |
|  6 | Hinge | ensLoss |   0.9907 | -2.8656 | greater       |
|  9 | EXP   | ensLoss |   0.9673 | -2.0969 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.1487 | -1.1062 | less          |
|  6 | Hinge | ensLoss |   0.0085 | -2.9199 | less          |
|  9 | EXP   | ensLoss |   0.0456 | -1.8911 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.8513 | -1.1062 | greater       |
|  6 | Hinge | ensLoss |   0.9915 | -2.9199 | greater       |
|  9 | EXP   | ensLoss |   0.9544 | -1.8911 | greater       |

#### Data ID: 1130 - model: TabMLP1 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1130,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP1'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.922  | 0.9263 |  0.9343 |    0.9338 |
| ('test_acc', 'std')  | 0.0041 | 0.0036 |  0.0025 |    0.0025 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9592 | 0.9528 |  0.9497 |    0.9601 |
| ('test_auc', 'std')  | 0.0055 | 0.0072 |  0.007  |    0.007  |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.001  | -4.3109 | less          |
|  6 | Hinge | ensLoss |   0.5629 |  0.1629 | less          |
|  9 | EXP   | ensLoss |   0.0075 | -3      | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.999  | -4.3109 | greater       |
|  6 | Hinge | ensLoss |   0.4371 |  0.1629 | greater       |
|  9 | EXP   | ensLoss |   0.9925 | -3      | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.4277 | -0.1876 | less          |
|  6 | Hinge | ensLoss |   0.0543 | -1.7814 | less          |
|  9 | EXP   | ensLoss |   0.0957 | -1.4129 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.5723 | -0.1876 | greater       |
|  6 | Hinge | ensLoss |   0.9457 | -1.7814 | greater       |
|  9 | EXP   | ensLoss |   0.9043 | -1.4129 | greater       |

#### Data ID: 1139 - model: TabMLP1 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1139,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP1'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8323 | 0.8459 |  0.8666 |    0.8474 |
| ('test_acc', 'std')  | 0.0078 | 0.0048 |  0.0062 |    0.0055 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.898  | 0.9069 |  0.8898 |    0.9099 |
| ('test_auc', 'std')  | 0.0117 | 0.0092 |  0.0148 |    0.0092 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0093 | -2.8684 | less          |
|  6 | Hinge | ensLoss |   0.997  |  3.5714 | less          |
|  9 | EXP   | ensLoss |   0.3731 | -0.3337 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9907 | -2.8684 | greater       |
|  6 | Hinge | ensLoss |   0.003  |  3.5714 | greater       |
|  9 | EXP   | ensLoss |   0.6269 | -0.3337 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0407 | -1.9618 | less          |
|  6 | Hinge | ensLoss |   0.0362 | -2.0354 | less          |
|  9 | EXP   | ensLoss |   0.2824 | -0.5975 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9593 | -1.9618 | greater       |
|  6 | Hinge | ensLoss |   0.9638 | -2.0354 | greater       |
|  9 | EXP   | ensLoss |   0.7176 | -0.5975 | greater       |

#### Data ID: 1161 - model: TabMLP1 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1161,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP1'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.958  | 0.9539 |  0.9522 |    0.9588 |
| ('test_acc', 'std')  | 0.0025 | 0.0023 |  0.0036 |    0.0025 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9584 | 0.9552 |  0.9578 |    0.9616 |
| ('test_auc', 'std')  | 0.0048 | 0.0054 |  0.0061 |    0.0052 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.2609 | -0.6667 | less          |
|  6 | Hinge | ensLoss |   0.008  | -2.9572 | less          |
|  9 | EXP   | ensLoss |   0.001  | -4.271  | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.7391 | -0.6667 | greater       |
|  6 | Hinge | ensLoss |   0.992  | -2.9572 | greater       |
|  9 | EXP   | ensLoss |   0.999  | -4.271  | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.1261 | -1.2236 | less          |
|  6 | Hinge | ensLoss |   0.0902 | -1.4523 | less          |
|  9 | EXP   | ensLoss |   0.0071 | -3.0302 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.8739 | -1.2236 | greater       |
|  6 | Hinge | ensLoss |   0.9098 | -1.4523 | greater       |
|  9 | EXP   | ensLoss |   0.9929 | -3.0302 | greater       |

#### Data ID: 1142 - model: TabMLP1 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1142,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP1'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8582 | 0.8655 |  0.8834 |    0.8664 |
| ('test_acc', 'std')  | 0.0048 | 0.0044 |  0.006  |    0.0048 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9237 | 0.9173 |  0.9076 |    0.9339 |
| ('test_auc', 'std')  | 0.0113 | 0.0172 |  0.0156 |    0.0111 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0327 | -2.0968 | less          |
|  6 | Hinge | ensLoss |   0.9993 |  4.5535 | less          |
|  9 | EXP   | ensLoss |   0.4049 | -0.2479 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9673 | -2.0968 | greater       |
|  6 | Hinge | ensLoss |   0.0007 |  4.5535 | greater       |
|  9 | EXP   | ensLoss |   0.5951 | -0.2479 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.019  | -2.4307 | less          |
|  6 | Hinge | ensLoss |   0.0216 | -2.3514 | less          |
|  9 | EXP   | ensLoss |   0.0664 | -1.6521 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.981  | -2.4307 | greater       |
|  6 | Hinge | ensLoss |   0.9784 | -2.3514 | greater       |
|  9 | EXP   | ensLoss |   0.9336 | -1.6521 | greater       |

#### Data ID: 1146 - model: TabMLP1 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 1146,
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'model': {'args': {},
           'net': 'TabMLP1'},
 'optimizer': {'args': {'T_max': 300},
               'lr': 0.0001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 5e-06},
 'save_model': False,
 'trainer': {'epochs': 300,
             'val_per_epochs': 10}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9819 | 0.9821 |  0.9914 |    0.9832 |
| ('test_acc', 'std')  | 0.0015 | 0.0026 |  0.0021 |    0.0015 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9934 | 0.9891 |  0.9939 |    0.9952 |
| ('test_auc', 'std')  | 0.0031 | 0.0046 |  0.0035 |    0.0023 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.1394 | -1.1523 | less          |
|  6 | Hinge | ensLoss |   0.9976 |  3.7262 | less          |
|  9 | EXP   | ensLoss |   0.2753 | -0.6202 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.8606 | -1.1523 | greater       |
|  6 | Hinge | ensLoss |   0.0024 |  3.7262 | greater       |
|  9 | EXP   | ensLoss |   0.7247 | -0.6202 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.095  | -1.4176 | less          |
|  6 | Hinge | ensLoss |   0.2855 | -0.588  | less          |
|  9 | EXP   | ensLoss |   0.0435 | -1.9206 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.905  | -1.4176 | greater       |
|  6 | Hinge | ensLoss |   0.7145 | -0.588  | greater       |
|  9 | EXP   | ensLoss |   0.9565 | -1.9206 | greater       |
