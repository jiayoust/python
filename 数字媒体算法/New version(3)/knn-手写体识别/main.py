# -*- coding: utf-8 -*-

import os
import Picture as OP
import Database as OD
import knn as PA
import csv
import numpy as np

# 基础变量
#标准大小
N = 100
#灰度阈值
color = 150/255

n = 10

#读取原CSV文件
reader = list(csv.reader(open('Data1.csv', encoding = 'utf-8')))
del reader[0]
l = len(reader)
newPic = np.zeros(l*(N*N+1)).reshape(l, (N*N+1))
for item in reader:
    item.pop()
reader = np.array(reader)
if len(reader) != 0:
    newPic[0:len(reader), :] = reader

testFiles = os.listdir(r"./test/")
testPic = OP.GetTestPicture(testFiles)

k = int(input('选取最邻近的K个值(1-10)，K='))


result = PA.CalculateResult(testPic, newPic)

newResult = PA.CalculateWeight(result, n, testFiles,k)