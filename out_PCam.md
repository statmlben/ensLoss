#### PCam - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'PCam',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 30},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 30,
             'val_per_epochs': 3}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7691 | 0.7378 |  0.772  |    0.8233 |
| ('test_acc', 'std')  | 0.0052 | 0.0052 |  0.0018 |    0.003  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8869 | 0.833  |  0.7611 |    0.9224 |
| ('test_auc', 'std')  | 0.0034 | 0.0057 |  0.0037 |    0.0013 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -12.9789 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -13.5018 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.6016 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -12.9789 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -13.5018 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.6016 | greater       |

#### PCam - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'PCam',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 30},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 30,
             'val_per_epochs': 3}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7723 | 0.741  |  0.7796 |    0.82   |
| ('test_acc', 'std')  | 0.0051 | 0.0049 |  0.0034 |    0.0007 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8875 | 0.8351 |  0.7724 |    0.9207 |
| ('test_auc', 'std')  | 0.003  | 0.0046 |  0.0067 |    0.0049 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 |  -9.7853 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -12.1145 | less          |
|  9 | EXP   | ensLoss |   0      | -15.5768 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 |  -9.7853 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -12.1145 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.5768 | greater       |

#### PCam - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'PCam',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 30},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 30,
             'val_per_epochs': 3}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8097 | 0.7711 |  0.8269 |    0.8577 |
| ('test_acc', 'std')  | 0.0025 | 0.005  |  0.003  |    0.0035 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9335 | 0.8877 |  0.8618 |    0.9544 |
| ('test_auc', 'std')  | 0.0026 | 0.0059 |  0.0056 |    0.0024 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 |  -9.9844 | less          |
|  6 | Hinge | ensLoss |   0.0018 |  -6.1443 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.032  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 |  -9.9844 | greater       |
|  6 | Hinge | ensLoss |   0.9982 |  -6.1443 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.032  | greater       |

#### PCam - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'PCam',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 30},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 30,
             'val_per_epochs': 3}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8158 | 0.7613 |  0.8277 |    0.8591 |
| ('test_acc', 'std')  | 0.0025 | 0.0035 |  0.0041 |    0.0019 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9349 | 0.8789 |  0.8409 |    0.9551 |
| ('test_auc', 'std')  | 0.0017 | 0.0046 |  0.006  |    0.0014 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -11.4364 | less          |
|  6 | Hinge | ensLoss |   0.0003 |  -9.8803 | less          |
|  9 | EXP   | ensLoss |   0      | -20.7083 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -11.4364 | greater       |
|  6 | Hinge | ensLoss |   0.9997 |  -9.8803 | greater       |
|  9 | EXP   | ensLoss |   1      | -20.7083 | greater       |
