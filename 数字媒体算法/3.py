# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:39:39 2019

@author: Administrator
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import math

def create_data():
    iris=load_iris()
    df=pd.DataFrame(iris.data,columns=iris.feature_names)
    df['label']=iris.target
    df.columns=['sepal length','sepal with','petal length','petal  width','label']
    data=np.array(df.iloc[:100,:])
   # print(data)
    return data[:,:-1],data[:,-1]
X,y=create_data()
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)

class NaiveBayes:
    def _init_(self):
        self.model=None
    def mean(self,X):
        return sum(X)/float(len(X))
    def stdev(self,X):
        avg=self.mean(X)
        return math.sqrt(sum([pow(x-avg,2)for x in X])/float(len(X)))
    def gaussian_probability(self,x,mean,stdev):
        exponent=math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
        return (1/(math.sqrt(2*math.pi)*stdev))*exponent
    def summarize(self,train_data):
        summarize=[(self.mean(i),self.stdev(i)) for i in zip(*train_data)]
        return summarize
    def fit(self,X,y):
        labels=list(set(y))
        data={label:[] for label in labels}
        for f,label in zip(X,y):
            data[label].append(f)
        self.model = {label:self.summarize(value) for label,value in data.items()}
        return 'guassianNB train done!'
    def calculate_probabilities(self,input_data):
        probabilities={}
        for label,value in self.model.items():
            probabilities[label]=1
            for i in range(len(value)):
                mean,stdev=value[i]
                probabilities[label]*=self.gaussian_probability(input_data[i],mean,stdev)
        return probabilities
    def predict(self,X_test):
        label=sorted(self.calculate_probabilities(X_test).items(),key=lambda x: x[-1])[-1][0]
        return label
    def score(self,X_test,y_train):
        right=0
        for X,y in zip(X_test,y_test):
            label=self.predict(X)
            if label==y:
                right+=1
        return right/float(len(X_test))
model=NaiveBayes()
model.fit(X_train,y_test)
print(model.score(X_test,y_test))
print(model.predict([4.4, 3.2, 1.3, 0.2]))
    
    
            
            
            
    
        