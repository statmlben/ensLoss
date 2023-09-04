import numpy as np
import pandas as pd
import random
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from scipy.io.arff import loadarff 
from sklearn.datasets import fetch_openml
import os
from torchvision.io import read_image
import torchvision

## lib used for argumentation
import glob
from os.path import exists
from skimage import color
import copy
from skimage.color import rgb2hed
from skimage.color import hed2rgb
from tqdm import tqdm
from torchvision import transforms
from PIL import Image
from albumentations import Compose, Rotate, CenterCrop, HorizontalFlip, RandomScale, Flip, Resize, ShiftScaleRotate, \
    RandomCrop, IAAAdditiveGaussianNoise, ElasticTransform, HueSaturationValue, LongestMaxSize, RandomBrightnessContrast, Blur

## Reproducibility
torch.manual_seed(1024)
random.seed(1024)
np.random.seed(1024)

## train data
class TrainData(Dataset):
    def __init__(self, X_data, y_data):
        self.X_data = X_data
        self.y_data = y_data

    def __getitem__(self, index):
        return self.X_data[index], self.y_data[index]
        
    def __len__ (self):
        return len(self.X_data)

## test data
class TestData(Dataset):
    def __init__(self, X_data):
        self.X_data = X_data
        
    def __getitem__(self, index):
        return self.X_data[index]
        
    def __len__ (self):
        return len(self.X_data)

## Tabular data in openml
def openml_data(random_state=0, data_id=43969):
    dataset = fetch_openml(data_id=data_id)
    target_set = list(set(dataset.target))
    #if condition returns True, then nothing happens:
    assert len(target_set) == 2, "Only binary classification is considered."

    encode_map = {target_set[0]: 0, target_set[1]: 1}

    if data_id == 42395:
        del dataset.data['ID_code']
    X = dataset.data
    y = dataset.target
    y.replace(encode_map, inplace=True)
    
    y = y.loc[~pd.isnull(X).any(axis=1)]
    X = X.loc[~pd.isnull(X).any(axis=1)]
    
    X = X.values
    y = y.values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=random_state)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    train_data = TrainData(torch.FloatTensor(X_train), torch.FloatTensor(y_train))
    test_data = TrainData(torch.FloatTensor(X_test), torch.FloatTensor(y_test))
    return train_data, test_data

## image dataset

# class MHIST_loader(Dataset):
#     def __init__(self, annotations_file, img_dir, label_map={'SSA': 0, 'HP': 1}, partition='train', transform=None):
#         self.img_labels = (pd.read_csv(annotations_file) [lambda df: df['Partition'] == partition])
#         self.label_map = label_map
#         self.img_labels['Majority Vote Label'] = self.img_labels['Majority Vote Label'].map(self.label_map)
#         self.img_dir = img_dir
#         self.transform = transform

#     def __len__(self):
#         return len(self.img_labels)

#     def __getitem__(self, idx):
        
#         img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
#         image = read_image(img_path)
#         label = self.img_labels.iloc[idx, 1]
#         if self.transform:
#             image = self.transform(image)
#         return image, label

def img_data(transform, name='MHIST'):
    if name == 'MHIST':
        train_data = DatasetMHIST_train()
        test_data = DatasetMHIST_test()
        # MHIST_loader(annotations_file='./dataset/MHIST/annotations.csv', img_dir='./dataset/MHIST/images/', partition='test', transform=transform)
    elif name == 'CIFAR':
        # ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
        # 3 (cat) vs 5 (dog)
        # 2 (bird) vs 4 (deer)
        # 1 (automobile) vs 9 (truck)
        binary_class_list = [2, 4]
        trainset = torchvision.datasets.CIFAR10(root='./dataset', train=True,
                                        download=False, transform=transform)
        train_index = [i for i, t in enumerate(trainset.targets) if (t in binary_class_list)]
        train_data = torch.utils.data.Subset(trainset, train_index)

        testset = torchvision.datasets.CIFAR10(root='./dataset', train=False,
                                       download=False, transform=transform)
        test_index = [i for i, t in enumerate(testset.targets) if (t in binary_class_list)]
        test_data = torch.utils.data.Subset(testset, test_index)
        # print(set(train_data.dataset.targets))
        encode_map = {2: 0, 4: 1}
        train_data.dataset.targets = list(map(encode_map.get, train_data.dataset.targets))
        test_data.dataset.targets = list(map(encode_map.get, test_data.dataset.targets))

    elif name == 'PCam':
        pass
    else:
        raise Exception("Sorry, no dataset provided.") 
    return train_data, test_data

############# List of data augmentations for fine-tuning ########################

# def HSV(img):
#     transform = Compose([HueSaturationValue(hue_shift_limit=(-0.1, 0.1), sat_shift_limit=(-1, 1))])
#     Aug_img = transform(image=img)
#     return Aug_img

# def Noise(img):
#     transform = Compose([IAAAdditiveGaussianNoise(loc=0, scale=(0 * 255, 0.1 * 255))])
#     Aug_img = transform(image=img)
#     return Aug_img

# def Scale_Resize_Crop(img):
#     transform = Compose([Rotate(limit=(-90, 90), interpolation=2), RandomScale(scale_limit=(0.8, 1.2), interpolation=2), Resize(img.shape[1] + 20, img.shape[1] + 20, interpolation=2),
#                          RandomCrop(img.shape[1], img.shape[1])])
#     Aug_img = transform(image=img)
#     return Aug_img

# def Shift_Scale_Rotate(img):
#     transform = Compose([HorizontalFlip(), ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.5, rotate_limit=45, interpolation=2),
#                          RandomCrop(img.shape[1], img.shape[1])])
#     Aug_img = transform(image=img)
#     return Aug_img

