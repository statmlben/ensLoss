
#### CIFAR35 - model: VGG16 ####


-- CONFIG --

{'batch_size': 128,
 'dataset': 'CIFAR35',
 'device': device(type='cuda', index=0),
 'ensLoss_per_epochs': -1,
 'loss_list': ['BCE',
               'Hinge'],
 'model': {'net': 'VGG16'},
 'optimizer': {'args': {'T_max': 100},
               'lr': 0.001,
               'lr_scheduler': 'CosineAnnealingLR',
               'type': 'SGD',
               'weight_decay': 0.0005},
 'save_model': False,
 'trainer': {'epochs': 100,
             'val_per_epochs': 5}}

-- Performance --

|                      |   BCE+ensLoss |   Hinge+ensLoss |
|:---------------------|--------------:|----------------:|
| ('test_acc', 'mean') |        0.7818 |          0.7923 |
| ('test_acc', 'std')  |        0.0018 |          0.0022 |


|                      |   BCE+ensLoss |   Hinge+ensLoss |
|:---------------------|--------------:|----------------:|
| ('test_auc', 'mean') |        0.8645 |          0.8742 |
| ('test_auc', 'std')  |        0.0024 |          0.0031 |

-- Testing --

| A   | B   | pvalue   | stat   | alternative   |
|-----|-----|----------|--------|---------------|


| A   | B   | pvalue   | stat   | alternative   |
|-----|-----|----------|--------|---------------|
| A   | B   | pvalue   | stat   | alternative   |
|-----|-----|----------|--------|---------------|


| A   | B   | pvalue   | stat   | alternative   |
|-----|-----|----------|--------|---------------|
