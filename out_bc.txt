
#### CIFAR35 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR35',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': False,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |   ensLoss |   ensLoss+bc10 |   ensLoss+bc20 |   ensLoss+bc50 |
|:---------------------|----------:|---------------:|---------------:|---------------:|
| ('test_acc', 'mean') |    0.7004 |         0.7087 |         0.7148 |         0.7022 |
| ('test_acc', 'std')  |    0.0121 |         0.0072 |         0.0062 |         0.0111 |


|                      |   ensLoss |   ensLoss+bc10 |   ensLoss+bc20 |   ensLoss+bc50 |
|:---------------------|----------:|---------------:|---------------:|---------------:|
| ('test_auc', 'mean') |    0.7655 |         0.7778 |         0.7851 |         0.7721 |
| ('test_auc', 'std')  |    0.0155 |         0.009  |         0.0074 |         0.0133 |

-- Testing --

|    | A            | B       |   pvalue |   stat | alternative   |
|---:|:-------------|:--------|---------:|-------:|:--------------|
|  3 | ensLoss+bc10 | ensLoss |   0.7967 | 0.8705 | less          |
|  6 | ensLoss+bc20 | ensLoss |   0.8132 | 0.9363 | less          |
|  9 | ensLoss+bc50 | ensLoss |   0.5372 | 0.096  | less          |


|    | A            | B       |   pvalue |   stat | alternative   |
|---:|:-------------|:--------|---------:|-------:|:--------------|
|  3 | ensLoss+bc10 | ensLoss |   0.2033 | 0.8705 | greater       |
|  6 | ensLoss+bc20 | ensLoss |   0.1868 | 0.9363 | greater       |
|  9 | ensLoss+bc50 | ensLoss |   0.4628 | 0.096  | greater       |
|    | A            | B       |   pvalue |   stat | alternative   |
|---:|:-------------|:--------|---------:|-------:|:--------------|
|  3 | ensLoss+bc10 | ensLoss |   0.8181 | 0.9563 | less          |
|  6 | ensLoss+bc20 | ensLoss |   0.8268 | 0.9935 | less          |
|  9 | ensLoss+bc50 | ensLoss |   0.6101 | 0.288  | less          |


|    | A            | B       |   pvalue |   stat | alternative   |
|---:|:-------------|:--------|---------:|-------:|:--------------|
|  3 | ensLoss+bc10 | ensLoss |   0.182  | 0.9563 | greater       |
|  6 | ensLoss+bc20 | ensLoss |   0.1732 | 0.9935 | greater       |
|  9 | ensLoss+bc50 | ensLoss |   0.3899 | 0.288  | greater       |

#### CIFAR23 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR23',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': False,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |   ensLoss |   ensLoss+bc10 |   ensLoss+bc20 |   ensLoss+bc50 |
|:---------------------|----------:|---------------:|---------------:|---------------:|
| ('test_acc', 'mean') |    0.8112 |         0.8045 |         0.8058 |         0.8063 |
| ('test_acc', 'std')  |    0.0028 |         0.003  |         0.0038 |         0.0047 |


|                      |   ensLoss |   ensLoss+bc10 |   ensLoss+bc20 |   ensLoss+bc50 |
|:---------------------|----------:|---------------:|---------------:|---------------:|
| ('test_auc', 'mean') |    0.892  |         0.8862 |         0.887  |         0.8871 |
| ('test_auc', 'std')  |    0.0025 |         0.003  |         0.0031 |         0.0045 |

-- Testing --

|    | A            | B       |   pvalue |    stat | alternative   |
|---:|:-------------|:--------|---------:|--------:|:--------------|
|  3 | ensLoss+bc10 | ensLoss |   0.0651 | -1.6657 | less          |
|  6 | ensLoss+bc20 | ensLoss |   0.144  | -1.1294 | less          |
|  9 | ensLoss+bc50 | ensLoss |   0.2419 | -0.7302 | less          |