# def Blur_img(img):
#     transform = Compose([Blur(blur_limit=(3, 7))])
#     Aug_img = transform(image=img)
#     return Aug_img

# def Brightness_Contrast(img):
#     transform = Compose([RandomBrightnessContrast(brightness_limit=(-0.2, 0.2), contrast_limit=(-0.2, 0.2))])
#     Aug_img = transform(image=img)
#     return Aug_img

# def Rotate_Crop(img):
#     transform = Compose([Rotate(limit=(-90, 90), interpolation=2), CenterCrop(img.shape[1], img.shape[1])])
#     Aug_img = transform(image=img)
#     return Aug_img

# def augment_pool():
#     augs = [HSV, Noise, Scale_Resize_Crop, Shift_Scale_Rotate, Blur_img, Brightness_Contrast, Rotate_Crop]
#     return augs

####### MHIST dataset

### MHIST train loader
class DatasetMHIST_train(Dataset):

    def __init__(self, dataset_path='./dataset/MHIST/images/', annot_path='./dataset/MHIST/annotations.csv', image_size=256):

        """
        MHIST dataset class wrapper (train with augmentation)
        """

        self.image_size = image_size

        # Resize images
        self.transform1 = Compose([Resize(image_size, image_size, interpolation=2)])

        # Data augmentations
        self.transform4 = Compose([Rotate(limit=(-90, 90), interpolation=2), CenterCrop(image_size, image_size)])
        self.transform5 = Compose([Rotate(limit=(-90, 90), interpolation=2), RandomScale(scale_limit=(0.8, 1.2), interpolation=2),
                                   Resize(image_size + 20, image_size + 20, interpolation=2), RandomCrop(image_size, image_size)])

        # GT annotation
        GT = pd.read_csv(annot_path, header=None)

        self.datalist = []
        img_paths = glob.glob('{}/*.png'.format(dataset_path))
        with tqdm(enumerate(sorted(img_paths)), disable=True) as t:
            for wj, img_path in t:
                head, tail = os.path.split(img_path)
                img_id = tail  # Get image_id

                # check if it belongs to train/val set
                set = GT.loc[GT[0] == img_id][3]
                label = GT.loc[GT[0] == img_id][1]

                # Add only train/test to the corresponding set
                if set.iloc[0] == 'train':
                    if label.iloc[0] == 'HP':
                        cls_id = 0
                    else:
                        cls_id = 1   # SSA
                    self.datalist.append((img_path, cls_id))
                else:
                    continue

    def __len__(self):
        return len(self.datalist)

    def __getitem__(self, index):

        img = Image.open(self.datalist[index][0]).convert('RGB')

        # label assignment
        label = int(self.datalist[index][1])

        #################
        # Convert PIL image to numpy array
        img = np.array(img)

        # First image
        img = self.transform1(image=img)
        img = Image.fromarray(img['image'])
        img = np.array(img)

        Aug1_img = self.transform4(image=img)
        Aug2_img = self.transform5(image=img)

        # Convert numpy array to PIL Image
        img = Image.fromarray(img)
        # img.show()
        Aug1_img = Image.fromarray(Aug1_img['image'])
        # Aug1_img.show()
        Aug2_img = Image.fromarray(Aug2_img['image'])
        # Aug2_img.show()

        # Convert to numpy array
        img = np.array(img)
        Aug1_img = np.array(Aug1_img)
        Aug2_img = np.array(Aug2_img)

        # Stack along specified dimension
        img = np.stack((img, Aug1_img, Aug2_img), axis=0)

        # Numpy to torch
        img = torch.from_numpy(img)

        # Randomize the augmentations
        shuffle_idx = torch.randperm(len(img))
        img = img[shuffle_idx, :, :, :]

        label = np.array(label)
        label = torch.from_numpy(label)
        label = label.repeat(img.shape[0])

        # Change Tensor Dimension to N x C x H x W
        img = img.permute(0, 3, 1, 2)

        return img, label


##### MHIST test loader
class DatasetMHIST_test(Dataset):

    def __init__(self, dataset_path='./dataset/MHIST/images/', annot_path='./dataset/MHIST/annotations.csv', image_size=256):

        """
        TBLN dataset class wrapper (train with augmentation)
        """

        self.image_size = image_size

        # Resize images
        self.transform1 = Compose([Resize(image_size, image_size, interpolation=2)])

        # GT annotation
        GT = pd.read_csv(annot_path, header=None)

        self.datalist = []
        img_paths = glob.glob('{}/*.png'.format(dataset_path))
        with tqdm(enumerate(sorted(img_paths)), disable=True) as t:
            for wj, img_path in t:
                head, tail = os.path.split(img_path)
                img_id = tail  # Get image_id

                # check if it belongs to train/test set
                set = GT.loc[GT[0] == img_id][3]
                label = GT.loc[GT[0] == img_id][1]

                # Add only train/val to the corresponding set
                if set.iloc[0] == 'test':
                    if label.iloc[0] == 'HP':
                        cls_id = 0
                    else:
                        cls_id = 1   # SSA
                    self.datalist.append((img_path, cls_id))
                else:
                    continue

    def __len__(self):
        return len(self.datalist)

    def __getitem__(self, index):

        img = Image.open(self.datalist[index][0]).convert('RGB')

        # label assignment
        label = int(self.datalist[index][1])

        #################
        # Convert PIL image to numpy array
        img = np.array(img)

        # First image
        img = self.transform1(image=img)
        img = Image.fromarray(img['image'])
        img = np.array(img)

        # Numpy to torch
        img = torch.from_numpy(img)
        label = np.array(label)
        label = torch.from_numpy(label)

        # Change Tensor Dimension to N x C x H x W
        img = img.permute(2, 0, 1)

        return img, label
