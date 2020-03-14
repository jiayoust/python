# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 13:10:14 2013

@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy as np


def WB(m, Xi, Yi):
    sumX = 0
    sumTop = 0
    sumT = 0
    sumXF = 0
    for i in range(m):
        sumX = sumX + Xi[i]
    xPing = sumX / m
    for i in range(m):
        sumTop = sumTop + Yi[i] * (Xi[i] - xPing)
    for i in range(m):
        sumXF = sumXF + Xi[i] * Xi[i]
    w = sumTop / (sumXF - (1 / m) * (sumX * sumX))

    for i in range(m):
        sumT = sumT + Yi[i] - w * Xi[i]
    b = (1 / m) * sumT
    return w, b


Xi = [8.19, 2.72, 6.39, 8.71, 4.7, 2.66, 3.78]
Yi = [7.01, 2.78, 6.47, 6.71, 4.1, 4.23, 4.05]
w, b = WB(7, Xi, Yi)
print("k=", w, '\n', "b=", b)
plt.scatter(Xi, Yi, color="red", label="Sample Point", linewidth=3)  # 画样本点
x = np.linspace(0, 10, 1000)
y = w * x + b
plt.plot(x, y, color="orange", label="Fitting Line", linewidth=2)  # 画	拟合直线
plt.show()

         
     
     
    