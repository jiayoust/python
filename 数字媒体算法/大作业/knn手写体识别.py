from os import listdir
from numpy import *
import numpy as np
import operator
import datetime
def KNN(test_data,train_data,train_label,k):
    dataSetSize = train_data.shape[0]
    all_distances = np.sqrt(np.sum(np.square(tile(test_data, (dataSetSize, 1)) - train_data), axis=1))
    sort_distance_index = all_distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = train_label[sort_distance_index[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
def img2vector(filename):
    returnVect = []
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect.append(int(lineStr[j]))
    return returnVect
def classnumCut(fileName):
    fileStr = fileName.split('.')[0]
    classNumStr = int(fileStr.split('_')[0])
    return classNumStr
def trainingDataSet():
    train_label = []
    trainingFileList = listdir('training')
    m = len(trainingFileList)
    train_data = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        train_label.append(classnumCut(fileNameStr))
        train_data[i,:] = img2vector('training/%s' % fileNameStr)
    return train_label,train_data
def main():
    t1 = datetime.datetime.now()
    Nearest_Neighbor_number = int(input('选取最邻近的K个值，K='))
    train_label,train_data = trainingDataSet()
    testFileList = listdir('test')
    error_sum = 0
    test_number = len(testFileList)
    for i in range(test_number):
        fileNameStr = testFileList[i]
        classNumStr = classnumCut(fileNameStr)
        test_data = img2vector('test/%s' % fileNameStr)
        classifierResult = KNN(test_data, train_data, train_label, Nearest_Neighbor_number)
        print ("第",i+1,"组：","预测值:",classifierResult,"真实值:",classNumStr)
        if (classifierResult != classNumStr):
            error_sum += 1.0
    print ("\n测试集总数为:",test_number)
    print ("测试出错总数:",error_sum)
    print ("\n错误率:",error_sum/float(test_number)*100,'%')
    t2 = datetime.datetime.now()
    print('耗 时 = ', t2 - t1)
if __name__ == "__main__": main()

