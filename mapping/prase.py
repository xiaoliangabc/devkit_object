#!/usr/bin/python
# -*- coding: UTF-8 -*-

import shutil
import os

# 读取打乱数据
rand_path = '/home/wxl/self_driving/detection_tracking/kitti/detection/devkit_object/mapping/train_rand.txt'
with open(rand_path, "r") as f:
    data = f.read().split(',')
    print(type(data))
print(data[0])

# 图片路径
image_path = '/media/wxl/WXLPassport/Data/kitti/dataset/object/training/image_2/'
file_dir ='./'

#读取mapping数据
mapping_path = '/home/wxl/self_driving/detection_tracking/kitti/detection/devkit_object/mapping/train_mapping.txt'
with open(mapping_path, "r") as f:
    i = 0
    for line in f.readlines():    
        curLine = line.strip().split(" ")
        if curLine[1] == '2011_09_26_drive_0017_sync':
            index = data.index(str(i))
            file_name = str(index).zfill(6)
            file_name += '.png'
            shutil.copy(image_path+file_name, file_dir)
            print(file_name)
            print(curLine)
            print(data.index(str(i)))
            print(i)
            print(data[i])
        i += 1
