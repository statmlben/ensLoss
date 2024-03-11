#!/bin/bash
# ResNet
python main_image.py -B=128 -e=30 -F="PCam" -N="ResNet18" -R=5 --log
python main_image.py -B=128 -e=30 -F="PCam" -N="ResNet34" -R=5 --log
# VGG
python main_image.py -B=128 -e=30 -F="PCam" -N="VGG16" -R=5 --log
python main_image.py -B=128 -e=30 -F="PCam" -N="VGG19" -R=5 --log
# # MobileNet
# python main_image.py -B=128 -e=30 -F="PCam" -N="MobileNet" -R=3 --log
# python main_image.py -B=128 -e=30 -F="PCam" -N="MobileNetV2" -R=3 --log
# # DenseNet
# python main_image.py -B=128 -e=30 -F="PCam" -N="DenseNet121" -R=3 --log
# python main_image.py -B=128 -e=30 -F="PCam" -N="DenseNet169" -R=3 --log