|    | A            | B       |   pvalue |    stat | alternative   |
|---:|:-------------|:--------|---------:|--------:|:--------------|
|  3 | ensLoss+bc10 | ensLoss |   0.9349 | -1.6657 | greater       |
|  6 | ensLoss+bc20 | ensLoss |   0.856  | -1.1294 | greater       |
|  9 | ensLoss+bc50 | ensLoss |   0.7581 | -0.7302 | greater       |
|    | A            | B       |   pvalue |    stat | alternative   |
|---:|:-------------|:--------|---------:|--------:|:--------------|
|  3 | ensLoss+bc10 | ensLoss |   0.0569 | -1.7516 | less          |
|  6 | ensLoss+bc20 | ensLoss |   0.0936 | -1.4278 | less          |
|  9 | ensLoss+bc50 | ensLoss |   0.2253 | -0.7886 | less          |


|    | A            | B       |   pvalue |    stat | alternative   |
|---:|:-------------|:--------|---------:|--------:|:--------------|
|  3 | ensLoss+bc10 | ensLoss |   0.9431 | -1.7516 | greater       |
|  6 | ensLoss+bc20 | ensLoss |   0.9064 | -1.4278 | greater       |
|  9 | ensLoss+bc50 | ensLoss |   0.7747 | -0.7886 | greater       |

#### CIFAR34 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR34',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': False,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |   ensLoss |   ensLoss+bc10 |   ensLoss+bc20 |   ensLoss+bc50 |
|:---------------------|----------:|---------------:|---------------:|---------------:|
| ('test_acc', 'mean') |    0.8311 |         0.8305 |         0.8282 |         0.8347 |
| ('test_acc', 'std')  |    0.0029 |         0.0012 |         0.0025 |         0.0015 |


|                      |   ensLoss |   ensLoss+bc10 |   ensLoss+bc20 |   ensLoss+bc50 |
|:---------------------|----------:|---------------:|---------------:|---------------:|
| ('test_auc', 'mean') |    0.9123 |         0.9093 |         0.9097 |         0.9134 |
| ('test_auc', 'std')  |    0.0018 |         0.0012 |         0.0018 |         0.0014 |

-- Testing --

|    | A            | B       |   pvalue |    stat | alternative   |
|---:|:-------------|:--------|---------:|--------:|:--------------|
|  3 | ensLoss+bc10 | ensLoss |   0.423  | -0.2    | less          |
|  6 | ensLoss+bc20 | ensLoss |   0.2454 | -0.7183 | less          |
|  9 | ensLoss+bc50 | ensLoss |   0.8766 |  1.2387 | less          |


|    | A            | B       |   pvalue |    stat | alternative   |
|---:|:-------------|:--------|---------:|--------:|:--------------|
|  3 | ensLoss+bc10 | ensLoss |   0.577  | -0.2    | greater       |
|  6 | ensLoss+bc20 | ensLoss |   0.7546 | -0.7183 | greater       |
|  9 | ensLoss+bc50 | ensLoss |   0.1234 |  1.2387 | greater       |
|    | A            | B       |   pvalue |    stat | alternative   |
|---:|:-------------|:--------|---------:|--------:|:--------------|
|  3 | ensLoss+bc10 | ensLoss |   0.1278 | -1.2139 | less          |
|  6 | ensLoss+bc20 | ensLoss |   0.1936 | -0.9088 | less          |
|  9 | ensLoss+bc50 | ensLoss |   0.681  |  0.4869 | less          |


|    | A            | B       |   pvalue |    stat | alternative   |
|---:|:-------------|:--------|---------:|--------:|:--------------|
|  3 | ensLoss+bc10 | ensLoss |   0.8722 | -1.2139 | greater       |
|  6 | ensLoss+bc20 | ensLoss |   0.8064 | -0.9088 | greater       |
|  9 | ensLoss+bc50 | ensLoss |   0.319  |  0.4869 | greater       |
