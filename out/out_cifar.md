

#### CIFAR01 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR01',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9586 | 0.9309 |  0.9641 |    0.9653 |
| ('test_acc', 'std')  | 0.0014 | 0.0013 |  0.001  |    0.0075 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9927 | 0.9819 |  0.9937 |    0.9928 |
| ('test_auc', 'std')  | 0.0002 | 0.0011 |  0.0004 |    0.003  |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.2166 | -0.8705 | less          |
|  6 | Hinge | ensLoss |   0.4445 | -0.1486 | less          |
|  9 | EXP   | ensLoss |   0.0038 | -4.9699 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.7834 | -0.8705 | greater       |
|  6 | Hinge | ensLoss |   0.5555 | -0.1486 | greater       |
|  9 | EXP   | ensLoss |   0.9962 | -4.9699 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.4798 | -0.0538 | less          |
|  6 | Hinge | ensLoss |   0.6212 |  0.3305 | less          |
|  9 | EXP   | ensLoss |   0.0064 | -4.2804 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.5202 | -0.0538 | greater       |
|  6 | Hinge | ensLoss |   0.3788 |  0.3305 | greater       |
|  9 | EXP   | ensLoss |   0.9936 | -4.2804 | greater       |


#### CIFAR01 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR01',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9621 | 0.922  |  0.9614 |    0.9697 |
| ('test_acc', 'std')  | 0.001  | 0.0013 |  0.0017 |    0.0056 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9928 | 0.9766 |  0.9928 |    0.9941 |
| ('test_auc', 'std')  | 0.0003 | 0.0007 |  0.0002 |    0.0017 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.1347 | -1.2812 | less          |
|  6 | Hinge | ensLoss |   0.069  | -1.8495 | less          |
|  9 | EXP   | ensLoss |   0.0008 | -7.4893 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.8653 | -1.2812 | greater       |
|  6 | Hinge | ensLoss |   0.931  | -1.8495 | greater       |
|  9 | EXP   | ensLoss |   0.9992 | -7.4893 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.2206 | -0.8543 | less          |
|  6 | Hinge | ensLoss |   0.2647 | -0.6878 | less          |
|  9 | EXP   | ensLoss |   0.0007 | -7.7715 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.7794 | -0.8543 | greater       |
|  6 | Hinge | ensLoss |   0.7353 | -0.6878 | greater       |
|  9 | EXP   | ensLoss |   0.9993 | -7.7715 | greater       |


#### CIFAR02 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR02',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9147 | 0.8892 |  0.9148 |    0.9288 |
| ('test_acc', 'std')  | 0.0022 | 0.002  |  0.0017 |    0.0025 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9731 | 0.9552 |  0.9725 |    0.9802 |
| ('test_auc', 'std')  | 0.0011 | 0.0008 |  0.0011 |    0.0009 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0165 |  -3.1984 | less          |
|  6 | Hinge | ensLoss |   0.0118 |  -3.5618 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.355  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9835 |  -3.1984 | greater       |
|  6 | Hinge | ensLoss |   0.9882 |  -3.5618 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.355  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0074 |  -4.1074 | less          |
|  6 | Hinge | ensLoss |   0.0039 |  -4.93   | less          |
|  9 | EXP   | ensLoss |   0      | -20.5148 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9926 |  -4.1074 | greater       |
|  6 | Hinge | ensLoss |   0.9961 |  -4.93   | greater       |
|  9 | EXP   | ensLoss |   1      | -20.5148 | greater       |


#### CIFAR02 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR02',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9159 | 0.8716 |  0.9199 |    0.9248 |
| ('test_acc', 'std')  | 0.003  | 0.0042 |  0.0019 |    0.0028 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9711 | 0.9452 |  0.9704 |    0.9772 |
| ('test_auc', 'std')  | 0.0007 | 0.0014 |  0.0003 |    0.0023 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0937 |  -1.588  | less          |
|  6 | Hinge | ensLoss |   0.0703 |  -1.8344 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -11.8618 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9063 |  -1.588  | greater       |
|  6 | Hinge | ensLoss |   0.9298 |  -1.8344 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -11.8618 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0458 |  -2.2097 | less          |
|  6 | Hinge | ensLoss |   0.023  |  -2.8607 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.0496 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9542 |  -2.2097 | greater       |
|  6 | Hinge | ensLoss |   0.977  |  -2.8607 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.0496 | greater       |


#### CIFAR03 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR03',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9413 | 0.9312 |  0.9468 |    0.9515 |
| ('test_acc', 'std')  | 0.0014 | 0.001  |  0.0018 |    0.0018 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9859 | 0.9795 |  0.9868 |    0.9897 |
| ('test_auc', 'std')  | 0.0009 | 0.0005 |  0.0002 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0052 |  -4.5434 | less          |
|  6 | Hinge | ensLoss |   0.0994 |  -1.5379 | less          |
|  9 | EXP   | ensLoss |   0      | -17.3751 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9948 |  -4.5434 | greater       |
|  6 | Hinge | ensLoss |   0.9006 |  -1.5379 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.3751 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0049 |  -4.6382 | less          |
|  6 | Hinge | ensLoss |   0.0021 |  -5.9002 | less          |
|  9 | EXP   | ensLoss |   0      | -15.2398 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9951 |  -4.6382 | greater       |
|  6 | Hinge | ensLoss |   0.9979 |  -5.9002 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.2398 | greater       |


#### CIFAR03 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR03',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9452 | 0.9165 |  0.9439 |    0.9519 |
| ('test_acc', 'std')  | 0.0013 | 0.0011 |  0.0022 |    0.0021 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9869 | 0.9745 |  0.983  |    0.9896 |
| ('test_auc', 'std')  | 0.0004 | 0.0003 |  0.0013 |    0.0006 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0036 |  -5.0432 | less          |
|  6 | Hinge | ensLoss |   0.0353 |  -2.4485 | less          |
|  9 | EXP   | ensLoss |   0      | -23.0434 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9964 |  -5.0432 | greater       |
|  6 | Hinge | ensLoss |   0.9647 |  -2.4485 | greater       |
|  9 | EXP   | ensLoss |   1      | -23.0434 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0007 |  -7.9971 | less          |
|  6 | Hinge | ensLoss |   0.0081 |  -3.9906 | less          |
|  9 | EXP   | ensLoss |   0      | -27.5393 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9993 |  -7.9971 | greater       |
|  6 | Hinge | ensLoss |   0.9919 |  -3.9906 | greater       |
|  9 | EXP   | ensLoss |   1      | -27.5393 | greater       |


#### CIFAR04 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR04',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9532 | 0.9333 |  0.9556 |    0.9631 |
| ('test_acc', 'std')  | 0.0026 | 0.0015 |  0.0011 |    0.0012 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9911 | 0.9817 |  0.9921 |    0.9939 |
| ('test_auc', 'std')  | 0.0003 | 0.0004 |  0.0001 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0199 |  -3.0041 | less          |
|  6 | Hinge | ensLoss |   0.0089 |  -3.886  | less          |
|  9 | EXP   | ensLoss |   0      | -17.7614 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9801 |  -3.0041 | greater       |
|  6 | Hinge | ensLoss |   0.9911 |  -3.886  | greater       |
|  9 | EXP   | ensLoss |   1      | -17.7614 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0031 |  -5.2736 | less          |
|  6 | Hinge | ensLoss |   0.0014 |  -6.5749 | less          |
|  9 | EXP   | ensLoss |   0      | -47.9093 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9969 |  -5.2736 | greater       |
|  6 | Hinge | ensLoss |   0.9986 |  -6.5749 | greater       |
|  9 | EXP   | ensLoss |   1      | -47.9093 | greater       |


#### CIFAR04 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR04',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9573 | 0.9246 |  0.9563 |    0.9658 |
| ('test_acc', 'std')  | 0.0017 | 0.003  |  0.0021 |    0.0014 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9922 | 0.9772 |  0.9903 |    0.9947 |
| ('test_auc', 'std')  | 0.0007 | 0.001  |  0.0005 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0034 |  -5.1492 | less          |
|  6 | Hinge | ensLoss |   0.0053 |  -4.5289 | less          |
|  9 | EXP   | ensLoss |   0      | -16.2667 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9966 |  -5.1492 | greater       |
|  6 | Hinge | ensLoss |   0.9947 |  -4.5289 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.2667 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0146 |  -3.3278 | less          |
|  6 | Hinge | ensLoss |   0.0006 |  -8.1045 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -15.0024 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9854 |  -3.3278 | greater       |
|  6 | Hinge | ensLoss |   0.9994 |  -8.1045 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -15.0024 | greater       |


#### CIFAR05 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR05',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9578 | 0.9494 |  0.9628 |    0.9612 |
| ('test_acc', 'std')  | 0.0008 | 0.0012 |  0.0015 |    0.001  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9924 | 0.9885 |  0.993  |    0.9933 |
| ('test_auc', 'std')  | 0.0003 | 0.0002 |  0.0004 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0166 | -3.1914 | less          |
|  6 | Hinge | ensLoss |   0.8012 |  0.9461 | less          |
|  9 | EXP   | ensLoss |   0.0024 | -5.6806 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9834 | -3.1914 | greater       |
|  6 | Hinge | ensLoss |   0.1988 |  0.9461 | greater       |
|  9 | EXP   | ensLoss |   0.9976 | -5.6806 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.015  | -3.2968 | less          |
|  6 | Hinge | ensLoss |   0.2035 | -0.9258 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -9.8308 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.985  | -3.2968 | greater       |
|  6 | Hinge | ensLoss |   0.7965 | -0.9258 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -9.8308 | greater       |


#### CIFAR05 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR05',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.96   | 0.9405 |  0.9603 |    0.9653 |
| ('test_acc', 'std')  | 0.0012 | 0.0015 |  0.0013 |    0.0016 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9929 | 0.9864 |  0.9918 |    0.9931 |
| ('test_auc', 'std')  | 0.0003 | 0.0004 |  0.0005 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.018  |  -3.1042 | less          |
|  6 | Hinge | ensLoss |   0.0651 |  -1.9    | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.8339 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.982  |  -3.1042 | greater       |
|  6 | Hinge | ensLoss |   0.9349 |  -1.9    | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.8339 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.3637 |  -0.3741 | less          |
|  6 | Hinge | ensLoss |   0.0519 |  -2.099  | less          |
|  9 | EXP   | ensLoss |   0      | -16.4387 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.6363 |  -0.3741 | greater       |
|  6 | Hinge | ensLoss |   0.9481 |  -2.099  | greater       |
|  9 | EXP   | ensLoss |   1      | -16.4387 | greater       |


#### CIFAR06 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR06',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9726 | 0.9627 |  0.972  |    0.9727 |
| ('test_acc', 'std')  | 0.0016 | 0.0009 |  0.0007 |    0.0019 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9962 | 0.9932 |  0.9956 |    0.9952 |
| ('test_auc', 'std')  | 0.0001 | 0.0003 |  0.0002 |    0.001  |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.4799 | -0.0536 | less          |
|  6 | Hinge | ensLoss |   0.3451 | -0.4288 | less          |
|  9 | EXP   | ensLoss |   0.0009 | -7.4536 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.5201 | -0.0536 | greater       |
|  6 | Hinge | ensLoss |   0.6549 | -0.4288 | greater       |
|  9 | EXP   | ensLoss |   0.9991 | -7.4536 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.7881 |  0.89   | less          |
|  6 | Hinge | ensLoss |   0.6466 |  0.404  | less          |
|  9 | EXP   | ensLoss |   0.0497 | -2.1365 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.2119 |  0.89   | greater       |
|  6 | Hinge | ensLoss |   0.3534 |  0.404  | greater       |
|  9 | EXP   | ensLoss |   0.9503 | -2.1365 | greater       |


#### CIFAR06 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR06',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9702 | 0.9584 |  0.9718 |    0.9754 |
| ('test_acc', 'std')  | 0.0015 | 0.0006 |  0.0012 |    0.002  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9961 | 0.991  |  0.9957 |    0.9966 |
| ('test_auc', 'std')  | 0.0002 | 0.0003 |  0.0003 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0132 | -3.4362 | less          |
|  6 | Hinge | ensLoss |   0.1141 | -1.4219 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -9.6946 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9868 | -3.4362 | greater       |
|  6 | Hinge | ensLoss |   0.8859 | -1.4219 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -9.6946 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.2275 | -0.8265 | less          |
|  6 | Hinge | ensLoss |   0.0602 | -1.969  | less          |
|  9 | EXP   | ensLoss |   0.0003 | -9.5087 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.7725 | -0.8265 | greater       |
|  6 | Hinge | ensLoss |   0.9398 | -1.969  | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -9.5087 | greater       |


#### CIFAR07 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR07',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9621 | 0.9411 |  0.9633 |    0.9702 |
| ('test_acc', 'std')  | 0.0016 | 0.0015 |  0.0014 |    0.0013 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9932 | 0.9865 |  0.9938 |    0.9947 |
| ('test_auc', 'std')  | 0.0005 | 0.0006 |  0.0002 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0044 |  -4.7688 | less          |
|  6 | Hinge | ensLoss |   0.0035 |  -5.0937 | less          |
|  9 | EXP   | ensLoss |   0      | -17.1325 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9956 |  -4.7688 | greater       |
|  6 | Hinge | ensLoss |   0.9965 |  -5.0937 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.1325 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.023  |  -2.8605 | less          |
|  6 | Hinge | ensLoss |   0.0122 |  -3.5251 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -11.9311 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.977  |  -2.8605 | greater       |
|  6 | Hinge | ensLoss |   0.9878 |  -3.5251 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -11.9311 | greater       |


#### CIFAR07 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR07',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9616 | 0.9345 |  0.9649 |    0.9709 |
| ('test_acc', 'std')  | 0.0008 | 0.0022 |  0.0014 |    0.0018 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9933 | 0.9835 |  0.9926 |    0.9948 |
| ('test_auc', 'std')  | 0.0002 | 0.0001 |  0.0003 |    0.0008 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0105 |  -3.6862 | less          |
|  6 | Hinge | ensLoss |   0.0213 |  -2.9364 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.6257 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9895 |  -3.6862 | greater       |
|  6 | Hinge | ensLoss |   0.9787 |  -2.9364 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.6257 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0718 |  -1.8151 | less          |
|  6 | Hinge | ensLoss |   0.0495 |  -2.1401 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.6755 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9282 |  -1.8151 | greater       |
|  6 | Hinge | ensLoss |   0.9505 |  -2.1401 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.6755 | greater       |

#### CIFAR08 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR08',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9245 | 0.8712 |  0.9262 |    0.9269 |
| ('test_acc', 'std')  | 0.0023 | 0.0012 |  0.001  |    0.0048 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9761 | 0.9433 |  0.9776 |    0.9778 |
| ('test_auc', 'std')  | 0.0008 | 0.0017 |  0.0005 |    0.0026 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.371  |  -0.3529 | less          |
|  6 | Hinge | ensLoss |   0.452  |  -0.1284 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.984  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.629  |  -0.3529 | greater       |
|  6 | Hinge | ensLoss |   0.548  |  -0.1284 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.984  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.2841 |  -0.6212 | less          |
|  6 | Hinge | ensLoss |   0.4667 |  -0.089  | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.4948 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.716  |  -0.6212 | greater       |
|  6 | Hinge | ensLoss |   0.5333 |  -0.089  | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.4948 | greater       |

#### CIFAR08 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR08',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9255 | 0.8557 |  0.9311 |    0.9395 |
| ('test_acc', 'std')  | 0.0034 | 0.0026 |  0.0015 |    0.0036 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9768 | 0.9286 |  0.9769 |    0.9835 |
| ('test_auc', 'std')  | 0.0007 | 0.002  |  0.0003 |    0.0011 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0299 |  -2.6031 | less          |
|  6 | Hinge | ensLoss |   0.0584 |  -1.9946 | less          |
|  9 | EXP   | ensLoss |   0      | -16.7886 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9701 |  -2.6031 | greater       |
|  6 | Hinge | ensLoss |   0.9416 |  -1.9946 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.7886 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0056 |  -4.4614 | less          |
|  6 | Hinge | ensLoss |   0.004  |  -4.8904 | less          |
|  9 | EXP   | ensLoss |   0      | -22.1356 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9944 |  -4.4614 | greater       |
|  6 | Hinge | ensLoss |   0.996  |  -4.8904 | greater       |
|  9 | EXP   | ensLoss |   1      | -22.1356 | greater       |

#### CIFAR09 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR09',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9413 | 0.9165 |  0.9444 |    0.9575 |
| ('test_acc', 'std')  | 0.0011 | 0.0017 |  0.0009 |    0.0022 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9865 | 0.9741 |  0.9877 |    0.9932 |
| ('test_auc', 'std')  | 0.0003 | 0.001  |  0.0003 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0008 |  -7.4805 | less          |
|  6 | Hinge | ensLoss |   0.0003 | -10.0918 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -11.923  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9992 |  -7.4805 | greater       |
|  6 | Hinge | ensLoss |   0.9997 | -10.0918 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -11.923  | greater       |
|    | A     | B       |   pvalue |      stat | alternative   |
|---:|:------|:--------|---------:|----------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -194.923  | less          |
|  6 | Hinge | ensLoss |        0 |  -18.9217 | less          |
|  9 | EXP   | ensLoss |        0 |  -20.5415 | less          |


|    | A     | B       |   pvalue |      stat | alternative   |
|---:|:------|:--------|---------:|----------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -194.923  | greater       |
|  6 | Hinge | ensLoss |        1 |  -18.9217 | greater       |
|  9 | EXP   | ensLoss |        1 |  -20.5415 | greater       |

#### CIFAR09 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR09',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9449 | 0.9009 |  0.9431 |    0.9594 |
| ('test_acc', 'std')  | 0.0013 | 0.0022 |  0.001  |    0.0028 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9876 | 0.9661 |  0.986  |    0.9931 |
| ('test_auc', 'std')  | 0.0004 | 0.0009 |  0.0004 |    0.0005 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0062 |  -4.3183 | less          |
|  6 | Hinge | ensLoss |   0.0036 |  -5.0508 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.1585 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9938 |  -4.3183 | greater       |
|  6 | Hinge | ensLoss |   0.9964 |  -5.0508 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.1585 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0008 |  -7.6458 | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -9.428  | less          |
|  9 | EXP   | ensLoss |   0      | -21.489  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9992 |  -7.6458 | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -9.428  | greater       |
|  9 | EXP   | ensLoss |   1      | -21.489  | greater       |

#### CIFAR12 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR12',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9705 | 0.9643 |  0.9743 |    0.9838 |
| ('test_acc', 'std')  | 0.0013 | 0.002  |  0.0009 |    0.0005 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9965 | 0.9945 |  0.9972 |    0.9987 |
| ('test_auc', 'std')  | 0.0002 | 0.0003 |  0.0001 |    0.0001 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0005 | -8.7889 | less          |
|  6 | Hinge | ensLoss |   0.0005 | -8.764  | less          |
|  9 | EXP   | ensLoss |   0.0005 | -8.656  | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9995 | -8.7889 | greater       |
|  6 | Hinge | ensLoss |   0.9995 | -8.764  | greater       |
|  9 | EXP   | ensLoss |   0.9995 | -8.656  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.8798 | less          |
|  6 | Hinge | ensLoss |   0.0009 |  -7.4578 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -11.0907 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.8798 | greater       |
|  6 | Hinge | ensLoss |   0.9991 |  -7.4578 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -11.0907 | greater       |

#### CIFAR12 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR12',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9721 | 0.9527 |  0.9708 |    0.9838 |
| ('test_acc', 'std')  | 0.0013 | 0.0014 |  0.0017 |    0.0009 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9971 | 0.9915 |  0.9963 |    0.9988 |
| ('test_auc', 'std')  | 0.0002 | 0.0002 |  0.0002 |    0.0001 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0015 |  -6.402  | less          |
|  6 | Hinge | ensLoss |   0.0024 |  -5.6469 | less          |
|  9 | EXP   | ensLoss |   0      | -19.6301 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9985 |  -6.402  | greater       |
|  6 | Hinge | ensLoss |   0.9976 |  -5.6469 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.6301 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0011 |  -7.0008 | less          |
|  6 | Hinge | ensLoss |   0.0003 |  -9.9743 | less          |
|  9 | EXP   | ensLoss |   0      | -33.6496 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9989 |  -7.0008 | greater       |
|  6 | Hinge | ensLoss |   0.9997 |  -9.9743 | greater       |
|  9 | EXP   | ensLoss |   1      | -33.6496 | greater       |

#### CIFAR13 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR13',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9664 | 0.9567 |  0.9693 |    0.9777 |
| ('test_acc', 'std')  | 0.0013 | 0.0014 |  0.0008 |    0.0012 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9953 | 0.9925 |  0.9959 |    0.9974 |
| ('test_auc', 'std')  | 0.0002 | 0.0003 |  0.0001 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0024 |  -5.6749 | less          |
|  6 | Hinge | ensLoss |   0.0028 |  -5.4109 | less          |
|  9 | EXP   | ensLoss |   0      | -18.9736 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9976 |  -5.6749 | greater       |
|  6 | Hinge | ensLoss |   0.9972 |  -5.4109 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.9736 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0046 |  -4.7188 | less          |
|  6 | Hinge | ensLoss |   0.0079 |  -4.0257 | less          |
|  9 | EXP   | ensLoss |   0      | -30.4575 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9954 |  -4.7188 | greater       |
|  6 | Hinge | ensLoss |   0.9921 |  -4.0257 | greater       |
|  9 | EXP   | ensLoss |   1      | -30.4575 | greater       |

#### CIFAR13 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR13',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9671 | 0.9511 |  0.9692 |    0.978  |
| ('test_acc', 'std')  | 0.0016 | 0.0013 |  0.002  |    0.0015 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9956 | 0.9905 |  0.9957 |    0.9974 |
| ('test_auc', 'std')  | 0.0002 | 0.0004 |  0.0004 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0016 |  -6.3355 | less          |
|  6 | Hinge | ensLoss |   0.0198 |  -3.0113 | less          |
|  9 | EXP   | ensLoss |   0      | -22.0744 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9984 |  -6.3355 | greater       |
|  6 | Hinge | ensLoss |   0.9802 |  -3.0113 | greater       |
|  9 | EXP   | ensLoss |   1      | -22.0744 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 |  -9.5277 | less          |
|  6 | Hinge | ensLoss |   0.0099 |  -3.7572 | less          |
|  9 | EXP   | ensLoss |   0      | -20.9191 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 |  -9.5277 | greater       |
|  6 | Hinge | ensLoss |   0.9901 |  -3.7572 | greater       |
|  9 | EXP   | ensLoss |   1      | -20.9191 | greater       |

#### CIFAR14 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR14',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9814 | 0.9709 |  0.9834 |    0.989  |
| ('test_acc', 'std')  | 0.0016 | 0.0014 |  0.0006 |    0.0009 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9987 | 0.9967 |  0.9992 |    0.9992 |
| ('test_auc', 'std')  | 0.0002 | 0.0001 |  0.0001 |    0.0001 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0025 |  -5.6104 | less          |
|  6 | Hinge | ensLoss |   0.002  |  -5.9527 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -11.4819 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9975 |  -5.6104 | greater       |
|  6 | Hinge | ensLoss |   0.998  |  -5.9527 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -11.4819 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0117 |  -3.567  | less          |
|  6 | Hinge | ensLoss |   0.576  |   0.2044 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.1916 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9883 |  -3.567  | greater       |
|  6 | Hinge | ensLoss |   0.424  |   0.2044 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.1916 | greater       |

#### CIFAR14 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR14',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9821 | 0.9678 |  0.9832 |    0.9892 |
| ('test_acc', 'std')  | 0.001  | 0.0015 |  0.0008 |    0.0008 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9988 | 0.9949 |  0.9988 |    0.9991 |
| ('test_auc', 'std')  | 0.0001 | 0.0002 |  0.0001 |    0.0001 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0004 |  -8.9098 | less          |
|  6 | Hinge | ensLoss |   0.005  |  -4.6018 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.3381 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9996 |  -8.9098 | greater       |
|  6 | Hinge | ensLoss |   0.995  |  -4.6018 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.3381 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0267 |  -2.712  | less          |
|  6 | Hinge | ensLoss |   0.0014 |  -6.5597 | less          |
|  9 | EXP   | ensLoss |   0      | -17.9268 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9733 |  -2.712  | greater       |
|  6 | Hinge | ensLoss |   0.9986 |  -6.5597 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.9268 | greater       |

#### CIFAR15 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR15',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.981  | 0.9708 |  0.9788 |    0.986  |
| ('test_acc', 'std')  | 0.0009 | 0.0008 |  0.001  |    0.0007 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9982 | 0.9964 |  0.998  |    0.9987 |
| ('test_auc', 'std')  | 0.0002 | 0.0001 |  0.0002 |    0.0001 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0005 |  -8.7704 | less          |
|  6 | Hinge | ensLoss |   0.0024 |  -5.6656 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.5144 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9995 |  -8.7704 | greater       |
|  6 | Hinge | ensLoss |   0.9976 |  -5.6656 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.5144 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0298 |  -2.6086 | less          |
|  6 | Hinge | ensLoss |   0.0118 |  -3.5617 | less          |
|  9 | EXP   | ensLoss |   0      | -25.0855 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9702 |  -2.6086 | greater       |
|  6 | Hinge | ensLoss |   0.9882 |  -3.5617 | greater       |
|  9 | EXP   | ensLoss |   1      | -25.0855 | greater       |

#### CIFAR15 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR15',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9808 | 0.9687 |  0.978  |    0.9867 |
| ('test_acc', 'std')  | 0.0011 | 0.0009 |  0.0015 |    0.0009 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9983 | 0.996  |  0.9979 |    0.9988 |
| ('test_auc', 'std')  | 0.0001 | 0.0002 |  0.0001 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0068 |  -4.2143 | less          |
|  6 | Hinge | ensLoss |   0.0011 |  -6.9544 | less          |
|  9 | EXP   | ensLoss |   0      | -15.787  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9932 |  -4.2143 | greater       |
|  6 | Hinge | ensLoss |   0.9989 |  -6.9544 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.787  | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0865 | -1.6561 | less          |
|  6 | Hinge | ensLoss |   0.0083 | -3.9636 | less          |
|  9 | EXP   | ensLoss |   0.0008 | -7.5459 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9135 | -1.6561 | greater       |
|  6 | Hinge | ensLoss |   0.9917 | -3.9636 | greater       |
|  9 | EXP   | ensLoss |   0.9992 | -7.5459 | greater       |

#### CIFAR16 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR16',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.98   | 0.9755 |  0.9822 |    0.9864 |
| ('test_acc', 'std')  | 0.0013 | 0.0006 |  0.0005 |    0.001  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9982 | 0.9969 |  0.9985 |    0.9992 |
| ('test_auc', 'std')  | 0.0001 | 0.0002 |  0.0001 |    0.0001 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0128 |  -3.4658 | less          |
|  6 | Hinge | ensLoss |   0.0088 |  -3.8912 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -10.0131 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9872 |  -3.4658 | greater       |
|  6 | Hinge | ensLoss |   0.9912 |  -3.8912 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -10.0131 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0004 | -9.3742 | less          |
|  6 | Hinge | ensLoss |   0.009  | -3.8735 | less          |
|  9 | EXP   | ensLoss |   0.0008 | -7.7527 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9996 | -9.3742 | greater       |
|  6 | Hinge | ensLoss |   0.991  | -3.8735 | greater       |
|  9 | EXP   | ensLoss |   0.9992 | -7.7527 | greater       |

#### CIFAR16 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR16',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9821 | 0.9676 |  0.9807 |    0.9847 |
| ('test_acc', 'std')  | 0.0012 | 0.0006 |  0.0012 |    0.0024 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9983 | 0.9954 |  0.998  |    0.999  |
| ('test_auc', 'std')  | 0.0001 | 0.0003 |  0.0001 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.1457 | -1.2142 | less          |
|  6 | Hinge | ensLoss |   0.1365 | -1.2697 | less          |
|  9 | EXP   | ensLoss |   0.0011 | -7.0044 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.8543 | -1.2142 | greater       |
|  6 | Hinge | ensLoss |   0.8635 | -1.2697 | greater       |
|  9 | EXP   | ensLoss |   0.9989 | -7.0044 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0562 | -2.0279 | less          |
|  6 | Hinge | ensLoss |   0.0356 | -2.4393 | less          |
|  9 | EXP   | ensLoss |   0.0015 | -6.4168 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9438 | -2.0279 | greater       |
|  6 | Hinge | ensLoss |   0.9644 | -2.4393 | greater       |
|  9 | EXP   | ensLoss |   0.9985 | -6.4168 | greater       |

#### CIFAR17 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR17',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9811 | 0.9683 |  0.9837 |    0.9892 |
| ('test_acc', 'std')  | 0.0012 | 0.0009 |  0.0007 |    0.0011 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9984 | 0.9962 |  0.9988 |    0.9995 |
| ('test_auc', 'std')  | 0.0003 | 0.0002 |  0.0001 |    0.0001 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0006 |  -8.1614 | less          |
|  6 | Hinge | ensLoss |   0.016  |  -3.2297 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -11.9478 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9994 |  -8.1614 | greater       |
|  6 | Hinge | ensLoss |   0.984  |  -3.2297 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -11.9478 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0017 |  -6.2581 | less          |
|  6 | Hinge | ensLoss |   0.0076 |  -4.0702 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -15.0376 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9983 |  -6.2581 | greater       |
|  6 | Hinge | ensLoss |   0.9924 |  -4.0702 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -15.0376 | greater       |

#### CIFAR17 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR17',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9817 | 0.96   |  0.9817 |    0.9854 |
| ('test_acc', 'std')  | 0.0005 | 0.0015 |  0.0004 |    0.0025 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9987 | 0.9933 |  0.9985 |    0.9984 |
| ('test_auc', 'std')  | 0.0001 | 0.0003 |  0.0001 |    0.0005 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0955 | -1.572  | less          |
|  6 | Hinge | ensLoss |   0.1006 | -1.5278 | less          |
|  9 | EXP   | ensLoss |   0.0007 | -7.8071 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9045 | -1.572  | greater       |
|  6 | Hinge | ensLoss |   0.8994 | -1.5278 | greater       |
|  9 | EXP   | ensLoss |   0.9993 | -7.8071 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.7137 |  0.6138 | less          |
|  6 | Hinge | ensLoss |   0.5989 |  0.2678 | less          |
|  9 | EXP   | ensLoss |   0.0011 | -7.0395 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.2863 |  0.6138 | greater       |
|  6 | Hinge | ensLoss |   0.4011 |  0.2678 | greater       |
|  9 | EXP   | ensLoss |   0.9989 | -7.0395 | greater       |

#### CIFAR18 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR18',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9581 | 0.9324 |  0.9618 |    0.9674 |
| ('test_acc', 'std')  | 0.0011 | 0.0012 |  0.002  |    0.0018 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9922 | 0.9815 |  0.9939 |    0.9956 |
| ('test_auc', 'std')  | 0.0007 | 0.0004 |  0.0004 |    0.0009 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0026 |  -5.5185 | less          |
|  6 | Hinge | ensLoss |   0.0039 |  -4.9401 | less          |
|  9 | EXP   | ensLoss |   0      | -15.6135 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9974 |  -5.5185 | greater       |
|  6 | Hinge | ensLoss |   0.9961 |  -4.9401 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.6135 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0132 |  -3.4359 | less          |
|  6 | Hinge | ensLoss |   0.049  |  -2.1501 | less          |
|  9 | EXP   | ensLoss |   0      | -19.6282 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9868 |  -3.4359 | greater       |
|  6 | Hinge | ensLoss |   0.951  |  -2.1501 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.6282 | greater       |

#### CIFAR18 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR18',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9612 | 0.9177 |  0.9628 |    0.9733 |
| ('test_acc', 'std')  | 0.0024 | 0.0025 |  0.0007 |    0.0009 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9932 | 0.9751 |  0.9917 |    0.9962 |
| ('test_auc', 'std')  | 0.0003 | 0.0011 |  0.0002 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0035 |  -5.0973 | less          |
|  6 | Hinge | ensLoss |   0.0003 | -10.0112 | less          |
|  9 | EXP   | ensLoss |   0      | -20.4597 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9965 |  -5.0973 | greater       |
|  6 | Hinge | ensLoss |   0.9997 | -10.0112 | greater       |
|  9 | EXP   | ensLoss |   1      | -20.4597 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -11.7702 | less          |
|  6 | Hinge | ensLoss |   0      | -20.6694 | less          |
|  9 | EXP   | ensLoss |   0      | -17.4422 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -11.7702 | greater       |
|  6 | Hinge | ensLoss |   1      | -20.6694 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.4422 | greater       |

#### CIFAR19 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR19',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9204 | 0.8423 |  0.9209 |    0.9283 |
| ('test_acc', 'std')  | 0.0013 | 0.004  |  0.0014 |    0.0145 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9762 | 0.9199 |  0.9757 |    0.9779 |
| ('test_auc', 'std')  | 0.0008 | 0.0028 |  0.0012 |    0.0084 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.3148 | -0.5214 | less          |
|  6 | Hinge | ensLoss |   0.3063 | -0.5484 | less          |
|  9 | EXP   | ensLoss |   0.0019 | -6.0543 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.6852 | -0.5214 | greater       |
|  6 | Hinge | ensLoss |   0.6937 | -0.5484 | greater       |
|  9 | EXP   | ensLoss |   0.9981 | -6.0543 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.4195 | -0.2168 | less          |
|  6 | Hinge | ensLoss |   0.3974 | -0.278  | less          |
|  9 | EXP   | ensLoss |   0.0006 | -8.2245 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.5805 | -0.2168 | greater       |
|  6 | Hinge | ensLoss |   0.6026 | -0.278  | greater       |
|  9 | EXP   | ensLoss |   0.9994 | -8.2245 | greater       |

#### CIFAR19 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR19',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9177 | 0.8073 |  0.9193 |    0.9303 |
| ('test_acc', 'std')  | 0.0027 | 0.0022 |  0.0014 |    0.0084 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9738 | 0.8906 |  0.9707 |    0.9794 |
| ('test_auc', 'std')  | 0.0011 | 0.0015 |  0.0004 |    0.0053 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.1482 |  -1.1998 | less          |
|  6 | Hinge | ensLoss |   0.1356 |  -1.2755 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.5815 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.8518 |  -1.1998 | greater       |
|  6 | Hinge | ensLoss |   0.8644 |  -1.2755 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.5815 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.1961 |  -0.9584 | less          |
|  6 | Hinge | ensLoss |   0.0781 |  -1.744  | less          |
|  9 | EXP   | ensLoss |   0      | -15.8893 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.8039 |  -0.9584 | greater       |
|  6 | Hinge | ensLoss |   0.9219 |  -1.744  | greater       |
|  9 | EXP   | ensLoss |   1      | -15.8893 | greater       |

#### CIFAR23 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR23',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.854  | 0.803  |  0.8539 |    0.8574 |
| ('test_acc', 'std')  | 0.0018 | 0.0023 |  0.0036 |    0.0168 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9288 | 0.8805 |  0.9294 |    0.932  |
| ('test_auc', 'std')  | 0.0006 | 0.0019 |  0.0023 |    0.0125 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.4246 | -0.2028 | less          |
|  6 | Hinge | ensLoss |   0.4322 | -0.182  | less          |
|  9 | EXP   | ensLoss |   0.0223 | -2.8901 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.5754 | -0.2028 | greater       |
|  6 | Hinge | ensLoss |   0.5678 | -0.182  | greater       |
|  9 | EXP   | ensLoss |   0.9777 | -2.8901 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.4061 | -0.2537 | less          |
|  6 | Hinge | ensLoss |   0.4275 | -0.1948 | less          |
|  9 | EXP   | ensLoss |   0.0106 | -3.6828 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.5939 | -0.2537 | greater       |
|  6 | Hinge | ensLoss |   0.5725 | -0.1948 | greater       |
|  9 | EXP   | ensLoss |   0.9894 | -3.6828 | greater       |

#### CIFAR23 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR23',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8525 | 0.7765 |  0.8555 |    0.863  |
| ('test_acc', 'std')  | 0.0037 | 0.0039 |  0.0005 |    0.0072 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9293 | 0.8631 |  0.9227 |    0.9362 |
| ('test_auc', 'std')  | 0.0022 | 0.0019 |  0.002  |    0.0061 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0479 | -2.1694 | less          |
|  6 | Hinge | ensLoss |   0.1906 | -0.9833 | less          |
|  9 | EXP   | ensLoss |   0.0004 | -9.1408 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9521 | -2.1694 | greater       |
|  6 | Hinge | ensLoss |   0.8094 | -0.9833 | greater       |
|  9 | EXP   | ensLoss |   0.9996 | -9.1408 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0924 |  -1.6005 | less          |
|  6 | Hinge | ensLoss |   0.0234 |  -2.8406 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.7227 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9076 |  -1.6005 | greater       |
|  6 | Hinge | ensLoss |   0.9766 |  -2.8406 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.7227 | greater       |

#### CIFAR24 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR24',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8792 | 0.7946 |  0.8825 |    0.9128 |
| ('test_acc', 'std')  | 0.0027 | 0.0027 |  0.0018 |    0.0063 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9486 | 0.8809 |   0.949 |    0.9704 |
| ('test_auc', 'std')  | 0.002  | 0.0035 |   0.001 |    0.0039 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0031 |  -5.2758 | less          |
|  6 | Hinge | ensLoss |   0.0049 |  -4.6266 | less          |
|  9 | EXP   | ensLoss |   0      | -26.7567 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9969 |  -5.2758 | greater       |
|  6 | Hinge | ensLoss |   0.9951 |  -4.6266 | greater       |
|  9 | EXP   | ensLoss |   1      | -26.7567 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0058 |  -4.4174 | less          |
|  6 | Hinge | ensLoss |   0.0042 |  -4.8405 | less          |
|  9 | EXP   | ensLoss |   0      | -33.3977 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9942 |  -4.4174 | greater       |
|  6 | Hinge | ensLoss |   0.9958 |  -4.8405 | greater       |
|  9 | EXP   | ensLoss |   1      | -33.3977 | greater       |

#### CIFAR24 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR24',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8789 | 0.78   |  0.8836 |    0.8582 |
| ('test_acc', 'std')  | 0.0039 | 0.0058 |  0.0033 |    0.0592 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.946  | 0.8588 |  0.9392 |    0.9127 |
| ('test_auc', 'std')  | 0.0017 | 0.0048 |  0.0029 |    0.0595 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.6286 |  0.3517 | less          |
|  6 | Hinge | ensLoss |   0.6558 |  0.4316 | less          |
|  9 | EXP   | ensLoss |   0.1388 | -1.2558 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.3714 |  0.3517 | greater       |
|  6 | Hinge | ensLoss |   0.3442 |  0.4316 | greater       |
|  9 | EXP   | ensLoss |   0.8612 | -1.2558 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.6968 |  0.5584 | less          |
|  6 | Hinge | ensLoss |   0.6628 |  0.4524 | less          |
|  9 | EXP   | ensLoss |   0.2171 | -0.8684 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.3032 |  0.5584 | greater       |
|  6 | Hinge | ensLoss |   0.3372 |  0.4524 | greater       |
|  9 | EXP   | ensLoss |   0.7829 | -0.8684 | greater       |

#### CIFAR25 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR25',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8867 | 0.8253 |  0.8907 |    0.915  |
| ('test_acc', 'std')  | 0.0041 | 0.0033 |  0.0028 |    0.0024 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9534 | 0.9071 |  0.957  |    0.9723 |
| ('test_auc', 'std')  | 0.0026 | 0.0023 |  0.0016 |    0.0014 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0034 |  -5.1315 | less          |
|  6 | Hinge | ensLoss |   0.0021 |  -5.8482 | less          |
|  9 | EXP   | ensLoss |   0      | -27.2444 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9966 |  -5.1315 | greater       |
|  6 | Hinge | ensLoss |   0.9979 |  -5.8482 | greater       |
|  9 | EXP   | ensLoss |   1      | -27.2444 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.003  |  -5.3394 | less          |
|  6 | Hinge | ensLoss |   0.0012 |  -6.8215 | less          |
|  9 | EXP   | ensLoss |   0      | -29.1318 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.997  |  -5.3394 | greater       |
|  6 | Hinge | ensLoss |   0.9988 |  -6.8215 | greater       |
|  9 | EXP   | ensLoss |   1      | -29.1318 | greater       |

#### CIFAR25 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR25',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8898 | 0.8058 |  0.8894 |    0.9128 |
| ('test_acc', 'std')  | 0.0028 | 0.0018 |  0.0022 |    0.0024 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9547 | 0.8886 |  0.9505 |    0.9701 |
| ('test_auc', 'std')  | 0.0016 | 0.0012 |  0.0017 |    0.0008 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0026 |  -5.5458 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -12.8618 | less          |
|  9 | EXP   | ensLoss |   0      | -33.2193 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9974 |  -5.5458 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -12.8618 | greater       |
|  9 | EXP   | ensLoss |   1      | -33.2193 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 | -10.0516 | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -9.1091 | less          |
|  9 | EXP   | ensLoss |   0      | -82.785  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 | -10.0516 | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -9.1091 | greater       |
|  9 | EXP   | ensLoss |   1      | -82.785  | greater       |

#### CIFAR26 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR26',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9099 | 0.8748 |  0.9117 |    0.9219 |
| ('test_acc', 'std')  | 0.0011 | 0.003  |  0.001  |    0.0051 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9717 | 0.9462 |  0.9752 |    0.9764 |
| ('test_auc', 'std')  | 0.0009 | 0.0019 |  0.0003 |    0.0036 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0249 |  -2.7787 | less          |
|  6 | Hinge | ensLoss |   0.0647 |  -1.9051 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.1726 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9751 |  -2.7787 | greater       |
|  6 | Hinge | ensLoss |   0.9353 |  -1.9051 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.1726 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0918 |  -1.6058 | less          |
|  6 | Hinge | ensLoss |   0.3835 |  -0.3171 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.7505 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9082 |  -1.6058 | greater       |
|  6 | Hinge | ensLoss |   0.6165 |  -0.3171 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.7505 | greater       |

#### CIFAR26 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR26',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9163 | 0.862  |  0.9182 |    0.9252 |
| ('test_acc', 'std')  | 0.0018 | 0.0031 |  0.0024 |    0.0034 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9743 | 0.9361 |  0.97   |    0.9784 |
| ('test_auc', 'std')  | 0.0009 | 0.0012 |  0.0006 |    0.0017 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0733 |  -1.7977 | less          |
|  6 | Hinge | ensLoss |   0.0958 |  -1.5692 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.7476 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9267 |  -1.7977 | greater       |
|  6 | Hinge | ensLoss |   0.9042 |  -1.5692 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.7476 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0691 |  -1.849  | less          |
|  6 | Hinge | ensLoss |   0.0022 |  -5.7713 | less          |
|  9 | EXP   | ensLoss |   0      | -30.3132 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9309 |  -1.849  | greater       |
|  6 | Hinge | ensLoss |   0.9978 |  -5.7713 | greater       |
|  9 | EXP   | ensLoss |   1      | -30.3132 | greater       |

#### CIFAR27 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR27',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9191 | 0.8808 |  0.9183 |    0.9325 |
| ('test_acc', 'std')  | 0.0019 | 0.0016 |  0.002  |    0.0037 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.976  | 0.9514 |  0.9755 |    0.9811 |
| ('test_auc', 'std')  | 0.0013 | 0.0008 |  0.0009 |    0.0016 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0065 |  -4.262  | less          |
|  6 | Hinge | ensLoss |   0.015  |  -3.3001 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.2001 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9935 |  -4.262  | greater       |
|  6 | Hinge | ensLoss |   0.985  |  -3.3001 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.2001 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.014  |  -3.3705 | less          |
|  6 | Hinge | ensLoss |   0.0024 |  -5.6755 | less          |
|  9 | EXP   | ensLoss |   0      | -17.3367 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.986  |  -3.3705 | greater       |
|  6 | Hinge | ensLoss |   0.9976 |  -5.6755 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.3367 | greater       |

#### CIFAR27 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR27',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9148 | 0.8627 |  0.9199 |    0.9289 |
| ('test_acc', 'std')  | 0.0009 | 0.004  |  0.0021 |    0.0052 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9716 | 0.9381 |  0.9722 |    0.9804 |
| ('test_auc', 'std')  | 0.0009 | 0.002  |  0.0011 |    0.0012 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0264 |  -2.7244 | less          |
|  6 | Hinge | ensLoss |   0.1211 |  -1.3713 | less          |
|  9 | EXP   | ensLoss |   0      | -28.1893 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9736 |  -2.7244 | greater       |
|  6 | Hinge | ensLoss |   0.8789 |  -1.3713 | greater       |
|  9 | EXP   | ensLoss |   1      | -28.1893 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0045 |  -4.7432 | less          |
|  6 | Hinge | ensLoss |   0.005  |  -4.6079 | less          |
|  9 | EXP   | ensLoss |   0      | -40.0276 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9955 |  -4.7432 | greater       |
|  6 | Hinge | ensLoss |   0.995  |  -4.6079 | greater       |
|  9 | EXP   | ensLoss |   1      | -40.0276 | greater       |

#### CIFAR28 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR28',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9611 | 0.9484 |  0.9626 |    0.9694 |
| ('test_acc', 'std')  | 0.0015 | 0.0014 |  0.0012 |    0.0018 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9929 | 0.9888 |  0.9934 |    0.9955 |
| ('test_auc', 'std')  | 0.0001 | 0.0005 |  0.0002 |    0.0005 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0059 | -4.3806 | less          |
|  6 | Hinge | ensLoss |   0.0004 | -9.0466 | less          |
|  9 | EXP   | ensLoss |   0.0011 | -7.0392 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9941 | -4.3806 | greater       |
|  6 | Hinge | ensLoss |   0.9996 | -9.0466 | greater       |
|  9 | EXP   | ensLoss |   0.9989 | -7.0392 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.004  | -4.9142 | less          |
|  6 | Hinge | ensLoss |   0.0031 | -5.2808 | less          |
|  9 | EXP   | ensLoss |   0.001  | -7.253  | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.996  | -4.9142 | greater       |
|  6 | Hinge | ensLoss |   0.9969 | -5.2808 | greater       |
|  9 | EXP   | ensLoss |   0.999  | -7.253  | greater       |

#### CIFAR28 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR28',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9615 | 0.9386 |  0.9609 |    0.9719 |
| ('test_acc', 'std')  | 0.0024 | 0.0018 |  0.0014 |    0.0008 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9926 | 0.9856 |  0.992  |    0.9955 |
| ('test_auc', 'std')  | 0.0003 | 0.001  |  0.0005 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0065 |  -4.269  | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.9999 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.692  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9935 |  -4.269  | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.9999 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.692  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0007 |  -7.9501 | less          |
|  6 | Hinge | ensLoss |   0.0022 |  -5.789  | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.4514 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9993 |  -7.9501 | greater       |
|  6 | Hinge | ensLoss |   0.9978 |  -5.789  | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.4514 | greater       |

#### CIFAR29 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR29',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9696 | 0.9512 |   0.972 |    0.9771 |
| ('test_acc', 'std')  | 0.0017 | 0.0023 |   0.001 |    0.0017 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9953 | 0.9904 |  0.9957 |    0.9974 |
| ('test_auc', 'std')  | 0.0003 | 0.0005 |  0.0002 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0388 | -2.3599 | less          |
|  6 | Hinge | ensLoss |   0.0315 | -2.5548 | less          |
|  9 | EXP   | ensLoss |   0.0007 | -7.8056 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9612 | -2.3599 | greater       |
|  6 | Hinge | ensLoss |   0.9685 | -2.5548 | greater       |
|  9 | EXP   | ensLoss |   0.9993 | -7.8056 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0102 | -3.7181 | less          |
|  6 | Hinge | ensLoss |   0.0081 | -3.9967 | less          |
|  9 | EXP   | ensLoss |   0.0004 | -9.2912 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9898 | -3.7181 | greater       |
|  6 | Hinge | ensLoss |   0.9919 | -3.9967 | greater       |
|  9 | EXP   | ensLoss |   0.9996 | -9.2912 | greater       |

#### CIFAR29 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR29',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9713 | 0.9445 |  0.9717 |    0.975  |
| ('test_acc', 'std')  | 0.0011 | 0.0024 |  0.0011 |    0.0004 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9956 | 0.9865 |  0.9957 |    0.9965 |
| ('test_auc', 'std')  | 0.0002 | 0.0008 |  0.0003 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0179 |  -3.1105 | less          |
|  6 | Hinge | ensLoss |   0.0435 |  -2.2558 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.2739 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9821 |  -3.1105 | greater       |
|  6 | Hinge | ensLoss |   0.9565 |  -2.2558 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.2739 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0225 |  -2.879  | less          |
|  6 | Hinge | ensLoss |   0.025  |  -2.7757 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.1738 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9775 |  -2.879  | greater       |
|  6 | Hinge | ensLoss |   0.975  |  -2.7757 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.1738 | greater       |

#### CIFAR34 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR34',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8794 | 0.8313 |  0.8804 |    0.9082 |
| ('test_acc', 'std')  | 0.0046 | 0.0025 |  0.0017 |    0.0049 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9475 | 0.9133 |  0.9507 |    0.9663 |
| ('test_auc', 'std')  | 0.0022 | 0.0011 |  0.001  |    0.0017 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0125 |  -3.496  | less          |
|  6 | Hinge | ensLoss |   0.0031 |  -5.2664 | less          |
|  9 | EXP   | ensLoss |   0      | -22.9936 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9875 |  -3.496  | greater       |
|  6 | Hinge | ensLoss |   0.9969 |  -5.2664 | greater       |
|  9 | EXP   | ensLoss |   1      | -22.9936 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.002  |  -5.9298 | less          |
|  6 | Hinge | ensLoss |   0.0012 |  -6.9127 | less          |
|  9 | EXP   | ensLoss |   0      | -59.7094 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.998  |  -5.9298 | greater       |
|  6 | Hinge | ensLoss |   0.9988 |  -6.9127 | greater       |
|  9 | EXP   | ensLoss |   1      | -59.7094 | greater       |

#### CIFAR34 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR34',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8751 | 0.8152 |  0.8787 |    0.8987 |
| ('test_acc', 'std')  | 0.0013 | 0.0044 |  0.0025 |    0.0084 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9492 | 0.8992 |  0.9442 |    0.9562 |
| ('test_auc', 'std')  | 0.0006 | 0.0039 |  0.0016 |    0.0054 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0234 | -2.8404 | less          |
|  6 | Hinge | ensLoss |   0.0685 | -1.8562 | less          |
|  9 | EXP   | ensLoss |   0.001  | -7.1733 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9766 | -2.8404 | greater       |
|  6 | Hinge | ensLoss |   0.9315 | -1.8562 | greater       |
|  9 | EXP   | ensLoss |   0.999  | -7.1733 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.1122 | -1.4354 | less          |
|  6 | Hinge | ensLoss |   0.067  | -1.876  | less          |
|  9 | EXP   | ensLoss |   0.001  | -7.0987 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.8878 | -1.4354 | greater       |
|  6 | Hinge | ensLoss |   0.933  | -1.876  | greater       |
|  9 | EXP   | ensLoss |   0.999  | -7.0987 | greater       |

#### CIFAR35 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR35',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7736 | 0.6927 |  0.7813 |    0.8113 |
| ('test_acc', 'std')  | 0.003  | 0.002  |  0.0039 |    0.0035 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8542 | 0.7613 |  0.862  |    0.8954 |
| ('test_auc', 'std')  | 0.0032 | 0.0042 |  0.0028 |    0.0013 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0012 |  -6.7914 | less          |
|  6 | Hinge | ensLoss |   0.0013 |  -6.6998 | less          |
|  9 | EXP   | ensLoss |   0      | -24.0172 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9988 |  -6.7914 | greater       |
|  6 | Hinge | ensLoss |   0.9987 |  -6.6998 | greater       |
|  9 | EXP   | ensLoss |   1      | -24.0172 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -11.6251 | less          |
|  6 | Hinge | ensLoss |   0      | -20.1298 | less          |
|  9 | EXP   | ensLoss |   0      | -27.5657 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -11.6251 | greater       |
|  6 | Hinge | ensLoss |   1      | -20.1298 | greater       |
|  9 | EXP   | ensLoss |   1      | -27.5657 | greater       |

#### CIFAR35 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR35',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7696 | 0.6638 |  0.7806 |    0.8057 |
| ('test_acc', 'std')  | 0.0046 | 0.0052 |  0.0031 |    0.0034 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8561 | 0.7288 |  0.8447 |    0.8755 |
| ('test_auc', 'std')  | 0.0043 | 0.005  |  0.0048 |    0.0048 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0022 |  -5.7725 | less          |
|  6 | Hinge | ensLoss |   0.0008 |  -7.5904 | less          |
|  9 | EXP   | ensLoss |   0      | -21.1803 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9978 |  -5.7725 | greater       |
|  6 | Hinge | ensLoss |   0.9992 |  -7.5904 | greater       |
|  9 | EXP   | ensLoss |   1      | -21.1803 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0295 |  -2.6164 | less          |
|  6 | Hinge | ensLoss |   0.0156 |  -3.258  | less          |
|  9 | EXP   | ensLoss |   0      | -18.7901 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9705 |  -2.6164 | greater       |
|  6 | Hinge | ensLoss |   0.9844 |  -3.258  | greater       |
|  9 | EXP   | ensLoss |   1      | -18.7901 | greater       |

#### CIFAR36 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR36',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9005 | 0.864  |  0.9052 |    0.9104 |
| ('test_acc', 'std')  | 0.0021 | 0.0031 |  0.0025 |    0.0103 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9622 | 0.9373 |  0.9656 |    0.9672 |
| ('test_auc', 'std')  | 0.0009 | 0.0025 |  0.0012 |    0.0055 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.1764 | -1.0502 | less          |
|  6 | Hinge | ensLoss |   0.3075 | -0.5445 | less          |
|  9 | EXP   | ensLoss |   0.0044 | -4.7862 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.8236 | -1.0502 | greater       |
|  6 | Hinge | ensLoss |   0.6925 | -0.5445 | greater       |
|  9 | EXP   | ensLoss |   0.9956 | -4.7862 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.1656 | -1.1048 | less          |
|  6 | Hinge | ensLoss |   0.3825 | -0.32   | less          |
|  9 | EXP   | ensLoss |   0.0042 | -4.8494 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.8344 | -1.1048 | greater       |
|  6 | Hinge | ensLoss |   0.6175 | -0.32   | greater       |
|  9 | EXP   | ensLoss |   0.9958 | -4.8494 | greater       |

#### CIFAR36 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR36',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8959 | 0.8536 |  0.9021 |    0.9108 |
| ('test_acc', 'std')  | 0.002  | 0.0043 |  0.0016 |    0.0016 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9606 | 0.9284 |  0.9574 |    0.9673 |
| ('test_auc', 'std')  | 0.0014 | 0.0026 |  0.0009 |    0.0008 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0067 |  -4.2254 | less          |
|  6 | Hinge | ensLoss |   0.0019 |  -6.0542 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.6522 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9933 |  -4.2254 | greater       |
|  6 | Hinge | ensLoss |   0.9981 |  -6.0542 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.6522 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0195 |  -3.023  | less          |
|  6 | Hinge | ensLoss |   0.0001 | -12.7581 | less          |
|  9 | EXP   | ensLoss |   0      | -17.1298 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9805 |  -3.023  | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -12.7581 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.1298 | greater       |

#### CIFAR37 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR37',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9097 | 0.8562 |  0.9117 |    0.9213 |
| ('test_acc', 'std')  | 0.0019 | 0.0031 |  0.0021 |    0.0061 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.971  | 0.9337 |  0.969  |    0.9752 |
| ('test_auc', 'std')  | 0.0004 | 0.0017 |  0.0006 |    0.0033 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0269 | -2.7054 | less          |
|  6 | Hinge | ensLoss |   0.1072 | -1.4741 | less          |
|  9 | EXP   | ensLoss |   0.0007 | -8.0111 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9731 | -2.7054 | greater       |
|  6 | Hinge | ensLoss |   0.8928 | -1.4741 | greater       |
|  9 | EXP   | ensLoss |   0.9993 | -8.0111 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.1239 | -1.3517 | less          |
|  6 | Hinge | ensLoss |   0.0882 | -1.6402 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -9.5254 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.8761 | -1.3517 | greater       |
|  6 | Hinge | ensLoss |   0.9118 | -1.6402 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -9.5254 | greater       |

#### CIFAR37 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR37',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.906  | 0.8384 |  0.9103 |    0.9264 |
| ('test_acc', 'std')  | 0.0026 | 0.002  |  0.001  |    0.0047 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9706 | 0.917  |  0.9671 |    0.9778 |
| ('test_auc', 'std')  | 0.0005 | 0.0007 |  0.0013 |    0.002  |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0095 |  -3.8023 | less          |
|  6 | Hinge | ensLoss |   0.0158 |  -3.2421 | less          |
|  9 | EXP   | ensLoss |   0      | -20.1753 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9905 |  -3.8023 | greater       |
|  6 | Hinge | ensLoss |   0.9842 |  -3.2421 | greater       |
|  9 | EXP   | ensLoss |   1      | -20.1753 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0105 |  -3.6948 | less          |
|  6 | Hinge | ensLoss |   0.009  |  -3.8696 | less          |
|  9 | EXP   | ensLoss |   0      | -24.3684 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9895 |  -3.6948 | greater       |
|  6 | Hinge | ensLoss |   0.991  |  -3.8696 | greater       |
|  9 | EXP   | ensLoss |   1      | -24.3684 | greater       |

#### CIFAR38 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR38',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9618 | 0.9511 |  0.965  |    0.9694 |
| ('test_acc', 'std')  | 0.0008 | 0.0009 |  0.0004 |    0.0009 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9924 | 0.9893 |  0.9927 |    0.9932 |
| ('test_auc', 'std')  | 0.0004 | 0.0003 |  0.0003 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0032 |  -5.232  | less          |
|  6 | Hinge | ensLoss |   0.0147 |  -3.3166 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.1387 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9968 |  -5.232  | greater       |
|  6 | Hinge | ensLoss |   0.9853 |  -3.3166 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.1387 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0188 | -3.0643 | less          |
|  6 | Hinge | ensLoss |   0.1699 | -1.0827 | less          |
|  9 | EXP   | ensLoss |   0.0012 | -6.8701 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9812 | -3.0643 | greater       |
|  6 | Hinge | ensLoss |   0.8301 | -1.0827 | greater       |
|  9 | EXP   | ensLoss |   0.9988 | -6.8701 | greater       |

#### CIFAR38 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR38',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9631 | 0.9454 |  0.963  |    0.9716 |
| ('test_acc', 'std')  | 0.0022 | 0.0024 |  0.0015 |    0.001  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9922 | 0.9866 |  0.9913 |    0.9944 |
| ('test_auc', 'std')  | 0.0004 | 0.0004 |  0.0004 |    0.0006 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0187 | -3.0682 | less          |
|  6 | Hinge | ensLoss |   0.0043 | -4.8189 | less          |
|  9 | EXP   | ensLoss |   0.0004 | -9.0588 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9813 | -3.0682 | greater       |
|  6 | Hinge | ensLoss |   0.9957 | -4.8189 | greater       |
|  9 | EXP   | ensLoss |   0.9996 | -9.0588 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0245 | -2.7975 | less          |
|  6 | Hinge | ensLoss |   0.0138 | -3.383  | less          |
|  9 | EXP   | ensLoss |   0.0007 | -7.9823 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9755 | -2.7975 | greater       |
|  6 | Hinge | ensLoss |   0.9862 | -3.383  | greater       |
|  9 | EXP   | ensLoss |   0.9993 | -7.9823 | greater       |

#### CIFAR39 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR39',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9596 | 0.9412 |  0.9604 |    0.9668 |
| ('test_acc', 'std')  | 0.0014 | 0.0016 |  0.0008 |    0.0037 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9925 | 0.9859 |  0.9932 |    0.9936 |
| ('test_auc', 'std')  | 0.0003 | 0.0008 |  0.0004 |    0.0011 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0494 |  -2.1428 | less          |
|  6 | Hinge | ensLoss |   0.0831 |  -1.6904 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -10.0142 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9506 |  -2.1428 | greater       |
|  6 | Hinge | ensLoss |   0.9169 |  -1.6904 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -10.0142 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.2147 | -0.8781 | less          |
|  6 | Hinge | ensLoss |   0.3152 | -0.5203 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -9.7153 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.7853 | -0.8781 | greater       |
|  6 | Hinge | ensLoss |   0.6848 | -0.5203 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -9.7153 | greater       |

#### CIFAR39 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR39',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9592 | 0.9324 |  0.9598 |    0.9718 |
| ('test_acc', 'std')  | 0.0012 | 0.0021 |  0.0016 |    0.0012 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9918 | 0.9822 |  0.991  |    0.9946 |
| ('test_auc', 'std')  | 0.0003 | 0.001  |  0.0006 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0019 |  -6.0517 | less          |
|  6 | Hinge | ensLoss |   0.0063 |  -4.2967 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.6472 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9981 |  -6.0517 | greater       |
|  6 | Hinge | ensLoss |   0.9937 |  -4.2967 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.6472 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0004 |  -9.1152 | less          |
|  6 | Hinge | ensLoss |   0.0048 |  -4.6507 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.5459 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9996 |  -9.1152 | greater       |
|  6 | Hinge | ensLoss |   0.9952 |  -4.6507 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.5459 | greater       |

#### CIFAR45 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR45',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9044 | 0.8568 |  0.9094 |    0.9231 |
| ('test_acc', 'std')  | 0.0014 | 0.0043 |  0.0025 |    0.0062 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9684 | 0.9315 |  0.9676 |    0.9781 |
| ('test_auc', 'std')  | 0.0006 | 0.0027 |  0.0009 |    0.0039 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0153 |  -3.2782 | less          |
|  6 | Hinge | ensLoss |   0.0292 |  -2.6261 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.5874 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9847 |  -3.2782 | greater       |
|  6 | Hinge | ensLoss |   0.9708 |  -2.6261 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.5874 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0259 |  -2.7424 | less          |
|  6 | Hinge | ensLoss |   0.0229 |  -2.8645 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.6666 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9741 |  -2.7424 | greater       |
|  6 | Hinge | ensLoss |   0.9771 |  -2.8645 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.6666 | greater       |

#### CIFAR45 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR45',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9014 | 0.8433 |  0.9096 |    0.9311 |
| ('test_acc', 'std')  | 0.0015 | 0.0012 |  0.0024 |    0.0017 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9649 | 0.9196 |  0.9629 |    0.9791 |
| ('test_auc', 'std')  | 0.0009 | 0.0011 |  0.0014 |    0.0018 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -11.2943 | less          |
|  6 | Hinge | ensLoss |   0.0018 |  -6.1304 | less          |
|  9 | EXP   | ensLoss |   0      | -37.387  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -11.2943 | greater       |
|  6 | Hinge | ensLoss |   0.9982 |  -6.1304 | greater       |
|  9 | EXP   | ensLoss |   1      | -37.387  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.002  |  -5.9297 | less          |
|  6 | Hinge | ensLoss |   0.0011 |  -7.009  | less          |
|  9 | EXP   | ensLoss |   0      | -24.0591 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.998  |  -5.9297 | greater       |
|  6 | Hinge | ensLoss |   0.9989 |  -7.009  | greater       |
|  9 | EXP   | ensLoss |   1      | -24.0591 | greater       |

#### CIFAR46 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR46',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9288 | 0.8775 |  0.9328 |    0.9518 |
| ('test_acc', 'std')  | 0.0019 | 0.004  |  0.0023 |    0.0034 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9807 | 0.9502 |  0.9815 |    0.9897 |
| ('test_auc', 'std')  | 0.001  | 0.002  |  0.0004 |    0.0007 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0004 |  -9.004  | less          |
|  6 | Hinge | ensLoss |   0.0015 |  -6.4324 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.4021 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9996 |  -9.004  | greater       |
|  6 | Hinge | ensLoss |   0.9985 |  -6.4324 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.4021 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.7186 | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -9.1011 | less          |
|  9 | EXP   | ensLoss |   0      | -21.6261 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.7186 | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -9.1011 | greater       |
|  9 | EXP   | ensLoss |   1      | -21.6261 | greater       |

#### CIFAR01 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR01',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.935  | 0.8677 |  0.9397 |    0.9585 |
| ('test_acc', 'std')  | 0.0015 | 0.0016 |  0.0023 |    0.0012 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9828 | 0.9425 |  0.9842 |    0.9922 |
| ('test_auc', 'std')  | 0.0005 | 0.0011 |  0.0009 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -16.121  | less          |
|  6 | Hinge | ensLoss |   0.0006 |  -8.1546 | less          |
|  9 | EXP   | ensLoss |   0      | -39.4781 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -16.121  | greater       |
|  6 | Hinge | ensLoss |   0.9994 |  -8.1546 | greater       |
|  9 | EXP   | ensLoss |   1      | -39.4781 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -17.1714 | less          |
|  6 | Hinge | ensLoss |   0.0006 |  -8.4146 | less          |
|  9 | EXP   | ensLoss |   0      | -43.2226 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -17.1714 | greater       |
|  6 | Hinge | ensLoss |   0.9994 |  -8.4146 | greater       |
|  9 | EXP   | ensLoss |   1      | -43.2226 | greater       |

#### CIFAR46 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR46',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9286 | 0.8587 |  0.934  |    0.9451 |
| ('test_acc', 'std')  | 0.0016 | 0.0039 |  0.0029 |    0.0017 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9795 | 0.9353 |  0.9766 |    0.9866 |
| ('test_auc', 'std')  | 0.001  | 0.0012 |  0.0008 |    0.0007 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0022 |  -5.8064 | less          |
|  6 | Hinge | ensLoss |   0.0132 |  -3.4362 | less          |
|  9 | EXP   | ensLoss |   0      | -19.6618 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9978 |  -5.8064 | greater       |
|  6 | Hinge | ensLoss |   0.9868 |  -3.4362 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.6618 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.001  |  -7.2631 | less          |
|  6 | Hinge | ensLoss |   0.0008 |  -7.7548 | less          |
|  9 | EXP   | ensLoss |   0      | -39.5861 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.999  |  -7.2631 | greater       |
|  6 | Hinge | ensLoss |   0.9992 |  -7.7548 | greater       |
|  9 | EXP   | ensLoss |   1      | -39.5861 | greater       |

#### CIFAR01 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR01',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9267 | 0.8678 |  0.9267 |    0.9605 |
| ('test_acc', 'std')  | 0.0015 | 0.0023 |  0.0017 |    0.0027 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9784 | 0.9436 |  0.9774 |    0.9929 |
| ('test_auc', 'std')  | 0.0008 | 0.0015 |  0.0003 |    0.0007 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.8441 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -12.5617 | less          |
|  9 | EXP   | ensLoss |   0      | -21.3854 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.8441 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -12.5617 | greater       |
|  9 | EXP   | ensLoss |   1      | -21.3854 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -17.0905 | less          |
|  6 | Hinge | ensLoss |        0 | -23.5767 | less          |
|  9 | EXP   | ensLoss |        0 | -23.257  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -17.0905 | greater       |
|  6 | Hinge | ensLoss |        1 | -23.5767 | greater       |
|  9 | EXP   | ensLoss |        1 | -23.257  | greater       |

#### CIFAR47 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR47',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9002 | 0.8544 |  0.9105 |    0.9247 |
| ('test_acc', 'std')  | 0.0016 | 0.0022 |  0.0015 |    0.0081 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9678 | 0.9298 |  0.9715 |    0.9786 |
| ('test_auc', 'std')  | 0.0016 | 0.0018 |  0.0002 |    0.0035 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0143 |  -3.3457 | less          |
|  6 | Hinge | ensLoss |   0.0562 |  -2.0288 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -11.3276 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9857 |  -3.3457 | greater       |
|  6 | Hinge | ensLoss |   0.9438 |  -2.0288 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -11.3276 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0277 |  -2.6776 | less          |
|  6 | Hinge | ensLoss |   0.0514 |  -2.107  | less          |
|  9 | EXP   | ensLoss |   0      | -23.3765 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9723 |  -2.6776 | greater       |
|  6 | Hinge | ensLoss |   0.9486 |  -2.107  | greater       |
|  9 | EXP   | ensLoss |   1      | -23.3765 | greater       |

#### CIFAR47 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR47',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9048 | 0.829  |  0.9077 |    0.9259 |
| ('test_acc', 'std')  | 0.0033 | 0.0023 |  0.0027 |    0.0021 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9686 | 0.9113 |  0.9623 |    0.9774 |
| ('test_auc', 'std')  | 0.0013 | 0.002  |  0.0033 |    0.0025 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0042 |  -4.8426 | less          |
|  6 | Hinge | ensLoss |   0.0037 |  -5.0304 | less          |
|  9 | EXP   | ensLoss |   0      | -38.4991 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9958 |  -4.8426 | greater       |
|  6 | Hinge | ensLoss |   0.9963 |  -5.0304 | greater       |
|  9 | EXP   | ensLoss |   1      | -38.4991 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0038 |  -4.9663 | less          |
|  6 | Hinge | ensLoss |   0.0026 |  -5.5527 | less          |
|  9 | EXP   | ensLoss |   0      | -20.4459 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9962 |  -4.9663 | greater       |
|  6 | Hinge | ensLoss |   0.9974 |  -5.5527 | greater       |
|  9 | EXP   | ensLoss |   1      | -20.4459 | greater       |

#### CIFAR48 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR48',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.973  | 0.9618 |  0.9726 |    0.978  |
| ('test_acc', 'std')  | 0.0012 | 0.0008 |  0.0004 |    0.0008 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9963 | 0.9927 |  0.9957 |    0.9975 |
| ('test_auc', 'std')  | 0.0002 | 0.0005 |  0.0003 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0061 |  -4.3437 | less          |
|  6 | Hinge | ensLoss |   0.0033 |  -5.1842 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.8659 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9939 |  -4.3437 | greater       |
|  6 | Hinge | ensLoss |   0.9967 |  -5.1842 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.8659 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.028  | -2.6652 | less          |
|  6 | Hinge | ensLoss |   0.0139 | -3.3769 | less          |
|  9 | EXP   | ensLoss |   0.0006 | -8.3822 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.972  | -2.6652 | greater       |
|  6 | Hinge | ensLoss |   0.9861 | -3.3769 | greater       |
|  9 | EXP   | ensLoss |   0.9994 | -8.3822 | greater       |

#### CIFAR01 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR01',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9205 | 0.7168 |  0.9198 |    0.9458 |
| ('test_acc', 'std')  | 0.0021 | 0.0112 |  0.0032 |    0.0043 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9757 | 0.7939 |  0.9702 |    0.9853 |
| ('test_auc', 'std')  | 0.0014 | 0.0125 |  0.0028 |    0.0021 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0034 |  -5.152  | less          |
|  6 | Hinge | ensLoss |   0.0023 |  -5.7389 | less          |
|  9 | EXP   | ensLoss |   0      | -19.7586 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9966 |  -5.152  | greater       |
|  6 | Hinge | ensLoss |   0.9977 |  -5.7389 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.7586 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.018  |  -3.1054 | less          |
|  6 | Hinge | ensLoss |   0.0019 |  -6.0045 | less          |
|  9 | EXP   | ensLoss |   0      | -16.438  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.982  |  -3.1054 | greater       |
|  6 | Hinge | ensLoss |   0.9981 |  -6.0045 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.438  | greater       |

#### CIFAR48 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR48',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9705 | 0.9546 |  0.9735 |    0.9775 |
| ('test_acc', 'std')  | 0.0016 | 0.0015 |  0.0007 |    0.0011 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9959 | 0.9905 |  0.9961 |    0.9976 |
| ('test_auc', 'std')  | 0.0002 | 0.0007 |  0.0002 |    0.0001 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0141 |  -3.3659 | less          |
|  6 | Hinge | ensLoss |   0.017  |  -3.1623 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.6367 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9859 |  -3.3659 | greater       |
|  6 | Hinge | ensLoss |   0.983  |  -3.1623 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.6367 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0012 |  -6.7545 | less          |
|  6 | Hinge | ensLoss |   0.0018 |  -6.1395 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.3667 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9988 |  -6.7545 | greater       |
|  6 | Hinge | ensLoss |   0.9982 |  -6.1395 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.3667 | greater       |

#### CIFAR02 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR02',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8834 | 0.8321 |  0.883  |    0.9002 |
| ('test_acc', 'std')  | 0.0016 | 0.0034 |  0.0008 |    0.0029 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9513 | 0.9099 |  0.946  |    0.9622 |
| ('test_auc', 'std')  | 0.0008 | 0.0017 |  0.0016 |    0.0024 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0045 |  -4.7536 | less          |
|  6 | Hinge | ensLoss |   0.0017 |  -6.1924 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.1221 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9955 |  -4.7536 | greater       |
|  6 | Hinge | ensLoss |   0.9983 |  -6.1924 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.1221 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0095 |  -3.8027 | less          |
|  6 | Hinge | ensLoss |   0.0026 |  -5.5264 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.6941 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9905 |  -3.8027 | greater       |
|  6 | Hinge | ensLoss |   0.9974 |  -5.5264 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.6941 | greater       |

#### CIFAR49 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR49',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.976  | 0.9635 |  0.976  |    0.982  |
| ('test_acc', 'std')  | 0.0014 | 0.0024 |  0.0005 |    0.0012 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9971 | 0.9928 |  0.9972 |    0.9983 |
| ('test_auc', 'std')  | 0.0001 | 0.0004 |  0.0001 |    0.0001 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0141 | -3.3673 | less          |
|  6 | Hinge | ensLoss |   0.0085 | -3.935  | less          |
|  9 | EXP   | ensLoss |   0.0019 | -6.0664 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9859 | -3.3673 | greater       |
|  6 | Hinge | ensLoss |   0.9915 | -3.935  | greater       |
|  9 | EXP   | ensLoss |   0.9981 | -6.0664 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0041 |  -4.8814 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -12.064  | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.4848 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9959 |  -4.8814 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -12.064  | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.4848 | greater       |

#### CIFAR02 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR02',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8758 | 0.8439 |  0.8741 |    0.8975 |
| ('test_acc', 'std')  | 0.0024 | 0.0028 |  0.0043 |    0.0021 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.947  | 0.9206 |  0.9408 |    0.9617 |
| ('test_auc', 'std')  | 0.0008 | 0.0026 |  0.0014 |    0.0013 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |    0.003 |  -5.3236 | less          |
|  6 | Hinge | ensLoss |    0.001 |  -7.2613 | less          |
|  9 | EXP   | ensLoss |    0     | -21.1296 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |    0.997 |  -5.3236 | greater       |
|  6 | Hinge | ensLoss |    0.999 |  -7.2613 | greater       |
|  9 | EXP   | ensLoss |    1     | -21.1296 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0006 |  -8.1571 | less          |
|  6 | Hinge | ensLoss |   0      | -20.4436 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.0955 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9994 |  -8.1571 | greater       |
|  6 | Hinge | ensLoss |   1      | -20.4436 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.0955 | greater       |

#### CIFAR49 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR49',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9761 | 0.9535 |  0.9772 |    0.9838 |
| ('test_acc', 'std')  | 0.0008 | 0.0014 |  0.001  |    0.0009 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.997  | 0.9908 |  0.9968 |    0.9982 |
| ('test_auc', 'std')  | 0.0003 | 0.0005 |  0.0002 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0006 |  -8.0497 | less          |
|  6 | Hinge | ensLoss |   0.008  |  -4.0092 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.9368 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9994 |  -8.0497 | greater       |
|  6 | Hinge | ensLoss |   0.992  |  -4.0092 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.9368 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0007 |  -7.8192 | less          |
|  6 | Hinge | ensLoss |   0.0062 |  -4.3278 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.4081 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9993 |  -7.8192 | greater       |
|  6 | Hinge | ensLoss |   0.9938 |  -4.3278 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.4081 | greater       |

#### CIFAR56 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR56',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9349 | 0.909  |  0.9395 |    0.9462 |
| ('test_acc', 'std')  | 0.0024 | 0.0016 |  0.0024 |    0.0033 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.984  | 0.9718 |  0.9862 |    0.9893 |
| ('test_auc', 'std')  | 0.0008 | 0.0007 |  0.0004 |    0.001  |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.026  | -2.7394 | less          |
|  6 | Hinge | ensLoss |   0.118  | -1.3928 | less          |
|  9 | EXP   | ensLoss |   0.0005 | -8.8135 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.974  | -2.7394 | greater       |
|  6 | Hinge | ensLoss |   0.882  | -1.3928 | greater       |
|  9 | EXP   | ensLoss |   0.9995 | -8.8135 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0076 |  -4.0666 | less          |
|  6 | Hinge | ensLoss |   0.032  |  -2.5392 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.1937 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9924 |  -4.0666 | greater       |
|  6 | Hinge | ensLoss |   0.968  |  -2.5392 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.1937 | greater       |

#### CIFAR56 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR56',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9409 | 0.9    |  0.9384 |    0.9404 |
| ('test_acc', 'std')  | 0.0007 | 0.0013 |  0.0019 |    0.0021 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9847 | 0.9643 |  0.9822 |    0.9833 |
| ('test_auc', 'std')  | 0.0002 | 0.0015 |  0.001  |    0.0037 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.5689 |   0.185  | less          |
|  6 | Hinge | ensLoss |   0.2092 |  -0.9012 | less          |
|  9 | EXP   | ensLoss |   0      | -26.2981 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.4311 |   0.185  | greater       |
|  6 | Hinge | ensLoss |   0.7908 |  -0.9012 | greater       |
|  9 | EXP   | ensLoss |   1      | -26.2981 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.6253 |  0.3422 | less          |
|  6 | Hinge | ensLoss |   0.3622 | -0.3785 | less          |
|  9 | EXP   | ensLoss |   0.0065 | -4.2624 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.3747 |  0.3422 | greater       |
|  6 | Hinge | ensLoss |   0.6378 | -0.3785 | greater       |
|  9 | EXP   | ensLoss |   0.9935 | -4.2624 | greater       |

#### CIFAR02 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR02',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8724 | 0.7398 |  0.8778 |    0.8879 |
| ('test_acc', 'std')  | 0.0017 | 0.0079 |  0.0012 |    0.0032 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9452 | 0.8123 |  0.9346 |    0.9562 |
| ('test_auc', 'std')  | 0.0016 | 0.0085 |  0.0014 |    0.0028 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0017 |  -6.225  | less          |
|  6 | Hinge | ensLoss |   0.0093 |  -3.8353 | less          |
|  9 | EXP   | ensLoss |   0      | -16.1031 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9983 |  -6.225  | greater       |
|  6 | Hinge | ensLoss |   0.9907 |  -3.8353 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.1031 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.013  |  -3.4483 | less          |
|  6 | Hinge | ensLoss |   0.0012 |  -6.8244 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.7315 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.987  |  -3.4483 | greater       |
|  6 | Hinge | ensLoss |   0.9988 |  -6.8244 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.7315 | greater       |

#### CIFAR57 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR57',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8934 | 0.8513 |  0.9015 |    0.9028 |
| ('test_acc', 'std')  | 0.0024 | 0.0036 |  0.0012 |    0.009  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9619 | 0.9248 |  0.9634 |    0.9618 |
| ('test_auc', 'std')  | 0.0016 | 0.0019 |  0.0007 |    0.0049 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.224  | -0.8406 | less          |
|  6 | Hinge | ensLoss |   0.4468 | -0.1424 | less          |
|  9 | EXP   | ensLoss |   0.0029 | -5.3802 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.776  | -0.8406 | greater       |
|  6 | Hinge | ensLoss |   0.5532 | -0.1424 | greater       |
|  9 | EXP   | ensLoss |   0.9971 | -5.3802 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.5079 |  0.0211 | less          |
|  6 | Hinge | ensLoss |   0.6246 |  0.3402 | less          |
|  9 | EXP   | ensLoss |   0.001  | -7.1402 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.4921 |  0.0211 | greater       |
|  6 | Hinge | ensLoss |   0.3754 |  0.3402 | greater       |
|  9 | EXP   | ensLoss |   0.999  | -7.1402 | greater       |

#### CIFAR03 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR03',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9247 | 0.8911 |  0.927  |    0.939  |
| ('test_acc', 'std')  | 0.0018 | 0.002  |  0.0023 |    0.0014 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9765 | 0.956  |  0.9772 |    0.9842 |
| ('test_auc', 'std')  | 0.0007 | 0.0013 |  0.0011 |    0.0008 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -11.0823 | less          |
|  6 | Hinge | ensLoss |   0.0054 |  -4.5115 | less          |
|  9 | EXP   | ensLoss |   0      | -24.1472 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -11.0823 | greater       |
|  6 | Hinge | ensLoss |   0.9946 |  -4.5115 | greater       |
|  9 | EXP   | ensLoss |   1      | -24.1472 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0006 |  -8.0577 | less          |
|  6 | Hinge | ensLoss |   0.0086 |  -3.9301 | less          |
|  9 | EXP   | ensLoss |   0      | -34.8785 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9994 |  -8.0577 | greater       |
|  6 | Hinge | ensLoss |   0.9914 |  -3.9301 | greater       |
|  9 | EXP   | ensLoss |   1      | -34.8785 | greater       |

#### CIFAR57 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR57',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8949 | 0.8291 |  0.8979 |    0.9188 |
| ('test_acc', 'std')  | 0.0035 | 0.0032 |  0.001  |    0.004  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.961  | 0.9082 |  0.9565 |    0.9689 |
| ('test_auc', 'std')  | 0.0016 | 0.0017 |  0.0013 |    0.0029 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0102 |  -3.7287 | less          |
|  6 | Hinge | ensLoss |   0.0029 |  -5.3502 | less          |
|  9 | EXP   | ensLoss |   0      | -18.9042 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9898 |  -3.7287 | greater       |
|  6 | Hinge | ensLoss |   0.9971 |  -5.3502 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.9042 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0653 |  -1.8979 | less          |
|  6 | Hinge | ensLoss |   0.0088 |  -3.9024 | less          |
|  9 | EXP   | ensLoss |   0      | -21.2105 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9347 |  -1.8979 | greater       |
|  6 | Hinge | ensLoss |   0.9912 |  -3.9024 | greater       |
|  9 | EXP   | ensLoss |   1      | -21.2105 | greater       |

#### CIFAR03 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR03',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9204 | 0.8855 |  0.9195 |    0.9316 |
| ('test_acc', 'std')  | 0.0014 | 0.0013 |  0.0006 |    0.0017 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9757 | 0.9559 |  0.9749 |    0.9808 |
| ('test_auc', 'std')  | 0.0009 | 0.0018 |  0.0006 |    0.0012 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0013 |  -6.6754 | less          |
|  6 | Hinge | ensLoss |   0.0007 |  -7.8764 | less          |
|  9 | EXP   | ensLoss |   0      | -16.0646 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9987 |  -6.6754 | greater       |
|  6 | Hinge | ensLoss |   0.9993 |  -7.8764 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.0646 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0161 | -3.2203 | less          |
|  6 | Hinge | ensLoss |   0.003  | -5.3392 | less          |
|  9 | EXP   | ensLoss |   0.0005 | -8.8198 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9839 | -3.2203 | greater       |
|  6 | Hinge | ensLoss |   0.997  | -5.3392 | greater       |
|  9 | EXP   | ensLoss |   0.9995 | -8.8198 | greater       |

#### CIFAR58 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR58',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9735 | 0.9658 |  0.9731 |    0.9805 |
| ('test_acc', 'std')  | 0.0006 | 0.0014 |  0.0014 |    0.0011 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9965 | 0.9948 |  0.9961 |    0.998  |
| ('test_auc', 'std')  | 0.0002 | 0.0002 |  0.0003 |    0.0001 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0009 |  -7.3786 | less          |
|  6 | Hinge | ensLoss |   0.0125 |  -3.4942 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -10.0486 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9991 |  -7.3786 | greater       |
|  6 | Hinge | ensLoss |   0.9875 |  -3.4942 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -10.0486 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0024 |  -5.6883 | less          |
|  6 | Hinge | ensLoss |   0.0026 |  -5.5456 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.4672 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9976 |  -5.6883 | greater       |
|  6 | Hinge | ensLoss |   0.9974 |  -5.5456 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.4672 | greater       |

#### CIFAR58 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR58',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9726 | 0.9621 |  0.9737 |    0.9786 |
| ('test_acc', 'std')  | 0.0018 | 0.0021 |  0.0009 |    0.001  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.996  | 0.9934 |  0.996  |    0.998  |
| ('test_auc', 'std')  | 0.0003 | 0.0004 |  0.0004 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0277 |  -2.6766 | less          |
|  6 | Hinge | ensLoss |   0.0292 |  -2.6248 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.5859 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9723 |  -2.6766 | greater       |
|  6 | Hinge | ensLoss |   0.9708 |  -2.6248 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.5859 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0005 |  -8.4277 | less          |
|  6 | Hinge | ensLoss |   0.0018 |  -6.1473 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.0165 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9995 |  -8.4277 | greater       |
|  6 | Hinge | ensLoss |   0.9982 |  -6.1473 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.0165 | greater       |

#### CIFAR59 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR59',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9712 | 0.9594 |  0.9721 |    0.9807 |
| ('test_acc', 'std')  | 0.001  | 0.0017 |  0.0008 |    0.0012 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9962 | 0.9931 |  0.9965 |    0.9974 |
| ('test_auc', 'std')  | 0.0002 | 0.0002 |  0.0002 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0052 | -4.5418 | less          |
|  6 | Hinge | ensLoss |   0.001  | -7.1791 | less          |
|  9 | EXP   | ensLoss |   0.0007 | -7.757  | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9948 | -4.5418 | greater       |
|  6 | Hinge | ensLoss |   0.999  | -7.1791 | greater       |
|  9 | EXP   | ensLoss |   0.9993 | -7.757  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0059 |  -4.394  | less          |
|  6 | Hinge | ensLoss |   0.0178 |  -3.1173 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.3289 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9941 |  -4.394  | greater       |
|  6 | Hinge | ensLoss |   0.9822 |  -3.1173 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.3289 | greater       |

#### CIFAR03 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR03',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9193 | 0.7511 |  0.9135 |    0.9382 |
| ('test_acc', 'std')  | 0.0026 | 0.016  |  0.002  |    0.0022 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9738 | 0.8359 |  0.9672 |    0.9804 |
| ('test_auc', 'std')  | 0.0009 | 0.0144 |  0.0006 |    0.0014 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0058 |  -4.4079 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -11.8907 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.4176 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9942 |  -4.4079 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -11.8907 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.4176 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0107 | -3.6742 | less          |
|  6 | Hinge | ensLoss |   0.0007 | -7.9458 | less          |
|  9 | EXP   | ensLoss |   0.0004 | -9.4456 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9893 | -3.6742 | greater       |
|  6 | Hinge | ensLoss |   0.9993 | -7.9458 | greater       |
|  9 | EXP   | ensLoss |   0.9996 | -9.4456 | greater       |

#### CIFAR59 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR59',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9688 | 0.9554 |  0.9685 |    0.9805 |
| ('test_acc', 'std')  | 0.0016 | 0.0011 |  0.0013 |    0.0008 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9957 | 0.9913 |  0.9958 |    0.9968 |
| ('test_auc', 'std')  | 0.0003 | 0.0003 |  0.0002 |    0.0001 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0015 |  -6.426  | less          |
|  6 | Hinge | ensLoss |   0      | -21.0497 | less          |
|  9 | EXP   | ensLoss |   0      | -15.9224 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9985 |  -6.426  | greater       |
|  6 | Hinge | ensLoss |   1      | -21.0497 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.9224 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0074 |  -4.1016 | less          |
|  6 | Hinge | ensLoss |   0.0048 |  -4.6704 | less          |
|  9 | EXP   | ensLoss |   0      | -18.9763 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9926 |  -4.1016 | greater       |
|  6 | Hinge | ensLoss |   0.9952 |  -4.6704 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.9763 | greater       |

#### CIFAR04 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR04',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9253 | 0.8753 |  0.9254 |    0.9418 |
| ('test_acc', 'std')  | 0.002  | 0.0019 |  0.0026 |    0.0015 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9767 | 0.9433 |  0.977  |    0.9872 |
| ('test_auc', 'std')  | 0.0007 | 0.0023 |  0.0007 |    0.0007 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -12.2138 | less          |
|  6 | Hinge | ensLoss |   0.0045 |  -4.7521 | less          |
|  9 | EXP   | ensLoss |   0      | -96.4877 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -12.2138 | greater       |
|  6 | Hinge | ensLoss |   0.9955 |  -4.7521 | greater       |
|  9 | EXP   | ensLoss |   1      | -96.4877 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -17.1095 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -12.0244 | less          |
|  9 | EXP   | ensLoss |   0      | -21.7098 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -17.1095 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -12.0244 | greater       |
|  9 | EXP   | ensLoss |   1      | -21.7098 | greater       |

#### CIFAR67 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR67',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9681 | 0.9504 |  0.9656 |    0.9728 |
| ('test_acc', 'std')  | 0.0017 | 0.0023 |  0.0021 |    0.0011 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9951 | 0.9893 |  0.9954 |    0.9962 |
| ('test_auc', 'std')  | 0.0002 | 0.0004 |  0.0004 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0432 | -2.2626 | less          |
|  6 | Hinge | ensLoss |   0.0014 | -6.532  | less          |
|  9 | EXP   | ensLoss |   0.001  | -7.1426 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9568 | -2.2626 | greater       |
|  6 | Hinge | ensLoss |   0.9986 | -6.532  | greater       |
|  9 | EXP   | ensLoss |   0.999  | -7.1426 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0012 |  -6.8284 | less          |
|  6 | Hinge | ensLoss |   0.103  |  -1.508  | less          |
|  9 | EXP   | ensLoss |   0      | -19.0943 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9988 |  -6.8284 | greater       |
|  6 | Hinge | ensLoss |   0.897  |  -1.508  | greater       |
|  9 | EXP   | ensLoss |   1      | -19.0943 | greater       |

#### CIFAR04 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR04',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9143 | 0.8919 |  0.918  |    0.9395 |
| ('test_acc', 'std')  | 0.0017 | 0.0011 |  0.0036 |    0.0033 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9712 | 0.9527 |  0.9698 |    0.9853 |
| ('test_auc', 'std')  | 0.0012 | 0.0017 |  0.002  |    0.0009 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.003  |  -5.3079 | less          |
|  6 | Hinge | ensLoss |   0.0039 |  -4.9422 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.1227 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.997  |  -5.3079 | greater       |
|  6 | Hinge | ensLoss |   0.9961 |  -4.9422 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.1227 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0009 |  -7.3648 | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -9.2833 | less          |
|  9 | EXP   | ensLoss |   0      | -26.3031 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9991 |  -7.3648 | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -9.2833 | greater       |
|  9 | EXP   | ensLoss |   1      | -26.3031 | greater       |

#### CIFAR67 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR67',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9652 | 0.9324 |  0.9695 |    0.9698 |
| ('test_acc', 'std')  | 0.0006 | 0.0019 |  0.0017 |    0.0016 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9946 | 0.9833 |  0.9957 |    0.9963 |
| ('test_auc', 'std')  | 0.0002 | 0.0007 |  0.0003 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0396 |  -2.3413 | less          |
|  6 | Hinge | ensLoss |   0.4303 |  -0.1873 | less          |
|  9 | EXP   | ensLoss |   0      | -32.0702 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9604 |  -2.3413 | greater       |
|  6 | Hinge | ensLoss |   0.5697 |  -0.1873 | greater       |
|  9 | EXP   | ensLoss |   1      | -32.0702 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0011 |  -7.0642 | less          |
|  6 | Hinge | ensLoss |   0.0656 |  -1.8942 | less          |
|  9 | EXP   | ensLoss |   0      | -15.6787 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9989 |  -7.0642 | greater       |
|  6 | Hinge | ensLoss |   0.9344 |  -1.8942 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.6787 | greater       |

#### CIFAR68 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR68',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.979  | 0.9755 |  0.9805 |    0.983  |
| ('test_acc', 'std')  | 0.0017 | 0.0013 |  0.0006 |    0.0004 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9978 | 0.9973 |  0.9978 |    0.9977 |
| ('test_auc', 'std')  | 0.0001 | 0.0002 |  0.0001 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0258 | -2.744  | less          |
|  6 | Hinge | ensLoss |   0.0234 | -2.8398 | less          |
|  9 | EXP   | ensLoss |   0.0041 | -4.8667 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9742 | -2.744  | greater       |
|  6 | Hinge | ensLoss |   0.9766 | -2.8398 | greater       |
|  9 | EXP   | ensLoss |   0.9959 | -4.8667 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.6438 |  0.3958 | less          |
|  6 | Hinge | ensLoss |   0.6235 |  0.337  | less          |
|  9 | EXP   | ensLoss |   0.0476 | -2.1754 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.3562 |  0.3958 | greater       |
|  6 | Hinge | ensLoss |   0.3765 |  0.337  | greater       |
|  9 | EXP   | ensLoss |   0.9524 | -2.1754 | greater       |

#### CIFAR04 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR04',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9138 | 0.8471 |  0.9089 |    0.936  |
| ('test_acc', 'std')  | 0.0021 | 0.0031 |  0.0021 |    0.0016 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9708 | 0.9171 |  0.9544 |    0.983  |
| ('test_auc', 'std')  | 0.0004 | 0.0018 |  0.0019 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0016 |  -6.3781 | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -9.2491 | less          |
|  9 | EXP   | ensLoss |   0      | -28.6402 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9984 |  -6.3781 | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -9.2491 | greater       |
|  9 | EXP   | ensLoss |   1      | -28.6402 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -23.0012 | less          |
|  6 | Hinge | ensLoss |        0 | -17.7008 | less          |
|  9 | EXP   | ensLoss |        0 | -34.9196 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -23.0012 | greater       |
|  6 | Hinge | ensLoss |        1 | -17.7008 | greater       |
|  9 | EXP   | ensLoss |        1 | -34.9196 | greater       |

#### CIFAR68 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR68',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9779 | 0.9712 |  0.9804 |    0.9826 |
| ('test_acc', 'std')  | 0.0008 | 0.0012 |  0.0008 |    0.0012 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9976 | 0.9961 |  0.9979 |    0.9974 |
| ('test_auc', 'std')  | 0.0001 | 0.0004 |  0.0001 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0112 |  -3.6154 | less          |
|  6 | Hinge | ensLoss |   0.1403 |  -1.2465 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.4754 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9888 |  -3.6154 | greater       |
|  6 | Hinge | ensLoss |   0.8597 |  -1.2465 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.4754 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.7607 |  0.7807 | less          |
|  6 | Hinge | ensLoss |   0.8135 |  1.002  | less          |
|  9 | EXP   | ensLoss |   0.0274 | -2.689  | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.2393 |  0.7807 | greater       |
|  6 | Hinge | ensLoss |   0.1865 |  1.002  | greater       |
|  9 | EXP   | ensLoss |   0.9726 | -2.689  | greater       |

#### CIFAR69 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR69',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9818 | 0.9732 |  0.9828 |    0.9854 |
| ('test_acc', 'std')  | 0.0011 | 0.0015 |  0.0013 |    0.0013 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9986 | 0.9961 |  0.9987 |    0.9989 |
| ('test_auc', 'std')  | 0.0001 | 0.0003 |  0.0002 |    0.0001 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0937 |  -1.5887 | less          |
|  6 | Hinge | ensLoss |   0.1255 |  -1.3408 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.726  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9063 |  -1.5887 | greater       |
|  6 | Hinge | ensLoss |   0.8745 |  -1.3408 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.726  | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.048  | -2.1674 | less          |
|  6 | Hinge | ensLoss |   0.131  | -1.3047 | less          |
|  9 | EXP   | ensLoss |   0.0006 | -8.133  | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.952  | -2.1674 | greater       |
|  6 | Hinge | ensLoss |   0.869  | -1.3047 | greater       |
|  9 | EXP   | ensLoss |   0.9994 | -8.133  | greater       |

#### CIFAR05 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR05',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |   EXP |   Hinge |   ensLoss |
|:---------------------|-------:|------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9392 | 0.905 |  0.9423 |    0.9525 |
| ('test_acc', 'std')  | 0.0015 | 0.004 |  0.0011 |    0.0009 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9856 | 0.9683 |  0.9849 |    0.9892 |
| ('test_auc', 'std')  | 0.0009 | 0.0023 |  0.0005 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0006 |  -8.0718 | less          |
|  6 | Hinge | ensLoss |   0.0016 |  -6.338  | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.4082 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9994 |  -8.0718 | greater       |
|  6 | Hinge | ensLoss |   0.9984 |  -6.338  | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.4082 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0039 | -4.9459 | less          |
|  6 | Hinge | ensLoss |   0.0004 | -8.8547 | less          |
|  9 | EXP   | ensLoss |   0.0004 | -8.8475 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9961 | -4.9459 | greater       |
|  6 | Hinge | ensLoss |   0.9996 | -8.8547 | greater       |
|  9 | EXP   | ensLoss |   0.9996 | -8.8475 | greater       |

#### CIFAR69 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR69',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9821 | 0.9653 |  0.9847 |    0.9848 |
| ('test_acc', 'std')  | 0.0008 | 0.002  |  0.0014 |    0.0007 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9985 | 0.9944 |  0.9986 |    0.999  |
| ('test_auc', 'std')  | 0.0001 | 0.0007 |  0.0002 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.065  | -1.9021 | less          |
|  6 | Hinge | ensLoss |   0.4783 | -0.0579 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -9.6599 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.935  | -1.9021 | greater       |
|  6 | Hinge | ensLoss |   0.5217 | -0.0579 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -9.6599 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0211 | -2.9457 | less          |
|  6 | Hinge | ensLoss |   0.0701 | -1.8362 | less          |
|  9 | EXP   | ensLoss |   0.0012 | -6.7858 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9789 | -2.9457 | greater       |
|  6 | Hinge | ensLoss |   0.9299 | -1.8362 | greater       |
|  9 | EXP   | ensLoss |   0.9988 | -6.7858 | greater       |

#### CIFAR05 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR05',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9388 | 0.9076 |  0.937  |    0.944  |
| ('test_acc', 'std')  | 0.0014 | 0.0019 |  0.0027 |    0.0032 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9854 | 0.9681 |  0.9831 |    0.9874 |
| ('test_auc', 'std')  | 0.0004 | 0.0013 |  0.0004 |    0.0015 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.1446 |  -1.2209 | less          |
|  6 | Hinge | ensLoss |   0.0638 |  -1.9176 | less          |
|  9 | EXP   | ensLoss |   0      | -17.0459 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.8554 |  -1.2209 | greater       |
|  6 | Hinge | ensLoss |   0.9362 |  -1.9176 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.0459 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0766 |  -1.7601 | less          |
|  6 | Hinge | ensLoss |   0.0159 |  -3.2353 | less          |
|  9 | EXP   | ensLoss |   0      | -15.5728 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9234 |  -1.7601 | greater       |
|  6 | Hinge | ensLoss |   0.9841 |  -3.2353 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.5728 | greater       |

#### CIFAR78 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR78',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.979  | 0.9658 |  0.9764 |    0.9788 |
| ('test_acc', 'std')  | 0.0008 | 0.0019 |  0.001  |    0.0009 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9976 | 0.9948 |  0.9976 |    0.9975 |
| ('test_auc', 'std')  | 0.0002 | 0.0003 |  0.0002 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.557  |  0.1527 | less          |
|  6 | Hinge | ensLoss |   0.1153 | -1.413  | less          |
|  9 | EXP   | ensLoss |   0.0042 | -4.8532 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.443  |  0.1527 | greater       |
|  6 | Hinge | ensLoss |   0.8847 | -1.413  | greater       |
|  9 | EXP   | ensLoss |   0.9958 | -4.8532 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.6119 |  0.3041 | less          |
|  6 | Hinge | ensLoss |   0.615  |  0.3128 | less          |
|  9 | EXP   | ensLoss |   0.003  | -5.3393 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.3881 |  0.3041 | greater       |
|  6 | Hinge | ensLoss |   0.385  |  0.3128 | greater       |
|  9 | EXP   | ensLoss |   0.997  | -5.3393 | greater       |

#### CIFAR78 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR78',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9755 | 0.9598 |  0.9795 |    0.9812 |
| ('test_acc', 'std')  | 0.0014 | 0.0014 |  0.0004 |    0.0011 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9973 | 0.9928 |  0.9976 |    0.9978 |
| ('test_auc', 'std')  | 0.0002 | 0.0006 |  0.0002 |    0.0001 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0292 |  -2.625  | less          |
|  6 | Hinge | ensLoss |   0.0989 |  -1.5423 | less          |
|  9 | EXP   | ensLoss |   0      | -19.4544 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9708 |  -2.625  | greater       |
|  6 | Hinge | ensLoss |   0.9011 |  -1.5423 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.4544 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0398 | -2.337  | less          |
|  6 | Hinge | ensLoss |   0.125  | -1.3443 | less          |
|  9 | EXP   | ensLoss |   0.0004 | -9.1934 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9602 | -2.337  | greater       |
|  6 | Hinge | ensLoss |   0.875  | -1.3443 | greater       |
|  9 | EXP   | ensLoss |   0.9996 | -9.1934 | greater       |

#### CIFAR79 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR79',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9659 | 0.9437 |  0.9675 |    0.9777 |
| ('test_acc', 'std')  | 0.0017 | 0.002  |  0.0008 |    0.0021 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9956 | 0.9872 |  0.9955 |    0.9977 |
| ('test_auc', 'std')  | 0.0002 | 0.0007 |  0.0002 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -11.0518 | less          |
|  6 | Hinge | ensLoss |   0.0057 |  -4.4243 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.3578 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -11.0518 | greater       |
|  6 | Hinge | ensLoss |   0.9943 |  -4.4243 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.3578 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -15.3319 | less          |
|  6 | Hinge | ensLoss |   0.0017 |  -6.2625 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.3208 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -15.3319 | greater       |
|  6 | Hinge | ensLoss |   0.9983 |  -6.2625 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.3208 | greater       |

#### CIFAR05 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR05',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9319 | 0.7811 |  0.9297 |    0.946  |
| ('test_acc', 'std')  | 0.0023 | 0.0121 |  0.0024 |    0.0019 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.982  | 0.8612 |  0.978  |    0.987  |
| ('test_auc', 'std')  | 0.0011 | 0.0081 |  0.0007 |    0.0009 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0032 |  -5.2062 | less          |
|  6 | Hinge | ensLoss |   0.0017 |  -6.2211 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.9686 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9968 |  -5.2062 | greater       |
|  6 | Hinge | ensLoss |   0.9983 |  -6.2211 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.9686 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.014  |  -3.3679 | less          |
|  6 | Hinge | ensLoss |   0.001  |  -7.2385 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.4417 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.986  |  -3.3679 | greater       |
|  6 | Hinge | ensLoss |   0.999  |  -7.2385 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.4417 | greater       |

#### CIFAR79 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR79',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.968  | 0.9353 |  0.968  |    0.9819 |
| ('test_acc', 'std')  | 0.0014 | 0.0015 |  0.0013 |    0.0011 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9958 | 0.9833 |  0.9955 |    0.9981 |
| ('test_auc', 'std')  | 0.0003 | 0.0005 |  0.0002 |    0.0001 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0008 |  -7.7282 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -12.0303 | less          |
|  9 | EXP   | ensLoss |   0      | -25.711  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9992 |  -7.7282 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -12.0303 | greater       |
|  9 | EXP   | ensLoss |   1      | -25.711  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.003  |  -5.3336 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -14.5407 | less          |
|  9 | EXP   | ensLoss |   0      | -28.1058 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.997  |  -5.3336 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -14.5407 | greater       |
|  9 | EXP   | ensLoss |   1      | -28.1058 | greater       |

#### CIFAR06 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR06',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9528 | 0.9312 |  0.9543 |    0.9664 |
| ('test_acc', 'std')  | 0.0011 | 0.0021 |  0.0016 |    0.001  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9894 | 0.9797 |  0.99   |    0.9928 |
| ('test_auc', 'std')  | 0.0003 | 0.0005 |  0.0006 |    0.0009 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -12.4935 | less          |
|  6 | Hinge | ensLoss |   0.0016 |  -6.3247 | less          |
|  9 | EXP   | ensLoss |   0      | -16.6118 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -12.4935 | greater       |
|  6 | Hinge | ensLoss |   0.9984 |  -6.3247 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.6118 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0057 |  -4.4427 | less          |
|  6 | Hinge | ensLoss |   0.0272 |  -2.6965 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -10.2053 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9943 |  -4.4427 | greater       |
|  6 | Hinge | ensLoss |   0.9728 |  -2.6965 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -10.2053 | greater       |

#### CIFAR89 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR89',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9559 | 0.9178 |  0.9553 |    0.9619 |
| ('test_acc', 'std')  | 0.0016 | 0.0028 |  0.001  |    0.0013 |


|                      |   BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.991 | 0.9765 |  0.9919 |    0.9931 |
| ('test_auc', 'std')  | 0.001 | 0.0012 |  0.0004 |    0.0006 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0426 |  -2.2759 | less          |
|  6 | Hinge | ensLoss |   0.018  |  -3.1078 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.2443 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9574 |  -2.2759 | greater       |
|  6 | Hinge | ensLoss |   0.982  |  -3.1078 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.2443 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.1058 |  -1.4859 | less          |
|  6 | Hinge | ensLoss |   0.0696 |  -1.8429 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.4428 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.8942 |  -1.4859 | greater       |
|  6 | Hinge | ensLoss |   0.9304 |  -1.8429 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.4428 | greater       |

#### CIFAR06 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR06',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9442 | 0.9275 |  0.9454 |    0.9627 |
| ('test_acc', 'std')  | 0.0013 | 0.0009 |  0.0012 |    0.0007 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9858 | 0.9775 |  0.9863 |    0.9934 |
| ('test_auc', 'std')  | 0.0005 | 0.0004 |  0.0005 |    0.0007 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -12.5441 | less          |
|  6 | Hinge | ensLoss |   0      | -15.6949 | less          |
|  9 | EXP   | ensLoss |   0      | -38.4064 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -12.5441 | greater       |
|  6 | Hinge | ensLoss |   1      | -15.6949 | greater       |
|  9 | EXP   | ensLoss |   1      | -38.4064 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0005 |  -8.6958 | less          |
|  6 | Hinge | ensLoss |   0.0018 |  -6.1676 | less          |
|  9 | EXP   | ensLoss |   0      | -27.8859 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9995 |  -8.6958 | greater       |
|  6 | Hinge | ensLoss |   0.9982 |  -6.1676 | greater       |
|  9 | EXP   | ensLoss |   1      | -27.8859 | greater       |

#### CIFAR89 - model: VGG19 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR89',
 'device': device(type='cuda', index=0),
 'model': {'net': 'VGG19'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9544 | 0.9117 |  0.9542 |    0.9653 |
| ('test_acc', 'std')  | 0.0016 | 0.0022 |  0.0013 |    0.0016 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9904 | 0.9704 |  0.9891 |    0.9934 |
| ('test_auc', 'std')  | 0.0006 | 0.001  |  0.0007 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0058 |  -4.4187 | less          |
|  6 | Hinge | ensLoss |   0.0072 |  -4.1411 | less          |
|  9 | EXP   | ensLoss |   0      | -18.0074 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9942 |  -4.4187 | greater       |
|  6 | Hinge | ensLoss |   0.9928 |  -4.1411 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.0074 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0094 |  -3.8155 | less          |
|  6 | Hinge | ensLoss |   0.0052 |  -4.5459 | less          |
|  9 | EXP   | ensLoss |   0      | -29.4402 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9906 |  -3.8155 | greater       |
|  6 | Hinge | ensLoss |   0.9948 |  -4.5459 | greater       |
|  9 | EXP   | ensLoss |   1      | -29.4402 | greater       |

#### CIFAR06 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR06',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9423 | 0.8841 |  0.9425 |    0.959  |
| ('test_acc', 'std')  | 0.0021 | 0.0052 |  0.0017 |    0.0012 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9835 | 0.9525 |  0.9817 |    0.9915 |
| ('test_auc', 'std')  | 0.0006 | 0.0018 |  0.0009 |    0.0006 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.6911 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.4881 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.2385 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.6911 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.4881 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.2385 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.5392 | less          |
|  6 | Hinge | ensLoss |   0.0012 |  -6.8164 | less          |
|  9 | EXP   | ensLoss |   0      | -18.0821 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.5392 | greater       |
|  6 | Hinge | ensLoss |   0.9988 |  -6.8164 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.0821 | greater       |

#### CIFAR07 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR07',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9457 | 0.893  |  0.9503 |    0.9583 |
| ('test_acc', 'std')  | 0.0014 | 0.0029 |  0.0029 |    0.0019 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.987  | 0.957  |  0.9874 |    0.9906 |
| ('test_auc', 'std')  | 0.0007 | 0.0032 |  0.0005 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0026 |  -5.5069 | less          |
|  6 | Hinge | ensLoss |   0.0498 |  -2.1362 | less          |
|  9 | EXP   | ensLoss |   0      | -15.659  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9974 |  -5.5069 | greater       |
|  6 | Hinge | ensLoss |   0.9502 |  -2.1362 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.659  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0182 |  -3.0938 | less          |
|  6 | Hinge | ensLoss |   0.01   |  -3.7529 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -10.0208 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9818 |  -3.0938 | greater       |
|  6 | Hinge | ensLoss |   0.99   |  -3.7529 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -10.0208 | greater       |

#### CIFAR07 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR07',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.941  | 0.8972 |  0.9395 |    0.9544 |
| ('test_acc', 'std')  | 0.0019 | 0.0026 |  0.0013 |    0.0021 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9841 | 0.9589 |  0.9825 |    0.9904 |
| ('test_auc', 'std')  | 0.0006 | 0.0027 |  0.001  |    0.0008 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0073 |  -4.1187 | less          |
|  6 | Hinge | ensLoss |   0.0041 |  -4.8702 | less          |
|  9 | EXP   | ensLoss |   0      | -16.8017 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9927 |  -4.1187 | greater       |
|  6 | Hinge | ensLoss |   0.9959 |  -4.8702 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.8017 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0014 |  -6.6048 | less          |
|  6 | Hinge | ensLoss |   0.0046 |  -4.7318 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.6482 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9986 |  -6.6048 | greater       |
|  6 | Hinge | ensLoss |   0.9954 |  -4.7318 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.6482 | greater       |

#### CIFAR07 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR07',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9307 | 0.7394 |  0.9314 |    0.9504 |
| ('test_acc', 'std')  | 0.0019 | 0.0146 |  0.0012 |    0.003  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.981  | 0.8124 |  0.9755 |    0.9885 |
| ('test_auc', 'std')  | 0.0007 | 0.018  |  0.0011 |    0.0006 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0004 |  -8.9316 | less          |
|  6 | Hinge | ensLoss |   0.0028 |  -5.4453 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.2455 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9996 |  -8.9316 | greater       |
|  6 | Hinge | ensLoss |   0.9972 |  -5.4453 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.2455 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -12.289  | less          |
|  6 | Hinge | ensLoss |   0.0003 |  -9.5191 | less          |
|  9 | EXP   | ensLoss |   0.0003 |  -9.5455 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -12.289  | greater       |
|  6 | Hinge | ensLoss |   0.9997 |  -9.5191 | greater       |
|  9 | EXP   | ensLoss |   0.9997 |  -9.5455 | greater       |

#### CIFAR08 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR08',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8691 | 0.7696 |  0.873  |    0.9022 |
| ('test_acc', 'std')  | 0.0038 | 0.0024 |  0.0017 |    0.01   |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9404 | 0.8431 |  0.9423 |    0.9614 |
| ('test_auc', 'std')  | 0.0027 | 0.0019 |  0.0025 |    0.0069 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0205 |  -2.9732 | less          |
|  6 | Hinge | ensLoss |   0.0312 |  -2.5623 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.0135 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9795 |  -2.9732 | greater       |
|  6 | Hinge | ensLoss |   0.9688 |  -2.5623 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.0135 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0247 |  -2.7876 | less          |
|  6 | Hinge | ensLoss |   0.0259 |  -2.7414 | less          |
|  9 | EXP   | ensLoss |   0      | -17.7537 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9753 |  -2.7876 | greater       |
|  6 | Hinge | ensLoss |   0.9741 |  -2.7414 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.7537 | greater       |

#### CIFAR08 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR08',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8489 | 0.7353 |  0.8504 |    0.9086 |
| ('test_acc', 'std')  | 0.0038 | 0.0037 |  0.0018 |    0.0027 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9238 | 0.8097 |  0.9218 |    0.9691 |
| ('test_auc', 'std')  | 0.0021 | 0.0036 |  0.0022 |    0.0012 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -11.0546 | less          |
|  6 | Hinge | ensLoss |   0      | -18.0557 | less          |
|  9 | EXP   | ensLoss |   0      | -29.935  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -11.0546 | greater       |
|  6 | Hinge | ensLoss |   1      | -18.0557 | greater       |
|  9 | EXP   | ensLoss |   1      | -29.935  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -17.0873 | less          |
|  6 | Hinge | ensLoss |        0 | -18.2344 | less          |
|  9 | EXP   | ensLoss |        0 | -37.3412 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -17.0873 | greater       |
|  6 | Hinge | ensLoss |        1 | -18.2344 | greater       |
|  9 | EXP   | ensLoss |        1 | -37.3412 | greater       |

#### CIFAR08 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR08',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8386 | 0.5526 |  0.8384 |    0.8911 |
| ('test_acc', 'std')  | 0.0033 | 0.0089 |  0.0054 |    0.0064 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9155 | 0.5858 |  0.8899 |    0.9513 |
| ('test_auc', 'std')  | 0.0014 | 0.0093 |  0.0035 |    0.004  |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0021 |  -5.8587 | less          |
|  6 | Hinge | ensLoss |   0.0006 |  -8.2364 | less          |
|  9 | EXP   | ensLoss |   0      | -28.464  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9979 |  -5.8587 | greater       |
|  6 | Hinge | ensLoss |   0.9994 |  -8.2364 | greater       |
|  9 | EXP   | ensLoss |   1      | -28.464  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0006 |  -8.4049 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -14.8342 | less          |
|  9 | EXP   | ensLoss |   0      | -33.411  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9994 |  -8.4049 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -14.8342 | greater       |
|  9 | EXP   | ensLoss |   1      | -33.411  | greater       |

#### CIFAR09 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR09',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9039 | 0.8475 |  0.9105 |     0.936 |
| ('test_acc', 'std')  | 0.0031 | 0.0023 |  0.0023 |     0.001 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9689 | 0.9261 |  0.9684 |    0.9835 |
| ('test_auc', 'std')  | 0.0011 | 0.0012 |  0.0009 |    0.0007 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -11.4862 | less          |
|  6 | Hinge | ensLoss |   0.0003 |  -9.8332 | less          |
|  9 | EXP   | ensLoss |   0      | -55.9721 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -11.4862 | greater       |
|  6 | Hinge | ensLoss |   0.9997 |  -9.8332 | greater       |
|  9 | EXP   | ensLoss |   1      | -55.9721 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -13.456  | less          |
|  6 | Hinge | ensLoss |   0.0001 | -13.2645 | less          |
|  9 | EXP   | ensLoss |   0      | -38.5748 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -13.456  | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -13.2645 | greater       |
|  9 | EXP   | ensLoss |   1      | -38.5748 | greater       |

#### CIFAR09 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR09',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8978 | 0.8462 |  0.8996 |    0.9244 |
| ('test_acc', 'std')  | 0.0025 | 0.0031 |  0.0009 |    0.0039 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9638 | 0.9274 |  0.9622 |    0.9787 |
| ('test_auc', 'std')  | 0.0006 | 0.0022 |  0.0007 |    0.0019 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 |  -9.8049 | less          |
|  6 | Hinge | ensLoss |   0.0007 |  -7.9362 | less          |
|  9 | EXP   | ensLoss |   0      | -17.5233 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 |  -9.8049 | greater       |
|  6 | Hinge | ensLoss |   0.9993 |  -7.9362 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.5233 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0007 |  -7.8635 | less          |
|  6 | Hinge | ensLoss |   0.0008 |  -7.6315 | less          |
|  9 | EXP   | ensLoss |   0      | -18.3045 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9993 |  -7.8635 | greater       |
|  6 | Hinge | ensLoss |   0.9992 |  -7.6315 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.3045 | greater       |

#### CIFAR09 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR09',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8928 | 0.718  |  0.8918 |    0.9143 |
| ('test_acc', 'std')  | 0.0017 | 0.0113 |  0.0027 |    0.0081 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9601 | 0.7854 |  0.951  |    0.9713 |
| ('test_auc', 'std')  | 0.0011 | 0.0103 |  0.0024 |    0.0036 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0214 |  -2.9312 | less          |
|  6 | Hinge | ensLoss |   0.0205 |  -2.975  | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.7601 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9786 |  -2.9312 | greater       |
|  6 | Hinge | ensLoss |   0.9795 |  -2.975  | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.7601 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0103 |  -3.7086 | less          |
|  6 | Hinge | ensLoss |   0.0009 |  -7.3203 | less          |
|  9 | EXP   | ensLoss |   0      | -18.2532 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9897 |  -3.7086 | greater       |
|  6 | Hinge | ensLoss |   0.9991 |  -7.3203 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.2532 | greater       |

#### CIFAR12 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR12',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9519 | 0.9188 |  0.9566 |    0.9681 |
| ('test_acc', 'std')  | 0.0021 | 0.0016 |  0.0025 |    0.0015 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9916 | 0.9763 |  0.9914 |    0.9965 |
| ('test_auc', 'std')  | 0.0006 | 0.001  |  0.0006 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0006 |  -8.1615 | less          |
|  6 | Hinge | ensLoss |   0.0174 |  -3.1445 | less          |
|  9 | EXP   | ensLoss |   0      | -20.4443 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9994 |  -8.1615 | greater       |
|  6 | Hinge | ensLoss |   0.9826 |  -3.1445 | greater       |
|  9 | EXP   | ensLoss |   1      | -20.4443 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0017 |  -6.1916 | less          |
|  6 | Hinge | ensLoss |   0.0003 | -10.2492 | less          |
|  9 | EXP   | ensLoss |   0      | -22.8362 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9983 |  -6.1916 | greater       |
|  6 | Hinge | ensLoss |   0.9997 | -10.2492 | greater       |
|  9 | EXP   | ensLoss |   1      | -22.8362 | greater       |

#### CIFAR12 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR12',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9491 | 0.9266 |  0.9482 |    0.9664 |
| ('test_acc', 'std')  | 0.0006 | 0.0024 |  0.0012 |    0.0016 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9892 | 0.9804 |  0.9879 |    0.9948 |
| ('test_auc', 'std')  | 0.0006 | 0.0006 |  0.0003 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.9088 | less          |
|  6 | Hinge | ensLoss |   0.0012 |  -6.8962 | less          |
|  9 | EXP   | ensLoss |   0      | -40.5155 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.9088 | greater       |
|  6 | Hinge | ensLoss |   0.9988 |  -6.8962 | greater       |
|  9 | EXP   | ensLoss |   1      | -40.5155 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0009 |  -7.2988 | less          |
|  6 | Hinge | ensLoss |   0      | -17.6269 | less          |
|  9 | EXP   | ensLoss |   0      | -18.3876 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9991 |  -7.2988 | greater       |
|  6 | Hinge | ensLoss |   1      | -17.6269 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.3876 | greater       |

#### CIFAR12 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR12',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9436 | 0.8043 |  0.9403 |    0.9617 |
| ('test_acc', 'std')  | 0.0015 | 0.0102 |  0.0014 |    0.0017 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9869 | 0.8852 |  0.985  |    0.9943 |
| ('test_auc', 'std')  | 0.0003 | 0.0074 |  0.0007 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -19.24   | less          |
|  6 | Hinge | ensLoss |   0.0005 |  -8.7842 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.5681 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -19.24   | greater       |
|  6 | Hinge | ensLoss |   0.9995 |  -8.7842 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.5681 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -22.5137 | less          |
|  6 | Hinge | ensLoss |   0.0003 |  -9.9472 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.9914 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -22.5137 | greater       |
|  6 | Hinge | ensLoss |   0.9997 |  -9.9472 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.9914 | greater       |

#### CIFAR13 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR13',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9496 | 0.9233 |  0.9533 |    0.956  |
| ('test_acc', 'std')  | 0.0015 | 0.0026 |  0.0019 |    0.0019 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.988  | 0.9779 |  0.9878 |    0.9914 |
| ('test_auc', 'std')  | 0.0006 | 0.0011 |  0.0009 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0493 |  -2.1441 | less          |
|  6 | Hinge | ensLoss |   0.1821 |  -1.0231 | less          |
|  9 | EXP   | ensLoss |   0      | -17.567  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9507 |  -2.1441 | greater       |
|  6 | Hinge | ensLoss |   0.8179 |  -1.0231 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.567  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0062 |  -4.3353 | less          |
|  6 | Hinge | ensLoss |   0.0122 |  -3.5264 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -11.4249 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9938 |  -4.3353 | greater       |
|  6 | Hinge | ensLoss |   0.9878 |  -3.5264 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -11.4249 | greater       |

#### CIFAR13 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR13',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9512 | 0.922  |  0.9509 |    0.9583 |
| ('test_acc', 'std')  | 0.0005 | 0.0023 |  0.0011 |    0.0027 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9885 | 0.9767 |  0.9873 |    0.9917 |
| ('test_auc', 'std')  | 0.0002 | 0.0012 |  0.001  |    0.0007 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0332 | -2.5048 | less          |
|  6 | Hinge | ensLoss |   0.0186 | -3.07   | less          |
|  9 | EXP   | ensLoss |   0.0003 | -9.5444 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9668 | -2.5048 | greater       |
|  6 | Hinge | ensLoss |   0.9814 | -3.07   | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -9.5444 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0019 |  -6.0312 | less          |
|  6 | Hinge | ensLoss |   0.0174 |  -3.1416 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -10.0862 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9981 |  -6.0312 | greater       |
|  6 | Hinge | ensLoss |   0.9826 |  -3.1416 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -10.0862 | greater       |

#### CIFAR13 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR13',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.948  | 0.7801 |  0.9453 |    0.9531 |
| ('test_acc', 'std')  | 0.0019 | 0.0283 |  0.0011 |    0.0017 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9883 | 0.8614 |  0.985  |    0.9894 |
| ('test_auc', 'std')  | 0.0006 | 0.0294 |  0.0009 |    0.0011 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.003  | -5.3463 | less          |
|  6 | Hinge | ensLoss |   0.0005 | -8.6401 | less          |
|  9 | EXP   | ensLoss |   0.0015 | -6.4037 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.997  | -5.3463 | greater       |
|  6 | Hinge | ensLoss |   0.9995 | -8.6401 | greater       |
|  9 | EXP   | ensLoss |   0.9985 | -6.4037 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0926 |  -1.598  | less          |
|  6 | Hinge | ensLoss |   0.0003 | -10.1045 | less          |
|  9 | EXP   | ensLoss |   0.0054 |  -4.5118 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9074 |  -1.598  | greater       |
|  6 | Hinge | ensLoss |   0.9997 | -10.1045 | greater       |
|  9 | EXP   | ensLoss |   0.9946 |  -4.5118 | greater       |

#### CIFAR14 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR14',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9659 | 0.9366 |  0.9692 |    0.9783 |
| ('test_acc', 'std')  | 0.0021 | 0.0012 |  0.0015 |    0.0013 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.996  | 0.9849 |  0.9957 |    0.9979 |
| ('test_auc', 'std')  | 0.0005 | 0.0008 |  0.0002 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0056 |  -4.4585 | less          |
|  6 | Hinge | ensLoss |   0.0137 |  -3.3949 | less          |
|  9 | EXP   | ensLoss |   0      | -22.4831 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9944 |  -4.4585 | greater       |
|  6 | Hinge | ensLoss |   0.9863 |  -3.3949 | greater       |
|  9 | EXP   | ensLoss |   1      | -22.4831 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0156 |  -3.2544 | less          |
|  6 | Hinge | ensLoss |   0.0015 |  -6.3988 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.8856 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9844 |  -3.2544 | greater       |
|  6 | Hinge | ensLoss |   0.9985 |  -6.3988 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.8856 | greater       |

#### CIFAR14 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR14',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9609 | 0.9341 |  0.9645 |    0.9717 |
| ('test_acc', 'std')  | 0.0015 | 0.0018 |  0.0009 |    0.0026 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9941 | 0.9837 |  0.993  |    0.9969 |
| ('test_auc', 'std')  | 0.0002 | 0.0008 |  0.0002 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0246 | -2.7942 | less          |
|  6 | Hinge | ensLoss |   0.0338 | -2.4894 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -9.6889 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9754 | -2.7942 | greater       |
|  6 | Hinge | ensLoss |   0.9662 | -2.4894 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -9.6889 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0014 |  -6.5273 | less          |
|  6 | Hinge | ensLoss |   0      | -15.2044 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.2655 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9986 |  -6.5273 | greater       |
|  6 | Hinge | ensLoss |   1      | -15.2044 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.2655 | greater       |

#### CIFAR14 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR14',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9617 | 0.876  |  0.96   |    0.9764 |
| ('test_acc', 'std')  | 0.003  | 0.0015 |  0.0014 |    0.0013 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.993  | 0.94   |  0.9922 |    0.9971 |
| ('test_auc', 'std')  | 0.0008 | 0.0024 |  0.0008 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.006  |  -4.3701 | less          |
|  6 | Hinge | ensLoss |   0.0008 |  -7.5169 | less          |
|  9 | EXP   | ensLoss |   0      | -41.212  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.994  |  -4.3701 | greater       |
|  6 | Hinge | ensLoss |   0.9992 |  -7.5169 | greater       |
|  9 | EXP   | ensLoss |   1      | -41.212  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0079 |  -4.0301 | less          |
|  6 | Hinge | ensLoss |   0.001  |  -7.072  | less          |
|  9 | EXP   | ensLoss |   0      | -21.5775 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9921 |  -4.0301 | greater       |
|  6 | Hinge | ensLoss |   0.999  |  -7.072  | greater       |
|  9 | EXP   | ensLoss |   1      | -21.5775 | greater       |

#### CIFAR15 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR15',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9643 | 0.9416 |  0.9672 |    0.9711 |
| ('test_acc', 'std')  | 0.001  | 0.0028 |  0.0019 |    0.0017 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9944 | 0.9875 |  0.9954 |    0.9961 |
| ('test_auc', 'std')  | 0.0001 | 0.001  |  0.0005 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0272 | -2.6953 | less          |
|  6 | Hinge | ensLoss |   0.1413 | -1.2404 | less          |
|  9 | EXP   | ensLoss |   0.0005 | -8.6897 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9728 | -2.6953 | greater       |
|  6 | Hinge | ensLoss |   0.8587 | -1.2404 | greater       |
|  9 | EXP   | ensLoss |   0.9995 | -8.6897 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0125 | -3.4918 | less          |
|  6 | Hinge | ensLoss |   0.1491 | -1.1948 | less          |
|  9 | EXP   | ensLoss |   0.0006 | -8.1444 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9875 | -3.4918 | greater       |
|  6 | Hinge | ensLoss |   0.8509 | -1.1948 | greater       |
|  9 | EXP   | ensLoss |   0.9994 | -8.1444 | greater       |

#### CIFAR15 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR15',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9632 | 0.941  |  0.9608 |    0.9669 |
| ('test_acc', 'std')  | 0.0025 | 0.0026 |  0.001  |    0.002  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9935 | 0.9876 |  0.9931 |    0.9956 |
| ('test_auc', 'std')  | 0.0004 | 0.0007 |  0.0003 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.1721 | -1.0719 | less          |
|  6 | Hinge | ensLoss |   0.0428 | -2.2718 | less          |
|  9 | EXP   | ensLoss |   0.0009 | -7.435  | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.8279 | -1.0719 | greater       |
|  6 | Hinge | ensLoss |   0.9572 | -2.2718 | greater       |
|  9 | EXP   | ensLoss |   0.9991 | -7.435  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0078 |  -4.0478 | less          |
|  6 | Hinge | ensLoss |   0.006  |  -4.361  | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.0028 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9922 |  -4.0478 | greater       |
|  6 | Hinge | ensLoss |   0.994  |  -4.361  | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.0028 | greater       |

#### CIFAR15 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR15',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9618 | 0.7932 |  0.9598 |    0.9677 |
| ('test_acc', 'std')  | 0.001  | 0.03   |  0.0014 |    0.0018 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9927 | 0.8779 |  0.9916 |    0.9948 |
| ('test_auc', 'std')  | 0.0005 | 0.0294 |  0.0003 |    0.0008 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0465 | -2.1973 | less          |
|  6 | Hinge | ensLoss |   0.0213 | -2.937  | less          |
|  9 | EXP   | ensLoss |   0.0025 | -5.6154 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9535 | -2.1973 | greater       |
|  6 | Hinge | ensLoss |   0.9787 | -2.937  | greater       |
|  9 | EXP   | ensLoss |   0.9975 | -5.6154 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0782 | -1.7428 | less          |
|  6 | Hinge | ensLoss |   0.0123 | -3.5129 | less          |
|  9 | EXP   | ensLoss |   0.0087 | -3.9046 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9218 | -1.7428 | greater       |
|  6 | Hinge | ensLoss |   0.9877 | -3.5129 | greater       |
|  9 | EXP   | ensLoss |   0.9913 | -3.9046 | greater       |

#### CIFAR16 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR16',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9637 | 0.9403 |  0.9651 |    0.9664 |
| ('test_acc', 'std')  | 0.0014 | 0.0029 |  0.0017 |    0.0009 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9945 | 0.9855 |  0.9949 |    0.9957 |
| ('test_auc', 'std')  | 0.0002 | 0.0009 |  0.0003 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0883 |  -1.6386 | less          |
|  6 | Hinge | ensLoss |   0.2678 |  -0.6768 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -11.0688 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9117 |  -1.6386 | greater       |
|  6 | Hinge | ensLoss |   0.7322 |  -0.6768 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -11.0688 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.003  |  -5.339  | less          |
|  6 | Hinge | ensLoss |   0.0024 |  -5.6483 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -10.213  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.997  |  -5.339  | greater       |
|  6 | Hinge | ensLoss |   0.9976 |  -5.6483 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -10.213  | greater       |

#### CIFAR16 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR16',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9633 | 0.9441 |  0.9644 |    0.9691 |
| ('test_acc', 'std')  | 0.0009 | 0.0022 |  0.0018 |    0.0004 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9936 | 0.9871 |  0.993  |    0.9957 |
| ('test_auc', 'std')  | 0.0006 | 0.0008 |  0.0006 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0012 |  -6.8592 | less          |
|  6 | Hinge | ensLoss |   0.0165 |  -3.1942 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.7    | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9988 |  -6.8592 | greater       |
|  6 | Hinge | ensLoss |   0.9835 |  -3.1942 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.7    | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0345 |  -2.4681 | less          |
|  6 | Hinge | ensLoss |   0.001  |  -7.0835 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -11.6741 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9655 |  -2.4681 | greater       |
|  6 | Hinge | ensLoss |   0.999  |  -7.0835 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -11.6741 | greater       |

#### CIFAR16 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR16',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9602 | 0.8929 |  0.9599 |    0.9655 |
| ('test_acc', 'std')  | 0.0014 | 0.0027 |  0.0016 |    0.001  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9935 | 0.9626 |  0.992  |    0.9946 |
| ('test_auc', 'std')  | 0.0003 | 0.002  |  0.0009 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0112 |  -3.623  | less          |
|  6 | Hinge | ensLoss |   0.0225 |  -2.8784 | less          |
|  9 | EXP   | ensLoss |   0      | -22.7766 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9888 |  -3.623  | greater       |
|  6 | Hinge | ensLoss |   0.9775 |  -2.8784 | greater       |
|  9 | EXP   | ensLoss |   1      | -22.7766 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0777 |  -1.7482 | less          |
|  6 | Hinge | ensLoss |   0.058  |  -2.0001 | less          |
|  9 | EXP   | ensLoss |   0      | -15.7113 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9223 |  -1.7482 | greater       |
|  6 | Hinge | ensLoss |   0.942  |  -2.0001 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.7113 | greater       |

#### CIFAR17 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR17',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9644 | 0.9232 |  0.966  |    0.9793 |
| ('test_acc', 'std')  | 0.0012 | 0.0029 |  0.0015 |    0.0011 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9947 | 0.9775 |  0.9955 |    0.9982 |
| ('test_auc', 'std')  | 0.0002 | 0.0013 |  0.0004 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0007 |  -7.897  | less          |
|  6 | Hinge | ensLoss |   0.0015 |  -6.4401 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.8953 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9993 |  -7.897  | greater       |
|  6 | Hinge | ensLoss |   0.9985 |  -6.4401 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.8953 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 | -10.0424 | less          |
|  6 | Hinge | ensLoss |   0.0054 |  -4.5048 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.9413 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 | -10.0424 | greater       |
|  6 | Hinge | ensLoss |   0.9946 |  -4.5048 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.9413 | greater       |

#### CIFAR17 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR17',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9599 | 0.9182 |  0.9566 |    0.9766 |
| ('test_acc', 'std')  | 0.0014 | 0.0024 |  0.0016 |    0.0021 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9935 | 0.9748 |  0.9926 |    0.9977 |
| ('test_auc', 'std')  | 0.0002 | 0.0018 |  0.0004 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0009 |  -7.3129 | less          |
|  6 | Hinge | ensLoss |   0.001  |  -7.2193 | less          |
|  9 | EXP   | ensLoss |   0      | -15.3711 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9991 |  -7.3129 | greater       |
|  6 | Hinge | ensLoss |   0.999  |  -7.2193 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.3711 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 |  -9.5004 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.3654 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.3065 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 |  -9.5004 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.3654 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.3065 | greater       |

#### CIFAR17 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR17',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9555 | 0.7025 |  0.9546 |    0.9673 |
| ('test_acc', 'std')  | 0.0011 | 0.0181 |  0.0015 |    0.0064 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9918 | 0.7799 |  0.9897 |    0.9947 |
| ('test_auc', 'std')  | 0.0002 | 0.021  |  0.0008 |    0.0018 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0536 |  -2.0694 | less          |
|  6 | Hinge | ensLoss |   0.0739 |  -1.7913 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -11.8963 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9464 |  -2.0694 | greater       |
|  6 | Hinge | ensLoss |   0.9261 |  -1.7913 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -11.8963 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0936 | -1.5897 | less          |
|  6 | Hinge | ensLoss |   0.0282 | -2.6588 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -9.7891 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9064 | -1.5897 | greater       |
|  6 | Hinge | ensLoss |   0.9718 | -2.6588 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -9.7891 | greater       |

#### CIFAR18 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR18',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9317 | 0.8394 |  0.9346 |    0.9494 |
| ('test_acc', 'std')  | 0.003  | 0.002  |  0.0023 |    0.0006 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9809 | 0.9192 |  0.9825 |    0.9899 |
| ('test_auc', 'std')  | 0.0013 | 0.003  |  0.0008 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0016 |  -6.2716 | less          |
|  6 | Hinge | ensLoss |   0.0015 |  -6.4809 | less          |
|  9 | EXP   | ensLoss |   0      | -53.5153 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9984 |  -6.2716 | greater       |
|  6 | Hinge | ensLoss |   0.9985 |  -6.4809 | greater       |
|  9 | EXP   | ensLoss |   1      | -53.5153 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0005 |  -8.4903 | less          |
|  6 | Hinge | ensLoss |   0      | -15.2576 | less          |
|  9 | EXP   | ensLoss |   0      | -24.2347 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9995 |  -8.4903 | greater       |
|  6 | Hinge | ensLoss |   1      | -15.2576 | greater       |
|  9 | EXP   | ensLoss |   1      | -24.2347 | greater       |

#### CIFAR18 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR18',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9195 | 0.8487 |  0.9133 |    0.9462 |
| ('test_acc', 'std')  | 0.0015 | 0.0043 |  0.0023 |    0.0014 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9764 | 0.926  |  0.97   |    0.9874 |
| ('test_auc', 'std')  | 0.0016 | 0.0039 |  0.0014 |    0.0006 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -13.325  | less          |
|  6 | Hinge | ensLoss |   0      | -16.7456 | less          |
|  9 | EXP   | ensLoss |   0      | -21.967  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -13.325  | greater       |
|  6 | Hinge | ensLoss |   1      | -16.7456 | greater       |
|  9 | EXP   | ensLoss |   1      | -21.967  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -11.2152 | less          |
|  6 | Hinge | ensLoss |   0      | -16.3162 | less          |
|  9 | EXP   | ensLoss |   0      | -16.0507 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -11.2152 | greater       |
|  6 | Hinge | ensLoss |   1      | -16.3162 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.0507 | greater       |

#### CIFAR01 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR01',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9197 | 0.84   |  0.9189 |    0.9474 |
| ('test_acc', 'std')  | 0.001  | 0.0029 |  0.0019 |    0.0023 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9744 | 0.9196 |  0.9705 |    0.9843 |
| ('test_auc', 'std')  | 0.0012 | 0.0026 |  0.0016 |    0.0012 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0005 |  -8.7421 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -14.25   | less          |
|  9 | EXP   | ensLoss |   0      | -46.4983 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9995 |  -8.7421 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -14.25   | greater       |
|  9 | EXP   | ensLoss |   1      | -46.4983 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0055 |  -4.4739 | less          |
|  6 | Hinge | ensLoss |   0.002  |  -5.9611 | less          |
|  9 | EXP   | ensLoss |   0      | -22.7748 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9945 |  -4.4739 | greater       |
|  6 | Hinge | ensLoss |   0.998  |  -5.9611 | greater       |
|  9 | EXP   | ensLoss |   1      | -22.7748 | greater       |

#### CIFAR01 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR01',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9371 | 0.8725 |  0.9406 |    0.9748 |
| ('test_acc', 'std')  | 0.0013 | 0.0046 |  0.0025 |    0.0018 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9839 | 0.9475 |  0.9845 |    0.9954 |
| ('test_auc', 'std')  | 0.0014 | 0.0028 |  0.0007 |    0.0005 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -26.5587 | less          |
|  6 | Hinge | ensLoss |        0 | -15.7501 | less          |
|  9 | EXP   | ensLoss |        0 | -23.0837 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -26.5587 | greater       |
|  6 | Hinge | ensLoss |        1 | -15.7501 | greater       |
|  9 | EXP   | ensLoss |        1 | -23.0837 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0004 |  -8.9194 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -12.2582 | less          |
|  9 | EXP   | ensLoss |   0      | -18.3585 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9996 |  -8.9194 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -12.2582 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.3585 | greater       |

#### CIFAR18 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR18',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9099 | 0.7233 |  0.9011 |    0.9458 |
| ('test_acc', 'std')  | 0.0047 | 0.0061 |  0.0048 |    0.0037 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9692 | 0.8065 |  0.9633 |    0.9875 |
| ('test_auc', 'std')  | 0.0026 | 0.0038 |  0.0014 |    0.0012 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0014 |  -6.5588 | less          |
|  6 | Hinge | ensLoss |   0.0011 |  -7.027  | less          |
|  9 | EXP   | ensLoss |   0      | -28.195  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9986 |  -6.5588 | greater       |
|  6 | Hinge | ensLoss |   0.9989 |  -7.027  | greater       |
|  9 | EXP   | ensLoss |   1      | -28.195  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0021 |  -5.8463 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -11.3892 | less          |
|  9 | EXP   | ensLoss |   0      | -50.5918 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9979 |  -5.8463 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -11.3892 | greater       |
|  9 | EXP   | ensLoss |   1      | -50.5918 | greater       |

#### CIFAR02 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR02',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8664 | 0.8263 |  0.8686 |    0.8858 |
| ('test_acc', 'std')  | 0.0027 | 0.0051 |  0.0035 |    0.0045 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9411 | 0.9048 |  0.9256 |    0.9451 |
| ('test_auc', 'std')  | 0.0021 | 0.0035 |  0.0024 |    0.0021 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0052 | -4.5619 | less          |
|  6 | Hinge | ensLoss |   0.0182 | -3.096  | less          |
|  9 | EXP   | ensLoss |   0.0004 | -8.9802 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9948 | -4.5619 | greater       |
|  6 | Hinge | ensLoss |   0.9818 | -3.096  | greater       |
|  9 | EXP   | ensLoss |   0.9996 | -8.9802 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.1553 | -1.1599 | less          |
|  6 | Hinge | ensLoss |   0.0011 | -6.942  | less          |
|  9 | EXP   | ensLoss |   0.0003 | -9.6366 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.8447 | -1.1599 | greater       |
|  6 | Hinge | ensLoss |   0.9989 | -6.942  | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -9.6366 | greater       |

#### CIFAR19 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR19',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8436 | 0.6904 |  0.848  |    0.8919 |
| ('test_acc', 'std')  | 0.0036 | 0.0036 |  0.0041 |    0.0062 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9219 | 0.7596 |  0.9187 |    0.9572 |
| ('test_auc', 'std')  | 0.0032 | 0.0031 |  0.0021 |    0.0039 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0017 |  -6.2166 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.8206 | less          |
|  9 | EXP   | ensLoss |   0      | -25.8153 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9983 |  -6.2166 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.8206 | greater       |
|  9 | EXP   | ensLoss |   1      | -25.8153 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0021 |  -5.9072 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -13.8506 | less          |
|  9 | EXP   | ensLoss |   0      | -30.7613 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9979 |  -5.9072 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -13.8506 | greater       |
|  9 | EXP   | ensLoss |   1      | -30.7613 | greater       |

#### CIFAR01 - model: DenseNet121 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR01',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet121'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9663 | 0.9395 |  0.9689 |    0.9861 |
| ('test_acc', 'std')  | 0.0008 | 0.0021 |  0.0013 |    0.0008 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9932 | 0.983  |  0.9934 |    0.9982 |
| ('test_auc', 'std')  | 0.0003 | 0.0004 |  0.0005 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -25.7775 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.4387 | less          |
|  9 | EXP   | ensLoss |   0      | -20.8715 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -25.7775 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.4387 | greater       |
|  9 | EXP   | ensLoss |   1      | -20.8715 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -23.2315 | less          |
|  6 | Hinge | ensLoss |   0.0003 |  -9.4832 | less          |
|  9 | EXP   | ensLoss |   0      | -55.5072 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -23.2315 | greater       |
|  6 | Hinge | ensLoss |   0.9997 |  -9.4832 | greater       |
|  9 | EXP   | ensLoss |   1      | -55.5072 | greater       |

#### CIFAR02 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR02',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8863 | 0.8471 |  0.8863 |    0.9129 |
| ('test_acc', 'std')  | 0.0023 | 0.002  |  0.0028 |    0.0025 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.956  | 0.9242 |  0.9547 |    0.9699 |
| ('test_auc', 'std')  | 0.0009 | 0.0017 |  0.0017 |    0.0007 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 | -10.1559 | less          |
|  6 | Hinge | ensLoss |   0.0016 |  -6.2942 | less          |
|  9 | EXP   | ensLoss |   0      | -24.4123 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 | -10.1559 | greater       |
|  6 | Hinge | ensLoss |   0.9984 |  -6.2942 | greater       |
|  9 | EXP   | ensLoss |   1      | -24.4123 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.306  | less          |
|  6 | Hinge | ensLoss |   0.0007 |  -7.944  | less          |
|  9 | EXP   | ensLoss |   0      | -22.5122 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.306  | greater       |
|  6 | Hinge | ensLoss |   0.9993 |  -7.944  | greater       |
|  9 | EXP   | ensLoss |   1      | -22.5122 | greater       |

#### CIFAR03 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR03',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9185 | 0.8786 |  0.9146 |    0.9318 |
| ('test_acc', 'std')  | 0.0015 | 0.0022 |  0.0022 |    0.0012 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9707 | 0.9508 |  0.9677 |    0.9713 |
| ('test_auc', 'std')  | 0.0007 | 0.0017 |  0.0009 |    0.0009 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0004 |  -9.1453 | less          |
|  6 | Hinge | ensLoss |   0.0021 |  -5.8944 | less          |
|  9 | EXP   | ensLoss |   0      | -17.3151 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9996 |  -9.1453 | greater       |
|  6 | Hinge | ensLoss |   0.9979 |  -5.8944 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.3151 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.3137 |  -0.5249 | less          |
|  6 | Hinge | ensLoss |   0.0068 |  -4.2031 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.387  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.6863 |  -0.5249 | greater       |
|  6 | Hinge | ensLoss |   0.9932 |  -4.2031 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.387  | greater       |

#### CIFAR19 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR19',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8247 | 0.6963 |  0.8266 |    0.8918 |
| ('test_acc', 'std')  | 0.0027 | 0.0059 |  0.0023 |    0.0027 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9031 | 0.7612 |  0.9033 |    0.9579 |
| ('test_auc', 'std')  | 0.0027 | 0.005  |  0.0035 |    0.0016 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -34.153  | less          |
|  6 | Hinge | ensLoss |        0 | -15.48   | less          |
|  9 | EXP   | ensLoss |        0 | -24.3946 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -34.153  | greater       |
|  6 | Hinge | ensLoss |        1 | -15.48   | greater       |
|  9 | EXP   | ensLoss |        1 | -24.3946 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -22.1495 | less          |
|  6 | Hinge | ensLoss |        0 | -15.9943 | less          |
|  9 | EXP   | ensLoss |        0 | -37.6675 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -22.1495 | greater       |
|  6 | Hinge | ensLoss |        1 | -15.9943 | greater       |
|  9 | EXP   | ensLoss |        1 | -37.6675 | greater       |

#### CIFAR03 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR03',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9296 | 0.9004 |  0.935  |    0.95   |
| ('test_acc', 'std')  | 0.0021 | 0.0024 |  0.0015 |    0.0021 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9797 | 0.9637 |  0.9816 |    0.9877 |
| ('test_auc', 'std')  | 0.0011 | 0.0021 |  0.0008 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |      stat | alternative   |
|---:|:------|:--------|---------:|----------:|:--------------|
|  3 | BCE   | ensLoss |   0.0031 |   -5.2611 | less          |
|  6 | Hinge | ensLoss |   0.0062 |   -4.3256 | less          |
|  9 | EXP   | ensLoss |   0      | -102.316  | less          |


|    | A     | B       |   pvalue |      stat | alternative   |
|---:|:------|:--------|---------:|----------:|:--------------|
|  3 | BCE   | ensLoss |   0.9969 |   -5.2611 | greater       |
|  6 | Hinge | ensLoss |   0.9938 |   -4.3256 | greater       |
|  9 | EXP   | ensLoss |   1      | -102.316  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0006 |  -8.1457 | less          |
|  6 | Hinge | ensLoss |   0.0016 |  -6.359  | less          |
|  9 | EXP   | ensLoss |   0.0002 | -11.4845 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9994 |  -8.1457 | greater       |
|  6 | Hinge | ensLoss |   0.9984 |  -6.359  | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -11.4845 | greater       |

#### CIFAR04 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR04',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.92   | 0.8841 |  0.9169 |    0.9323 |
| ('test_acc', 'std')  | 0.0018 | 0.0047 |  0.0021 |    0.002  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9729 | 0.9505 |  0.9614 |    0.9786 |
| ('test_auc', 'std')  | 0.0007 | 0.0021 |  0.0023 |    0.0014 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0118 |  -3.5633 | less          |
|  6 | Hinge | ensLoss |   0.008  |  -4.0118 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -10.2495 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9882 |  -3.5633 | greater       |
|  6 | Hinge | ensLoss |   0.992  |  -4.0118 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -10.2495 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0128 |  -3.4679 | less          |
|  6 | Hinge | ensLoss |   0.0022 |  -5.8334 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.8651 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9872 |  -3.4679 | greater       |
|  6 | Hinge | ensLoss |   0.9978 |  -5.8334 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.8651 | greater       |

#### CIFAR19 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR19',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8068 | 0.5634 |  0.8109 |    0.8767 |
| ('test_acc', 'std')  | 0.0043 | 0.0061 |  0.0049 |    0.0049 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8924 | 0.5932 |  0.8731 |    0.9429 |
| ('test_auc', 'std')  | 0.0026 | 0.0092 |  0.005  |    0.0052 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -14.9933 | less          |
|  6 | Hinge | ensLoss |   0      | -22.9924 | less          |
|  9 | EXP   | ensLoss |   0      | -41.9077 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -14.9933 | greater       |
|  6 | Hinge | ensLoss |   1      | -22.9924 | greater       |
|  9 | EXP   | ensLoss |   1      | -41.9077 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 | -10.1315 | less          |
|  6 | Hinge | ensLoss |   0      | -38.4001 | less          |
|  9 | EXP   | ensLoss |   0      | -30.1516 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 | -10.1315 | greater       |
|  6 | Hinge | ensLoss |   1      | -38.4001 | greater       |
|  9 | EXP   | ensLoss |   1      | -30.1516 | greater       |

#### CIFAR04 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR04',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9397 | 0.9046 |  0.9393 |    0.9561 |
| ('test_acc', 'std')  | 0.0019 | 0.0019 |  0.0016 |    0.0016 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9837 | 0.967  |  0.9848 |    0.9906 |
| ('test_auc', 'std')  | 0.0006 | 0.0014 |  0.0007 |    0.0012 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0026 |  -5.5097 | less          |
|  6 | Hinge | ensLoss |   0.0006 |  -8.2073 | less          |
|  9 | EXP   | ensLoss |   0      | -24.0775 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9974 |  -5.5097 | greater       |
|  6 | Hinge | ensLoss |   0.9994 |  -8.2073 | greater       |
|  9 | EXP   | ensLoss |   1      | -24.0775 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0058 |  -4.4098 | less          |
|  6 | Hinge | ensLoss |   0.0043 |  -4.8192 | less          |
|  9 | EXP   | ensLoss |   0      | -27.4653 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9942 |  -4.4098 | greater       |
|  6 | Hinge | ensLoss |   0.9957 |  -4.8192 | greater       |
|  9 | EXP   | ensLoss |   1      | -27.4653 | greater       |

#### CIFAR23 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR23',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7897 | 0.7202 |  0.7976 |    0.8133 |
| ('test_acc', 'std')  | 0.0021 | 0.002  |  0.0032 |    0.0061 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8708 | 0.7941 |  0.8712 |    0.8895 |
| ('test_auc', 'std')  | 0.0027 | 0.0018 |  0.002  |    0.0064 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0081 |  -3.9957 | less          |
|  6 | Hinge | ensLoss |   0.034  |  -2.4842 | less          |
|  9 | EXP   | ensLoss |   0      | -15.8942 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9919 |  -3.9957 | greater       |
|  6 | Hinge | ensLoss |   0.966  |  -2.4842 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.8942 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0257 |  -2.7507 | less          |
|  6 | Hinge | ensLoss |   0.0187 |  -3.0691 | less          |
|  9 | EXP   | ensLoss |   0      | -15.9872 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9743 |  -2.7507 | greater       |
|  6 | Hinge | ensLoss |   0.9813 |  -3.0691 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.9872 | greater       |

#### CIFAR01 - model: DenseNet169 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR01',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet169'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9656 | 0.94   |  0.9667 |    0.9839 |
| ('test_acc', 'std')  | 0.0011 | 0.0025 |  0.0007 |    0.001  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9933 | 0.9829 |  0.9932 |    0.9981 |
| ('test_auc', 'std')  | 0.0005 | 0.001  |  0.0003 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -16.2708 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -13.5346 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.8238 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -16.2708 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -13.5346 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.8238 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0004 |  -9.2973 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.6164 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -15.1176 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9996 |  -9.2973 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.6164 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -15.1176 | greater       |

#### CIFAR05 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR05',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9358 | 0.9052 |  0.9313 |    0.9426 |
| ('test_acc', 'std')  | 0.0014 | 0.0044 |  0.0019 |    0.0022 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.983  | 0.9659 |  0.9799 |    0.9808 |
| ('test_auc', 'std')  | 0.0004 | 0.0017 |  0.0012 |    0.0009 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0492 | -2.1461 | less          |
|  6 | Hinge | ensLoss |   0.0013 | -6.7053 | less          |
|  9 | EXP   | ensLoss |   0.0011 | -6.9408 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9508 | -2.1461 | greater       |
|  6 | Hinge | ensLoss |   0.9987 | -6.7053 | greater       |
|  9 | EXP   | ensLoss |   0.9989 | -6.9408 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9616 |  2.3706 | less          |
|  6 | Hinge | ensLoss |   0.3154 | -0.5194 | less          |
|  9 | EXP   | ensLoss |   0.0008 | -7.6067 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0384 |  2.3706 | greater       |
|  6 | Hinge | ensLoss |   0.6846 | -0.5194 | greater       |
|  9 | EXP   | ensLoss |   0.9992 | -7.6067 | greater       |

#### CIFAR23 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR23',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7795 | 0.7272 |  0.7887 |    0.8131 |
| ('test_acc', 'std')  | 0.0028 | 0.003  |  0.0021 |    0.0038 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8598 | 0.8021 |  0.8633 |    0.8921 |
| ('test_auc', 'std')  | 0.0025 | 0.0017 |  0.0036 |    0.0034 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0004 |  -9.2798 | less          |
|  6 | Hinge | ensLoss |   0.0027 |  -5.4752 | less          |
|  9 | EXP   | ensLoss |   0      | -21.5526 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9996 |  -9.2798 | greater       |
|  6 | Hinge | ensLoss |   0.9973 |  -5.4752 | greater       |
|  9 | EXP   | ensLoss |   1      | -21.5526 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0007 |  -7.9622 | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -9.4133 | less          |
|  9 | EXP   | ensLoss |   0      | -22.1124 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9993 |  -7.9622 | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -9.4133 | greater       |
|  9 | EXP   | ensLoss |   1      | -22.1124 | greater       |

#### CIFAR05 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR05',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9489 | 0.9231 |  0.9505 |    0.964  |
| ('test_acc', 'std')  | 0.0007 | 0.0014 |  0.0016 |    0.0018 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9882 | 0.9771 |  0.989  |    0.9923 |
| ('test_auc', 'std')  | 0.0004 | 0.0006 |  0.0007 |    0.0005 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0016 |  -6.3054 | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -9.0001 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.3865 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9984 |  -6.3054 | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -9.0001 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.3865 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0043 |  -4.8194 | less          |
|  6 | Hinge | ensLoss |   0.0019 |  -6.0402 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.1259 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9957 |  -4.8194 | greater       |
|  6 | Hinge | ensLoss |   0.9981 |  -6.0402 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.1259 | greater       |

#### CIFAR06 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR06',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9485 | 0.9246 |  0.9465 |    0.9632 |
| ('test_acc', 'std')  | 0.0022 | 0.0018 |  0.0016 |    0.0014 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9872 | 0.9761 |  0.9866 |    0.9909 |
| ('test_auc', 'std')  | 0.0006 | 0.0008 |  0.0006 |    0.0008 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0034 |  -5.1444 | less          |
|  6 | Hinge | ensLoss |   0.0021 |  -5.8988 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.6848 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9966 |  -5.1444 | greater       |
|  6 | Hinge | ensLoss |   0.9979 |  -5.8988 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.6848 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.027  |  -2.7003 | less          |
|  6 | Hinge | ensLoss |   0.0145 |  -3.3306 | less          |
|  9 | EXP   | ensLoss |   0      | -30.658  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.973  |  -2.7003 | greater       |
|  6 | Hinge | ensLoss |   0.9855 |  -3.3306 | greater       |
|  9 | EXP   | ensLoss |   1      | -30.658  | greater       |

#### CIFAR23 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR23',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7787 | 0.5977 |  0.7819 |    0.7995 |
| ('test_acc', 'std')  | 0.003  | 0.0026 |  0.0029 |    0.0083 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.858  | 0.6447 |  0.8365 |    0.8767 |
| ('test_auc', 'std')  | 0.0027 | 0.0057 |  0.0043 |    0.0086 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0536 |  -2.0706 | less          |
|  6 | Hinge | ensLoss |   0.0751 |  -1.7776 | less          |
|  9 | EXP   | ensLoss |   0      | -19.3587 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9464 |  -2.0706 | greater       |
|  6 | Hinge | ensLoss |   0.9249 |  -1.7776 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.3587 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0563 |  -2.0269 | less          |
|  6 | Hinge | ensLoss |   0.0148 |  -3.3109 | less          |
|  9 | EXP   | ensLoss |   0      | -17.3909 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9437 |  -2.0269 | greater       |
|  6 | Hinge | ensLoss |   0.9852 |  -3.3109 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.3909 | greater       |

#### CIFAR06 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR06',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.959  | 0.9369 |  0.9584 |    0.9745 |
| ('test_acc', 'std')  | 0.0015 | 0.0018 |  0.0013 |    0.0015 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9913 | 0.9824 |  0.9925 |    0.9962 |
| ('test_auc', 'std')  | 0.0005 | 0.0007 |  0.0002 |    0.0005 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0023 |  -5.727  | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -8.9514 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.6803 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9977 |  -5.727  | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -8.9514 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.6803 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0038 |  -4.9666 | less          |
|  6 | Hinge | ensLoss |   0.0026 |  -5.5636 | less          |
|  9 | EXP   | ensLoss |   0      | -17.0883 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9962 |  -4.9666 | greater       |
|  6 | Hinge | ensLoss |   0.9974 |  -5.5636 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.0883 | greater       |

#### CIFAR02 - model: DenseNet121 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR02',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet121'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9276 | 0.9014 |  0.9271 |    0.9495 |
| ('test_acc', 'std')  | 0.0012 | 0.0017 |  0.0022 |    0.0019 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.979  | 0.9629 |  0.9794 |    0.9865 |
| ('test_auc', 'std')  | 0.0007 | 0.0009 |  0.0007 |    0.0013 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0004 |  -9.351  | less          |
|  6 | Hinge | ensLoss |   0.0024 |  -5.6924 | less          |
|  9 | EXP   | ensLoss |   0      | -20.6322 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9996 |  -9.351  | greater       |
|  6 | Hinge | ensLoss |   0.9976 |  -5.6924 | greater       |
|  9 | EXP   | ensLoss |   1      | -20.6322 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0024 |  -5.6836 | less          |
|  6 | Hinge | ensLoss |   0.0063 |  -4.299  | less          |
|  9 | EXP   | ensLoss |   0      | -22.121  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9976 |  -5.6836 | greater       |
|  6 | Hinge | ensLoss |   0.9937 |  -4.299  | greater       |
|  9 | EXP   | ensLoss |   1      | -22.121  | greater       |

#### CIFAR07 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR07',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9354 | 0.8963 |  0.9287 |    0.9495 |
| ('test_acc', 'std')  | 0.0012 | 0.0039 |  0.0012 |    0.0015 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9806 | 0.9573 |  0.9779 |    0.984  |
| ('test_auc', 'std')  | 0.0009 | 0.0012 |  0.0005 |    0.0007 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -25.324  | less          |
|  6 | Hinge | ensLoss |   0.0001 | -12.1307 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.8504 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -25.324  | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -12.1307 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.8504 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0156 |  -3.2567 | less          |
|  6 | Hinge | ensLoss |   0.0018 |  -6.152  | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.7829 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9844 |  -3.2567 | greater       |
|  6 | Hinge | ensLoss |   0.9982 |  -6.152  | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.7829 | greater       |

#### CIFAR24 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR24',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7914 | 0.6614 |  0.8073 |    0.7979 |
| ('test_acc', 'std')  | 0.003  | 0.0069 |  0.0061 |    0.0306 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8734 | 0.72   |  0.8663 |    0.8725 |
| ('test_auc', 'std')  | 0.0024 | 0.0063 |  0.0037 |    0.0303 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.4183 | -0.22   | less          |
|  6 | Hinge | ensLoss |   0.6321 |  0.3619 | less          |
|  9 | EXP   | ensLoss |   0.0061 | -4.3463 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.5817 | -0.22   | greater       |
|  6 | Hinge | ensLoss |   0.3679 |  0.3619 | greater       |
|  9 | EXP   | ensLoss |   0.9939 | -4.3463 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.5121 |  0.0322 | less          |
|  6 | Hinge | ensLoss |   0.4156 | -0.2274 | less          |
|  9 | EXP   | ensLoss |   0.0044 | -4.7761 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.4879 |  0.0322 | greater       |
|  6 | Hinge | ensLoss |   0.5844 | -0.2274 | greater       |
|  9 | EXP   | ensLoss |   0.9956 | -4.7761 | greater       |

#### CIFAR07 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR07',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9491 | 0.917  |  0.9438 |    0.9643 |
| ('test_acc', 'std')  | 0.0011 | 0.0021 |  0.0008 |    0.0025 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9872 | 0.972  |  0.9863 |    0.9921 |
| ('test_auc', 'std')  | 0.0005 | 0.0007 |  0.0008 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0027 |  -5.4635 | less          |
|  6 | Hinge | ensLoss |   0.0009 |  -7.2821 | less          |
|  9 | EXP   | ensLoss |   0      | -24.4582 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9973 |  -5.4635 | greater       |
|  6 | Hinge | ensLoss |   0.9991 |  -7.2821 | greater       |
|  9 | EXP   | ensLoss |   1      | -24.4582 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0012 |  -6.829  | less          |
|  6 | Hinge | ensLoss |   0.002  |  -5.9656 | less          |
|  9 | EXP   | ensLoss |   0      | -27.0908 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9988 |  -6.829  | greater       |
|  6 | Hinge | ensLoss |   0.998  |  -5.9656 | greater       |
|  9 | EXP   | ensLoss |   1      | -27.0908 | greater       |

#### CIFAR24 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR24',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7642 | 0.6527 |  0.754  |    0.8478 |
| ('test_acc', 'std')  | 0.0047 | 0.0062 |  0.0045 |    0.0021 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8406 | 0.7087 |  0.8251 |    0.9219 |
| ('test_auc', 'std')  | 0.0062 | 0.0063 |  0.008  |    0.0016 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -15.2226 | less          |
|  6 | Hinge | ensLoss |        0 | -24.288  | less          |
|  9 | EXP   | ensLoss |        0 | -34.43   | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -15.2226 | greater       |
|  6 | Hinge | ensLoss |        1 | -24.288  | greater       |
|  9 | EXP   | ensLoss |        1 | -34.43   | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -12.8497 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -13.3942 | less          |
|  9 | EXP   | ensLoss |   0      | -35.5323 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -12.8497 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -13.3942 | greater       |
|  9 | EXP   | ensLoss |   1      | -35.5323 | greater       |

#### CIFAR08 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR08',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8474 | 0.6943 |  0.8418 |    0.8892 |
| ('test_acc', 'std')  | 0.0021 | 0.0059 |  0.0025 |    0.0031 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9255 | 0.7603 |   0.923 |    0.9457 |
| ('test_auc', 'std')  | 0.0004 | 0.0076 |   0.001 |    0.0017 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.4696 | less          |
|  6 | Hinge | ensLoss |   0      | -15.8796 | less          |
|  9 | EXP   | ensLoss |   0      | -24.0571 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.4696 | greater       |
|  6 | Hinge | ensLoss |   1      | -15.8796 | greater       |
|  9 | EXP   | ensLoss |   1      | -24.0571 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.9642 | less          |
|  6 | Hinge | ensLoss |   0      | -23.1455 | less          |
|  9 | EXP   | ensLoss |   0      | -21.5773 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.9642 | greater       |
|  6 | Hinge | ensLoss |   1      | -23.1455 | greater       |
|  9 | EXP   | ensLoss |   1      | -21.5773 | greater       |

#### CIFAR08 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR08',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8925 | 0.7852 |  0.8948 |    0.9306 |
| ('test_acc', 'std')  | 0.0015 | 0.004  |  0.0021 |    0.0024 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9591 | 0.8692 |  0.9576 |    0.978  |
| ('test_auc', 'std')  | 0.0018 | 0.0051 |  0.0011 |    0.0008 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -12.9656 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -14.5971 | less          |
|  9 | EXP   | ensLoss |   0      | -50.2876 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -12.9656 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -14.5971 | greater       |
|  9 | EXP   | ensLoss |   1      | -50.2876 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -13.2628 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -13.7121 | less          |
|  9 | EXP   | ensLoss |   0      | -22.1013 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -13.2628 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -13.7121 | greater       |
|  9 | EXP   | ensLoss |   1      | -22.1013 | greater       |

#### CIFAR09 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR09',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8957 | 0.833  |  0.9006 |    0.9243 |
| ('test_acc', 'std')  | 0.002  | 0.0027 |  0.0034 |    0.0027 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.962  | 0.9148 |  0.9587 |    0.9703 |
| ('test_auc', 'std')  | 0.0003 | 0.002  |  0.0017 |    0.002  |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -12.7458 | less          |
|  6 | Hinge | ensLoss |   0.0058 |  -4.4208 | less          |
|  9 | EXP   | ensLoss |   0      | -23.0311 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -12.7458 | greater       |
|  6 | Hinge | ensLoss |   0.9942 |  -4.4208 | greater       |
|  9 | EXP   | ensLoss |   1      | -23.0311 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0075 |  -4.085  | less          |
|  6 | Hinge | ensLoss |   0.0095 |  -3.8086 | less          |
|  9 | EXP   | ensLoss |   0      | -19.0772 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9925 |  -4.085  | greater       |
|  6 | Hinge | ensLoss |   0.9905 |  -3.8086 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.0772 | greater       |

#### CIFAR24 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR24',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7402 | 0.5732 |  0.7546 |    0.8293 |
| ('test_acc', 'std')  | 0.0056 | 0.0084 |  0.0058 |    0.0024 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8163 | 0.6006 |  0.7914 |    0.9041 |
| ('test_auc', 'std')  | 0.005  | 0.0065 |  0.0085 |    0.0037 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -19.0135 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -11.5554 | less          |
|  9 | EXP   | ensLoss |   0      | -32.0225 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -19.0135 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -11.5554 | greater       |
|  9 | EXP   | ensLoss |   1      | -32.0225 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -32.9272 | less          |
|  6 | Hinge | ensLoss |   0.0003 | -10.1768 | less          |
|  9 | EXP   | ensLoss |   0      | -33.3343 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -32.9272 | greater       |
|  6 | Hinge | ensLoss |   0.9997 | -10.1768 | greater       |
|  9 | EXP   | ensLoss |   1      | -33.3343 | greater       |

#### CIFAR02 - model: DenseNet169 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR02',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet169'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9231 | 0.8979 |  0.9208 |    0.9478 |
| ('test_acc', 'std')  | 0.0019 | 0.0023 |  0.0014 |    0.0011 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9783 | 0.9618 |  0.9777 |    0.986  |
| ('test_auc', 'std')  | 0.0005 | 0.0008 |  0.0007 |    0.0005 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -18.0867 | less          |
|  6 | Hinge | ensLoss |        0 | -16.0641 | less          |
|  9 | EXP   | ensLoss |        0 | -17.7705 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -18.0867 | greater       |
|  6 | Hinge | ensLoss |        1 | -16.0641 | greater       |
|  9 | EXP   | ensLoss |        1 | -17.7705 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -22.4726 | less          |
|  6 | Hinge | ensLoss |   0.0005 |  -8.6361 | less          |
|  9 | EXP   | ensLoss |   0      | -27.3322 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -22.4726 | greater       |
|  6 | Hinge | ensLoss |   0.9995 |  -8.6361 | greater       |
|  9 | EXP   | ensLoss |   1      | -27.3322 | greater       |

#### CIFAR25 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR25',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8152 | 0.7263 |  0.825  |    0.8505 |
| ('test_acc', 'std')  | 0.0039 | 0.0024 |  0.0024 |    0.0066 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8962 | 0.8081 |  0.8966 |    0.9255 |
| ('test_auc', 'std')  | 0.0027 | 0.0031 |  0.0017 |    0.003  |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0042 |  -4.8334 | less          |
|  6 | Hinge | ensLoss |   0.0069 |  -4.1851 | less          |
|  9 | EXP   | ensLoss |   0      | -15.8905 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9958 |  -4.8334 | greater       |
|  6 | Hinge | ensLoss |   0.9931 |  -4.1851 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.8905 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.5209 | less          |
|  6 | Hinge | ensLoss |   0.0006 |  -8.3551 | less          |
|  9 | EXP   | ensLoss |   0      | -21.9744 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.5209 | greater       |
|  6 | Hinge | ensLoss |   0.9994 |  -8.3551 | greater       |
|  9 | EXP   | ensLoss |   1      | -21.9744 | greater       |

#### CIFAR09 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR09',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9241 | 0.8709 |  0.9253 |    0.9462 |
| ('test_acc', 'std')  | 0.0034 | 0.005  |  0.0034 |    0.0012 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.979  | 0.945  |  0.9789 |    0.9868 |
| ('test_auc', 'std')  | 0.0009 | 0.0014 |  0.0012 |    0.001  |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0012 |  -6.7609 | less          |
|  6 | Hinge | ensLoss |   0.0031 |  -5.2857 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.8252 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9988 |  -6.7609 | greater       |
|  6 | Hinge | ensLoss |   0.9969 |  -5.2857 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.8252 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -11.3647 | less          |
|  6 | Hinge | ensLoss |   0.0026 |  -5.5276 | less          |
|  9 | EXP   | ensLoss |   0      | -18.6185 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -11.3647 | greater       |
|  6 | Hinge | ensLoss |   0.9974 |  -5.5276 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.6185 | greater       |

#### CIFAR12 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR12',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9466 | 0.8963 |  0.9442 |    0.9654 |
| ('test_acc', 'std')  | 0.0012 | 0.0044 |  0.0015 |    0.0015 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.989  | 0.9636 |  0.986  |    0.9916 |
| ('test_auc', 'std')  | 0.0005 | 0.0017 |  0.0008 |    0.0006 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 |  -9.7213 | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -9.0686 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.1613 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 |  -9.7213 | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -9.0686 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.1613 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.023  |  -2.8579 | less          |
|  6 | Hinge | ensLoss |   0.0036 |  -5.0543 | less          |
|  9 | EXP   | ensLoss |   0      | -17.3321 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.977  |  -2.8579 | greater       |
|  6 | Hinge | ensLoss |   0.9964 |  -5.0543 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.3321 | greater       |

#### CIFAR25 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR25',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8108 | 0.742  |  0.8136 |    0.8356 |
| ('test_acc', 'std')  | 0.005  | 0.0011 |  0.0027 |    0.0047 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8947 | 0.8187 |  0.8927 |    0.9131 |
| ('test_auc', 'std')  | 0.0039 | 0.0029 |  0.0021 |    0.0035 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0148 |  -3.3158 | less          |
|  6 | Hinge | ensLoss |   0.008  |  -4.005  | less          |
|  9 | EXP   | ensLoss |   0      | -18.3706 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9852 |  -3.3158 | greater       |
|  6 | Hinge | ensLoss |   0.992  |  -4.005  | greater       |
|  9 | EXP   | ensLoss |   1      | -18.3706 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0082 |  -3.985  | less          |
|  6 | Hinge | ensLoss |   0.0007 |  -8.0082 | less          |
|  9 | EXP   | ensLoss |   0      | -16.946  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9918 |  -3.985  | greater       |
|  6 | Hinge | ensLoss |   0.9993 |  -8.0082 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.946  | greater       |

#### CIFAR12 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR12',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9646 | 0.9282 |  0.9645 |    0.9798 |
| ('test_acc', 'std')  | 0.0014 | 0.0046 |  0.0007 |    0.0009 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9945 | 0.9809 |  0.9947 |    0.9986 |
| ('test_auc', 'std')  | 0.0003 | 0.0012 |  0.0003 |    0.0001 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 |  -9.781  | less          |
|  6 | Hinge | ensLoss |   0      | -16.9479 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.6533 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 |  -9.781  | greater       |
|  6 | Hinge | ensLoss |   1      | -16.9479 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.6533 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -11.45   | less          |
|  6 | Hinge | ensLoss |   0.0001 | -13.7844 | less          |
|  9 | EXP   | ensLoss |   0      | -16.1007 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -11.45   | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -13.7844 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.1007 | greater       |

#### CIFAR03 - model: DenseNet121 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR03',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet121'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9595 | 0.9443 |  0.9533 |    0.9715 |
| ('test_acc', 'std')  | 0.0015 | 0.0009 |  0.0015 |    0.0009 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9917 | 0.9858 |  0.9902 |    0.9943 |
| ('test_auc', 'std')  | 0.0005 | 0.0005 |  0.0006 |    0.0005 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0033 |  -5.2002 | less          |
|  6 | Hinge | ensLoss |   0.0005 |  -8.7616 | less          |
|  9 | EXP   | ensLoss |   0      | -90.6679 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9967 |  -5.2002 | greater       |
|  6 | Hinge | ensLoss |   0.9995 |  -8.7616 | greater       |
|  9 | EXP   | ensLoss |   1      | -90.6679 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0025 |  -5.5908 | less          |
|  6 | Hinge | ensLoss |   0.0014 |  -6.5587 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.6889 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9975 |  -5.5908 | greater       |
|  6 | Hinge | ensLoss |   0.9986 |  -6.5587 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.6889 | greater       |

#### CIFAR13 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR13',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9432 | 0.9017 |  0.945  |    0.9551 |
| ('test_acc', 'std')  | 0.0015 | 0.002  |  0.0007 |    0.0007 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9865 | 0.9641 |  0.9862 |    0.986  |
| ('test_auc', 'std')  | 0.0005 | 0.0015 |  0.0008 |    0.0007 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0008 |  -7.6655 | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -9.4803 | less          |
|  9 | EXP   | ensLoss |   0      | -25.3567 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9992 |  -7.6655 | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -9.4803 | greater       |
|  9 | EXP   | ensLoss |   1      | -25.3567 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.7102 |   0.602  | less          |
|  6 | Hinge | ensLoss |   0.5859 |   0.2316 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.3595 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.2898 |   0.602  | greater       |
|  6 | Hinge | ensLoss |   0.4141 |   0.2316 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.3595 | greater       |

#### CIFAR25 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR25',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8021 | 0.6376 |  0.7968 |    0.842  |
| ('test_acc', 'std')  | 0.0045 | 0.0036 |  0.0061 |    0.0052 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8843 | 0.6982 |  0.8615 |    0.9154 |
| ('test_auc', 'std')  | 0.0033 | 0.0058 |  0.0057 |    0.0062 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0047 |  -4.693  | less          |
|  6 | Hinge | ensLoss |   0.0023 |  -5.7247 | less          |
|  9 | EXP   | ensLoss |   0      | -36.3554 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9953 |  -4.693  | greater       |
|  6 | Hinge | ensLoss |   0.9977 |  -5.7247 | greater       |
|  9 | EXP   | ensLoss |   1      | -36.3554 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0104 |  -3.7038 | less          |
|  6 | Hinge | ensLoss |   0.0022 |  -5.7639 | less          |
|  9 | EXP   | ensLoss |   0      | -36.6734 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9896 |  -3.7038 | greater       |
|  6 | Hinge | ensLoss |   0.9978 |  -5.7639 | greater       |
|  9 | EXP   | ensLoss |   1      | -36.6734 | greater       |

#### CIFAR13 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR13',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9536 | 0.9274 |  0.9578 |    0.972  |
| ('test_acc', 'std')  | 0.0012 | 0.0027 |  0.0017 |    0.0005 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9909 | 0.9794 |  0.992  |    0.9953 |
| ('test_auc', 'std')  | 0.0006 | 0.0015 |  0.0003 |    0.0006 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -14.39   | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -9.2828 | less          |
|  9 | EXP   | ensLoss |   0      | -17.685  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -14.39   | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -9.2828 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.685  | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0032 | -5.2269 | less          |
|  6 | Hinge | ensLoss |   0.0046 | -4.7224 | less          |
|  9 | EXP   | ensLoss |   0.0005 | -8.5434 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9968 | -5.2269 | greater       |
|  6 | Hinge | ensLoss |   0.9954 | -4.7224 | greater       |
|  9 | EXP   | ensLoss |   0.9995 | -8.5434 | greater       |

#### CIFAR26 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR26',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8619 | 0.7797 |  0.871  |    0.8901 |
| ('test_acc', 'std')  | 0.0035 | 0.0016 |  0.0028 |    0.0055 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9394 | 0.8588 |  0.9413 |    0.9506 |
| ('test_auc', 'std')  | 0.0025 | 0.0033 |  0.0018 |    0.0058 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0152 |  -3.2845 | less          |
|  6 | Hinge | ensLoss |   0.017  |  -3.1686 | less          |
|  9 | EXP   | ensLoss |   0      | -20.3921 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9848 |  -3.2845 | greater       |
|  6 | Hinge | ensLoss |   0.983  |  -3.1686 | greater       |
|  9 | EXP   | ensLoss |   1      | -20.3921 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.1187 |  -1.3883 | less          |
|  6 | Hinge | ensLoss |   0.0782 |  -1.7422 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.8536 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.8813 |  -1.3883 | greater       |
|  6 | Hinge | ensLoss |   0.9218 |  -1.7422 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.8536 | greater       |

#### CIFAR14 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR14',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9584 | 0.9167 |  0.957  |    0.9746 |
| ('test_acc', 'std')  | 0.0011 | 0.0034 |  0.0019 |    0.0016 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9919 | 0.9748 |  0.9917 |    0.9956 |
| ('test_auc', 'std')  | 0.0003 | 0.0016 |  0.0007 |    0.0008 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0014 |  -6.5646 | less          |
|  6 | Hinge | ensLoss |   0.0033 |  -5.1765 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.9679 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9986 |  -6.5646 | greater       |
|  6 | Hinge | ensLoss |   0.9967 |  -5.1765 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.9679 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0095 | -3.8016 | less          |
|  6 | Hinge | ensLoss |   0.0157 | -3.2508 | less          |
|  9 | EXP   | ensLoss |   0.0004 | -8.9068 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9905 | -3.8016 | greater       |
|  6 | Hinge | ensLoss |   0.9843 | -3.2508 | greater       |
|  9 | EXP   | ensLoss |   0.9996 | -8.9068 | greater       |

#### CIFAR26 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR26',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8564 | 0.7825 |  0.8539 |    0.8782 |
| ('test_acc', 'std')  | 0.001  | 0.0028 |  0.0015 |    0.0031 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9311 | 0.8631 |  0.9286 |    0.95   |
| ('test_auc', 'std')  | 0.0022 | 0.0015 |  0.0011 |    0.0015 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0007 |  -7.8106 | less          |
|  6 | Hinge | ensLoss |   0.0013 |  -6.6284 | less          |
|  9 | EXP   | ensLoss |   0      | -24.1794 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9993 |  -7.8106 | greater       |
|  6 | Hinge | ensLoss |   0.9987 |  -6.6284 | greater       |
|  9 | EXP   | ensLoss |   1      | -24.1794 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.001  |  -7.1656 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.9362 | less          |
|  9 | EXP   | ensLoss |   0      | -45.3686 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.999  |  -7.1656 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.9362 | greater       |
|  9 | EXP   | ensLoss |   1      | -45.3686 | greater       |

#### CIFAR14 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR14',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9714 | 0.9452 |  0.9713 |    0.9879 |
| ('test_acc', 'std')  | 0.0011 | 0.0025 |  0.0016 |    0.0006 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9959 | 0.9868 |  0.9964 |    0.999  |
| ('test_auc', 'std')  | 0.0004 | 0.0008 |  0.0003 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -12.5629 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.426  | less          |
|  9 | EXP   | ensLoss |   0      | -17.784  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -12.5629 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.426  | greater       |
|  9 | EXP   | ensLoss |   1      | -17.784  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0027 |  -5.4759 | less          |
|  6 | Hinge | ensLoss |   0.0008 |  -7.5155 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.7978 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9973 |  -5.4759 | greater       |
|  6 | Hinge | ensLoss |   0.9992 |  -7.5155 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.7978 | greater       |

#### CIFAR15 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR15',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9582 | 0.9274 |  0.9552 |    0.9682 |
| ('test_acc', 'std')  | 0.0009 | 0.0021 |  0.0013 |    0.0009 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9926 | 0.9816 |  0.9924 |    0.9932 |
| ('test_auc', 'std')  | 0.0005 | 0.0011 |  0.0007 |    0.0005 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0027 |  -5.4841 | less          |
|  6 | Hinge | ensLoss |   0      | -18.3846 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.8604 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9973 |  -5.4841 | greater       |
|  6 | Hinge | ensLoss |   1      | -18.3846 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.8604 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.2135 |  -0.8831 | less          |
|  6 | Hinge | ensLoss |   0.2216 |  -0.8501 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.9264 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.7865 |  -0.8831 | greater       |
|  6 | Hinge | ensLoss |   0.7784 |  -0.8501 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.9264 | greater       |

#### CIFAR03 - model: DenseNet169 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR03',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet169'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9594 | 0.9455 |  0.9547 |    0.9715 |
| ('test_acc', 'std')  | 0.0006 | 0.0021 |  0.0011 |    0.001  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9916 | 0.9861 |  0.9904 |    0.9933 |
| ('test_auc', 'std')  | 0.0004 | 0.0007 |  0.0004 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0006 |  -8.0937 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.389  | less          |
|  9 | EXP   | ensLoss |   0.0003 |  -9.6896 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9994 |  -8.0937 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.389  | greater       |
|  9 | EXP   | ensLoss |   0.9997 |  -9.6896 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0115 |  -3.5841 | less          |
|  6 | Hinge | ensLoss |   0.0031 |  -5.2969 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -10.1246 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9885 |  -3.5841 | greater       |
|  6 | Hinge | ensLoss |   0.997  |  -5.2969 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -10.1246 | greater       |

#### CIFAR15 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR15',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9689 | 0.9481 |  0.9682 |    0.9858 |
| ('test_acc', 'std')  | 0.0018 | 0.0016 |  0.001  |    0.0011 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9958 | 0.9893 |  0.9956 |    0.9987 |
| ('test_auc', 'std')  | 0.0003 | 0.0006 |  0.0002 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0012 |  -6.837  | less          |
|  6 | Hinge | ensLoss |   0      | -18.4496 | less          |
|  9 | EXP   | ensLoss |   0      | -31.6931 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9988 |  -6.837  | greater       |
|  6 | Hinge | ensLoss |   1      | -18.4496 | greater       |
|  9 | EXP   | ensLoss |   1      | -31.6931 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0024 |  -5.6824 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -11.5029 | less          |
|  9 | EXP   | ensLoss |   0      | -18.5251 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9976 |  -5.6824 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -11.5029 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.5251 | greater       |

#### CIFAR26 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR26',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8546 | 0.6212 |  0.8578 |    0.8609 |
| ('test_acc', 'std')  | 0.0013 | 0.0092 |  0.0023 |    0.0087 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9274 | 0.6696 |  0.909  |    0.9345 |
| ('test_auc', 'std')  | 0.0012 | 0.0112 |  0.0015 |    0.0071 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.2723 |  -0.6611 | less          |
|  6 | Hinge | ensLoss |   0.3865 |  -0.3086 | less          |
|  9 | EXP   | ensLoss |   0      | -29.889  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.7277 |  -0.6611 | greater       |
|  6 | Hinge | ensLoss |   0.6135 |  -0.3086 | greater       |
|  9 | EXP   | ensLoss |   1      | -29.889  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.1651 |  -1.1073 | less          |
|  6 | Hinge | ensLoss |   0.01   |  -3.7491 | less          |
|  9 | EXP   | ensLoss |   0      | -37.4123 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.8349 |  -1.1073 | greater       |
|  6 | Hinge | ensLoss |   0.99   |  -3.7491 | greater       |
|  9 | EXP   | ensLoss |   1      | -37.4123 | greater       |

#### CIFAR16 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR16',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9613 | 0.9302 |  0.9614 |    0.9698 |
| ('test_acc', 'std')  | 0.0007 | 0.0068 |  0.0025 |    0.002  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.993  | 0.9807 |  0.9928 |    0.9939 |
| ('test_auc', 'std')  | 0.0001 | 0.0024 |  0.0007 |    0.0009 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0104 | -3.7009 | less          |
|  6 | Hinge | ensLoss |   0.0593 | -1.9821 | less          |
|  9 | EXP   | ensLoss |   0.0037 | -5.0056 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9896 | -3.7009 | greater       |
|  6 | Hinge | ensLoss |   0.9407 | -1.9821 | greater       |
|  9 | EXP   | ensLoss |   0.9963 | -5.0056 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.2154 | -0.8755 | less          |
|  6 | Hinge | ensLoss |   0.2432 | -0.7658 | less          |
|  9 | EXP   | ensLoss |   0.0051 | -4.5844 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.7846 | -0.8755 | greater       |
|  6 | Hinge | ensLoss |   0.7568 | -0.7658 | greater       |
|  9 | EXP   | ensLoss |   0.9949 | -4.5844 | greater       |

#### CIFAR27 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR27',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8808 | 0.7872 |  0.8824 |    0.9038 |
| ('test_acc', 'std')  | 0.003  | 0.0038 |  0.0018 |    0.0029 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9497 | 0.8676 |  0.9504 |    0.9655 |
| ('test_auc', 'std')  | 0.0023 | 0.0041 |  0.0008 |    0.0013 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -14.7698 | less          |
|  6 | Hinge | ensLoss |   0.0012 |  -6.8676 | less          |
|  9 | EXP   | ensLoss |   0      | -28.916  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -14.7698 | greater       |
|  6 | Hinge | ensLoss |   0.9988 |  -6.8676 | greater       |
|  9 | EXP   | ensLoss |   1      | -28.916  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0018 |  -6.1153 | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -9.0407 | less          |
|  9 | EXP   | ensLoss |   0      | -20.4688 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9982 |  -6.1153 | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -9.0407 | greater       |
|  9 | EXP   | ensLoss |   1      | -20.4688 | greater       |

#### CIFAR16 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR16',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9716 | 0.9532 |  0.9735 |    0.9855 |
| ('test_acc', 'std')  | 0.0016 | 0.0028 |  0.0012 |    0.0015 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.996  | 0.9912 |  0.9964 |    0.9989 |
| ('test_auc', 'std')  | 0.0003 | 0.0005 |  0.0003 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0036 |  -5.0554 | less          |
|  6 | Hinge | ensLoss |   0.0009 |  -7.4066 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -11.3038 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9964 |  -5.0554 | greater       |
|  6 | Hinge | ensLoss |   0.9991 |  -7.4066 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -11.3038 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0012 |  -6.7601 | less          |
|  6 | Hinge | ensLoss |   0.0012 |  -6.7638 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.0429 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9988 |  -6.7601 | greater       |
|  6 | Hinge | ensLoss |   0.9988 |  -6.7638 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.0429 | greater       |

#### CIFAR17 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR17',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9561 | 0.9002 |  0.9574 |    0.9743 |
| ('test_acc', 'std')  | 0.0023 | 0.0069 |  0.0012 |    0.0014 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9923 | 0.965  |  0.9922 |    0.9961 |
| ('test_auc', 'std')  | 0.0006 | 0.0038 |  0.0005 |    0.0007 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0023 |  -5.751  | less          |
|  6 | Hinge | ensLoss |   0      | -15.6912 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.6583 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9977 |  -5.751  | greater       |
|  6 | Hinge | ensLoss |   1      | -15.6912 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.6583 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0078 | -4.0485 | less          |
|  6 | Hinge | ensLoss |   0.0039 | -4.9342 | less          |
|  9 | EXP   | ensLoss |   0.0009 | -7.3042 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9922 | -4.0485 | greater       |
|  6 | Hinge | ensLoss |   0.9961 | -4.9342 | greater       |
|  9 | EXP   | ensLoss |   0.9991 | -7.3042 | greater       |

#### CIFAR27 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR27',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8744 | 0.7943 |  0.8705 |    0.9045 |
| ('test_acc', 'std')  | 0.0037 | 0.0054 |  0.0007 |    0.0025 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.944  | 0.8756 |  0.9426 |    0.9638 |
| ('test_auc', 'std')  | 0.0026 | 0.0049 |  0.0018 |    0.0029 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0011 |  -7.0152 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -14.3039 | less          |
|  9 | EXP   | ensLoss |   0      | -25.6106 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9989 |  -7.0152 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -14.3039 | greater       |
|  9 | EXP   | ensLoss |   1      | -25.6106 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0014 |  -6.6133 | less          |
|  6 | Hinge | ensLoss |   0.0009 |  -7.4162 | less          |
|  9 | EXP   | ensLoss |   0      | -23.7641 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9986 |  -6.6133 | greater       |
|  6 | Hinge | ensLoss |   0.9991 |  -7.4162 | greater       |
|  9 | EXP   | ensLoss |   1      | -23.7641 | greater       |

#### CIFAR04 - model: DenseNet121 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR04',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet121'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9621 | 0.9514 |  0.9622 |    0.9751 |
| ('test_acc', 'std')  | 0.0009 | 0.0013 |  0.0007 |    0.0011 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9944 | 0.99   |  0.994  |    0.996  |
| ('test_auc', 'std')  | 0.0004 | 0.0004 |  0.0001 |    0.0006 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0004 |  -9.0248 | less          |
|  6 | Hinge | ensLoss |   0      | -16.5169 | less          |
|  9 | EXP   | ensLoss |   0      | -18.0974 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9996 |  -9.0248 | greater       |
|  6 | Hinge | ensLoss |   1      | -16.5169 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.0974 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0151 |  -3.2897 | less          |
|  6 | Hinge | ensLoss |   0.0197 |  -3.0123 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -10.1197 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9849 |  -3.2897 | greater       |
|  6 | Hinge | ensLoss |   0.9803 |  -3.0123 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -10.1197 | greater       |

#### CIFAR17 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR17',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.969  | 0.9342 |  0.9692 |    0.9886 |
| ('test_acc', 'std')  | 0.0031 | 0.0026 |  0.0007 |    0.0006 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9957 | 0.9831 |  0.9959 |    0.9988 |
| ('test_auc', 'std')  | 0.0007 | 0.0008 |  0.0002 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0022 |  -5.7772 | less          |
|  6 | Hinge | ensLoss |   0      | -48.4992 | less          |
|  9 | EXP   | ensLoss |   0      | -24.1837 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9978 |  -5.7772 | greater       |
|  6 | Hinge | ensLoss |   1      | -48.4992 | greater       |
|  9 | EXP   | ensLoss |   1      | -24.1837 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0112 |  -3.6185 | less          |
|  6 | Hinge | ensLoss |   0.0008 |  -7.6221 | less          |
|  9 | EXP   | ensLoss |   0      | -15.6093 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9888 |  -3.6185 | greater       |
|  6 | Hinge | ensLoss |   0.9992 |  -7.6221 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.6093 | greater       |

#### CIFAR18 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR18',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9207 | 0.8299 |  0.9173 |    0.9396 |
| ('test_acc', 'std')  | 0.002  | 0.0029 |  0.0029 |    0.0028 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9753 | 0.9099 |  0.9697 |    0.9816 |
| ('test_auc', 'std')  | 0.0011 | 0.0028 |  0.002  |    0.0008 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0007 |  -7.9443 | less          |
|  6 | Hinge | ensLoss |   0.0044 |  -4.7663 | less          |
|  9 | EXP   | ensLoss |   0      | -29.1988 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9993 |  -7.9443 | greater       |
|  6 | Hinge | ensLoss |   0.9956 |  -4.7663 | greater       |
|  9 | EXP   | ensLoss |   1      | -29.1988 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0081 |  -3.9976 | less          |
|  6 | Hinge | ensLoss |   0.0035 |  -5.0792 | less          |
|  9 | EXP   | ensLoss |   0      | -27.9169 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9919 |  -3.9976 | greater       |
|  6 | Hinge | ensLoss |   0.9965 |  -5.0792 | greater       |
|  9 | EXP   | ensLoss |   1      | -27.9169 | greater       |

#### CIFAR27 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR27',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8654 | 0.6716 |  0.8577 |    0.9011 |
| ('test_acc', 'std')  | 0.0058 | 0.0035 |  0.0039 |    0.0036 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9422 | 0.7415 |  0.9191 |    0.9627 |
| ('test_auc', 'std')  | 0.0034 | 0.0035 |  0.0033 |    0.0013 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0028 |  -5.4181 | less          |
|  6 | Hinge | ensLoss |   0.0012 |  -6.9111 | less          |
|  9 | EXP   | ensLoss |   0      | -37.8835 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9972 |  -5.4181 | greater       |
|  6 | Hinge | ensLoss |   0.9988 |  -6.9111 | greater       |
|  9 | EXP   | ensLoss |   1      | -37.8835 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0031 |  -5.2672 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -11.3831 | less          |
|  9 | EXP   | ensLoss |   0      | -58.3769 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9969 |  -5.2672 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -11.3831 | greater       |
|  9 | EXP   | ensLoss |   1      | -58.3769 | greater       |

#### CIFAR28 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR28',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9392 | 0.8971 |  0.939  |    0.9541 |
| ('test_acc', 'std')  | 0.0013 | 0.0022 |  0.0031 |    0.002  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9842 | 0.9632 |  0.9838 |    0.9883 |
| ('test_auc', 'std')  | 0.0007 | 0.0008 |  0.0007 |    0.0015 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0045 |  -4.7451 | less          |
|  6 | Hinge | ensLoss |   0.0109 |  -3.6478 | less          |
|  9 | EXP   | ensLoss |   0      | -34.689  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9955 |  -4.7451 | greater       |
|  6 | Hinge | ensLoss |   0.9891 |  -3.6478 | greater       |
|  9 | EXP   | ensLoss |   1      | -34.689  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0347 |  -2.4629 | less          |
|  6 | Hinge | ensLoss |   0.03   |  -2.5992 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.387  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9653 |  -2.4629 | greater       |
|  6 | Hinge | ensLoss |   0.97   |  -2.5992 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.387  | greater       |

#### CIFAR18 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR18',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9459 | 0.8654 |  0.9481 |    0.9655 |
| ('test_acc', 'std')  | 0.0019 | 0.0082 |  0.0019 |    0.0009 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9871 | 0.9435 |  0.9883 |    0.9929 |
| ('test_auc', 'std')  | 0.0008 | 0.0042 |  0.0005 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 |  -9.944  | less          |
|  6 | Hinge | ensLoss |   0.0007 |  -7.7932 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -11.3098 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 |  -9.944  | greater       |
|  6 | Hinge | ensLoss |   0.9993 |  -7.7932 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -11.3098 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.4374 | less          |
|  6 | Hinge | ensLoss |   0.0009 |  -7.3643 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.4447 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.4374 | greater       |
|  6 | Hinge | ensLoss |   0.9991 |  -7.3643 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.4447 | greater       |

#### CIFAR19 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR19',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8331 | 0.6438 |  0.8325 |    0.8832 |
| ('test_acc', 'std')  | 0.0054 | 0.0148 |  0.0087 |    0.0056 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9116 | 0.7024 |  0.9021 |    0.9428 |
| ('test_auc', 'std')  | 0.0047 | 0.0191 |  0.0083 |    0.0045 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0013 |  -6.675  | less          |
|  6 | Hinge | ensLoss |   0.0044 |  -4.7872 | less          |
|  9 | EXP   | ensLoss |   0      | -25.0362 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9987 |  -6.675  | greater       |
|  6 | Hinge | ensLoss |   0.9956 |  -4.7872 | greater       |
|  9 | EXP   | ensLoss |   1      | -25.0362 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0038 |  -4.9692 | less          |
|  6 | Hinge | ensLoss |   0.0075 |  -4.0913 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -15.0619 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9962 |  -4.9692 | greater       |
|  6 | Hinge | ensLoss |   0.9925 |  -4.0913 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -15.0619 | greater       |

#### CIFAR04 - model: DenseNet169 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR04',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet169'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.962  | 0.9514 |  0.9631 |    0.9761 |
| ('test_acc', 'std')  | 0.0017 | 0.0021 |  0.0019 |    0.002  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9938 | 0.9896 |  0.9935 |    0.9961 |
| ('test_auc', 'std')  | 0.0003 | 0.0005 |  0.0004 |    0.0006 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0041 | -4.8693 | less          |
|  6 | Hinge | ensLoss |   0.0096 | -3.7965 | less          |
|  9 | EXP   | ensLoss |   0.001  | -7.2475 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9959 | -4.8693 | greater       |
|  6 | Hinge | ensLoss |   0.9904 | -3.7965 | greater       |
|  9 | EXP   | ensLoss |   0.999  | -7.2475 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0111 | -3.6324 | less          |
|  6 | Hinge | ensLoss |   0.0191 | -3.0477 | less          |
|  9 | EXP   | ensLoss |   0.0009 | -7.436  | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9889 | -3.6324 | greater       |
|  6 | Hinge | ensLoss |   0.9809 | -3.0477 | greater       |
|  9 | EXP   | ensLoss |   0.9991 | -7.436  | greater       |

#### CIFAR28 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR28',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9343 | 0.8996 |  0.9352 |    0.9495 |
| ('test_acc', 'std')  | 0.0021 | 0.0033 |  0.0012 |    0.0015 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9807 | 0.966  |  0.9818 |    0.9883 |
| ('test_auc', 'std')  | 0.0007 | 0.0019 |  0.0006 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0034 |  -5.1489 | less          |
|  6 | Hinge | ensLoss |   0.0014 |  -6.5169 | less          |
|  9 | EXP   | ensLoss |   0      | -19.3358 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9966 |  -5.1489 | greater       |
|  6 | Hinge | ensLoss |   0.9986 |  -6.5169 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.3358 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -13.8857 | less          |
|  6 | Hinge | ensLoss |   0.0003 |  -9.771  | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.779  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -13.8857 | greater       |
|  6 | Hinge | ensLoss |   0.9997 |  -9.771  | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.779  | greater       |

#### CIFAR19 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR19',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8997 | 0.767  |  0.898  |    0.9323 |
| ('test_acc', 'std')  | 0.003  | 0.0082 |  0.0043 |    0.0014 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.961  | 0.8429 |  0.9614 |    0.9783 |
| ('test_auc', 'std')  | 0.0012 | 0.009  |  0.0025 |    0.0008 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -18.7902 | less          |
|  6 | Hinge | ensLoss |   0.0009 |  -7.4469 | less          |
|  9 | EXP   | ensLoss |   0      | -19.5604 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -18.7902 | greater       |
|  6 | Hinge | ensLoss |   0.9991 |  -7.4469 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.5604 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.7981 | less          |
|  6 | Hinge | ensLoss |   0.0031 |  -5.292  | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.8007 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.7981 | greater       |
|  6 | Hinge | ensLoss |   0.9969 |  -5.292  | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.8007 | greater       |

#### CIFAR23 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR23',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7805 | 0.6764 |  0.7743 |    0.7978 |
| ('test_acc', 'std')  | 0.0032 | 0.005  |  0.0037 |    0.003  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8597 | 0.7457 |  0.8394 |    0.8656 |
| ('test_auc', 'std')  | 0.0028 | 0.0054 |  0.0016 |    0.0027 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0007 |  -7.7836 | less          |
|  6 | Hinge | ensLoss |   0.0046 |  -4.7094 | less          |
|  9 | EXP   | ensLoss |   0      | -36.0587 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9993 |  -7.7836 | greater       |
|  6 | Hinge | ensLoss |   0.9954 |  -4.7094 | greater       |
|  9 | EXP   | ensLoss |   1      | -36.0587 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0819 |  -1.703  | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -9.3683 | less          |
|  9 | EXP   | ensLoss |   0      | -25.8012 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9181 |  -1.703  | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -9.3683 | greater       |
|  9 | EXP   | ensLoss |   1      | -25.8012 | greater       |

#### CIFAR28 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR28',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9341 | 0.7439 |  0.9281 |    0.9424 |
| ('test_acc', 'std')  | 0.0013 | 0.0154 |  0.001  |    0.0021 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9803 | 0.8193 |  0.9747 |    0.9839 |
| ('test_auc', 'std')  | 0.0007 | 0.0163 |  0.001  |    0.0014 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0065 |  -4.2634 | less          |
|  6 | Hinge | ensLoss |   0.0005 |  -8.8011 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.8628 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9935 |  -4.2634 | greater       |
|  6 | Hinge | ensLoss |   0.9995 |  -8.8011 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.8628 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0351 | -2.4538 | less          |
|  6 | Hinge | ensLoss |   0.0042 | -4.8399 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -9.9713 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9649 | -2.4538 | greater       |
|  6 | Hinge | ensLoss |   0.9958 | -4.8399 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -9.9713 | greater       |

#### CIFAR23 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR23',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8185 | 0.732  |  0.8203 |    0.8549 |
| ('test_acc', 'std')  | 0.006  | 0.0031 |  0.006  |    0.0021 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8962 | 0.8062 |  0.8959 |    0.9276 |
| ('test_auc', 'std')  | 0.0032 | 0.0044 |  0.0043 |    0.0018 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0026 |  -5.5616 | less          |
|  6 | Hinge | ensLoss |   0.003  |  -5.3288 | less          |
|  9 | EXP   | ensLoss |   0      | -51.3198 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9974 |  -5.5616 | greater       |
|  6 | Hinge | ensLoss |   0.997  |  -5.3288 | greater       |
|  9 | EXP   | ensLoss |   1      | -51.3198 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0004 |  -9.3182 | less          |
|  6 | Hinge | ensLoss |   0.0016 |  -6.3546 | less          |
|  9 | EXP   | ensLoss |   0      | -28.225  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9996 |  -9.3182 | greater       |
|  6 | Hinge | ensLoss |   0.9984 |  -6.3546 | greater       |
|  9 | EXP   | ensLoss |   1      | -28.225  | greater       |

#### CIFAR24 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR24',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7765 | 0.6368 |  0.7715 |    0.8143 |
| ('test_acc', 'std')  | 0.0048 | 0.0088 |  0.0068 |    0.0054 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8572 | 0.6877 |  0.8325 |    0.8856 |
| ('test_auc', 'std')  | 0.0032 | 0.012  |  0.0048 |    0.0048 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.004  |  -4.8896 | less          |
|  6 | Hinge | ensLoss |   0.0021 |  -5.8727 | less          |
|  9 | EXP   | ensLoss |   0      | -20.5646 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.996  |  -4.8896 | greater       |
|  6 | Hinge | ensLoss |   0.9979 |  -5.8727 | greater       |
|  9 | EXP   | ensLoss |   1      | -20.5646 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0046 |  -4.7309 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -13.5051 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.885  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9954 |  -4.7309 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -13.5051 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.885  | greater       |

#### CIFAR29 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR29',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9373 | 0.8966 |  0.9401 |    0.9577 |
| ('test_acc', 'std')  | 0.0017 | 0.0023 |  0.0013 |    0.0017 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9849 | 0.961  |  0.9861 |    0.9925 |
| ('test_auc', 'std')  | 0.0006 | 0.0016 |  0.0006 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.4512 | less          |
|  6 | Hinge | ensLoss |   0.0003 |  -9.9401 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -15.0715 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.4512 | greater       |
|  6 | Hinge | ensLoss |   0.9997 |  -9.9401 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -15.0715 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -14.8527 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.6139 | less          |
|  9 | EXP   | ensLoss |   0      | -18.1366 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -14.8527 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.6139 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.1366 | greater       |

#### CIFAR05 - model: DenseNet121 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR05',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet121'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9712 | 0.9591 |  0.968  |    0.9781 |
| ('test_acc', 'std')  | 0.0005 | 0.0008 |  0.0015 |    0.0011 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9957 | 0.9925 |  0.9948 |    0.9966 |
| ('test_auc', 'std')  | 0.0001 | 0.0002 |  0.0002 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0011 |  -6.9523 | less          |
|  6 | Hinge | ensLoss |   0.0022 |  -5.7975 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.8099 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9989 |  -6.9523 | greater       |
|  6 | Hinge | ensLoss |   0.9978 |  -5.7975 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.8099 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0324 |  -2.5281 | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -9.2818 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -10.1405 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9676 |  -2.5281 | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -9.2818 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -10.1405 | greater       |

#### CIFAR24 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR24',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8233 | 0.7258 |  0.8387 |    0.8877 |
| ('test_acc', 'std')  | 0.005  | 0.0062 |  0.0031 |    0.0028 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9033 | 0.8024 |  0.9092 |    0.9492 |
| ('test_auc', 'std')  | 0.0049 | 0.0066 |  0.0029 |    0.0016 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -22.51   | less          |
|  6 | Hinge | ensLoss |        0 | -32.8496 | less          |
|  9 | EXP   | ensLoss |        0 | -18.9965 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -22.51   | greater       |
|  6 | Hinge | ensLoss |        1 | -32.8496 | greater       |
|  9 | EXP   | ensLoss |        1 | -18.9965 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -11.4238 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -12.7722 | less          |
|  9 | EXP   | ensLoss |   0      | -19.9654 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -11.4238 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -12.7722 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.9654 | greater       |

#### CIFAR29 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR29',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9378 | 0.9085 |  0.9349 |    0.9564 |
| ('test_acc', 'std')  | 0.0025 | 0.0035 |  0.0018 |    0.0018 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9842 | 0.9693 |  0.9825 |    0.9911 |
| ('test_auc', 'std')  | 0.0007 | 0.0011 |  0.0006 |    0.0007 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0041 |  -4.8829 | less          |
|  6 | Hinge | ensLoss |   0.0006 |  -8.083  | less          |
|  9 | EXP   | ensLoss |   0      | -17.1951 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9959 |  -4.8829 | greater       |
|  6 | Hinge | ensLoss |   0.9994 |  -8.083  | greater       |
|  9 | EXP   | ensLoss |   1      | -17.1951 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0012 |  -6.8994 | less          |
|  6 | Hinge | ensLoss |   0      | -16.6022 | less          |
|  9 | EXP   | ensLoss |   0      | -33.4401 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9988 |  -6.8994 | greater       |
|  6 | Hinge | ensLoss |   1      | -16.6022 | greater       |
|  9 | EXP   | ensLoss |   1      | -33.4401 | greater       |

#### CIFAR25 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR25',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8063 | 0.703  |  0.8045 |    0.8314 |
| ('test_acc', 'std')  | 0.0034 | 0.0041 |  0.0025 |    0.0018 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8892 | 0.7762 |  0.8674 |    0.899  |
| ('test_auc', 'std')  | 0.0034 | 0.0047 |  0.0024 |    0.0027 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0018 |  -6.0948 | less          |
|  6 | Hinge | ensLoss |   0      | -20.4222 | less          |
|  9 | EXP   | ensLoss |   0      | -31.7448 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9982 |  -6.0948 | greater       |
|  6 | Hinge | ensLoss |   1      | -20.4222 | greater       |
|  9 | EXP   | ensLoss |   1      | -31.7448 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0315 |  -2.554  | less          |
|  6 | Hinge | ensLoss |   0      | -16.3417 | less          |
|  9 | EXP   | ensLoss |   0      | -18.9902 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9685 |  -2.554  | greater       |
|  6 | Hinge | ensLoss |   1      | -16.3417 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.9902 | greater       |

#### CIFAR25 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR25',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8556 | 0.7722 |  0.862  |    0.8882 |
| ('test_acc', 'std')  | 0.0024 | 0.0033 |  0.0029 |    0.0024 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9286 | 0.8554 |  0.9319 |    0.9518 |
| ('test_auc', 'std')  | 0.0026 | 0.0024 |  0.0016 |    0.0015 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -27.454  | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -9.3871 | less          |
|  9 | EXP   | ensLoss |   0      | -21.9122 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -27.454  | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -9.3871 | greater       |
|  9 | EXP   | ensLoss |   1      | -21.9122 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0004 |  -8.8688 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.7449 | less          |
|  9 | EXP   | ensLoss |   0      | -28.5922 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9996 |  -8.8688 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.7449 | greater       |
|  9 | EXP   | ensLoss |   1      | -28.5922 | greater       |

#### CIFAR26 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR26',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8577 | 0.7732 |  0.856  |    0.8674 |
| ('test_acc', 'std')  | 0.0026 | 0.002  |  0.0047 |    0.0029 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9286 | 0.8537 |  0.9151 |    0.9338 |
| ('test_auc', 'std')  | 0.0035 | 0.0013 |  0.0055 |    0.0018 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0171 |  -3.1613 | less          |
|  6 | Hinge | ensLoss |   0.0239 |  -2.8206 | less          |
|  9 | EXP   | ensLoss |   0      | -34.7698 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9829 |  -3.1613 | greater       |
|  6 | Hinge | ensLoss |   0.9761 |  -2.8206 | greater       |
|  9 | EXP   | ensLoss |   1      | -34.7698 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.06   |  -1.9706 | less          |
|  6 | Hinge | ensLoss |   0.0054 |  -4.5083 | less          |
|  9 | EXP   | ensLoss |   0      | -33.9871 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.94   |  -1.9706 | greater       |
|  6 | Hinge | ensLoss |   0.9946 |  -4.5083 | greater       |
|  9 | EXP   | ensLoss |   1      | -33.9871 | greater       |

#### CIFAR29 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR29',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9324 | 0.7755 |  0.9302 |    0.9508 |
| ('test_acc', 'std')  | 0.0027 | 0.0115 |  0.0025 |    0.0019 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9812 | 0.8546 |  0.9796 |    0.9892 |
| ('test_auc', 'std')  | 0.001  | 0.0098 |  0.0011 |    0.0007 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0013 |  -6.6591 | less          |
|  6 | Hinge | ensLoss |   0.0016 |  -6.3694 | less          |
|  9 | EXP   | ensLoss |   0      | -15.8667 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9987 |  -6.6591 | greater       |
|  6 | Hinge | ensLoss |   0.9984 |  -6.3694 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.8667 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0011 |  -6.967  | less          |
|  6 | Hinge | ensLoss |   0.0008 |  -7.6229 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.9034 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9989 |  -6.967  | greater       |
|  6 | Hinge | ensLoss |   0.9992 |  -7.6229 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.9034 | greater       |

#### CIFAR34 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR34',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8173 | 0.749  |  0.8241 |    0.8364 |
| ('test_acc', 'std')  | 0.0036 | 0.0037 |  0.0014 |    0.0037 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9015 | 0.828  |  0.897  |    0.9174 |
| ('test_auc', 'std')  | 0.0032 | 0.0024 |  0.0014 |    0.0027 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.001  |  -7.1009 | less          |
|  6 | Hinge | ensLoss |   0.0258 |  -2.7459 | less          |
|  9 | EXP   | ensLoss |   0      | -15.6697 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.999  |  -7.1009 | greater       |
|  6 | Hinge | ensLoss |   0.9742 |  -2.7459 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.6697 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0206 |  -2.9692 | less          |
|  6 | Hinge | ensLoss |   0.0025 |  -5.5774 | less          |
|  9 | EXP   | ensLoss |   0      | -23.5178 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9794 |  -2.9692 | greater       |
|  6 | Hinge | ensLoss |   0.9975 |  -5.5774 | greater       |
|  9 | EXP   | ensLoss |   1      | -23.5178 | greater       |

#### CIFAR05 - model: DenseNet169 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR05',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet169'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9686 | 0.9585 |  0.9667 |    0.9786 |
| ('test_acc', 'std')  | 0.0012 | 0.0013 |  0.0015 |    0.0007 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9954 | 0.9925 |  0.9944 |    0.9963 |
| ('test_auc', 'std')  | 0.0003 | 0.0003 |  0.0001 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0008 |  -7.7267 | less          |
|  6 | Hinge | ensLoss |   0.0011 |  -7.0061 | less          |
|  9 | EXP   | ensLoss |   0      | -16.3571 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9992 |  -7.7267 | greater       |
|  6 | Hinge | ensLoss |   0.9989 |  -7.0061 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.3571 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0355 | -2.4425 | less          |
|  6 | Hinge | ensLoss |   0.0044 | -4.7912 | less          |
|  9 | EXP   | ensLoss |   0.001  | -7.0847 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9645 | -2.4425 | greater       |
|  6 | Hinge | ensLoss |   0.9956 | -4.7912 | greater       |
|  9 | EXP   | ensLoss |   0.999  | -7.0847 | greater       |

#### CIFAR26 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR26',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8686 | 0.8044 |  0.8759 |    0.9055 |
| ('test_acc', 'std')  | 0.0024 | 0.0042 |  0.002  |    0.0017 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.942  | 0.8848 |  0.9442 |    0.9636 |
| ('test_auc', 'std')  | 0.0024 | 0.0026 |  0.0009 |    0.0013 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -11.8878 | less          |
|  6 | Hinge | ensLoss |   0      | -26.9091 | less          |
|  9 | EXP   | ensLoss |   0      | -24.335  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -11.8878 | greater       |
|  6 | Hinge | ensLoss |   1      | -26.9091 | greater       |
|  9 | EXP   | ensLoss |   1      | -24.335  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -15.7954 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -14.5214 | less          |
|  9 | EXP   | ensLoss |   0      | -22.6585 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -15.7954 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -14.5214 | greater       |
|  9 | EXP   | ensLoss |   1      | -22.6585 | greater       |

#### CIFAR27 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR27',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8608 | 0.7628 |  0.8583 |    0.8933 |
| ('test_acc', 'std')  | 0.0032 | 0.0023 |  0.0033 |    0.0025 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9352 | 0.8475 |  0.9246 |    0.9467 |
| ('test_auc', 'std')  | 0.0023 | 0.003  |  0.004  |    0.0023 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0022 |  -5.7724 | less          |
|  6 | Hinge | ensLoss |   0      | -16.2747 | less          |
|  9 | EXP   | ensLoss |   0      | -49.5908 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9978 |  -5.7724 | greater       |
|  6 | Hinge | ensLoss |   1      | -16.2747 | greater       |
|  9 | EXP   | ensLoss |   1      | -49.5908 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0345 |  -2.4691 | less          |
|  6 | Hinge | ensLoss |   0.0056 |  -4.4477 | less          |
|  9 | EXP   | ensLoss |   0      | -29.8894 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9655 |  -2.4691 | greater       |
|  6 | Hinge | ensLoss |   0.9944 |  -4.4477 | greater       |
|  9 | EXP   | ensLoss |   1      | -29.8894 | greater       |

#### CIFAR34 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR34',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8083 | 0.7631 |  0.8161 |    0.8311 |
| ('test_acc', 'std')  | 0.0044 | 0.002  |  0.0024 |    0.0012 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8898 | 0.8431 |  0.8892 |    0.912  |
| ('test_auc', 'std')  | 0.0026 | 0.0034 |  0.0018 |    0.0014 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0052 |  -4.5564 | less          |
|  6 | Hinge | ensLoss |   0.0025 |  -5.5805 | less          |
|  9 | EXP   | ensLoss |   0      | -29.8201 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9948 |  -4.5564 | greater       |
|  6 | Hinge | ensLoss |   0.9975 |  -5.5805 | greater       |
|  9 | EXP   | ensLoss |   1      | -29.8201 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.6808 | less          |
|  6 | Hinge | ensLoss |   0.0003 | -10.1997 | less          |
|  9 | EXP   | ensLoss |   0      | -21.1088 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.6808 | greater       |
|  6 | Hinge | ensLoss |   0.9997 | -10.1997 | greater       |
|  9 | EXP   | ensLoss |   1      | -21.1088 | greater       |

#### CIFAR27 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR27',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8851 | 0.8101 |  0.8905 |    0.9181 |
| ('test_acc', 'std')  | 0.003  | 0.0034 |  0.0017 |    0.0016 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9566 | 0.8892 |  0.9586 |    0.975  |
| ('test_auc', 'std')  | 0.0012 | 0.0036 |  0.0004 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0009 |  -7.3153 | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -9.1069 | less          |
|  9 | EXP   | ensLoss |   0      | -35.3671 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9991 |  -7.3153 | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -9.1069 | greater       |
|  9 | EXP   | ensLoss |   1      | -35.3671 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -13.7107 | less          |
|  6 | Hinge | ensLoss |   0      | -33.074  | less          |
|  9 | EXP   | ensLoss |   0      | -23.5928 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -13.7107 | greater       |
|  6 | Hinge | ensLoss |   1      | -33.074  | greater       |
|  9 | EXP   | ensLoss |   1      | -23.5928 | greater       |

#### CIFAR28 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR28',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9289 | 0.887  |  0.9309 |    0.9502 |
| ('test_acc', 'std')  | 0.0024 | 0.0017 |  0.0024 |    0.0023 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9809 | 0.9544 |  0.9787 |    0.9837 |
| ('test_auc', 'std')  | 0.0004 | 0.001  |  0.0012 |    0.001  |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0009 |  -7.4315 | less          |
|  6 | Hinge | ensLoss |   0.0008 |  -7.6201 | less          |
|  9 | EXP   | ensLoss |   0      | -19.2401 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9991 |  -7.4315 | greater       |
|  6 | Hinge | ensLoss |   0.9992 |  -7.6201 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.2401 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0392 |  -2.3518 | less          |
|  6 | Hinge | ensLoss |   0.0034 |  -5.1216 | less          |
|  9 | EXP   | ensLoss |   0      | -15.5639 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9608 |  -2.3518 | greater       |
|  6 | Hinge | ensLoss |   0.9966 |  -5.1216 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.5639 | greater       |

#### CIFAR34 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR34',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8074 | 0.6693 |  0.814  |    0.8246 |
| ('test_acc', 'std')  | 0.0024 | 0.003  |  0.0037 |    0.0022 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8902 | 0.734  |  0.8786 |    0.9053 |
| ('test_auc', 'std')  | 0.0013 | 0.0016 |  0.003  |    0.0022 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0053 |  -4.5224 | less          |
|  6 | Hinge | ensLoss |   0.0369 |  -2.406  | less          |
|  9 | EXP   | ensLoss |   0      | -32.1284 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9947 |  -4.5224 | greater       |
|  6 | Hinge | ensLoss |   0.9631 |  -2.406  | greater       |
|  9 | EXP   | ensLoss |   1      | -32.1284 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0042 |  -4.8459 | less          |
|  6 | Hinge | ensLoss |   0.0003 | -10.1656 | less          |
|  9 | EXP   | ensLoss |   0      | -50.3355 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9958 |  -4.8459 | greater       |
|  6 | Hinge | ensLoss |   0.9997 | -10.1656 | greater       |
|  9 | EXP   | ensLoss |   1      | -50.3355 | greater       |

#### CIFAR06 - model: DenseNet121 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR06',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet121'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9708 | 0.9662 |  0.9695 |    0.9842 |
| ('test_acc', 'std')  | 0.0015 | 0.0019 |  0.0014 |    0.001  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9949 | 0.9932 |  0.9951 |    0.9976 |
| ('test_auc', 'std')  | 0.0003 | 0.0003 |  0.0003 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0007 | -7.8892 | less          |
|  6 | Hinge | ensLoss |   0.0007 | -7.7855 | less          |
|  9 | EXP   | ensLoss |   0.0009 | -7.458  | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9993 | -7.8892 | greater       |
|  6 | Hinge | ensLoss |   0.9993 | -7.7855 | greater       |
|  9 | EXP   | ensLoss |   0.9991 | -7.458  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -12.897  | less          |
|  6 | Hinge | ensLoss |   0.0023 |  -5.7546 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.9246 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -12.897  | greater       |
|  6 | Hinge | ensLoss |   0.9977 |  -5.7546 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.9246 | greater       |

#### CIFAR28 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR28',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9474 | 0.9171 |  0.9474 |    0.9682 |
| ('test_acc', 'std')  | 0.0027 | 0.0027 |  0.0019 |    0.0021 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9884 | 0.9739 |  0.9877 |    0.9942 |
| ('test_auc', 'std')  | 0.0006 | 0.0007 |  0.0005 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0024 |  -5.6737 | less          |
|  6 | Hinge | ensLoss |   0.0013 |  -6.6992 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.3475 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9976 |  -5.6737 | greater       |
|  6 | Hinge | ensLoss |   0.9987 |  -6.6992 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.3475 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -13.7236 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -11.5655 | less          |
|  9 | EXP   | ensLoss |   0      | -21.0527 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -13.7236 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -11.5655 | greater       |
|  9 | EXP   | ensLoss |   1      | -21.0527 | greater       |

#### CIFAR35 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR35',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.6894 | 0.601  |  0.7039 |    0.7203 |
| ('test_acc', 'std')  | 0.0045 | 0.0044 |  0.0037 |    0.0071 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.7597 | 0.6439 |  0.7602 |    0.7924 |
| ('test_auc', 'std')  | 0.0044 | 0.0052 |  0.0032 |    0.0109 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0058 |  -4.4172 | less          |
|  6 | Hinge | ensLoss |   0.0511 |  -2.1118 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.9502 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9942 |  -4.4172 | greater       |
|  6 | Hinge | ensLoss |   0.9489 |  -2.1118 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.9502 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0275 |  -2.6848 | less          |
|  6 | Hinge | ensLoss |   0.0115 |  -3.5882 | less          |
|  9 | EXP   | ensLoss |   0      | -15.2304 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9725 |  -2.6848 | greater       |
|  6 | Hinge | ensLoss |   0.9885 |  -3.5882 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.2304 | greater       |

#### CIFAR29 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR29',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9411 | 0.8899 |  0.9364 |    0.9596 |
| ('test_acc', 'std')  | 0.0021 | 0.0031 |  0.0025 |    0.0008 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9863 | 0.9566 |  0.9825 |    0.9893 |
| ('test_auc', 'std')  | 0.0004 | 0.0009 |  0.0014 |    0.0009 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0007 |  -7.7658 | less          |
|  6 | Hinge | ensLoss |   0.0005 |  -8.8225 | less          |
|  9 | EXP   | ensLoss |   0      | -22.8987 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9993 |  -7.7658 | greater       |
|  6 | Hinge | ensLoss |   0.9995 |  -8.8225 | greater       |
|  9 | EXP   | ensLoss |   1      | -22.8987 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0202 |  -2.9867 | less          |
|  6 | Hinge | ensLoss |   0.0005 |  -8.7017 | less          |
|  9 | EXP   | ensLoss |   0      | -28.4971 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9798 |  -2.9867 | greater       |
|  6 | Hinge | ensLoss |   0.9995 |  -8.7017 | greater       |
|  9 | EXP   | ensLoss |   1      | -28.4971 | greater       |

#### CIFAR35 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR35',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.6759 | 0.6157 |  0.6757 |    0.7204 |
| ('test_acc', 'std')  | 0.0035 | 0.0056 |  0.0028 |    0.0035 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.7396 | 0.6552 |  0.7437 |    0.794  |
| ('test_auc', 'std')  | 0.0029 | 0.006  |  0.0023 |    0.0031 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.2905 | less          |
|  6 | Hinge | ensLoss |   0      | -16.4154 | less          |
|  9 | EXP   | ensLoss |   0      | -32.288  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.2905 | greater       |
|  6 | Hinge | ensLoss |   1      | -16.4154 | greater       |
|  9 | EXP   | ensLoss |   1      | -32.288  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -15.0664 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -13.9492 | less          |
|  9 | EXP   | ensLoss |   0      | -30.7331 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -15.0664 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -13.9492 | greater       |
|  9 | EXP   | ensLoss |   1      | -30.7331 | greater       |

#### CIFAR29 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR29',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9611 | 0.9298 |  0.9638 |    0.9772 |
| ('test_acc', 'std')  | 0.0024 | 0.0045 |  0.0032 |    0.0012 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9938 | 0.9806 |  0.9933 |    0.9965 |
| ('test_auc', 'std')  | 0.0004 | 0.0012 |  0.0007 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0013 | -6.6367 | less          |
|  6 | Hinge | ensLoss |   0.0048 | -4.6624 | less          |
|  9 | EXP   | ensLoss |   0.0004 | -8.9924 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9987 | -6.6367 | greater       |
|  6 | Hinge | ensLoss |   0.9952 | -4.6624 | greater       |
|  9 | EXP   | ensLoss |   0.9996 | -8.9924 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0074 |  -4.1015 | less          |
|  6 | Hinge | ensLoss |   0.0166 |  -3.1879 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.3563 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9926 |  -4.1015 | greater       |
|  6 | Hinge | ensLoss |   0.9834 |  -3.1879 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.3563 | greater       |

#### CIFAR34 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR34',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8051 | 0.7173 |  0.8031 |    0.8308 |
| ('test_acc', 'std')  | 0.0029 | 0.0056 |  0.0041 |    0.0022 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8876 | 0.7878 |  0.8713 |    0.8994 |
| ('test_auc', 'std')  | 0.0025 | 0.0045 |  0.0024 |    0.0031 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0024 |  -5.6741 | less          |
|  6 | Hinge | ensLoss |   0.001  |  -7.2519 | less          |
|  9 | EXP   | ensLoss |   0      | -20.3035 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9976 |  -5.6741 | greater       |
|  6 | Hinge | ensLoss |   0.999  |  -7.2519 | greater       |
|  9 | EXP   | ensLoss |   1      | -20.3035 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0426 |  -2.2759 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -13.1568 | less          |
|  9 | EXP   | ensLoss |   0      | -17.0368 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9574 |  -2.2759 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -13.1568 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.0368 | greater       |

#### CIFAR34 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR34',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8469 | 0.7652 |  0.8502 |    0.8849 |
| ('test_acc', 'std')  | 0.0018 | 0.0054 |  0.0042 |    0.0024 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9252 | 0.8471 |  0.9223 |    0.9497 |
| ('test_auc', 'std')  | 0.0014 | 0.0047 |  0.0027 |    0.002  |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -17.5749 | less          |
|  6 | Hinge | ensLoss |   0.0028 |  -5.3985 | less          |
|  9 | EXP   | ensLoss |   0      | -19.2315 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -17.5749 | greater       |
|  6 | Hinge | ensLoss |   0.9972 |  -5.3985 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.2315 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |    0     | -24.1891 | less          |
|  6 | Hinge | ensLoss |    0.001 |  -7.2475 | less          |
|  9 | EXP   | ensLoss |    0     | -19.694  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |    1     | -24.1891 | greater       |
|  6 | Hinge | ensLoss |    0.999 |  -7.2475 | greater       |
|  9 | EXP   | ensLoss |    1     | -19.694  | greater       |

#### CIFAR06 - model: DenseNet169 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR06',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet169'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9728 | 0.9658 |  0.9703 |    0.984  |
| ('test_acc', 'std')  | 0.0008 | 0.0013 |  0.0015 |    0.0012 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9955 | 0.9935 |  0.9949 |    0.9974 |
| ('test_auc', 'std')  | 0.0003 | 0.0003 |  0.0003 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0006 | -8.2567 | less          |
|  6 | Hinge | ensLoss |   0.0017 | -6.2272 | less          |
|  9 | EXP   | ensLoss |   0.0005 | -8.7363 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9994 | -8.2567 | greater       |
|  6 | Hinge | ensLoss |   0.9983 | -6.2272 | greater       |
|  9 | EXP   | ensLoss |   0.9995 | -8.7363 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0019 |  -6.0098 | less          |
|  6 | Hinge | ensLoss |   0.0024 |  -5.6891 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.4856 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9981 |  -6.0098 | greater       |
|  6 | Hinge | ensLoss |   0.9976 |  -5.6891 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.4856 | greater       |

#### CIFAR35 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR35',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.6732 | 0.5357 |  0.6712 |    0.7007 |
| ('test_acc', 'std')  | 0.0023 | 0.0041 |  0.0032 |    0.009  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.7335 | 0.5488 |  0.6861 |    0.766  |
| ('test_auc', 'std')  | 0.0024 | 0.0034 |  0.0066 |    0.0087 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0328 |  -2.5167 | less          |
|  6 | Hinge | ensLoss |   0.018  |  -3.1074 | less          |
|  9 | EXP   | ensLoss |   0      | -16.2995 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9672 |  -2.5167 | greater       |
|  6 | Hinge | ensLoss |   0.982  |  -3.1074 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.2995 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0174 |  -3.1391 | less          |
|  6 | Hinge | ensLoss |   0.0017 |  -6.1975 | less          |
|  9 | EXP   | ensLoss |   0      | -20.1019 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9826 |  -3.1391 | greater       |
|  6 | Hinge | ensLoss |   0.9983 |  -6.1975 | greater       |
|  9 | EXP   | ensLoss |   1      | -20.1019 | greater       |

#### CIFAR35 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR35',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.6677 | 0.5589 |  0.6766 |    0.6998 |
| ('test_acc', 'std')  | 0.0038 | 0.0076 |  0.0046 |    0.0048 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.7312 | 0.5851 |  0.7396 |    0.7661 |
| ('test_auc', 'std')  | 0.0043 | 0.0079 |  0.006  |    0.0055 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0018 |  -6.1118 | less          |
|  6 | Hinge | ensLoss |   0.0291 |  -2.6308 | less          |
|  9 | EXP   | ensLoss |   0      | -20.7949 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9982 |  -6.1118 | greater       |
|  6 | Hinge | ensLoss |   0.9709 |  -2.6308 | greater       |
|  9 | EXP   | ensLoss |   1      | -20.7949 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0065 |  -4.2704 | less          |
|  6 | Hinge | ensLoss |   0.0197 |  -3.0152 | less          |
|  9 | EXP   | ensLoss |   0      | -37.4026 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9935 |  -4.2704 | greater       |
|  6 | Hinge | ensLoss |   0.9803 |  -3.0152 | greater       |
|  9 | EXP   | ensLoss |   1      | -37.4026 | greater       |

#### CIFAR36 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR36',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8503 | 0.7676 |  0.8588 |    0.8648 |
| ('test_acc', 'std')  | 0.0039 | 0.0039 |  0.0017 |    0.005  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9274 | 0.8428 |  0.9301 |    0.9356 |
| ('test_auc', 'std')  | 0.0018 | 0.0028 |  0.0013 |    0.0047 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0794 |  -1.7294 | less          |
|  6 | Hinge | ensLoss |   0.1114 |  -1.4415 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.2276 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9206 |  -1.7294 | greater       |
|  6 | Hinge | ensLoss |   0.8886 |  -1.4415 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.2276 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.1106 |  -1.4475 | less          |
|  6 | Hinge | ensLoss |   0.1661 |  -1.1024 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.331  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.8894 |  -1.4475 | greater       |
|  6 | Hinge | ensLoss |   0.8339 |  -1.1024 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.331  | greater       |

#### CIFAR35 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR35',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.7334 | 0.6294 |  0.7345 |     0.784 |
| ('test_acc', 'std')  | 0.005  | 0.0049 |  0.0045 |     0.007 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.8129 | 0.6753 |  0.8131 |    0.8622 |
| ('test_auc', 'std')  | 0.0043 | 0.005  |  0.0033 |    0.0061 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 | -10.0828 | less          |
|  6 | Hinge | ensLoss |   0.0005 |  -8.4397 | less          |
|  9 | EXP   | ensLoss |   0      | -18.8895 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 | -10.0828 | greater       |
|  6 | Hinge | ensLoss |   0.9995 |  -8.4397 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.8895 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -11.5084 | less          |
|  6 | Hinge | ensLoss |   0.0008 |  -7.6541 | less          |
|  9 | EXP   | ensLoss |   0      | -25.4952 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -11.5084 | greater       |
|  6 | Hinge | ensLoss |   0.9992 |  -7.6541 | greater       |
|  9 | EXP   | ensLoss |   1      | -25.4952 | greater       |

#### CIFAR36 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR36',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8488 | 0.7492 |  0.8458 |    0.8629 |
| ('test_acc', 'std')  | 0.003  | 0.0087 |  0.0036 |    0.0022 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9239 | 0.8263 |  0.9123 |    0.929  |
| ('test_auc', 'std')  | 0.0012 | 0.0078 |  0.0022 |    0.0012 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0012 |  -6.8115 | less          |
|  6 | Hinge | ensLoss |   0.0139 |  -3.3823 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.7228 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9988 |  -6.8115 | greater       |
|  6 | Hinge | ensLoss |   0.9861 |  -3.3823 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.7228 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0078 |  -4.0333 | less          |
|  6 | Hinge | ensLoss |   0.004  |  -4.8994 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.0167 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9922 |  -4.0333 | greater       |
|  6 | Hinge | ensLoss |   0.996  |  -4.8994 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.0167 | greater       |

#### CIFAR36 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR36',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8408 | 0.7627 |  0.8485 |    0.8648 |
| ('test_acc', 'std')  | 0.0026 | 0.0027 |  0.0019 |    0.0026 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9234 | 0.8501 |  0.9222 |    0.9397 |
| ('test_auc', 'std')  | 0.0011 | 0.0019 |  0.0018 |    0.0017 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0011 |  -7.0695 | less          |
|  6 | Hinge | ensLoss |   0.0065 |  -4.2601 | less          |
|  9 | EXP   | ensLoss |   0      | -56.5478 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9989 |  -7.0695 | greater       |
|  6 | Hinge | ensLoss |   0.9935 |  -4.2601 | greater       |
|  9 | EXP   | ensLoss |   1      | -56.5478 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.001  |  -7.1539 | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -9.2352 | less          |
|  9 | EXP   | ensLoss |   0      | -37.1227 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.999  |  -7.1539 | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -9.2352 | greater       |
|  9 | EXP   | ensLoss |   1      | -37.1227 | greater       |

#### CIFAR07 - model: DenseNet121 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR07',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet121'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9634 | 0.9526 |  0.9619 |    0.9766 |
| ('test_acc', 'std')  | 0.0008 | 0.0016 |  0.0015 |    0.0008 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9936 | 0.9893 |  0.9941 |    0.9975 |
| ('test_auc', 'std')  | 0.0004 | 0.0001 |  0.0003 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -14.1927 | less          |
|  6 | Hinge | ensLoss |   0.0005 |  -8.8007 | less          |
|  9 | EXP   | ensLoss |   0      | -19.7613 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -14.1927 | greater       |
|  6 | Hinge | ensLoss |   0.9995 |  -8.8007 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.7613 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.6064 | less          |
|  6 | Hinge | ensLoss |   0.0009 |  -7.4375 | less          |
|  9 | EXP   | ensLoss |   0      | -49.2023 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.6064 | greater       |
|  6 | Hinge | ensLoss |   0.9991 |  -7.4375 | greater       |
|  9 | EXP   | ensLoss |   1      | -49.2023 | greater       |

#### CIFAR36 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR36',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8636 | 0.8056 |  0.8735 |    0.8981 |
| ('test_acc', 'std')  | 0.0032 | 0.0017 |  0.0017 |    0.0014 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9351 | 0.8867 |  0.9392 |    0.9565 |
| ('test_auc', 'std')  | 0.0024 | 0.0022 |  0.0015 |    0.0018 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -14.1734 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.6256 | less          |
|  9 | EXP   | ensLoss |   0      | -37.3754 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -14.1734 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.6256 | greater       |
|  9 | EXP   | ensLoss |   1      | -37.3754 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |    0.002 |  -5.9789 | less          |
|  6 | Hinge | ensLoss |    0     | -16.9281 | less          |
|  9 | EXP   | ensLoss |    0     | -20.9497 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |    0.998 |  -5.9789 | greater       |
|  6 | Hinge | ensLoss |    1     | -16.9281 | greater       |
|  9 | EXP   | ensLoss |    1     | -20.9497 | greater       |

#### CIFAR37 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR37',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8412 | 0.7268 |  0.8451 |    0.8729 |
| ('test_acc', 'std')  | 0.0023 | 0.0074 |  0.0013 |    0.0027 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9148 | 0.798  |  0.9116 |    0.9372 |
| ('test_auc', 'std')  | 0.002  | 0.0105 |  0.001  |    0.0026 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0011 |  -7.0636 | less          |
|  6 | Hinge | ensLoss |   0.0005 |  -8.741  | less          |
|  9 | EXP   | ensLoss |   0      | -27.5196 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9989 |  -7.0636 | greater       |
|  6 | Hinge | ensLoss |   0.9995 |  -8.741  | greater       |
|  9 | EXP   | ensLoss |   1      | -27.5196 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -11.6605 | less          |
|  6 | Hinge | ensLoss |   0.0006 |  -8.1389 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.3235 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -11.6605 | greater       |
|  6 | Hinge | ensLoss |   0.9994 |  -8.1389 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.3235 | greater       |

#### CIFAR36 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR36',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8375 | 0.6605 |  0.8403 |    0.8612 |
| ('test_acc', 'std')  | 0.0026 | 0.0046 |  0.0033 |    0.0051 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9158 | 0.7254 |  0.8965 |    0.9325 |
| ('test_auc', 'std')  | 0.002  | 0.0052 |  0.0036 |    0.0026 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0044 |  -4.7794 | less          |
|  6 | Hinge | ensLoss |   0.0293 |  -2.6231 | less          |
|  9 | EXP   | ensLoss |   0      | -21.6654 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9956 |  -4.7794 | greater       |
|  6 | Hinge | ensLoss |   0.9707 |  -2.6231 | greater       |
|  9 | EXP   | ensLoss |   1      | -21.6654 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0038 |  -4.9709 | less          |
|  6 | Hinge | ensLoss |   0.0007 |  -7.8327 | less          |
|  9 | EXP   | ensLoss |   0      | -28.7286 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9962 |  -4.9709 | greater       |
|  6 | Hinge | ensLoss |   0.9993 |  -7.8327 | greater       |
|  9 | EXP   | ensLoss |   1      | -28.7286 | greater       |

#### CIFAR37 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR37',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8802 | 0.7969 |  0.8763 |    0.9094 |
| ('test_acc', 'std')  | 0.0021 | 0.0034 |  0.0027 |    0.0019 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9515 | 0.8731 |  0.948  |    0.9683 |
| ('test_auc', 'std')  | 0.0016 | 0.0042 |  0.0007 |    0.0006 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0006 |  -8.2376 | less          |
|  6 | Hinge | ensLoss |   0.0005 |  -8.5082 | less          |
|  9 | EXP   | ensLoss |   0      | -23.2193 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9994 |  -8.2376 | greater       |
|  6 | Hinge | ensLoss |   0.9995 |  -8.5082 | greater       |
|  9 | EXP   | ensLoss |   1      | -23.2193 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 | -10.2279 | less          |
|  6 | Hinge | ensLoss |   0      | -53.9739 | less          |
|  9 | EXP   | ensLoss |   0      | -25.8843 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 | -10.2279 | greater       |
|  6 | Hinge | ensLoss |   1      | -53.9739 | greater       |
|  9 | EXP   | ensLoss |   1      | -25.8843 | greater       |

#### CIFAR37 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR37',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8691 | 0.7615 |  0.8687 |    0.8886 |
| ('test_acc', 'std')  | 0.0028 | 0.0031 |  0.0025 |    0.0051 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9437 | 0.8404 |  0.9328 |    0.9569 |
| ('test_auc', 'std')  | 0.0021 | 0.0025 |  0.0014 |    0.0026 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0198 |  -3.0107 | less          |
|  6 | Hinge | ensLoss |   0.0038 |  -4.9851 | less          |
|  9 | EXP   | ensLoss |   0      | -53.9025 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9802 |  -3.0107 | greater       |
|  6 | Hinge | ensLoss |   0.9962 |  -4.9851 | greater       |
|  9 | EXP   | ensLoss |   1      | -53.9025 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0077 |  -4.0553 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -13.8208 | less          |
|  9 | EXP   | ensLoss |   0      | -52.7865 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9923 |  -4.0553 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -13.8208 | greater       |
|  9 | EXP   | ensLoss |   1      | -52.7865 | greater       |

#### CIFAR38 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR38',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9385 | 0.9092 |  0.9392 |    0.9506 |
| ('test_acc', 'std')  | 0.0012 | 0.004  |  0.0013 |    0.0019 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.983  | 0.9687 |  0.9835 |    0.9839 |
| ('test_auc', 'std')  | 0.0008 | 0.0009 |  0.0007 |    0.0011 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0009 | -7.3844 | less          |
|  6 | Hinge | ensLoss |   0.0024 | -5.6404 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -9.6033 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9991 | -7.3844 | greater       |
|  6 | Hinge | ensLoss |   0.9976 | -5.6404 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -9.6033 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.2695 | -0.671  | less          |
|  6 | Hinge | ensLoss |   0.4178 | -0.2214 | less          |
|  9 | EXP   | ensLoss |   0.0005 | -8.4791 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.7305 | -0.671  | greater       |
|  6 | Hinge | ensLoss |   0.5822 | -0.2214 | greater       |
|  9 | EXP   | ensLoss |   0.9995 | -8.4791 | greater       |

#### CIFAR37 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR37',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8558 | 0.7587 |  0.8525 |    0.8867 |
| ('test_acc', 'std')  | 0.0021 | 0.0041 |  0.0031 |    0.0044 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9284 | 0.8394 |  0.9246 |    0.9532 |
| ('test_auc', 'std')  | 0.0013 | 0.0032 |  0.0013 |    0.0029 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0024 |  -5.6906 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.572  | less          |
|  9 | EXP   | ensLoss |   0      | -20.1257 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9976 |  -5.6906 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.572  | greater       |
|  9 | EXP   | ensLoss |   1      | -20.1257 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0004 |  -9.2548 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -11.4249 | less          |
|  9 | EXP   | ensLoss |   0      | -27.4554 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9996 |  -9.2548 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -11.4249 | greater       |
|  9 | EXP   | ensLoss |   1      | -27.4554 | greater       |

#### CIFAR38 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR38',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9507 | 0.9289 |  0.9505 |    0.9646 |
| ('test_acc', 'std')  | 0.0012 | 0.0029 |  0.0014 |    0.0013 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9886 | 0.98   |  0.9892 |    0.9916 |
| ('test_auc', 'std')  | 0.0004 | 0.0008 |  0.0005 |    0.0005 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -19.0036 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -13.0916 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.2993 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -19.0036 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -13.0916 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.2993 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0058 |  -4.4163 | less          |
|  6 | Hinge | ensLoss |   0.0305 |  -2.5858 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.9847 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9942 |  -4.4163 | greater       |
|  6 | Hinge | ensLoss |   0.9695 |  -2.5858 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.9847 | greater       |

#### CIFAR07 - model: DenseNet169 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR07',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet169'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9618 | 0.9504 |  0.9655 |    0.9762 |
| ('test_acc', 'std')  | 0.0013 | 0.0018 |  0.0007 |    0.0014 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9937 | 0.9877 |  0.9944 |    0.9973 |
| ('test_auc', 'std')  | 0.0004 | 0.0006 |  0.0004 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 | -10.2208 | less          |
|  6 | Hinge | ensLoss |   0.0028 |  -5.4251 | less          |
|  9 | EXP   | ensLoss |   0.0006 |  -8.2352 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 | -10.2208 | greater       |
|  6 | Hinge | ensLoss |   0.9972 |  -5.4251 | greater       |
|  9 | EXP   | ensLoss |   0.9994 |  -8.2352 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0014 |  -6.5695 | less          |
|  6 | Hinge | ensLoss |   0.0027 |  -5.4887 | less          |
|  9 | EXP   | ensLoss |   0      | -21.2275 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9986 |  -6.5695 | greater       |
|  6 | Hinge | ensLoss |   0.9973 |  -5.4887 | greater       |
|  9 | EXP   | ensLoss |   1      | -21.2275 | greater       |

#### CIFAR39 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR39',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9328 | 0.888  |  0.9291 |    0.9461 |
| ('test_acc', 'std')  | 0.0022 | 0.0025 |  0.0022 |    0.002  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9814 | 0.9535 |  0.9775 |    0.9796 |
| ('test_auc', 'std')  | 0.001  | 0.0015 |  0.0017 |    0.0013 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0051 |  -4.578  | less          |
|  6 | Hinge | ensLoss |   0.0015 |  -6.3912 | less          |
|  9 | EXP   | ensLoss |   0      | -16.3938 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9949 |  -4.578  | greater       |
|  6 | Hinge | ensLoss |   0.9985 |  -6.3912 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.3938 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9208 |   1.7321 | less          |
|  6 | Hinge | ensLoss |   0.2286 |  -0.8222 | less          |
|  9 | EXP   | ensLoss |   0      | -18.7642 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0792 |   1.7321 | greater       |
|  6 | Hinge | ensLoss |   0.7714 |  -0.8222 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.7642 | greater       |

#### CIFAR37 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR37',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8442 | 0.6002 |  0.8469 |     0.887 |
| ('test_acc', 'std')  | 0.0048 | 0.0051 |  0.0041 |     0.002 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9221 | 0.6365 |  0.9097 |    0.9508 |
| ('test_auc', 'std')  | 0.0026 | 0.0057 |  0.0025 |    0.0025 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0005 |  -8.5489 | less          |
|  6 | Hinge | ensLoss |   0      | -17.122  | less          |
|  9 | EXP   | ensLoss |   0      | -74.2    | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9995 |  -8.5489 | greater       |
|  6 | Hinge | ensLoss |   1      | -17.122  | greater       |
|  9 | EXP   | ensLoss |   1      | -74.2    | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0016 |  -6.3348 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -11.1672 | less          |
|  9 | EXP   | ensLoss |   0      | -78.8685 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9984 |  -6.3348 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -11.1672 | greater       |
|  9 | EXP   | ensLoss |   1      | -78.8685 | greater       |

#### CIFAR39 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR39',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9501 | 0.918  |  0.9521 |    0.9693 |
| ('test_acc', 'std')  | 0.0015 | 0.0029 |  0.0029 |    0.0011 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9888 | 0.9729 |  0.9888 |    0.9936 |
| ('test_auc', 'std')  | 0.0011 | 0.0016 |  0.0009 |    0.0008 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -13.4426 | less          |
|  6 | Hinge | ensLoss |   0.0005 |  -8.5573 | less          |
|  9 | EXP   | ensLoss |   0      | -19.7234 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -13.4426 | greater       |
|  6 | Hinge | ensLoss |   0.9995 |  -8.5573 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.7234 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0076 |  -4.0674 | less          |
|  6 | Hinge | ensLoss |   0.0015 |  -6.4652 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.7964 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9924 |  -4.0674 | greater       |
|  6 | Hinge | ensLoss |   0.9985 |  -6.4652 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.7964 | greater       |

#### CIFAR45 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR45',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8345 | 0.7474 |  0.8433 |    0.8653 |
| ('test_acc', 'std')  | 0.0036 | 0.0019 |  0.0017 |    0.0027 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9113 | 0.8305 |  0.9002 |    0.9273 |
| ('test_auc', 'std')  | 0.0032 | 0.0018 |  0.0014 |    0.0033 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0016 |  -6.3549 | less          |
|  6 | Hinge | ensLoss |   0.0003 |  -9.5561 | less          |
|  9 | EXP   | ensLoss |   0      | -33.6034 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9984 |  -6.3549 | greater       |
|  6 | Hinge | ensLoss |   0.9997 |  -9.5561 | greater       |
|  9 | EXP   | ensLoss |   1      | -33.6034 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0196 |  -3.017  | less          |
|  6 | Hinge | ensLoss |   0.0008 |  -7.7405 | less          |
|  9 | EXP   | ensLoss |   0      | -23.1904 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9804 |  -3.017  | greater       |
|  6 | Hinge | ensLoss |   0.9992 |  -7.7405 | greater       |
|  9 | EXP   | ensLoss |   1      | -23.1904 | greater       |

#### CIFAR38 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR38',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9473 | 0.9145 |  0.9484 |    0.9566 |
| ('test_acc', 'std')  | 0.0016 | 0.0029 |  0.0013 |    0.0005 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9862 | 0.9733 |  0.9869 |    0.9884 |
| ('test_auc', 'std')  | 0.0006 | 0.0015 |  0.0004 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0046 |  -4.7002 | less          |
|  6 | Hinge | ensLoss |   0.0026 |  -5.5097 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.7606 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9954 |  -4.7002 | greater       |
|  6 | Hinge | ensLoss |   0.9974 |  -5.5097 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.7606 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0101 |  -3.733  | less          |
|  6 | Hinge | ensLoss |   0.021  |  -2.949  | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.4957 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9899 |  -3.733  | greater       |
|  6 | Hinge | ensLoss |   0.979  |  -2.949  | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.4957 | greater       |

#### CIFAR45 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR45',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8689 | 0.7918 |  0.8787 |    0.9098 |
| ('test_acc', 'std')  | 0.0026 | 0.0046 |  0.0016 |    0.0024 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9364 | 0.8763 |  0.9447 |    0.9641 |
| ('test_auc', 'std')  | 0.0021 | 0.004  |  0.0013 |    0.0017 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 | -10.2059 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -13.3709 | less          |
|  9 | EXP   | ensLoss |   0      | -47.106  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 | -10.2059 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -13.3709 | greater       |
|  9 | EXP   | ensLoss |   1      | -47.106  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0005 |  -8.6284 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -12.3936 | less          |
|  9 | EXP   | ensLoss |   0      | -24.6679 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9995 |  -8.6284 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -12.3936 | greater       |
|  9 | EXP   | ensLoss |   1      | -24.6679 | greater       |

#### CIFAR08 - model: DenseNet121 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR08',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet121'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9333 | 0.8817 |  0.9378 |    0.9565 |
| ('test_acc', 'std')  | 0.0023 | 0.0009 |  0.0032 |    0.001  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9817 | 0.9517 |  0.9835 |    0.9896 |
| ('test_auc', 'std')  | 0.0011 | 0.0007 |  0.001  |    0.0006 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0009 |  -7.4625 | less          |
|  6 | Hinge | ensLoss |   0.001  |  -7.2164 | less          |
|  9 | EXP   | ensLoss |   0      | -52.3707 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9991 |  -7.4625 | greater       |
|  6 | Hinge | ensLoss |   0.999  |  -7.2164 | greater       |
|  9 | EXP   | ensLoss |   1      | -52.3707 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 | -10.2214 | less          |
|  6 | Hinge | ensLoss |   0.0054 |  -4.5022 | less          |
|  9 | EXP   | ensLoss |   0      | -37.4334 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 | -10.2214 | greater       |
|  6 | Hinge | ensLoss |   0.9946 |  -4.5022 | greater       |
|  9 | EXP   | ensLoss |   1      | -37.4334 | greater       |

#### CIFAR38 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR38',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9435 | 0.9131 |  0.9414 |    0.9453 |
| ('test_acc', 'std')  | 0.0009 | 0.0013 |  0.0013 |    0.0013 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9837 | 0.9715 |  0.9843 |    0.9866 |
| ('test_auc', 'std')  | 0.0006 | 0.0009 |  0.0006 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.1342 |  -1.2841 | less          |
|  6 | Hinge | ensLoss |   0.0586 |  -1.9915 | less          |
|  9 | EXP   | ensLoss |   0      | -15.7779 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.8658 |  -1.2841 | greater       |
|  6 | Hinge | ensLoss |   0.9414 |  -1.9915 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.7779 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |    0.006 |  -4.3636 | less          |
|  6 | Hinge | ensLoss |    0.001 |  -7.1025 | less          |
|  9 | EXP   | ensLoss |    0     | -16.3971 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |    0.994 |  -4.3636 | greater       |
|  6 | Hinge | ensLoss |    0.999 |  -7.1025 | greater       |
|  9 | EXP   | ensLoss |    1     | -16.3971 | greater       |

#### CIFAR46 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR46',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8637 | 0.7335 |  0.8615 |    0.8999 |
| ('test_acc', 'std')  | 0.0027 | 0.0027 |  0.0033 |    0.0013 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9372 | 0.8078 |  0.9299 |    0.9555 |
| ('test_auc', 'std')  | 0.0021 | 0.0033 |  0.0032 |    0.0014 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.7736 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -14.2762 | less          |
|  9 | EXP   | ensLoss |   0      | -84.6956 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.7736 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -14.2762 | greater       |
|  9 | EXP   | ensLoss |   1      | -84.6956 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0016 |  -6.3428 | less          |
|  6 | Hinge | ensLoss |   0.0008 |  -7.604  | less          |
|  9 | EXP   | ensLoss |   0      | -60.8407 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9984 |  -6.3428 | greater       |
|  6 | Hinge | ensLoss |   0.9992 |  -7.604  | greater       |
|  9 | EXP   | ensLoss |   1      | -60.8407 | greater       |

#### CIFAR46 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR46',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8887 | 0.8051 |  0.8926 |    0.9378 |
| ('test_acc', 'std')  | 0.0013 | 0.0019 |  0.0015 |    0.0016 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9565 | 0.8851 |  0.9598 |    0.9821 |
| ('test_auc', 'std')  | 0.0004 | 0.0022 |  0.001  |    0.0006 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -21.6676 | less          |
|  6 | Hinge | ensLoss |        0 | -20.084  | less          |
|  9 | EXP   | ensLoss |        0 | -48.0879 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -21.6676 | greater       |
|  6 | Hinge | ensLoss |        1 | -20.084  | greater       |
|  9 | EXP   | ensLoss |        1 | -48.0879 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -26.6915 | less          |
|  6 | Hinge | ensLoss |        0 | -22.7468 | less          |
|  9 | EXP   | ensLoss |        0 | -45.1403 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -26.6915 | greater       |
|  6 | Hinge | ensLoss |        1 | -22.7468 | greater       |
|  9 | EXP   | ensLoss |        1 | -45.1403 | greater       |

#### CIFAR38 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR38',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9424 | 0.7853 |  0.935  |    0.9454 |
| ('test_acc', 'std')  | 0.0015 | 0.0086 |  0.0028 |    0.0009 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9838 | 0.8718 |  0.9825 |    0.9855 |
| ('test_auc', 'std')  | 0.0007 | 0.0108 |  0.0013 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.1288 |  -1.3188 | less          |
|  6 | Hinge | ensLoss |   0.0038 |  -4.9665 | less          |
|  9 | EXP   | ensLoss |   0      | -18.2587 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.8712 |  -1.3188 | greater       |
|  6 | Hinge | ensLoss |   0.9962 |  -4.9665 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.2587 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0616 |  -1.948  | less          |
|  6 | Hinge | ensLoss |   0.0355 |  -2.4436 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.4517 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9384 |  -1.948  | greater       |
|  6 | Hinge | ensLoss |   0.9645 |  -2.4436 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.4517 | greater       |

#### CIFAR47 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR47',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |   BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.824 | 0.7399 |  0.8259 |    0.8647 |
| ('test_acc', 'std')  | 0.003 | 0.0018 |  0.0014 |    0.0011 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9038 | 0.8162 |  0.8855 |    0.9296 |
| ('test_auc', 'std')  | 0.0012 | 0.0019 |  0.0008 |    0.0017 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -17.952  | less          |
|  6 | Hinge | ensLoss |        0 | -20.2673 | less          |
|  9 | EXP   | ensLoss |        0 | -79.895  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -17.952  | greater       |
|  6 | Hinge | ensLoss |        1 | -20.2673 | greater       |
|  9 | EXP   | ensLoss |        1 | -79.895  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -12.8435 | less          |
|  6 | Hinge | ensLoss |   0      | -25.0695 | less          |
|  9 | EXP   | ensLoss |   0      | -41.6245 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -12.8435 | greater       |
|  6 | Hinge | ensLoss |   1      | -25.0695 | greater       |
|  9 | EXP   | ensLoss |   1      | -41.6245 | greater       |

#### CIFAR39 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR39',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9293 | 0.8876 |  0.9312 |    0.9487 |
| ('test_acc', 'std')  | 0.0015 | 0.0047 |  0.0006 |    0.0017 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9818 | 0.9538 |  0.9803 |    0.9857 |
| ('test_auc', 'std')  | 0.0008 | 0.003  |  0.0011 |    0.0007 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -11.0452 | less          |
|  6 | Hinge | ensLoss |   0.0007 |  -7.8856 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.4759 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -11.0452 | greater       |
|  6 | Hinge | ensLoss |   0.9993 |  -7.8856 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.4759 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.004  |  -4.9128 | less          |
|  6 | Hinge | ensLoss |   0.0106 |  -3.6809 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -11.1359 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.996  |  -4.9128 | greater       |
|  6 | Hinge | ensLoss |   0.9894 |  -3.6809 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -11.1359 | greater       |

#### CIFAR47 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR47',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8657 | 0.7673 |  0.8725 |    0.9177 |
| ('test_acc', 'std')  | 0.0033 | 0.0045 |  0.002  |    0.0019 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9378 | 0.8457 |  0.942  |    0.9748 |
| ('test_auc', 'std')  | 0.003  | 0.0061 |  0.0014 |    0.0007 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -20.8001 | less          |
|  6 | Hinge | ensLoss |        0 | -17.5741 | less          |
|  9 | EXP   | ensLoss |        0 | -30.1646 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -20.8001 | greater       |
|  6 | Hinge | ensLoss |        1 | -17.5741 | greater       |
|  9 | EXP   | ensLoss |        1 | -30.1646 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.765  | less          |
|  6 | Hinge | ensLoss |   0      | -21.2784 | less          |
|  9 | EXP   | ensLoss |   0      | -19.2974 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.765  | greater       |
|  6 | Hinge | ensLoss |   1      | -21.2784 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.2974 | greater       |

#### CIFAR08 - model: DenseNet169 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR08',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet169'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.936  | 0.8768 |  0.9387 |    0.959  |
| ('test_acc', 'std')  | 0.0004 | 0.0037 |  0.0028 |    0.0013 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.983  | 0.9484 |  0.9838 |    0.989  |
| ('test_auc', 'std')  | 0.0005 | 0.0018 |  0.0011 |    0.0005 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -17.6402 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.985  | less          |
|  9 | EXP   | ensLoss |   0      | -18.2599 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -17.6402 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.985  | greater       |
|  9 | EXP   | ensLoss |   1      | -18.2599 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0006 |  -8.3622 | less          |
|  6 | Hinge | ensLoss |   0.004  |  -4.9122 | less          |
|  9 | EXP   | ensLoss |   0      | -19.6102 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9994 |  -8.3622 | greater       |
|  6 | Hinge | ensLoss |   0.996  |  -4.9122 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.6102 | greater       |

#### CIFAR48 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR48',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9531 | 0.9032 |  0.9471 |    0.9624 |
| ('test_acc', 'std')  | 0.0016 | 0.0018 |  0.0011 |    0.0017 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9878 | 0.9677 |  0.9857 |    0.9906 |
| ('test_auc', 'std')  | 0.0007 | 0.0013 |  0.0004 |    0.001  |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0164 |  -3.2012 | less          |
|  6 | Hinge | ensLoss |   0.0007 |  -7.9114 | less          |
|  9 | EXP   | ensLoss |   0      | -24.8179 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9836 |  -3.2012 | greater       |
|  6 | Hinge | ensLoss |   0.9993 |  -7.9114 | greater       |
|  9 | EXP   | ensLoss |   1      | -24.8179 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0776 |  -1.7492 | less          |
|  6 | Hinge | ensLoss |   0.0019 |  -6.0554 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.8193 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9224 |  -1.7492 | greater       |
|  6 | Hinge | ensLoss |   0.9981 |  -6.0554 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.8193 | greater       |

#### CIFAR39 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR39',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9297 | 0.8943 |  0.9283 |    0.9415 |
| ('test_acc', 'std')  | 0.0005 | 0.0035 |  0.0013 |    0.0044 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9791 | 0.9612 |  0.9758 |    0.9858 |
| ('test_auc', 'std')  | 0.0008 | 0.0018 |  0.0005 |    0.0017 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.023  | -2.8607 | less          |
|  6 | Hinge | ensLoss |   0.0173 | -3.1473 | less          |
|  9 | EXP   | ensLoss |   0.0004 | -8.8663 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.977  | -2.8607 | greater       |
|  6 | Hinge | ensLoss |   0.9827 | -3.1473 | greater       |
|  9 | EXP   | ensLoss |   0.9996 | -8.8663 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0071 | -4.1526 | less          |
|  6 | Hinge | ensLoss |   0.0022 | -5.8188 | less          |
|  9 | EXP   | ensLoss |   0.0004 | -8.8311 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9929 | -4.1526 | greater       |
|  6 | Hinge | ensLoss |   0.9978 | -5.8188 | greater       |
|  9 | EXP   | ensLoss |   0.9996 | -8.8311 | greater       |

#### CIFAR48 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR48',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9631 | 0.9368 |  0.9629 |    0.9766 |
| ('test_acc', 'std')  | 0.0006 | 0.0012 |  0.0017 |    0.0021 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9926 | 0.9841 |  0.9936 |    0.9968 |
| ('test_auc', 'std')  | 0.0002 | 0.0007 |  0.0002 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0009 |  -7.4035 | less          |
|  6 | Hinge | ensLoss |   0.0079 |  -4.0286 | less          |
|  9 | EXP   | ensLoss |   0      | -17.4284 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9991 |  -7.4035 | greater       |
|  6 | Hinge | ensLoss |   0.9921 |  -4.0286 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.4284 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 | -10.1984 | less          |
|  6 | Hinge | ensLoss |   0.0015 |  -6.4101 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -15.0983 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 | -10.1984 | greater       |
|  6 | Hinge | ensLoss |   0.9985 |  -6.4101 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -15.0983 | greater       |

#### CIFAR49 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR49',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9434 | 0.9002 |  0.9434 |    0.9626 |
| ('test_acc', 'std')  | 0.0026 | 0.0032 |  0.0017 |    0.0027 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9862 | 0.9629 |  0.9859 |    0.9888 |
| ('test_auc', 'std')  | 0.0007 | 0.0013 |  0.0015 |    0.0009 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0045 |  -4.7498 | less          |
|  6 | Hinge | ensLoss |   0.0007 |  -7.8945 | less          |
|  9 | EXP   | ensLoss |   0      | -33.5465 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9955 |  -4.7498 | greater       |
|  6 | Hinge | ensLoss |   0.9993 |  -7.8945 | greater       |
|  9 | EXP   | ensLoss |   1      | -33.5465 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0523 |  -2.092  | less          |
|  6 | Hinge | ensLoss |   0.0662 |  -1.8862 | less          |
|  9 | EXP   | ensLoss |   0      | -41.1872 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9477 |  -2.092  | greater       |
|  6 | Hinge | ensLoss |   0.9338 |  -1.8862 | greater       |
|  9 | EXP   | ensLoss |   1      | -41.1872 | greater       |

#### CIFAR39 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR39',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9228 | 0.7463 |  0.9121 |    0.9423 |
| ('test_acc', 'std')  | 0.0017 | 0.0113 |  0.0012 |    0.0032 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9759 | 0.8217 |  0.9676 |    0.9856 |
| ('test_auc', 'std')  | 0.0008 | 0.009  |  0.0017 |    0.0018 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0039 |  -4.9332 | less          |
|  6 | Hinge | ensLoss |   0.0008 |  -7.5583 | less          |
|  9 | EXP   | ensLoss |   0      | -16.1975 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9961 |  -4.9332 | greater       |
|  6 | Hinge | ensLoss |   0.9992 |  -7.5583 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.1975 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0029 |  -5.3708 | less          |
|  6 | Hinge | ensLoss |   0.0028 |  -5.435  | less          |
|  9 | EXP   | ensLoss |   0      | -17.744  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9971 |  -5.3708 | greater       |
|  6 | Hinge | ensLoss |   0.9972 |  -5.435  | greater       |
|  9 | EXP   | ensLoss |   1      | -17.744  | greater       |

#### CIFAR49 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR49',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9631 | 0.9274 |  0.9624 |    0.9823 |
| ('test_acc', 'std')  | 0.0017 | 0.004  |  0.0014 |    0.0011 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9937 | 0.9796 |  0.9942 |    0.9979 |
| ('test_auc', 'std')  | 0.0006 | 0.0017 |  0.0002 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -12.4849 | less          |
|  6 | Hinge | ensLoss |   0.0003 |  -9.9687 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.1105 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -12.4849 | greater       |
|  6 | Hinge | ensLoss |   0.9997 |  -9.9687 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.1105 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0004 |  -9.4254 | less          |
|  6 | Hinge | ensLoss |   0      | -15.8238 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -10.0688 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9996 |  -9.4254 | greater       |
|  6 | Hinge | ensLoss |   1      | -15.8238 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -10.0688 | greater       |

#### CIFAR45 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR45',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8434 | 0.7661 |  0.8491 |    0.8718 |
| ('test_acc', 'std')  | 0.0044 | 0.0034 |  0.0031 |    0.0039 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9195 | 0.8472 |  0.9167 |    0.9413 |
| ('test_auc', 'std')  | 0.0021 | 0.0024 |  0.0039 |    0.0034 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |    0.006 |  -4.3752 | less          |
|  6 | Hinge | ensLoss |    0.01  |  -3.7438 | less          |
|  9 | EXP   | ensLoss |    0     | -15.2462 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |    0.994 |  -4.3752 | greater       |
|  6 | Hinge | ensLoss |    0.99  |  -3.7438 | greater       |
|  9 | EXP   | ensLoss |    1     | -15.2462 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0028 |  -5.4018 | less          |
|  6 | Hinge | ensLoss |   0.0051 |  -4.5856 | less          |
|  9 | EXP   | ensLoss |   0      | -18.2934 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9972 |  -5.4018 | greater       |
|  6 | Hinge | ensLoss |   0.9949 |  -4.5856 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.2934 | greater       |

#### CIFAR09 - model: DenseNet121 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR09',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet121'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9547 | 0.9328 |  0.9513 |    0.9726 |
| ('test_acc', 'std')  | 0.001  | 0.0012 |  0.0019 |    0.0017 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9912 | 0.9824 |  0.9907 |    0.9954 |
| ('test_auc', 'std')  | 0.0003 | 0.0007 |  0.0003 |    0.0005 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0007 |  -7.9971 | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -8.9294 | less          |
|  9 | EXP   | ensLoss |   0      | -42.793  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9993 |  -7.9971 | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -8.9294 | greater       |
|  9 | EXP   | ensLoss |   1      | -42.793  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0016 |  -6.3193 | less          |
|  6 | Hinge | ensLoss |   0.002  |  -5.9402 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.1255 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9984 |  -6.3193 | greater       |
|  6 | Hinge | ensLoss |   0.998  |  -5.9402 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.1255 | greater       |

#### CIFAR56 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR56',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8958 | 0.8164 |  0.8925 |    0.9134 |
| ('test_acc', 'std')  | 0.0014 | 0.0054 |  0.0037 |    0.003  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9592 | 0.8999 |  0.9568 |    0.9665 |
| ('test_auc', 'std')  | 0.001  | 0.0052 |  0.0019 |    0.0012 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0028 |  -5.416  | less          |
|  6 | Hinge | ensLoss |   0.0065 |  -4.2698 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -15.1489 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9972 |  -5.416  | greater       |
|  6 | Hinge | ensLoss |   0.9935 |  -4.2698 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -15.1489 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0024 |  -5.6584 | less          |
|  6 | Hinge | ensLoss |   0.0057 |  -4.4389 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.0742 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9976 |  -5.6584 | greater       |
|  6 | Hinge | ensLoss |   0.9943 |  -4.4389 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.0742 | greater       |

#### CIFAR45 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR45',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.826  | 0.785  |  0.8344 |    0.8692 |
| ('test_acc', 'std')  | 0.0015 | 0.0034 |  0.002  |    0.0024 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9089 | 0.8685 |  0.9086 |    0.9387 |
| ('test_auc', 'std')  | 0.0019 | 0.0028 |  0.0014 |    0.0031 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -24.0931 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -11.2375 | less          |
|  9 | EXP   | ensLoss |   0      | -29.2439 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -24.0931 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -11.2375 | greater       |
|  9 | EXP   | ensLoss |   1      | -29.2439 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -11.6341 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.8482 | less          |
|  9 | EXP   | ensLoss |   0      | -18.0163 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -11.6341 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.8482 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.0163 | greater       |

#### CIFAR56 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR56',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9171 | 0.8733 |  0.9192 |    0.9373 |
| ('test_acc', 'std')  | 0.003  | 0.0028 |  0.0031 |    0.0018 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9737 | 0.9441 |  0.9754 |    0.9822 |
| ('test_auc', 'std')  | 0.0013 | 0.0012 |  0.0009 |    0.0011 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0018 |  -6.1638 | less          |
|  6 | Hinge | ensLoss |   0.0037 |  -5.0181 | less          |
|  9 | EXP   | ensLoss |   0      | -16.0628 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9982 |  -6.1638 | greater       |
|  6 | Hinge | ensLoss |   0.9963 |  -5.0181 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.0628 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0052 |  -4.5634 | less          |
|  6 | Hinge | ensLoss |   0.0046 |  -4.7263 | less          |
|  9 | EXP   | ensLoss |   0      | -20.537  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9948 |  -4.5634 | greater       |
|  6 | Hinge | ensLoss |   0.9954 |  -4.7263 | greater       |
|  9 | EXP   | ensLoss |   1      | -20.537  | greater       |

#### CIFAR57 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR57',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8355 | 0.7225 |  0.8367 |    0.8678 |
| ('test_acc', 'std')  | 0.0019 | 0.0092 |  0.001  |    0.0043 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9112 | 0.7982 |  0.9086 |    0.928  |
| ('test_auc', 'std')  | 0.0008 | 0.0098 |  0.0018 |    0.0011 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0006 |  -8.0524 | less          |
|  6 | Hinge | ensLoss |   0.0005 |  -8.6222 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -11.0005 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9994 |  -8.0524 | greater       |
|  6 | Hinge | ensLoss |   0.9995 |  -8.6222 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -11.0005 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -14.1816 | less          |
|  6 | Hinge | ensLoss |   0.0008 |  -7.6451 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.827  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -14.1816 | greater       |
|  6 | Hinge | ensLoss |   0.9992 |  -7.6451 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.827  | greater       |

#### CIFAR57 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR57',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8597 | 0.7801 |  0.8627 |    0.8954 |
| ('test_acc', 'std')  | 0.0033 | 0.0065 |  0.0021 |    0.0041 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9328 | 0.8592 |  0.935  |    0.9578 |
| ('test_auc', 'std')  | 0.0015 | 0.0069 |  0.0017 |    0.0018 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0013 |  -6.7299 | less          |
|  6 | Hinge | ensLoss |   0.0014 |  -6.5056 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -11.8426 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9987 |  -6.7299 | greater       |
|  6 | Hinge | ensLoss |   0.9986 |  -6.5056 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -11.8426 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0006 |  -8.3147 | less          |
|  6 | Hinge | ensLoss |   0.0003 | -10.2319 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.2518 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9994 |  -8.3147 | greater       |
|  6 | Hinge | ensLoss |   0.9997 | -10.2319 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.2518 | greater       |

#### CIFAR45 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR45',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8278 | 0.7078 |  0.8287 |    0.8603 |
| ('test_acc', 'std')  | 0.002  | 0.0016 |  0.0035 |    0.0037 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9058 | 0.7861 |  0.8936 |    0.9306 |
| ('test_auc', 'std')  | 0.0014 | 0.0025 |  0.0046 |    0.0023 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0007 |  -7.7801 | less          |
|  6 | Hinge | ensLoss |   0.0022 |  -5.8097 | less          |
|  9 | EXP   | ensLoss |   0      | -40.0139 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9993 |  -7.7801 | greater       |
|  6 | Hinge | ensLoss |   0.9978 |  -5.8097 | greater       |
|  9 | EXP   | ensLoss |   1      | -40.0139 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0005 |  -8.7494 | less          |
|  6 | Hinge | ensLoss |   0.0007 |  -7.8638 | less          |
|  9 | EXP   | ensLoss |   0      | -65.0573 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9995 |  -8.7494 | greater       |
|  6 | Hinge | ensLoss |   0.9993 |  -7.8638 | greater       |
|  9 | EXP   | ensLoss |   1      | -65.0573 | greater       |

#### CIFAR58 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR58',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9525 | 0.9268 |  0.9537 |    0.9621 |
| ('test_acc', 'std')  | 0.0023 | 0.0034 |  0.0021 |    0.0015 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9908 | 0.9791 |  0.9896 |    0.9911 |
| ('test_auc', 'std')  | 0.0004 | 0.0012 |  0.0006 |    0.0009 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0023 |  -5.7016 | less          |
|  6 | Hinge | ensLoss |   0.0315 |  -2.5548 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.699  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9977 |  -5.7016 | greater       |
|  6 | Hinge | ensLoss |   0.9685 |  -2.5548 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.699  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.2911 |  -0.5979 | less          |
|  6 | Hinge | ensLoss |   0.0456 |  -2.2146 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -10.0102 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.7089 |  -0.5979 | greater       |
|  6 | Hinge | ensLoss |   0.9544 |  -2.2146 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -10.0102 | greater       |

#### CIFAR09 - model: DenseNet169 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR09',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet169'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9527 | 0.9295 |  0.9537 |    0.9684 |
| ('test_acc', 'std')  | 0.0009 | 0.0017 |  0.0007 |    0.0018 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9912 | 0.9833 |  0.9905 |    0.9952 |
| ('test_auc', 'std')  | 0.0005 | 0.0006 |  0.0003 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0018 |  -6.1043 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.9114 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.9643 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9982 |  -6.1043 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.9114 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.9643 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0005 |  -8.5154 | less          |
|  6 | Hinge | ensLoss |   0.0006 |  -8.199  | less          |
|  9 | EXP   | ensLoss |   0      | -45.5222 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9995 |  -8.5154 | greater       |
|  6 | Hinge | ensLoss |   0.9994 |  -8.199  | greater       |
|  9 | EXP   | ensLoss |   1      | -45.5222 | greater       |

#### CIFAR46 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR46',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8805 | 0.7519 |  0.8866 |    0.9159 |
| ('test_acc', 'std')  | 0.0039 | 0.0057 |  0.0029 |    0.0029 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9505 | 0.829  |  0.9548 |    0.9721 |
| ('test_auc', 'std')  | 0.0022 | 0.0067 |  0.0009 |    0.0005 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0018 |  -6.1336 | less          |
|  6 | Hinge | ensLoss |   0.0031 |  -5.2782 | less          |
|  9 | EXP   | ensLoss |   0      | -35.9594 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9982 |  -6.1336 | greater       |
|  6 | Hinge | ensLoss |   0.9969 |  -5.2782 | greater       |
|  9 | EXP   | ensLoss |   1      | -35.9594 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.6367 | less          |
|  6 | Hinge | ensLoss |   0      | -23.2091 | less          |
|  9 | EXP   | ensLoss |   0      | -20.386  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.6367 | greater       |
|  6 | Hinge | ensLoss |   1      | -23.2091 | greater       |
|  9 | EXP   | ensLoss |   1      | -20.386  | greater       |

#### CIFAR58 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR58',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9662 | 0.9498 |  0.9697 |    0.9773 |
| ('test_acc', 'std')  | 0.0019 | 0.0017 |  0.001  |    0.0012 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9946 | 0.989  |  0.9948 |    0.9971 |
| ('test_auc', 'std')  | 0.0007 | 0.0007 |  0.0004 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0032 |  -5.2413 | less          |
|  6 | Hinge | ensLoss |   0.0022 |  -5.7698 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.6994 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9968 |  -5.2413 | greater       |
|  6 | Hinge | ensLoss |   0.9978 |  -5.7698 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.6994 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0144 |  -3.3443 | less          |
|  6 | Hinge | ensLoss |   0.0042 |  -4.8294 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.1364 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9856 |  -3.3443 | greater       |
|  6 | Hinge | ensLoss |   0.9958 |  -4.8294 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.1364 | greater       |

#### CIFAR46 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR46',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8663 | 0.7295 |  0.8703 |    0.9101 |
| ('test_acc', 'std')  | 0.004  | 0.0043 |  0.0013 |    0.0019 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9431 | 0.803  |  0.943  |    0.9712 |
| ('test_auc', 'std')  | 0.0018 | 0.0036 |  0.0014 |    0.0014 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -13.1674 | less          |
|  6 | Hinge | ensLoss |   0      | -17.7284 | less          |
|  9 | EXP   | ensLoss |   0      | -30.2538 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -13.1674 | greater       |
|  6 | Hinge | ensLoss |   1      | -17.7284 | greater       |
|  9 | EXP   | ensLoss |   1      | -30.2538 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -28.4564 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -11.87   | less          |
|  9 | EXP   | ensLoss |   0      | -43.2868 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -28.4564 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -11.87   | greater       |
|  9 | EXP   | ensLoss |   1      | -43.2868 | greater       |

#### CIFAR59 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR59',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9435 | 0.9148 |  0.9449 |    0.9619 |
| ('test_acc', 'std')  | 0.002  | 0.005  |  0.0032 |    0.0011 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9861 | 0.9732 |  0.9867 |    0.9899 |
| ('test_auc', 'std')  | 0.0002 | 0.0009 |  0.0012 |    0.0012 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0014 | -6.5423 | less          |
|  6 | Hinge | ensLoss |   0.0036 | -5.0516 | less          |
|  9 | EXP   | ensLoss |   0.0004 | -8.9194 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9986 | -6.5423 | greater       |
|  6 | Hinge | ensLoss |   0.9964 | -5.0516 | greater       |
|  9 | EXP   | ensLoss |   0.9996 | -8.9194 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0163 |  -3.2117 | less          |
|  6 | Hinge | ensLoss |   0.0692 |  -1.8471 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.7817 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9837 |  -3.2117 | greater       |
|  6 | Hinge | ensLoss |   0.9308 |  -1.8471 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.7817 | greater       |

#### CIFAR59 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR59',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9676 | 0.9392 |  0.9617 |    0.9764 |
| ('test_acc', 'std')  | 0.0015 | 0.0024 |  0.0022 |    0.0016 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9947 | 0.9854 |  0.9934 |    0.9963 |
| ('test_auc', 'std')  | 0.0006 | 0.0006 |  0.0006 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0032 |  -5.245  | less          |
|  6 | Hinge | ensLoss |   0.0001 | -12.3578 | less          |
|  9 | EXP   | ensLoss |   0      | -16.2898 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9968 |  -5.245  | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -12.3578 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.2898 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0364 |  -2.4201 | less          |
|  6 | Hinge | ensLoss |   0.0055 |  -4.4873 | less          |
|  9 | EXP   | ensLoss |   0      | -15.2647 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9636 |  -2.4201 | greater       |
|  6 | Hinge | ensLoss |   0.9945 |  -4.4873 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.2647 | greater       |

#### CIFAR12 - model: DenseNet121 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR12',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet121'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9796 | 0.9709 |  0.9781 |    0.9892 |
| ('test_acc', 'std')  | 0.0007 | 0.0015 |  0.0007 |    0.0007 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9979 | 0.996  |  0.9979 |    0.9994 |
| ('test_auc', 'std')  | 0.0002 | 0.0001 |  0.0002 |    0.0001 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0005 |  -8.8188 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.5356 | less          |
|  9 | EXP   | ensLoss |   0.0005 |  -8.6363 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9995 |  -8.8188 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.5356 | greater       |
|  9 | EXP   | ensLoss |   0.9995 |  -8.6363 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.6187 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.4283 | less          |
|  9 | EXP   | ensLoss |   0      | -29.1162 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.6187 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.4283 | greater       |
|  9 | EXP   | ensLoss |   1      | -29.1162 | greater       |

#### CIFAR67 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR67',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9311 | 0.8429 |  0.9251 |    0.9585 |
| ('test_acc', 'std')  | 0.003  | 0.0049 |  0.003  |    0.0015 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9818 | 0.9187 |  0.9782 |    0.9897 |
| ('test_auc', 'std')  | 0.0007 | 0.0036 |  0.002  |    0.0005 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0009 |  -7.4615 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -15.0733 | less          |
|  9 | EXP   | ensLoss |   0      | -19.5581 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9991 |  -7.4615 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -15.0733 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.5581 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0006 |  -8.0885 | less          |
|  6 | Hinge | ensLoss |   0.0014 |  -6.6258 | less          |
|  9 | EXP   | ensLoss |   0      | -17.3323 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9994 |  -8.0885 | greater       |
|  6 | Hinge | ensLoss |   0.9986 |  -6.6258 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.3323 | greater       |

#### CIFAR46 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR46',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8657 | 0.5733 |  0.8503 |    0.9012 |
| ('test_acc', 'std')  | 0.002  | 0.0094 |  0.0028 |    0.0025 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9396 | 0.6063 |  0.9153 |    0.9622 |
| ('test_auc', 'std')  | 0.0022 | 0.0119 |  0.004  |    0.0013 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.7526 | less          |
|  6 | Hinge | ensLoss |   0.0003 |  -9.8258 | less          |
|  9 | EXP   | ensLoss |   0      | -36.4818 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.7526 | greater       |
|  6 | Hinge | ensLoss |   0.9997 |  -9.8258 | greater       |
|  9 | EXP   | ensLoss |   1      | -36.4818 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0009 |  -7.4579 | less          |
|  6 | Hinge | ensLoss |   0.0003 |  -9.6031 | less          |
|  9 | EXP   | ensLoss |   0      | -29.7226 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9991 |  -7.4579 | greater       |
|  6 | Hinge | ensLoss |   0.9997 |  -9.6031 | greater       |
|  9 | EXP   | ensLoss |   1      | -29.7226 | greater       |

#### CIFAR47 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR47',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8465 | 0.7671 |  0.8553 |    0.8834 |
| ('test_acc', 'std')  | 0.0022 | 0.0031 |  0.001  |    0.0045 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9268 | 0.8477 |  0.9292 |    0.9547 |
| ('test_auc', 'std')  | 0.0007 | 0.0031 |  0.0009 |    0.002  |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0004 |  -9.116  | less          |
|  6 | Hinge | ensLoss |   0.0028 |  -5.4219 | less          |
|  9 | EXP   | ensLoss |   0      | -35.5291 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9996 |  -9.116  | greater       |
|  6 | Hinge | ensLoss |   0.9972 |  -5.4219 | greater       |
|  9 | EXP   | ensLoss |   1      | -35.5291 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -13.0126 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -12.8985 | less          |
|  9 | EXP   | ensLoss |   0      | -35.2089 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -13.0126 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -12.8985 | greater       |
|  9 | EXP   | ensLoss |   1      | -35.2089 | greater       |

#### CIFAR67 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR67',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9521 | 0.9119 |  0.9481 |     0.972 |
| ('test_acc', 'std')  | 0.0024 | 0.0028 |  0.0028 |     0.002 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9901 | 0.9713 |  0.9888 |    0.9961 |
| ('test_auc', 'std')  | 0.0006 | 0.0009 |  0.0006 |    0.0006 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -12.4988 | less          |
|  6 | Hinge | ensLoss |   0.0021 |  -5.8954 | less          |
|  9 | EXP   | ensLoss |   0      | -19.3619 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -12.4988 | greater       |
|  6 | Hinge | ensLoss |   0.9979 |  -5.8954 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.3619 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -14.4434 | less          |
|  6 | Hinge | ensLoss |   0.001  |  -7.1009 | less          |
|  9 | EXP   | ensLoss |   0      | -19.3129 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -14.4434 | greater       |
|  6 | Hinge | ensLoss |   0.999  |  -7.1009 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.3129 | greater       |

#### CIFAR68 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR68',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9626 | 0.942  |  0.9673 |    0.9715 |
| ('test_acc', 'std')  | 0.0023 | 0.0026 |  0.0012 |    0.0012 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9935 | 0.9858 |  0.9937 |    0.9933 |
| ('test_auc', 'std')  | 0.0004 | 0.0012 |  0.0005 |    0.001  |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0237 | -2.8272 | less          |
|  6 | Hinge | ensLoss |   0.0153 | -3.2796 | less          |
|  9 | EXP   | ensLoss |   0.0004 | -9.3995 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9763 | -2.8272 | greater       |
|  6 | Hinge | ensLoss |   0.9847 | -3.2796 | greater       |
|  9 | EXP   | ensLoss |   0.9996 | -9.3995 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.5747 |  0.201  | less          |
|  6 | Hinge | ensLoss |   0.6428 |  0.3929 | less          |
|  9 | EXP   | ensLoss |   0.0051 | -4.5769 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.4253 |  0.201  | greater       |
|  6 | Hinge | ensLoss |   0.3572 |  0.3929 | greater       |
|  9 | EXP   | ensLoss |   0.9949 | -4.5769 | greater       |

#### CIFAR47 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR47',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8396 | 0.7736 |  0.8386 |    0.8742 |
| ('test_acc', 'std')  | 0.0016 | 0.0027 |  0.0038 |    0.004  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9152 | 0.8546 |  0.914  |    0.9465 |
| ('test_auc', 'std')  | 0.002  | 0.0017 |  0.0032 |    0.0014 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.7888 | less          |
|  6 | Hinge | ensLoss |   0.0025 |  -5.5985 | less          |
|  9 | EXP   | ensLoss |   0      | -20.4246 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.7888 | greater       |
|  6 | Hinge | ensLoss |   0.9975 |  -5.5985 | greater       |
|  9 | EXP   | ensLoss |   1      | -20.4246 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -26.8593 | less          |
|  6 | Hinge | ensLoss |   0.0005 |  -8.7531 | less          |
|  9 | EXP   | ensLoss |   0      | -40.4232 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -26.8593 | greater       |
|  6 | Hinge | ensLoss |   0.9995 |  -8.7531 | greater       |
|  9 | EXP   | ensLoss |   1      | -40.4232 | greater       |

#### CIFAR68 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR68',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9728 | 0.9618 |  0.972  |    0.9839 |
| ('test_acc', 'std')  | 0.0009 | 0.0013 |  0.0005 |    0.0011 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9963 | 0.9933 |  0.9964 |    0.9974 |
| ('test_auc', 'std')  | 0.0003 | 0.0005 |  0.0002 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0007 |  -7.8785 | less          |
|  6 | Hinge | ensLoss |   0.0005 |  -8.7847 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -11.2852 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9993 |  -7.8785 | greater       |
|  6 | Hinge | ensLoss |   0.9995 |  -8.7847 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -11.2852 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0619 | -1.9442 | less          |
|  6 | Hinge | ensLoss |   0.0626 | -1.9341 | less          |
|  9 | EXP   | ensLoss |   0.0034 | -5.1249 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9381 | -1.9442 | greater       |
|  6 | Hinge | ensLoss |   0.9374 | -1.9341 | greater       |
|  9 | EXP   | ensLoss |   0.9966 | -5.1249 | greater       |

#### CIFAR69 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR69',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |   EXP |   Hinge |   ensLoss |
|:---------------------|-------:|------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9648 | 0.916 |  0.9599 |    0.9744 |
| ('test_acc', 'std')  | 0.0011 | 0.003 |  0.0017 |    0.0011 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9941 | 0.9734 |  0.9921 |    0.9953 |
| ('test_auc', 'std')  | 0.0008 | 0.0015 |  0.0006 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0023 |  -5.7269 | less          |
|  6 | Hinge | ensLoss |   0.0033 |  -5.2002 | less          |
|  9 | EXP   | ensLoss |   0      | -19.7315 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9977 |  -5.7269 | greater       |
|  6 | Hinge | ensLoss |   0.9967 |  -5.2002 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.7315 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.1384 |  -1.2582 | less          |
|  6 | Hinge | ensLoss |   0.0037 |  -5.0085 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.6761 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.8616 |  -1.2582 | greater       |
|  6 | Hinge | ensLoss |   0.9963 |  -5.0085 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.6761 | greater       |

#### CIFAR12 - model: DenseNet169 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR12',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet169'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9779 | 0.9719 |  0.9781 |    0.9876 |
| ('test_acc', 'std')  | 0.0008 | 0.0015 |  0.0019 |    0.0013 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9975 | 0.9962 |  0.9981 |    0.9991 |
| ('test_auc', 'std')  | 0.0003 | 0.0002 |  0.0001 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0009 |  -7.3013 | less          |
|  6 | Hinge | ensLoss |   0.009  |  -3.8703 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -11.9021 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9991 |  -7.3013 | greater       |
|  6 | Hinge | ensLoss |   0.991  |  -3.8703 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -11.9021 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0017 | -6.2574 | less          |
|  6 | Hinge | ensLoss |   0.0197 | -3.0151 | less          |
|  9 | EXP   | ensLoss |   0.0005 | -8.7879 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9983 | -6.2574 | greater       |
|  6 | Hinge | ensLoss |   0.9803 | -3.0151 | greater       |
|  9 | EXP   | ensLoss |   0.9995 | -8.7879 | greater       |

#### CIFAR47 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR47',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8378 | 0.7308 |  0.8313 |    0.863  |
| ('test_acc', 'std')  | 0.0024 | 0.0022 |  0.0035 |    0.0072 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9134 | 0.806  |  0.8957 |    0.9346 |
| ('test_auc', 'std')  | 0.0017 | 0.0017 |  0.0031 |    0.0055 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0083 |  -3.9664 | less          |
|  6 | Hinge | ensLoss |   0.0009 |  -7.3721 | less          |
|  9 | EXP   | ensLoss |   0      | -19.214  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9917 |  -3.9664 | greater       |
|  6 | Hinge | ensLoss |   0.9991 |  -7.3721 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.214  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.006  |  -4.3587 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -11.5882 | less          |
|  9 | EXP   | ensLoss |   0      | -30.6621 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.994  |  -4.3587 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -11.5882 | greater       |
|  9 | EXP   | ensLoss |   1      | -30.6621 | greater       |

#### CIFAR69 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR69',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9737 | 0.96   |  0.9733 |    0.9859 |
| ('test_acc', 'std')  | 0.001  | 0.0019 |  0.0011 |    0.001  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9965 | 0.9926 |  0.9961 |    0.9984 |
| ('test_auc', 'std')  | 0.0002 | 0.0008 |  0.0004 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0009 |  -7.4733 | less          |
|  6 | Hinge | ensLoss |   0.0013 |  -6.7016 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -15.118  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9991 |  -7.4733 | greater       |
|  6 | Hinge | ensLoss |   0.9987 |  -6.7016 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -15.118  | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 | -9.847  | less          |
|  6 | Hinge | ensLoss |   0.006  | -4.3558 | less          |
|  9 | EXP   | ensLoss |   0.0004 | -9.0224 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 | -9.847  | greater       |
|  6 | Hinge | ensLoss |   0.994  | -4.3558 | greater       |
|  9 | EXP   | ensLoss |   0.9996 | -9.0224 | greater       |

#### CIFAR48 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR48',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9487 | 0.9112 |  0.9544 |    0.9689 |
| ('test_acc', 'std')  | 0.0018 | 0.0016 |  0.0014 |    0.0017 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9897 | 0.9709 |  0.9902 |    0.994  |
| ('test_auc', 'std')  | 0.0006 | 0.0009 |  0.0005 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0011 |  -6.9428 | less          |
|  6 | Hinge | ensLoss |   0.0038 |  -4.9955 | less          |
|  9 | EXP   | ensLoss |   0      | -23.8255 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9989 |  -6.9428 | greater       |
|  6 | Hinge | ensLoss |   0.9962 |  -4.9955 | greater       |
|  9 | EXP   | ensLoss |   1      | -23.8255 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0004 |  -8.9613 | less          |
|  6 | Hinge | ensLoss |   0.0007 |  -7.9495 | less          |
|  9 | EXP   | ensLoss |   0      | -25.015  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9996 |  -8.9613 | greater       |
|  6 | Hinge | ensLoss |   0.9993 |  -7.9495 | greater       |
|  9 | EXP   | ensLoss |   1      | -25.015  | greater       |

#### CIFAR78 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR78',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9529 | 0.911  |  0.9488 |    0.9635 |
| ('test_acc', 'std')  | 0.0017 | 0.0027 |  0.001  |    0.0012 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9894 | 0.9695 |  0.988  |    0.9913 |
| ('test_auc', 'std')  | 0.0003 | 0.0019 |  0.0005 |    0.0005 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0098 |  -3.7689 | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -9.4593 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.1325 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9902 |  -3.7689 | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -9.4593 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.1325 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0134 |  -3.4209 | less          |
|  6 | Hinge | ensLoss |   0.0012 |  -6.7938 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.8344 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9866 |  -3.4209 | greater       |
|  6 | Hinge | ensLoss |   0.9988 |  -6.7938 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.8344 | greater       |

#### CIFAR78 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR78',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9657 | 0.9448 |  0.9631 |    0.9821 |
| ('test_acc', 'std')  | 0.0011 | 0.0024 |  0.0018 |    0.0012 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9943 | 0.9869 |  0.9944 |    0.9979 |
| ('test_auc', 'std')  | 0.0004 | 0.001  |  0.0003 |    0.0001 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 |  -9.5729 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -12.8832 | less          |
|  9 | EXP   | ensLoss |   0      | -17.7519 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 |  -9.5729 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -12.8832 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.7519 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 |  -9.8636 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -12.1495 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.9388 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 |  -9.8636 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -12.1495 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.9388 | greater       |

#### CIFAR48 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR48',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9462 | 0.9203 |  0.9394 |    0.9619 |
| ('test_acc', 'std')  | 0.0011 | 0.0025 |  0.0018 |    0.0025 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9881 | 0.9749 |  0.9845 |    0.9923 |
| ('test_auc', 'std')  | 0.0007 | 0.0007 |  0.0007 |    0.0006 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.004  | -4.9003 | less          |
|  6 | Hinge | ensLoss |   0.0014 | -6.6205 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -9.823  | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.996  | -4.9003 | greater       |
|  6 | Hinge | ensLoss |   0.9986 | -6.6205 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -9.823  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0052 |  -4.5541 | less          |
|  6 | Hinge | ensLoss |   0.001  |  -7.2728 | less          |
|  9 | EXP   | ensLoss |   0      | -16.8833 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9948 |  -4.5541 | greater       |
|  6 | Hinge | ensLoss |   0.999  |  -7.2728 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.8833 | greater       |

#### CIFAR79 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR79',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9258 | 0.8655 |  0.9261 |    0.9518 |
| ('test_acc', 'std')  | 0.0018 | 0.0044 |  0.0031 |    0.002  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9786 | 0.9383 |  0.9771 |    0.9852 |
| ('test_auc', 'std')  | 0.0008 | 0.0029 |  0.0015 |    0.0005 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -14.3671 | less          |
|  6 | Hinge | ensLoss |   0.0011 |  -6.9396 | less          |
|  9 | EXP   | ensLoss |   0      | -16.1259 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -14.3671 | greater       |
|  6 | Hinge | ensLoss |   0.9989 |  -6.9396 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.1259 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -11.8667 | less          |
|  6 | Hinge | ensLoss |   0.0034 |  -5.1388 | less          |
|  9 | EXP   | ensLoss |   0      | -15.1762 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -11.8667 | greater       |
|  6 | Hinge | ensLoss |   0.9966 |  -5.1388 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.1762 | greater       |

#### CIFAR13 - model: DenseNet121 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR13',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet121'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9726 | 0.9638 |  0.9715 |    0.9841 |
| ('test_acc', 'std')  | 0.001  | 0.0009 |  0.0004 |    0.0007 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9974 | 0.9951 |  0.9968 |    0.9983 |
| ('test_auc', 'std')  | 0.0002 | 0.0002 |  0.0002 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0006 |  -8.1831 | less          |
|  6 | Hinge | ensLoss |   0      | -19.678  | less          |
|  9 | EXP   | ensLoss |   0      | -20.6648 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9994 |  -8.1831 | greater       |
|  6 | Hinge | ensLoss |   1      | -19.678  | greater       |
|  9 | EXP   | ensLoss |   1      | -20.6648 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0018 |  -6.1613 | less          |
|  6 | Hinge | ensLoss |   0.0085 |  -3.9332 | less          |
|  9 | EXP   | ensLoss |   0      | -19.7681 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9982 |  -6.1613 | greater       |
|  6 | Hinge | ensLoss |   0.9915 |  -3.9332 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.7681 | greater       |

#### CIFAR79 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR79',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.949  | 0.9064 |  0.9509 |    0.9762 |
| ('test_acc', 'std')  | 0.0025 | 0.0025 |  0.0014 |    0.0008 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9894 | 0.9672 |  0.9895 |    0.9962 |
| ('test_auc', 'std')  | 0.0003 | 0.0012 |  0.0003 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -13.4086 | less          |
|  6 | Hinge | ensLoss |   0      | -17.7136 | less          |
|  9 | EXP   | ensLoss |   0      | -25.633  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -13.4086 | greater       |
|  6 | Hinge | ensLoss |   1      | -17.7136 | greater       |
|  9 | EXP   | ensLoss |   1      | -25.633  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -14.7188 | less          |
|  6 | Hinge | ensLoss |   0      | -21.066  | less          |
|  9 | EXP   | ensLoss |   0      | -19.8647 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -14.7188 | greater       |
|  6 | Hinge | ensLoss |   1      | -21.066  | greater       |
|  9 | EXP   | ensLoss |   1      | -19.8647 | greater       |

#### CIFAR48 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR48',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9396 | 0.859  |  0.935  |    0.9549 |
| ('test_acc', 'std')  | 0.0016 | 0.0049 |  0.0022 |    0.0028 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.985  | 0.9247 |  0.9808 |    0.9907 |
| ('test_auc', 'std')  | 0.0006 | 0.0042 |  0.001  |    0.0005 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0049 |  -4.631  | less          |
|  6 | Hinge | ensLoss |   0.0048 |  -4.6698 | less          |
|  9 | EXP   | ensLoss |   0      | -17.8901 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9951 |  -4.631  | greater       |
|  6 | Hinge | ensLoss |   0.9952 |  -4.6698 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.8901 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -11.6881 | less          |
|  6 | Hinge | ensLoss |   0.0014 |  -6.558  | less          |
|  9 | EXP   | ensLoss |   0      | -15.6904 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -11.6881 | greater       |
|  6 | Hinge | ensLoss |   0.9986 |  -6.558  | greater       |
|  9 | EXP   | ensLoss |   1      | -15.6904 | greater       |

#### CIFAR89 - model: MobileNet ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR89',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNet'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9113 | 0.8312 |  0.9123 |    0.9388 |
| ('test_acc', 'std')  | 0.0028 | 0.0051 |  0.0012 |    0.0006 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9709 | 0.9109 |  0.9682 |    0.9778 |
| ('test_auc', 'std')  | 0.0013 | 0.0032 |  0.001  |    0.0007 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0005 |  -8.7846 | less          |
|  6 | Hinge | ensLoss |   0      | -16.9302 | less          |
|  9 | EXP   | ensLoss |   0      | -19.0854 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9995 |  -8.7846 | greater       |
|  6 | Hinge | ensLoss |   1      | -16.9302 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.0854 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.007  |  -4.1731 | less          |
|  6 | Hinge | ensLoss |   0.0006 |  -8.0318 | less          |
|  9 | EXP   | ensLoss |   0      | -18.9572 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.993  |  -4.1731 | greater       |
|  6 | Hinge | ensLoss |   0.9994 |  -8.0318 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.9572 | greater       |

#### CIFAR49 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR49',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9562 | 0.9102 |  0.9571 |    0.9642 |
| ('test_acc', 'std')  | 0.0017 | 0.0041 |  0.002  |    0.0012 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9911 | 0.97   |  0.991  |    0.9935 |
| ('test_auc', 'std')  | 0.0003 | 0.0017 |  0.0006 |    0.0006 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0103 |  -3.7099 | less          |
|  6 | Hinge | ensLoss |   0.0255 |  -2.7564 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.0111 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9897 |  -3.7099 | greater       |
|  6 | Hinge | ensLoss |   0.9745 |  -2.7564 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.0111 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0177 |  -3.126  | less          |
|  6 | Hinge | ensLoss |   0.0236 |  -2.835  | less          |
|  9 | EXP   | ensLoss |   0.0002 | -11.3444 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9823 |  -3.126  | greater       |
|  6 | Hinge | ensLoss |   0.9764 |  -2.835  | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -11.3444 | greater       |

#### CIFAR89 - model: MobileNetV2 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR89',
 'device': device(type='cuda', index=0),
 'model': {'net': 'MobileNetV2'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9381 | 0.8748 |  0.937  |    0.9567 |
| ('test_acc', 'std')  | 0.0027 | 0.0038 |  0.0017 |    0.0009 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9839 | 0.9475 |  0.9841 |    0.9897 |
| ('test_auc', 'std')  | 0.0007 | 0.0026 |  0.0009 |    0.0007 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0009 |  -7.3181 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -11.8473 | less          |
|  9 | EXP   | ensLoss |   0      | -20.6304 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9991 |  -7.3181 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -11.8473 | greater       |
|  9 | EXP   | ensLoss |   1      | -20.6304 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0006 |  -8.1793 | less          |
|  6 | Hinge | ensLoss |   0.0029 |  -5.3627 | less          |
|  9 | EXP   | ensLoss |   0      | -15.2709 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9994 |  -8.1793 | greater       |
|  6 | Hinge | ensLoss |   0.9971 |  -5.3627 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.2709 | greater       |

#### CIFAR49 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR49',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9463 | 0.9152 |  0.9493 |    0.9657 |
| ('test_acc', 'std')  | 0.0028 | 0.0019 |  0.0021 |    0.0013 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9878 | 0.9715 |  0.9883 |    0.9945 |
| ('test_auc', 'std')  | 0.0008 | 0.0011 |  0.0009 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0008 |  -7.6477 | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -8.9804 | less          |
|  9 | EXP   | ensLoss |   0      | -17.296  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9992 |  -7.6477 | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -8.9804 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.296  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.7664 | less          |
|  6 | Hinge | ensLoss |   0.0011 |  -6.9223 | less          |
|  9 | EXP   | ensLoss |   0      | -23.4274 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.7664 | greater       |
|  6 | Hinge | ensLoss |   0.9989 |  -6.9223 | greater       |
|  9 | EXP   | ensLoss |   1      | -23.4274 | greater       |

#### CIFAR13 - model: DenseNet169 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR13',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet169'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9726 | 0.9652 |  0.9716 |    0.9832 |
| ('test_acc', 'std')  | 0.0009 | 0.0018 |  0.0006 |    0.0007 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9968 | 0.9955 |  0.9966 |    0.9984 |
| ('test_auc', 'std')  | 0.0003 | 0.0001 |  0.0002 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0004 |  -8.9269 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -14.5569 | less          |
|  9 | EXP   | ensLoss |   0.0005 |  -8.4618 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9996 |  -8.9269 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -14.5569 | greater       |
|  9 | EXP   | ensLoss |   0.9995 |  -8.4618 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0013 |  -6.7048 | less          |
|  6 | Hinge | ensLoss |   0.001  |  -7.1212 | less          |
|  9 | EXP   | ensLoss |   0      | -23.3278 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9987 |  -6.7048 | greater       |
|  6 | Hinge | ensLoss |   0.999  |  -7.1212 | greater       |
|  9 | EXP   | ensLoss |   1      | -23.3278 | greater       |

#### CIFAR49 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR49',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9415 | 0.8522 |  0.943  |    0.9594 |
| ('test_acc', 'std')  | 0.0015 | 0.0036 |  0.0022 |    0.0009 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9868 | 0.9205 |  0.9853 |    0.9919 |
| ('test_auc', 'std')  | 0.0005 | 0.0035 |  0.0008 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 |  -9.6581 | less          |
|  6 | Hinge | ensLoss |   0.0008 |  -7.7224 | less          |
|  9 | EXP   | ensLoss |   0      | -37.7478 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 |  -9.6581 | greater       |
|  6 | Hinge | ensLoss |   0.9992 |  -7.7224 | greater       |
|  9 | EXP   | ensLoss |   1      | -37.7478 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 |  -9.6828 | less          |
|  6 | Hinge | ensLoss |   0.0018 |  -6.1517 | less          |
|  9 | EXP   | ensLoss |   0      | -22.9036 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 |  -9.6828 | greater       |
|  6 | Hinge | ensLoss |   0.9982 |  -6.1517 | greater       |
|  9 | EXP   | ensLoss |   1      | -22.9036 | greater       |

#### CIFAR56 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR56',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8978 | 0.8157 |  0.9029 |    0.9079 |
| ('test_acc', 'std')  | 0.0009 | 0.0022 |  0.0023 |    0.0024 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9638 | 0.8964 |  0.963  |    0.9709 |
| ('test_auc', 'std')  | 0.0007 | 0.0022 |  0.0015 |    0.0008 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0145 |  -3.3371 | less          |
|  6 | Hinge | ensLoss |   0.1086 |  -1.4633 | less          |
|  9 | EXP   | ensLoss |   0      | -38.7374 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9855 |  -3.3371 | greater       |
|  6 | Hinge | ensLoss |   0.8914 |  -1.4633 | greater       |
|  9 | EXP   | ensLoss |   1      | -38.7374 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0034 |  -5.1603 | less          |
|  6 | Hinge | ensLoss |   0.0082 |  -3.9845 | less          |
|  9 | EXP   | ensLoss |   0      | -29.5119 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9966 |  -5.1603 | greater       |
|  6 | Hinge | ensLoss |   0.9918 |  -3.9845 | greater       |
|  9 | EXP   | ensLoss |   1      | -29.5119 | greater       |

#### CIFAR14 - model: DenseNet121 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR14',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet121'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9851 | 0.9787 |  0.983  |    0.9931 |
| ('test_acc', 'std')  | 0.0009 | 0.0017 |  0.0005 |    0.001  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9989 | 0.9975 |  0.9987 |    0.9994 |
| ('test_auc', 'std')  | 0.0001 | 0.0002 |  0.0001 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0033 |  -5.191  | less          |
|  6 | Hinge | ensLoss |   0.0001 | -13.205  | less          |
|  9 | EXP   | ensLoss |   0.0005 |  -8.6288 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9967 |  -5.191  | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -13.205  | greater       |
|  9 | EXP   | ensLoss |   0.9995 |  -8.6288 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0492 | -2.1471 | less          |
|  6 | Hinge | ensLoss |   0.038  | -2.3805 | less          |
|  9 | EXP   | ensLoss |   0.0014 | -6.5132 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9508 | -2.1471 | greater       |
|  6 | Hinge | ensLoss |   0.962  | -2.3805 | greater       |
|  9 | EXP   | ensLoss |   0.9986 | -6.5132 | greater       |

#### CIFAR56 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR56',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.894  | 0.8158 |  0.8923 |    0.9175 |
| ('test_acc', 'std')  | 0.0016 | 0.0025 |  0.0015 |    0.0047 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9565 | 0.9012 |  0.9528 |    0.9732 |
| ('test_auc', 'std')  | 0.0011 | 0.0025 |  0.0018 |    0.0015 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0034 |  -5.1527 | less          |
|  6 | Hinge | ensLoss |   0.0008 |  -7.5249 | less          |
|  9 | EXP   | ensLoss |   0      | -15.8848 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9966 |  -5.1527 | greater       |
|  6 | Hinge | ensLoss |   0.9992 |  -7.5249 | greater       |
|  9 | EXP   | ensLoss |   1      | -15.8848 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -13.3175 | less          |
|  6 | Hinge | ensLoss |   0      | -33.9216 | less          |
|  9 | EXP   | ensLoss |   0      | -18.2563 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -13.3175 | greater       |
|  6 | Hinge | ensLoss |   1      | -33.9216 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.2563 | greater       |

#### CIFAR56 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR56',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8848 | 0.7247 |  0.8803 |    0.9049 |
| ('test_acc', 'std')  | 0.0019 | 0.0031 |  0.0032 |    0.0025 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.951  | 0.804  |  0.9368 |    0.9655 |
| ('test_auc', 'std')  | 0.0007 | 0.0035 |  0.0027 |    0.0017 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0033 |  -5.1752 | less          |
|  6 | Hinge | ensLoss |   0      | -15.6053 | less          |
|  9 | EXP   | ensLoss |   0      | -32.6478 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9967 |  -5.1752 | greater       |
|  6 | Hinge | ensLoss |   1      | -15.6053 | greater       |
|  9 | EXP   | ensLoss |   1      | -32.6478 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0009 |  -7.4437 | less          |
|  6 | Hinge | ensLoss |   0.0003 |  -9.9012 | less          |
|  9 | EXP   | ensLoss |   0      | -31.3873 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9991 |  -7.4437 | greater       |
|  6 | Hinge | ensLoss |   0.9997 |  -9.9012 | greater       |
|  9 | EXP   | ensLoss |   1      | -31.3873 | greater       |

#### CIFAR57 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR57',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8518 | 0.7355 |  0.8585 |    0.8595 |
| ('test_acc', 'std')  | 0.0024 | 0.0045 |  0.0034 |    0.0107 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.927  | 0.8166 |  0.9295 |    0.9291 |
| ('test_auc', 'std')  | 0.0014 | 0.0048 |  0.0024 |    0.0075 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.2603 | -0.7034 | less          |
|  6 | Hinge | ensLoss |   0.4668 | -0.0887 | less          |
|  9 | EXP   | ensLoss |   0.0004 | -9.034  | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.7397 | -0.7034 | greater       |
|  6 | Hinge | ensLoss |   0.5332 | -0.0887 | greater       |
|  9 | EXP   | ensLoss |   0.9996 | -9.034  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.3979 |  -0.2766 | less          |
|  6 | Hinge | ensLoss |   0.5162 |   0.0434 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.8704 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.6021 |  -0.2766 | greater       |
|  6 | Hinge | ensLoss |   0.4838 |   0.0434 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.8704 | greater       |

#### CIFAR14 - model: DenseNet169 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR14',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet169'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9824 | 0.9784 |  0.9839 |    0.9928 |
| ('test_acc', 'std')  | 0.0012 | 0.0008 |  0.0005 |    0.0004 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9986 | 0.9975 |  0.9986 |    0.9994 |
| ('test_auc', 'std')  | 0.0002 | 0.0002 |  0.0001 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -11.2145 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -13.1224 | less          |
|  9 | EXP   | ensLoss |   0      | -19.6871 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -11.2145 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -13.1224 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.6871 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0059 |  -4.3848 | less          |
|  6 | Hinge | ensLoss |   0.0118 |  -3.5593 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.6383 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9941 |  -4.3848 | greater       |
|  6 | Hinge | ensLoss |   0.9882 |  -3.5593 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.6383 | greater       |

#### CIFAR57 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR57',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8352 | 0.729  |  0.8365 |    0.87   |
| ('test_acc', 'std')  | 0.0033 | 0.0048 |  0.0025 |    0.0046 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9176 | 0.8086 |  0.912  |    0.9428 |
| ('test_auc', 'std')  | 0.0016 | 0.004  |  0.0026 |    0.0026 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0026 |  -5.5221 | less          |
|  6 | Hinge | ensLoss |   0.0008 |  -7.562  | less          |
|  9 | EXP   | ensLoss |   0      | -25.3039 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9974 |  -5.5221 | greater       |
|  6 | Hinge | ensLoss |   0.9992 |  -7.562  | greater       |
|  9 | EXP   | ensLoss |   1      | -25.3039 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 |  -9.7307 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.3429 | less          |
|  9 | EXP   | ensLoss |   0      | -36.3064 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 |  -9.7307 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.3429 | greater       |
|  9 | EXP   | ensLoss |   1      | -36.3064 | greater       |

#### CIFAR57 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR57',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8298 | 0.5811 |  0.8286 |    0.8462 |
| ('test_acc', 'std')  | 0.0021 | 0.0094 |  0.0034 |    0.014  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9088 | 0.6176 |  0.8942 |    0.9179 |
| ('test_auc', 'std')  | 0.0023 | 0.0132 |  0.0032 |    0.0115 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.1576 |  -1.1471 | less          |
|  6 | Hinge | ensLoss |   0.1717 |  -1.0738 | less          |
|  9 | EXP   | ensLoss |   0      | -16.2046 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.8424 |  -1.1471 | greater       |
|  6 | Hinge | ensLoss |   0.8283 |  -1.0738 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.2046 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.2107 |  -0.8948 | less          |
|  6 | Hinge | ensLoss |   0.071  |  -1.8249 | less          |
|  9 | EXP   | ensLoss |   0      | -18.2106 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.7893 |  -0.8948 | greater       |
|  6 | Hinge | ensLoss |   0.929  |  -1.8249 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.2106 | greater       |

#### CIFAR15 - model: DenseNet121 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR15',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet121'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9817 | 0.9773 |  0.9821 |    0.9909 |
| ('test_acc', 'std')  | 0.001  | 0.0011 |  0.0009 |    0.0002 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9988 | 0.9979 |  0.9986 |    0.9993 |
| ('test_auc', 'std')  | 0.0001 | 0.0002 |  0.0001 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.5186 | less          |
|  6 | Hinge | ensLoss |   0.0003 | -10.2297 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.6653 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.5186 | greater       |
|  6 | Hinge | ensLoss |   0.9997 | -10.2297 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.6653 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0172 | -3.1512 | less          |
|  6 | Hinge | ensLoss |   0.0173 | -3.1494 | less          |
|  9 | EXP   | ensLoss |   0.0054 | -4.5046 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9828 | -3.1512 | greater       |
|  6 | Hinge | ensLoss |   0.9827 | -3.1494 | greater       |
|  9 | EXP   | ensLoss |   0.9946 | -4.5046 | greater       |

#### CIFAR58 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR58',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9542 | 0.9255 |  0.958  |    0.9624 |
| ('test_acc', 'std')  | 0.0007 | 0.0035 |  0.0011 |    0.0015 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9906 | 0.9781 |  0.9908 |    0.9933 |
| ('test_auc', 'std')  | 0.0004 | 0.0016 |  0.0004 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0031 |  -5.2766 | less          |
|  6 | Hinge | ensLoss |   0.0128 |  -3.4677 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -10.0207 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9969 |  -5.2766 | greater       |
|  6 | Hinge | ensLoss |   0.9872 |  -3.4677 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -10.0207 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0139 | -3.3799 | less          |
|  6 | Hinge | ensLoss |   0.0154 | -3.2682 | less          |
|  9 | EXP   | ensLoss |   0.0005 | -8.7729 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9861 | -3.3799 | greater       |
|  6 | Hinge | ensLoss |   0.9846 | -3.2682 | greater       |
|  9 | EXP   | ensLoss |   0.9995 | -8.7729 | greater       |

#### CIFAR58 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR58',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9491 | 0.927  |  0.9476 |    0.9606 |
| ('test_acc', 'std')  | 0.0027 | 0.0013 |  0.0016 |    0.0015 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9892 | 0.9785 |  0.988  |    0.9929 |
| ('test_auc', 'std')  | 0.0002 | 0.0007 |  0.0006 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0195 |  -3.0226 | less          |
|  6 | Hinge | ensLoss |   0      | -15.8233 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.3433 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9805 |  -3.0226 | greater       |
|  6 | Hinge | ensLoss |   1      | -15.8233 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.3433 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0016 |  -6.3135 | less          |
|  6 | Hinge | ensLoss |   0      | -16.1338 | less          |
|  9 | EXP   | ensLoss |   0      | -28.2549 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9984 |  -6.3135 | greater       |
|  6 | Hinge | ensLoss |   1      | -16.1338 | greater       |
|  9 | EXP   | ensLoss |   1      | -28.2549 | greater       |

#### CIFAR15 - model: DenseNet169 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR15',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet169'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9822 | 0.9773 |  0.9819 |    0.9902 |
| ('test_acc', 'std')  | 0.0013 | 0.0007 |  0.001  |    0.0005 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9988 | 0.9982 |  0.9989 |    0.9993 |
| ('test_auc', 'std')  | 0.0001 | 0.0002 |  0.0001 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0038 |  -4.9854 | less          |
|  6 | Hinge | ensLoss |   0.0003 | -10.1781 | less          |
|  9 | EXP   | ensLoss |   0      | -25.2988 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9962 |  -4.9854 | greater       |
|  6 | Hinge | ensLoss |   0.9997 | -10.1781 | greater       |
|  9 | EXP   | ensLoss |   1      | -25.2988 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.051  | -2.1146 | less          |
|  6 | Hinge | ensLoss |   0.0252 | -2.7675 | less          |
|  9 | EXP   | ensLoss |   0.0005 | -8.5101 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.949  | -2.1146 | greater       |
|  6 | Hinge | ensLoss |   0.9748 | -2.7675 | greater       |
|  9 | EXP   | ensLoss |   0.9995 | -8.5101 | greater       |

#### CIFAR58 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR58',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9493 | 0.8102 |  0.9476 |    0.9551 |
| ('test_acc', 'std')  | 0.0018 | 0.0212 |  0.0017 |    0.0017 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9874 | 0.8906 |  0.9866 |    0.9911 |
| ('test_auc', 'std')  | 0.0005 | 0.0203 |  0.0006 |    0.0011 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0035 | -5.1066 | less          |
|  6 | Hinge | ensLoss |   0.0234 | -2.8398 | less          |
|  9 | EXP   | ensLoss |   0.0014 | -6.6001 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9965 | -5.1066 | greater       |
|  6 | Hinge | ensLoss |   0.9766 | -2.8398 | greater       |
|  9 | EXP   | ensLoss |   0.9986 | -6.6001 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0344 | -2.471  | less          |
|  6 | Hinge | ensLoss |   0.019  | -3.0506 | less          |
|  9 | EXP   | ensLoss |   0.0044 | -4.7684 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9656 | -2.471  | greater       |
|  6 | Hinge | ensLoss |   0.981  | -3.0506 | greater       |
|  9 | EXP   | ensLoss |   0.9956 | -4.7684 | greater       |

#### CIFAR59 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR59',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9507 | 0.9144 |  0.9532 |    0.9603 |
| ('test_acc', 'std')  | 0.0021 | 0.003  |  0.0007 |    0.0018 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.99   | 0.9716 |  0.9894 |    0.9934 |
| ('test_auc', 'std')  | 0.0008 | 0.0019 |  0.0005 |    0.0007 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.012  |  -3.5386 | less          |
|  6 | Hinge | ensLoss |   0.0095 |  -3.8033 | less          |
|  9 | EXP   | ensLoss |   0      | -26.3471 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.988  |  -3.5386 | greater       |
|  6 | Hinge | ensLoss |   0.9905 |  -3.8033 | greater       |
|  9 | EXP   | ensLoss |   1      | -26.3471 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.033  |  -2.5103 | less          |
|  6 | Hinge | ensLoss |   0.0058 |  -4.4132 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.2612 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.967  |  -2.5103 | greater       |
|  6 | Hinge | ensLoss |   0.9942 |  -4.4132 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.2612 | greater       |

#### CIFAR59 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR59',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9473 | 0.9219 |  0.9435 |    0.9574 |
| ('test_acc', 'std')  | 0.0022 | 0.003  |  0.0022 |    0.0029 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.988  | 0.9767 |  0.9862 |    0.9917 |
| ('test_auc', 'std')  | 0.0005 | 0.0012 |  0.0009 |    0.0007 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0486 |  -2.1565 | less          |
|  6 | Hinge | ensLoss |   0.0011 |  -6.985  | less          |
|  9 | EXP   | ensLoss |   0      | -15.6813 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9514 |  -2.1565 | greater       |
|  6 | Hinge | ensLoss |   0.9989 |  -6.985  | greater       |
|  9 | EXP   | ensLoss |   1      | -15.6813 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0191 |  -3.0447 | less          |
|  6 | Hinge | ensLoss |   0.0024 |  -5.6779 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -11.6322 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9809 |  -3.0447 | greater       |
|  6 | Hinge | ensLoss |   0.9976 |  -5.6779 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -11.6322 | greater       |

#### CIFAR16 - model: DenseNet121 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR16',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet121'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9845 | 0.9796 |  0.9842 |    0.9918 |
| ('test_acc', 'std')  | 0.0007 | 0.0012 |  0.0004 |    0.0008 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9979 | 0.9976 |  0.9979 |    0.9997 |
| ('test_auc', 'std')  | 0.0003 | 0.0002 |  0.0001 |    0      |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0022 |  -5.8353 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -14.9048 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.7262 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9978 |  -5.8353 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -14.9048 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.7262 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0016 |  -6.3461 | less          |
|  6 | Hinge | ensLoss |   0      | -16.0236 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -11.4271 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9984 |  -6.3461 | greater       |
|  6 | Hinge | ensLoss |   1      | -16.0236 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -11.4271 | greater       |

#### CIFAR59 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR59',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9394 | 0.7717 |  0.9309 |    0.9557 |
| ('test_acc', 'std')  | 0.0022 | 0.0139 |  0.0006 |    0.0015 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9842 | 0.8516 |  0.9797 |    0.9916 |
| ('test_auc', 'std')  | 0.0007 | 0.0122 |  0.0008 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0028 |  -5.399  | less          |
|  6 | Hinge | ensLoss |   0.0001 | -14.9823 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.9342 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9972 |  -5.399  | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -14.9823 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.9342 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0008 |  -7.514  | less          |
|  6 | Hinge | ensLoss |   0      | -20.7005 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -11.3364 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9992 |  -7.514  | greater       |
|  6 | Hinge | ensLoss |   1      | -20.7005 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -11.3364 | greater       |

#### CIFAR67 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR67',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.94   | 0.8676 |  0.9416 |    0.9581 |
| ('test_acc', 'std')  | 0.0029 | 0.0033 |  0.0012 |    0.0016 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9861 | 0.9384 |  0.9864 |    0.9931 |
| ('test_auc', 'std')  | 0.0005 | 0.0018 |  0.0007 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0064 |  -4.2919 | less          |
|  6 | Hinge | ensLoss |   0.0011 |  -7.0517 | less          |
|  9 | EXP   | ensLoss |   0      | -18.58   | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9936 |  -4.2919 | greater       |
|  6 | Hinge | ensLoss |   0.9989 |  -7.0517 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.58   | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.8925 | less          |
|  6 | Hinge | ensLoss |   0.0007 |  -7.7952 | less          |
|  9 | EXP   | ensLoss |   0      | -28.5648 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.8925 | greater       |
|  6 | Hinge | ensLoss |   0.9993 |  -7.7952 | greater       |
|  9 | EXP   | ensLoss |   1      | -28.5648 | greater       |

#### CIFAR67 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR67',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.928  | 0.8648 |  0.9294 |    0.9549 |
| ('test_acc', 'std')  | 0.0015 | 0.0016 |  0.0031 |    0.0027 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9792 | 0.9374 |  0.979  |    0.9912 |
| ('test_auc', 'std')  | 0.0008 | 0.0017 |  0.0007 |    0.0006 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -11.1841 | less          |
|  6 | Hinge | ensLoss |   0.0022 |  -5.7932 | less          |
|  9 | EXP   | ensLoss |   0      | -35.2455 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -11.1841 | greater       |
|  6 | Hinge | ensLoss |   0.9978 |  -5.7932 | greater       |
|  9 | EXP   | ensLoss |   1      | -35.2455 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.4036 | less          |
|  6 | Hinge | ensLoss |   0.0003 | -10.2024 | less          |
|  9 | EXP   | ensLoss |   0      | -31.5589 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.4036 | greater       |
|  6 | Hinge | ensLoss |   0.9997 | -10.2024 | greater       |
|  9 | EXP   | ensLoss |   1      | -31.5589 | greater       |

#### CIFAR16 - model: DenseNet169 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR16',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet169'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9836 | 0.9779 |  0.9818 |    0.9909 |
| ('test_acc', 'std')  | 0.0007 | 0.0011 |  0.0008 |    0.0007 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.998  | 0.9969 |  0.9977 |    0.9993 |
| ('test_auc', 'std')  | 0.0001 | 0.0003 |  0.0002 |    0.0001 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0012 |  -6.9133 | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -9.169  | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.2774 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9988 |  -6.9133 | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -9.169  | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.2774 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0005 | -8.5946 | less          |
|  6 | Hinge | ensLoss |   0.0022 | -5.7727 | less          |
|  9 | EXP   | ensLoss |   0.0009 | -7.4736 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9995 | -8.5946 | greater       |
|  6 | Hinge | ensLoss |   0.9978 | -5.7727 | greater       |
|  9 | EXP   | ensLoss |   0.9991 | -7.4736 | greater       |

#### CIFAR67 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR67',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9247 | 0.7508 |  0.9179 |    0.9514 |
| ('test_acc', 'std')  | 0.0024 | 0.0046 |  0.0034 |    0.0039 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9768 | 0.833  |  0.9659 |    0.9892 |
| ('test_auc', 'std')  | 0.0015 | 0.0042 |  0.0012 |    0.0014 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0013 |  -6.7352 | less          |
|  6 | Hinge | ensLoss |   0.0007 |  -7.7991 | less          |
|  9 | EXP   | ensLoss |   0      | -54.7794 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9987 |  -6.7352 | greater       |
|  6 | Hinge | ensLoss |   0.9993 |  -7.7991 | greater       |
|  9 | EXP   | ensLoss |   1      | -54.7794 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 |  -9.8066 | less          |
|  6 | Hinge | ensLoss |   0      | -22.7203 | less          |
|  9 | EXP   | ensLoss |   0      | -47.0766 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 |  -9.8066 | greater       |
|  6 | Hinge | ensLoss |   1      | -22.7203 | greater       |
|  9 | EXP   | ensLoss |   1      | -47.0766 | greater       |

#### CIFAR68 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR68',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9663 | 0.9511 |  0.9688 |    0.9727 |
| ('test_acc', 'std')  | 0.0024 | 0.0019 |  0.0014 |    0.0004 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9941 | 0.9891 |  0.9948 |    0.995  |
| ('test_auc', 'std')  | 0.0005 | 0.0003 |  0.0004 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0373 |  -2.396  | less          |
|  6 | Hinge | ensLoss |   0.0384 |  -2.3691 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.151  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9627 |  -2.396  | greater       |
|  6 | Hinge | ensLoss |   0.9616 |  -2.3691 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.151  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.1038 |  -1.5019 | less          |
|  6 | Hinge | ensLoss |   0.3245 |  -0.4912 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.3944 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.8962 |  -1.5019 | greater       |
|  6 | Hinge | ensLoss |   0.6755 |  -0.4912 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.3944 | greater       |

#### CIFAR17 - model: DenseNet121 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR17',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet121'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9819 | 0.9738 |  0.9814 |    0.9927 |
| ('test_acc', 'std')  | 0.0004 | 0.0017 |  0.0007 |    0.0006 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9987 | 0.9967 |  0.9988 |    0.9997 |
| ('test_auc', 'std')  | 0.0001 | 0.0002 |  0.0001 |    0      |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        0 | -31.8473 | less          |
|  6 | Hinge | ensLoss |        0 | -17.5407 | less          |
|  9 | EXP   | ensLoss |        0 | -15.6416 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |        1 | -31.8473 | greater       |
|  6 | Hinge | ensLoss |        1 | -17.5407 | greater       |
|  9 | EXP   | ensLoss |        1 | -15.6416 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0006 |  -8.333  | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.5444 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.5502 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9994 |  -8.333  | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.5444 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.5502 | greater       |

#### CIFAR68 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR68',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9651 | 0.9514 |  0.9663 |    0.9716 |
| ('test_acc', 'std')  | 0.0011 | 0.002  |  0.0014 |    0.0008 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9938 | 0.9887 |  0.9933 |    0.9949 |
| ('test_auc', 'std')  | 0.0004 | 0.0006 |  0.0005 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0008 |  -7.6339 | less          |
|  6 | Hinge | ensLoss |   0.0144 |  -3.342  | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.2762 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9992 |  -7.6339 | greater       |
|  6 | Hinge | ensLoss |   0.9856 |  -3.342  | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.2762 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0786 | -1.738  | less          |
|  6 | Hinge | ensLoss |   0.0402 | -2.3288 | less          |
|  9 | EXP   | ensLoss |   0.0007 | -7.8179 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9214 | -1.738  | greater       |
|  6 | Hinge | ensLoss |   0.9598 | -2.3288 | greater       |
|  9 | EXP   | ensLoss |   0.9993 | -7.8179 | greater       |

#### CIFAR68 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR68',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9641 | 0.8879 |  0.9615 |    0.9661 |
| ('test_acc', 'std')  | 0.0005 | 0.014  |  0.0013 |    0.0024 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.993  | 0.959  |  0.9913 |    0.9932 |
| ('test_auc', 'std')  | 0.0004 | 0.0083 |  0.0004 |    0.0006 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.2237 | -0.8414 | less          |
|  6 | Hinge | ensLoss |   0.0829 | -1.6927 | less          |
|  9 | EXP   | ensLoss |   0.0034 | -5.1481 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.7763 | -0.8414 | greater       |
|  6 | Hinge | ensLoss |   0.9171 | -1.6927 | greater       |
|  9 | EXP   | ensLoss |   0.9966 | -5.1481 | greater       |
|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.3963 | -0.2811 | less          |
|  6 | Hinge | ensLoss |   0.046  | -2.2064 | less          |
|  9 | EXP   | ensLoss |   0.0074 | -4.0997 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.6037 | -0.2811 | greater       |
|  6 | Hinge | ensLoss |   0.954  | -2.2064 | greater       |
|  9 | EXP   | ensLoss |   0.9926 | -4.0997 | greater       |

#### CIFAR69 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR69',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9623 | 0.9193 |  0.9647 |    0.9664 |
| ('test_acc', 'std')  | 0.0006 | 0.0027 |  0.0022 |    0.0009 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9939 | 0.9764 |  0.9939 |    0.9948 |
| ('test_auc', 'std')  | 0.0002 | 0.0008 |  0.0004 |    0.0007 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0152 |  -3.2826 | less          |
|  6 | Hinge | ensLoss |   0.2555 |  -0.7206 | less          |
|  9 | EXP   | ensLoss |   0      | -17.2157 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9848 |  -3.2826 | greater       |
|  6 | Hinge | ensLoss |   0.7445 |  -0.7206 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.2157 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.1603 |  -1.1327 | less          |
|  6 | Hinge | ensLoss |   0.1043 |  -1.4977 | less          |
|  9 | EXP   | ensLoss |   0      | -19.5653 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.8397 |  -1.1327 | greater       |
|  6 | Hinge | ensLoss |   0.8957 |  -1.4977 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.5653 | greater       |

#### CIFAR17 - model: DenseNet169 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR17',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet169'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD'},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9828 | 0.9771 |  0.9802 |    0.993  |
| ('test_acc', 'std')  | 0.001  | 0.0011 |  0.0007 |    0.0007 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9985 | 0.9971 |  0.9987 |    0.9997 |
| ('test_auc', 'std')  | 0.0002 | 0      |  0.0001 |    0      |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.001  |  -7.1856 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.3992 | less          |
|  9 | EXP   | ensLoss |   0      | -18.2385 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.999  |  -7.1856 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.3992 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.2385 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0019 |  -6.057  | less          |
|  6 | Hinge | ensLoss |   0      | -15.217  | less          |
|  9 | EXP   | ensLoss |   0      | -49.7605 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9981 |  -6.057  | greater       |
|  6 | Hinge | ensLoss |   1      | -15.217  | greater       |
|  9 | EXP   | ensLoss |   1      | -49.7605 | greater       |

#### CIFAR69 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR69',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9563 | 0.9246 |  0.9573 |    0.9636 |
| ('test_acc', 'std')  | 0.0017 | 0.0017 |  0.0018 |    0.0013 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9915 | 0.9798 |  0.9913 |    0.9939 |
| ('test_auc', 'std')  | 0.0003 | 0.0011 |  0.0009 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0316 |  -2.5508 | less          |
|  6 | Hinge | ensLoss |   0.0438 |  -2.25   | less          |
|  9 | EXP   | ensLoss |   0      | -22.5167 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9684 |  -2.5508 | greater       |
|  6 | Hinge | ensLoss |   0.9562 |  -2.25   | greater       |
|  9 | EXP   | ensLoss |   1      | -22.5167 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0105 |  -3.6931 | less          |
|  6 | Hinge | ensLoss |   0.0225 |  -2.8812 | less          |
|  9 | EXP   | ensLoss |   0.0002 | -11.4677 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9895 |  -3.6931 | greater       |
|  6 | Hinge | ensLoss |   0.9775 |  -2.8812 | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -11.4677 | greater       |

#### CIFAR69 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR69',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9513 | 0.8617 |  0.9506 |    0.963  |
| ('test_acc', 'std')  | 0.0021 | 0.0011 |  0.0019 |    0.0021 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9893 | 0.9325 |  0.988  |    0.993  |
| ('test_auc', 'std')  | 0.0004 | 0.0015 |  0.0009 |    0.0008 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0016 |  -6.3546 | less          |
|  6 | Hinge | ensLoss |   0      | -20.6667 | less          |
|  9 | EXP   | ensLoss |   0      | -40.7158 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9984 |  -6.3546 | greater       |
|  6 | Hinge | ensLoss |   1      | -20.6667 | greater       |
|  9 | EXP   | ensLoss |   1      | -40.7158 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0065 |  -4.2586 | less          |
|  6 | Hinge | ensLoss |   0.0004 |  -9.3263 | less          |
|  9 | EXP   | ensLoss |   0      | -31.5884 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9935 |  -4.2586 | greater       |
|  6 | Hinge | ensLoss |   0.9996 |  -9.3263 | greater       |
|  9 | EXP   | ensLoss |   1      | -31.5884 | greater       |

#### CIFAR18 - model: DenseNet121 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR18',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet121'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9673 | 0.9471 |  0.969  |    0.9817 |
| ('test_acc', 'std')  | 0.0015 | 0.0014 |  0.0012 |    0.0009 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9954 | 0.9897 |  0.9955 |    0.997  |
| ('test_auc', 'std')  | 0.0003 | 0.0006 |  0.0003 |    0.0002 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -12.5813 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.9711 | less          |
|  9 | EXP   | ensLoss |   0      | -19.6198 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -12.5813 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.9711 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.6198 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0051 |  -4.5779 | less          |
|  6 | Hinge | ensLoss |   0.0046 |  -4.7306 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -12.0363 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9949 |  -4.5779 | greater       |
|  6 | Hinge | ensLoss |   0.9954 |  -4.7306 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -12.0363 | greater       |

#### CIFAR78 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR78',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9584 | 0.9226 |  0.9622 |    0.9677 |
| ('test_acc', 'std')  | 0.0011 | 0.0041 |  0.0007 |    0.0017 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9922 | 0.9767 |  0.9936 |    0.9953 |
| ('test_auc', 'std')  | 0.0006 | 0.0013 |  0.0004 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.0011 | -7.0002 | less          |
|  6 | Hinge | ensLoss |   0.033  | -2.5104 | less          |
|  9 | EXP   | ensLoss |   0.0003 | -9.9768 | less          |


|    | A     | B       |   pvalue |    stat | alternative   |
|---:|:------|:--------|---------:|--------:|:--------------|
|  3 | BCE   | ensLoss |   0.9989 | -7.0002 | greater       |
|  6 | Hinge | ensLoss |   0.967  | -2.5104 | greater       |
|  9 | EXP   | ensLoss |   0.9997 | -9.9768 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0008 |  -7.5244 | less          |
|  6 | Hinge | ensLoss |   0.0085 |  -3.9353 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.2626 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9992 |  -7.5244 | greater       |
|  6 | Hinge | ensLoss |   0.9915 |  -3.9353 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.2626 | greater       |

#### CIFAR78 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR78',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9536 | 0.9202 |  0.9527 |    0.9664 |
| ('test_acc', 'std')  | 0.0018 | 0.0027 |  0.0017 |    0.0014 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9898 | 0.9746 |  0.9894 |    0.994  |
| ('test_auc', 'std')  | 0.0005 | 0.0013 |  0.0008 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -12.8646 | less          |
|  6 | Hinge | ensLoss |   0.0006 |  -8.0242 | less          |
|  9 | EXP   | ensLoss |   0      | -20.4778 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -12.8646 | greater       |
|  6 | Hinge | ensLoss |   0.9994 |  -8.0242 | greater       |
|  9 | EXP   | ensLoss |   1      | -20.4778 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -17.522  | less          |
|  6 | Hinge | ensLoss |   0.0014 |  -6.5625 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -13.8397 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -17.522  | greater       |
|  6 | Hinge | ensLoss |   0.9986 |  -6.5625 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -13.8397 | greater       |

#### CIFAR19 - model: DenseNet121 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR19',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet121'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9332 | 0.8861 |  0.9356 |    0.9553 |
| ('test_acc', 'std')  | 0.0015 | 0.0012 |  0.0019 |    0.0012 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9825 | 0.9569 |  0.9823 |    0.9895 |
| ('test_auc', 'std')  | 0.0006 | 0.0009 |  0.0005 |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -12.7915 | less          |
|  6 | Hinge | ensLoss |   0.0012 |  -6.7911 | less          |
|  9 | EXP   | ensLoss |   0      | -39.0519 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -12.7915 | greater       |
|  6 | Hinge | ensLoss |   0.9988 |  -6.7911 | greater       |
|  9 | EXP   | ensLoss |   1      | -39.0519 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.4962 | less          |
|  6 | Hinge | ensLoss |   0      | -27.5405 | less          |
|  9 | EXP   | ensLoss |   0      | -31.6251 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.4962 | greater       |
|  6 | Hinge | ensLoss |   1      | -27.5405 | greater       |
|  9 | EXP   | ensLoss |   1      | -31.6251 | greater       |

#### CIFAR78 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR78',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9506 | 0.8186 |  0.9506 |    0.9668 |
| ('test_acc', 'std')  | 0.0009 | 0.0136 |  0.0019 |    0.0022 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.989  | 0.899  |  0.9869 |    0.9936 |
| ('test_auc', 'std')  | 0.0007 | 0.0116 |  0.0007 |    0.0006 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0014 |  -6.5245 | less          |
|  6 | Hinge | ensLoss |   0.0049 |  -4.64   | less          |
|  9 | EXP   | ensLoss |   0.0002 | -10.584  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9986 |  -6.5245 | greater       |
|  6 | Hinge | ensLoss |   0.9951 |  -4.64   | greater       |
|  9 | EXP   | ensLoss |   0.9998 | -10.584  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0018 |  -6.1069 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.5425 | less          |
|  9 | EXP   | ensLoss |   0.0007 |  -7.8098 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9982 |  -6.1069 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.5425 | greater       |
|  9 | EXP   | ensLoss |   0.9993 |  -7.8098 | greater       |

#### CIFAR79 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR79',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9367 | 0.8725 |  0.9441 |    0.9559 |
| ('test_acc', 'std')  | 0.0022 | 0.002  |  0.0013 |    0.0017 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9858 | 0.9432 |  0.9867 |    0.9924 |
| ('test_auc', 'std')  | 0.0004 | 0.002  |  0.0005 |    0.0007 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0026 |  -5.5449 | less          |
|  6 | Hinge | ensLoss |   0.0003 | -10.1936 | less          |
|  9 | EXP   | ensLoss |   0      | -26.262  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9974 |  -5.5449 | greater       |
|  6 | Hinge | ensLoss |   0.9997 | -10.1936 | greater       |
|  9 | EXP   | ensLoss |   1      | -26.262  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0013 |  -6.6412 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -11.7929 | less          |
|  9 | EXP   | ensLoss |   0      | -19.6311 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9987 |  -6.6412 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -11.7929 | greater       |
|  9 | EXP   | ensLoss |   1      | -19.6311 | greater       |

#### CIFAR79 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR79',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9295 | 0.8883 |  0.9252 |    0.9534 |
| ('test_acc', 'std')  | 0.0026 | 0.0028 |  0.0015 |    0.0011 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.98   | 0.9532 |  0.9777 |    0.9912 |
| ('test_auc', 'std')  | 0.0014 | 0.0018 |  0.001  |    0.0004 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0008 |  -7.6798 | less          |
|  6 | Hinge | ensLoss |   0      | -16.8078 | less          |
|  9 | EXP   | ensLoss |   0      | -24.2866 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9992 |  -7.6798 | greater       |
|  6 | Hinge | ensLoss |   1      | -16.8078 | greater       |
|  9 | EXP   | ensLoss |   1      | -24.2866 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0014 |  -6.5969 | less          |
|  6 | Hinge | ensLoss |   0      | -16.1066 | less          |
|  9 | EXP   | ensLoss |   0      | -18.3901 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9986 |  -6.5969 | greater       |
|  6 | Hinge | ensLoss |   1      | -16.1066 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.3901 | greater       |

#### CIFAR19 - model: DenseNet169 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR19',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet169'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9341 | 0.8832 |  0.9335 |    0.9577 |
| ('test_acc', 'std')  | 0.0025 | 0.0027 |  0.0027 |    0.0014 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9824 | 0.9567 |  0.983  |    0.9909 |
| ('test_auc', 'std')  | 0.0013 | 0.0004 |  0.0006 |    0.0006 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0013 |  -6.7264 | less          |
|  6 | Hinge | ensLoss |   0.0009 |  -7.4541 | less          |
|  9 | EXP   | ensLoss |   0      | -27.621  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9987 |  -6.7264 | greater       |
|  6 | Hinge | ensLoss |   0.9991 |  -7.4541 | greater       |
|  9 | EXP   | ensLoss |   1      | -27.621  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0025 |  -5.5716 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -15.0005 | less          |
|  9 | EXP   | ensLoss |   0      | -42.2473 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9975 |  -5.5716 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -15.0005 | greater       |
|  9 | EXP   | ensLoss |   1      | -42.2473 | greater       |

#### CIFAR79 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR79',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9223 | 0.6333 |  0.9144 |    0.9463 |
| ('test_acc', 'std')  | 0.0015 | 0.0054 |  0.0032 |    0.0031 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9764 | 0.6921 |  0.9689 |    0.9872 |
| ('test_auc', 'std')  | 0.0011 | 0.0037 |  0.0013 |    0.0016 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0026 |  -5.5574 | less          |
|  6 | Hinge | ensLoss |   0.0015 |  -6.4141 | less          |
|  9 | EXP   | ensLoss |   0      | -80.3489 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9974 |  -5.5574 | greater       |
|  6 | Hinge | ensLoss |   0.9985 |  -6.4141 | greater       |
|  9 | EXP   | ensLoss |   1      | -80.3489 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0048 |  -4.6464 | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.2816 | less          |
|  9 | EXP   | ensLoss |   0      | -70.4538 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9952 |  -4.6464 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.2816 | greater       |
|  9 | EXP   | ensLoss |   1      | -70.4538 | greater       |

#### CIFAR89 - model: ResNet34 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR89',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet34'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9193 | 0.8339 |  0.9204 |    0.9471 |
| ('test_acc', 'std')  | 0.0029 | 0.0062 |  0.0011 |    0.0015 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9757 | 0.9104 |  0.9741 |    0.9873 |
| ('test_auc', 'std')  | 0.0013 | 0.0046 |  0.001  |    0.0006 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 | -10.1749 | less          |
|  6 | Hinge | ensLoss |   0      | -16.6712 | less          |
|  9 | EXP   | ensLoss |   0      | -17.2749 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 | -10.1749 | greater       |
|  6 | Hinge | ensLoss |   1      | -16.6712 | greater       |
|  9 | EXP   | ensLoss |   1      | -17.2749 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0002 | -10.3874 | less          |
|  6 | Hinge | ensLoss |   0      | -25.2231 | less          |
|  9 | EXP   | ensLoss |   0      | -16.7379 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9998 | -10.3874 | greater       |
|  6 | Hinge | ensLoss |   1      | -25.2231 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.7379 | greater       |

#### CIFAR89 - model: ResNet50 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR89',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet50'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9077 | 0.8263 |  0.905  |    0.9384 |
| ('test_acc', 'std')  | 0.0034 | 0.0038 |  0.0018 |    0.0038 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9682 | 0.9063 |  0.9644 |    0.9833 |
| ('test_auc', 'std')  | 0.0018 | 0.0033 |  0.0011 |    0.002  |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0047 |  -4.6809 | less          |
|  6 | Hinge | ensLoss |   0.0005 |  -8.8139 | less          |
|  9 | EXP   | ensLoss |   0      | -16.145  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9953 |  -4.6809 | greater       |
|  6 | Hinge | ensLoss |   0.9995 |  -8.8139 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.145  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0052 |  -4.5627 | less          |
|  6 | Hinge | ensLoss |   0.0006 |  -8.392  | less          |
|  9 | EXP   | ensLoss |   0      | -16.754  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9948 |  -4.5627 | greater       |
|  6 | Hinge | ensLoss |   0.9994 |  -8.392  | greater       |
|  9 | EXP   | ensLoss |   1      | -16.754  | greater       |

#### CIFAR23 - model: DenseNet121 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR23',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet121'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8853 | 0.8416 |  0.8798 |    0.9155 |
| ('test_acc', 'std')  | 0.0017 | 0.0023 |  0.0012 |    0.0032 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9553 | 0.9193 |  0.9505 |    0.9708 |
| ('test_auc', 'std')  | 0.0006 | 0.002  |  0.0008 |    0.0018 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0012 |  -6.832  | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.4526 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.711  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9988 |  -6.832  | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.4526 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.711  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.001  |  -7.1888 | less          |
|  6 | Hinge | ensLoss |   0.0005 |  -8.7451 | less          |
|  9 | EXP   | ensLoss |   0.0001 | -14.0682 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.999  |  -7.1888 | greater       |
|  6 | Hinge | ensLoss |   0.9995 |  -8.7451 | greater       |
|  9 | EXP   | ensLoss |   0.9999 | -14.0682 | greater       |

#### CIFAR89 - model: ResNet101 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR89',
 'device': device(type='cuda', index=0),
 'model': {'net': 'ResNet101'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8989 | 0.7223 |  0.8874 |    0.9347 |
| ('test_acc', 'std')  | 0.0041 | 0.0045 |  0.003  |    0.004  |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9644 | 0.7967 |  0.9513 |    0.9819 |
| ('test_auc', 'std')  | 0.0007 | 0.0058 |  0.0012 |    0.0016 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0024 |  -5.6524 | less          |
|  6 | Hinge | ensLoss |   0.0009 |  -7.3411 | less          |
|  9 | EXP   | ensLoss |   0      | -29.1658 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9976 |  -5.6524 | greater       |
|  6 | Hinge | ensLoss |   0.9991 |  -7.3411 | greater       |
|  9 | EXP   | ensLoss |   1      | -29.1658 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -14.0446 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -11.8434 | less          |
|  9 | EXP   | ensLoss |   0      | -26.8991 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -14.0446 | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -11.8434 | greater       |
|  9 | EXP   | ensLoss |   1      | -26.8991 | greater       |

#### CIFAR23 - model: DenseNet169 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR23',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet169'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |   BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.881 | 0.8428 |  0.88   |    0.912  |
| ('test_acc', 'std')  | 0.001 | 0.0029 |  0.0037 |    0.0015 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9523 | 0.92   |  0.9531 |    0.9695 |
| ('test_auc', 'std')  | 0.0013 | 0.0018 |  0.0012 |    0.0012 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -15.3567 | less          |
|  6 | Hinge | ensLoss |   0.0015 |  -6.4193 | less          |
|  9 | EXP   | ensLoss |   0      | -18.258  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -15.3567 | greater       |
|  6 | Hinge | ensLoss |   0.9985 |  -6.4193 | greater       |
|  9 | EXP   | ensLoss |   1      | -18.258  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.001  |  -7.2415 | less          |
|  6 | Hinge | ensLoss |   0.0008 |  -7.5165 | less          |
|  9 | EXP   | ensLoss |   0      | -21.5973 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.999  |  -7.2415 | greater       |
|  6 | Hinge | ensLoss |   0.9992 |  -7.5165 | greater       |
|  9 | EXP   | ensLoss |   1      | -21.5973 | greater       |

#### CIFAR24 - model: DenseNet121 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR24',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet121'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.899  | 0.8423 |  0.8957 |    0.9356 |
| ('test_acc', 'std')  | 0.0022 | 0.0043 |  0.0033 |    0.0017 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9593 | 0.9218 |  0.9584 |    0.98   |
| ('test_auc', 'std')  | 0.0011 | 0.0021 |  0.0019 |    0.0003 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -13.3334 | less          |
|  6 | Hinge | ensLoss |   0      | -16.8834 | less          |
|  9 | EXP   | ensLoss |   0      | -16.666  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -13.3334 | greater       |
|  6 | Hinge | ensLoss |   1      | -16.8834 | greater       |
|  9 | EXP   | ensLoss |   1      | -16.666  | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0      | -21.7267 | less          |
|  6 | Hinge | ensLoss |   0.0003 | -10.1653 | less          |
|  9 | EXP   | ensLoss |   0      | -25.6177 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   1      | -21.7267 | greater       |
|  6 | Hinge | ensLoss |   0.9997 | -10.1653 | greater       |
|  9 | EXP   | ensLoss |   1      | -25.6177 | greater       |

#### CIFAR24 - model: DenseNet169 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR24',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet169'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.8963 | 0.8412 |  0.9017 |    0.9358 |
| ('test_acc', 'std')  | 0.0028 | 0.0027 |  0.0016 |    0.0023 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9578 | 0.9182 |  0.9608 |    0.9805 |
| ('test_auc', 'std')  | 0.0011 | 0.0029 |  0.0019 |    0.0009 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0003 |  -9.6014 | less          |
|  6 | Hinge | ensLoss |   0.0001 | -14.7634 | less          |
|  9 | EXP   | ensLoss |   0      | -37.0057 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9997 |  -9.6014 | greater       |
|  6 | Hinge | ensLoss |   0.9999 | -14.7634 | greater       |
|  9 | EXP   | ensLoss |   1      | -37.0057 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0001 | -11.979  | less          |
|  6 | Hinge | ensLoss |   0.0002 | -10.2562 | less          |
|  9 | EXP   | ensLoss |   0      | -23.9947 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9999 | -11.979  | greater       |
|  6 | Hinge | ensLoss |   0.9998 | -10.2562 | greater       |
|  9 | EXP   | ensLoss |   1      | -23.9947 | greater       |

#### CIFAR25 - model: DenseNet121 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR25',
 'device': device(type='cuda', index=0),
 'model': {'net': 'DenseNet121'},
 'optimizer': {'args': {'T_max': 200},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': True,
 'trainer': {'epochs': 200,
             'val_per_epochs': 5}}

-- Performance --

|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_acc', 'mean') | 0.9139 | 0.8748 |  0.9167 |    0.9356 |
| ('test_acc', 'std')  | 0.0018 | 0.0018 |  0.0017 |    0.0013 |


|                      |    BCE |    EXP |   Hinge |   ensLoss |
|:---------------------|-------:|-------:|--------:|----------:|
| ('test_auc', 'mean') | 0.9733 | 0.946  |  0.9729 |    0.9815 |
| ('test_auc', 'std')  | 0.0005 | 0.0013 |  0.0006 |    0.0009 |

-- Testing --

|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0006 |  -8.267  | less          |
|  6 | Hinge | ensLoss |   0.0007 |  -7.858  | less          |
|  9 | EXP   | ensLoss |   0      | -34.4488 | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9994 |  -8.267  | greater       |
|  6 | Hinge | ensLoss |   0.9993 |  -7.858  | greater       |
|  9 | EXP   | ensLoss |   1      | -34.4488 | greater       |
|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.0018 |  -6.0917 | less          |
|  6 | Hinge | ensLoss |   0.0012 |  -6.8056 | less          |
|  9 | EXP   | ensLoss |   0      | -37.247  | less          |


|    | A     | B       |   pvalue |     stat | alternative   |
|---:|:------|:--------|---------:|---------:|:--------------|
|  3 | BCE   | ensLoss |   0.9982 |  -6.0917 | greater       |
|  6 | Hinge | ensLoss |   0.9988 |  -6.8056 | greater       |
|  9 | EXP   | ensLoss |   1      | -37.247  | greater       |
