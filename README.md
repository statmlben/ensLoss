# 🔂 *EnsLoss*: Stochastic Calibrated Loss Ensembles for Preventing Overfitting in Classification

Empirical risk minimization (ERM) with a computationally feasible surrogate loss is a widely accepted approach for classification. Notably, the surrogate loss is not arbitrary, typically requiring *convexity* and *calibration* (CC) properties to ensure consistency in maximizing accuracy. 

In this project, we propose a novel loss ensemble method, namely **EnsLoss**, which extends the ensemble learning concept to combine losses within the ERM framework. Unlike existing ensemble methods, our method distinctively preserves the "*legitimacy*" of the combined losses, i.e., ensuring the CC properties.

This repo describes a set of experiments that demonstrate the performance of the proposed **EnsLoss** method compared with existing methods based on a *fixed loss function*, and also assess its *compatibility* with other regularization methods.

## Motivation

### {ensemble + CC} losses in SGD
The primary motivation behind consists of two components: **ensemble** and the **calibration** (CC conditions) of the loss functions.

![demo](./fig/demo.png)

### CC losses | CC loss-derivatives

The key observation of SGD is that the *impact of the loss function $\phi$ on SGD is solely reflected in its loss-derivative $\partial \phi$*. We only need to generate the valid loss derivatives; refer to the following figure illustrating the transformation of the CC conditions of losses into loss-derivatives.

![CC](./fig/ensLoss_CC.png)

Hence, it allows us to bypass the generation of loss and directly generate the loss-derivatives in SGD, thereby inspires *doubly stochastic gradients* (i.e., random batch samples and random calibrated loss-derivatives) of our Algorithm.

## Overview of the Experiment

Different **loss functions** can be integrated with **various neural networks** and **regularization methods** to tackle the classification problem across **diverse datasets**. In order to compare the advantages of our proposed method, we have provided reproducible benchmark code and results in this repository.

This repository supports:

- **Data Modes**
  - Tabular data ([main_tab.py](./main_tab.py))
  - Image data ([main_img.py](./main_image.py))
  - Text data ([main_text.py](./main_text.py))

- **Loss** ([losses.py](./losses.py))
  - [x] `ensLoss` (our method)
  - [x] `BCELoss`: binary cross entropy
  - [x] `Hinge`: hinge loss
  - [x] `EXP`: exponential loss
  - [x] `BinFocal`: binary focal loss

- **Model** ([img_models](./img_models/) + [tab_models](./tab_models/) + [text_models](./text_models/))
  - [x] TabMLP\{D\} with different depths `D=1,3,5`
  - [x] VGG: `VGG16`, `VGG19`
  - [x] ResNet: `ResNet18`, `ResNet34`, `ResNet50`, `ResNet101`, `ResNet152`
  - [x] MobileNet: `MobileNet`, `MobileNetV2`
  - [x] DenseNet: `DenseNet121`, `DenseNet161`, `DenseNet169`, `DenseNet201`
  - [x] LSTM: `LSTM`, `BiLSTM`

- **Regularization methods**
  - [x] `dropout` in [ResNet](./img_models/resnet.py)
  - [x] `weight_decay`
  - [x] `data augumentation` in [CIFAR](./loader.py) 

## Benchmarks for Tabular data

This benchmark contain 14 tabular datasets in [openml](https://www.openml.org/). These datasets were selected based on the following filtering criteria: `verified`, `>1000 instances`, `>1000 features`, `binary class`, `dense`, and with at least one official run. The resulting datasets can be found [here](https://www.openml.org/search?type=data&sort=runs&status=active&qualities.NumberOfInstances=between_1000_10000&qualities.NumberOfFeatures=between_1000_10000&qualities.NumberOfClasses=%3D_2&format=ARFF):

| **Dataset**       | **Data ID** | **(n,d) (× 10³)** |
|-------------------|-------------|-------------------|
| Bioresponse       | 4134        | (3.75, 1.78)      |
| guillermo         | 41159       | (20.0, 4.30)      |
| riccardo          | 41161       | (20.0, 4.30)      |
| hiva-agnostic     | 1039        | (4.23, 1.62)      |
| christine         | 41142       | (5.42, 1.64)      |
| OVA-Breast        | 1128        | (1.54, 10.9)      |
| OVA-Uterus        | 1138        | (1.54, 10.9)      |
| OVA-Ovary         | 1166        | (1.54, 10.9)      |
| OVA-Kidney        | 1134        | (1.54, 10.9)      |
| OVA-Lung          | 1130        | (1.54, 10.9)      |
| OVA-Omentum       | 1139        | (1.54, 10.9)      |
| OVA-Colon         | 1161        | (1.54, 10.9)      |
| OVA-Endometrium   | 1142        | (1.54, 10.9)      |
| OVA-Prostate      | 1146        | (1.54, 10.9)      |

### Replicating Restuls
To replicate the benchmark results presented in our paper, please use the following command:
```bash
bash ./sh_files/runs_tab.sh
``` 
Our runing results are publicly avaliable in our W\&B project [ensLoss-tab](https://wandb.ai/bdai/ensLoss-tab?nw=nwuserbdai).

### Customize the Run 
To execute the methods on a dataset, use the following command:
```bash
python main_tab.py -ID=4134
```
Note that the `ID` refers to the dataset ID in OpenML. The runing configuration is included in `main_tab.py`, with the default settings as follows:

```python
config = {
        'dataset' : 4134,
        'model': {'net': 'TabMLP3', 'args': {}},
        'batch_size': 128,
        'save_model': False,
        'ensLoss_per_epochs': -1,
        'trainer': {'epochs': 300, 'val_per_epochs': 10}, 
        'optimizer': {'lr': 1e-4, 'type': 'SGD', 'weight_decay': 5e-6, 
                        'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 300}},
        'device': torch.device("cuda:0" if torch.cuda.is_available() else "cpu")}
```
To customize your experiment, please adjust the parameters in the configuration file.

### Benchmarks for Image data

Benchmarks for Image data contain two dataset: [CIFAR10](https://www.cs.toronto.edu/~kriz/cifar.html) and [PCam](https://github.com/basveeling/pcam).

- We adopted the MHIST dataloader from (https://github.com/srinidhiPY/ICCV-CDPATH2021-ID-8). 

To run the benchmarks available use the following command:

```bash
## run for CIFAR
python main_image.py -B=128 -e=200 -F="CIFAR" -R=3 --no-log
## run for PCam
python main_image.py -B=128 -e=100 -F="PCam" -R=3 --no-log
```

The network config is included in `main_image.py`, and the default setting is:

```python
config = {
        'model': {'net': 'VGG', 'args': {'vgg_name': 'VGG19'}},
        'batch_size': args.batch,
        'trainer': {'epochs': args.epoch, 'val_per_epochs': 10}, 
        'optimizer': {'lr': 1e-3, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}},
        'device': torch.device("cuda:0" if torch.cuda.is_available() else "cpu")}
```
If you need to switch networks, please modify the parameters in the config.

### Model list

- ResNet18, ResNet34, ResNet50, ResNet101, ResNet152
- DenseNet121, DenseNet169, DenseNet201, DenseNet161
- MobileNet, MobileNetV2
- VGG11, VGG13, VGG16, VGG19

## References

- [Train CIFAR10 with PyTorch](https://github.com/kuangliu/pytorch-cifar)

## More obs


