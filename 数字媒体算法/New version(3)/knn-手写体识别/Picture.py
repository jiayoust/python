# -*- coding: utf-8 -*-


import os
from skimage import io
import numpy as np
import knn as PA


N = 100
#Gray threshold 灰度阈值
color = 150/255

STR = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def JudgeEdge(img, length, flag, size):
    '''判断图片切割的边界'''
    for i in range(length):
        #判断是行是列
        if flag == 0:
            #正序判断该行是否有手写数字
            line1 = img[i, img[i,:]<color]
            #倒序判断该行是否有手写数字
            line2 = img[length-1-i, img[length-1-i,:]<color]
        else:
            line1 = img[img[:,i]<color, i]
            line2 = img[img[:,length-1-i]<color,length-1-i]
        #若有手写数字，即到达边界，记录下行
        if len(line1)>=1 and size[0]==-1:
            size[0] = i
        if len(line2)>=1 and size[1]==-1:
            size[1] = length-1-i
        #若上下边界都得到，则跳出
        if size[0]!=-1 and size[1]!=-1:
            break
    return size

def CutPicture(img):
    '''Cut the Picture 切割图象'''
    #初始化新大小
    size = []
    #图片的行数
    length = len(img)
    #图片的列数
    width = len(img[0,:])
    #计算新大小
    size.append(JudgeEdge(img, length, 0, [-1, -1]))
    size.append(JudgeEdge(img, width, 1, [-1, -1]))
    size = np.array(size).reshape(4)
    return img[size[0]:size[1]+1, size[2]:size[3]+1]

def StretchPicture(img):
    '''Stretch the Picture拉伸图像'''
    newImg1 = np.zeros(N*len(img)).reshape(len(img), N)
    newImg2 = np.zeros(N**2).reshape(N, N)
    #对每一行进行拉伸/压缩
    #每一行拉伸/压缩的步长
    temp1 = len(img[0])/N 
    #每一列拉伸/压缩的步长
    temp2 = len(img)/N
    #对每一行进行操作
    for i in range(len(img)):
        for j in range(N):
            newImg1[i, j] = img[i, int(np.floor(j*temp1))]
    #对每一列进行操作
    for i in range(N):
        for j in range(N):
            newImg2[i, j] = newImg1[int(np.floor(i*temp2)), j]
    return newImg2



def GetTestPicture(files):
    '''得到待检测图片并保存'''
    Picture = np.zeros([len(files), N**2])
    #循环所有图片文件
    for i, item in enumerate(files):
        #读取这个图片并转为灰度值
        img = io.imread('./test/'+item, as_grey = True)
        #清除噪音
        img[img>color] = 1
        #将图片进行切割，得到有手写数字的的图像
        img = CutPicture(img)
        #将图片进行拉伸，得到标准大小100x100
        img = StretchPicture(img).reshape(N**2)
        #将图片存入矩阵
        Picture[i, 0:N**2] = img
        #将图片的名字存入矩阵
    return Picture
