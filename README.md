# 🔂 *ensLoss*: Stochastic Calibrated Loss Ensembles for Preventing Overfitting in Classification
ecSGD (ensemble calibrated SGD) is a ensemble method bagging random classification surrogate losses.

## Results

In binary classification, different loss functions can be combined with various neural networks to solve the problem. In order to compare the advantages of our proposed method, we have provided reproducible benchmark code and results in this repository.

### Dependencies

For all benchmarks, it is necessary to install the following packages.

```bash
pip install pytorch
```

### Benchmarks for Tabular data

Benchmarks for Tabular data contain various dataset in [openml](https://www.openml.org/).

To run the benchmarks available use the following command:

```bash
python main_image.py -B=128 -e=200 -ID=43969 -R=3 --no-log
```
Note that `ID` is the `openml` dataset ID. 

The network config is included in `main_tab.py`, and the default setting is:

```python
    config = {
            'model': {'net': 'TabMLP5', 'args': {'H': 256}},
            'batch_size': args.batch,
            'trainer': {'epochs': args.epoch, 'val_per_epochs': 10}, 
            'optimizer': {'lr': 1e-4, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 1./3, 'total_iters': 1}},
            'device': torch.device("cuda:0" if torch.cuda.is_available() else "cpu")}
```
If you need to switch networks, please modify the parameters in the config.


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


