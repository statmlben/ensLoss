#!/bin/bash

## CIFAR
filename="CIFAR"
for ((u=0; u<10; u++)); do
    for ((v=u+1; v<10; v++)); do
        filename_tmp="${filename}${u}${v}"
        python main_image.py -B=128 -e=200 -F="$filename_tmp" -N="MobileNet" -R=5 --log
        python main_image.py -B=128 -e=200 -F="$filename_tmp" -N="MobileNetV2" -R=5 --log
    done
done

# nohup bash ./runs_cifar_mobilenet.sh >/dev/null 2>&1 &
