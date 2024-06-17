
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
               'weight_decay': 0.0},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.6799 | 0.6009 |  0.6819 |    0.6952 |
| ('test_acc', 'std')  | 0.003  | 0.0019 |  0.004  |    0.0138 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.7473 | 0.6431 |  0.7412 |    0.7624 |
| ('test_auc', 'std')  | 0.0034 | 0.003  |  0.0041 |    0.0166 |

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
               'weight_decay': 0.005},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.68   | 0.6226 |  0.6826 |    0.7084 |
| ('test_acc', 'std')  | 0.0031 | 0.0045 |  0.0035 |    0.0067 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.7425 | 0.6681 |  0.7485 |    0.7772 |
| ('test_auc', 'std')  | 0.0047 | 0.0046 |  0.0036 |    0.0066 |

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
               'weight_decay': 5e-05},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.6764 | 0.6043 |  0.6826 |    0.7101 |
| ('test_acc', 'std')  | 0.0014 | 0.0023 |  0.0065 |    0.0104 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.7438 | 0.6469 |  0.7425 |    0.7783 |
| ('test_auc', 'std')  | 0.0024 | 0.0022 |  0.0044 |    0.0143 |


#### CIFAR35 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataAug': False,
 'dataset': 'CIFAR35',
 'device': device(type='cuda', index=0),
 'model': {'dropout_rate': 0.1,
           'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0},
 'save_model': False,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.675  | 0.607  |  0.6789 |    0.7248 |
| ('test_acc', 'std')  | 0.0039 | 0.0034 |  0.003  |    0.0022 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.7375 | 0.6429 |  0.7461 |    0.7944 |
| ('test_auc', 'std')  | 0.0028 | 0.0028 |  0.003  |    0.0019 |

#### CIFAR35 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataAug': False,
 'dataset': 'CIFAR35',
 'device': device(type='cuda', index=0),
 'model': {'dropout_rate': 0.2,
           'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0},
 'save_model': False,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.6813 | 0.6002 |  0.6778 |    0.7008 |
| ('test_acc', 'std')  | 0.0054 | 0.0052 |  0.0044 |    0.0128 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.7456 | 0.6345 |  0.7422 |    0.7713 |
| ('test_auc', 'std')  | 0.0058 | 0.0065 |  0.0023 |    0.0156 |

#### CIFAR35 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataAug': False,
 'dataset': 'CIFAR35',
 'device': device(type='cuda', index=0),
 'model': {'dropout_rate': 0.3,
           'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0},
 'save_model': False,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.6765 | 0.597  |  0.6778 |    0.7244 |
| ('test_acc', 'std')  | 0.0029 | 0.0046 |  0.0049 |    0.0068 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.7429 | 0.6367 |  0.7421 |    0.7948 |
| ('test_auc', 'std')  | 0.0013 | 0.0031 |  0.0034 |    0.0065 |

#### CIFAR35 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataAug': True,
 'dataset': 'CIFAR35',
 'device': device(type='cuda', index=0),
 'model': {'dropout_rate': 0.0,
           'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0},
 'save_model': False,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7922 | 0.5896 |  0.8047 |    0.83   |
| ('test_acc', 'std')  | 0.0012 | 0.0031 |  0.0026 |    0.0025 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8731 | 0.6227 |  0.8526 |    0.9098 |
| ('test_auc', 'std')  | 0.002  | 0.0036 |  0.002  |    0.0021 |
