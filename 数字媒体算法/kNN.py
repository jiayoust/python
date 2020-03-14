# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def EucDist(A,B):
    sumT=0
    if len(A)==len(B):
        length=len(A)
    else:
        return False
    for i in range(length):
        sumT=sumT+(A[i]-B[i])*(A[i]-B[i])
    L=sumT**0.5
    return L

def MahDist(A,B):
    sumT=0
    if len(A)==len(B):
        length=len(A)
    else:
        return False
    for i in range(length):
        sumT=sumT+abs(A[i]-B[i])
    L=sumT
    return L

A1=[5.1,3.5,1.4,0.2] #"setosa"
A2=[4.9,3,1.4,0.2]# "setosa"
A3=[4.7,3.2,1.3,0.2]# "setosa"
A4=[4.6,3.1,1.5,0.2]# "setosa"
A5=[5,3.6,1.4,0.2]# "setosa"

B1=[7,3.2,4.7,1.4]# "versicolor"
B2=[6.4,3.2,4.5,1.5]# "versicolor"
B3=[6.9,3.1,4.9,1.5]# "versicolor"
B4=[5.5,2.3,4,1.3]# "versicolor"
B5=[6.5,2.8,4.6,1.5]# "versicolor"

C1=[6.3,3.3,6,2.5]# "virginica"
C2=[5.8,2.7,5.1,1.9]# "virginica"
C3=[7.1,3,5.9,2.1]# "virginica"
C4=[6.3,2.9,5.6,1.8]# "virginica"
C5=[6.5,3,5.8,2.2]# "virginica"

def getAverA():
    A=[]
    for i in range(4):
        A.append((A1[i]+A2[i]+A3[i]+A4[i]+A5[i])/5)
    return A

def getAverB():
    A=[]
    for i in range(4):
        A.append((B1[i]+B2[i]+B3[i]+B4[i]+B5[i])/5)
    return A

def getAverC():
    A=[]
    for i in range(4):
        A.append((C1[i]+C2[i]+C3[i]+C4[i]+C5[i])/5)
    return A

#####test#####
def test():
    #testA=[5.1,3.8,1.5,0.3]#A类花
    #testA=[5.6,2.5,3.9,1.1]#B类花
    testA=[6.4,3.1,5.5,1.8]#C类花
    #欧氏距离 
    T1=[EucDist(getAverA(),testA),EucDist(getAverB(),testA),EucDist(getAverC(),testA)]
    T2=[MahDist(getAverA(),testA),MahDist(getAverB(),testA),MahDist(getAverC(),testA)]
    flag1,flag2='A','A'
    minT1,minT2=T1[0],T2[0]
    for i in range(2):
        if minT1>T1[i+1]:
            flag1='B'
            minT1=T1[i+1]
        if minT2>T2[i+1]:
            flag2='B'
            minT2=T2[i+1]
    print("欧式距离得出该花的种类是：  ",flag1)
    print("曼哈顿距离得出该花的种类是：",flag2)
    
if __name__ == "__main__":
   test()
