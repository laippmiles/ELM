from ELMDataStruct import ELMDataStruct
from csv2ListOrMatrix import csv2ListOrMatrix
def loadDataToTest(name = 'Haberman'):
    path = r'D:\桌面\ELM\dataSet' + '\\' + name
    trainSet = '\\' + name + '-train' + str(1) + '.csv'
    testSet = '\\' + name + '-test' + str(1) + '.csv'
    train = csv2ListOrMatrix(path + trainSet)
    test = csv2ListOrMatrix(path + testSet)
    trainStr = ELMDataStruct(train)
    testStr = ELMDataStruct(test)
    return trainStr,testStr