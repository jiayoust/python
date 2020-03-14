# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n=int(input('请输入一个数：'))
def fab(n):
    if n<1:
        print('输入有误!')
        return -1
    if n==1 or n==2:
        return 1
    else:
        return fab(n-1)+fab(n-2)
result=[]
for i in range(1,n+1):
    result.append(fab(i))
def fib(n):
    if n==0 or n==1:
        return n
    else:
        temp=fib(n-1)+fib(n-2)
        return temp
for i in range(n):
    print(fib(i+1),end=" ")