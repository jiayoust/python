# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:13:40 2019

@author: Administrator
"""
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def create_data():
    iris=load_iris()
    df=pd.DataFrame(iris.data,columns=iris.feature_names)
    df['label']=iris.target
    df.columns=['sepal length','sepal with','petal length','petal  width','label']
    data=np.array(df.iloc[:100,:])
    print(data)
    return data[:,:-1],data[:,-1]
X,y=create_data()
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)

from sklearn.naive_bayes import GaussianNB

clf=GaussianNB()
clf.fit(X_train,y_train)
print(clf.score(X_test,y_test))
print(clf.predict([[4.4, 3.2, 1.3, 0.2]]))
    
