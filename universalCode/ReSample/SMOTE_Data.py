from loadData import loadData
from ELMDataStruct import ELMDataStruct
from numpy import column_stack, row_stack, shape, zeros, ones, mat
from array2CSV import array2CSV_Once
from SMOTE import Smote
import random

def SMOTEData(trainStr):
    names = locals()
    for nameOfClass in range(trainStr.numOfClass):
        names['indexOfClass_%s' % nameOfClass] = []
    for i in range(trainStr.numOfData):
        for j in range(trainStr.numOfClass):#range（x）里头包含0~（x-1）的迭代对象
            if trainStr.y[i] == j+1 :
                names['indexOfClass_%s' % j] .append(i)

    for i in range(trainStr.numOfData):
        for nameOfClass in range(trainStr.numOfClass):  # range（x）里头包含0~（x-1）的迭代对象
            if i in names['indexOfClass_%s' % nameOfClass]:
                data = column_stack((trainStr.y[i],trainStr.X[i,:]))
                if  'Class_'+str(nameOfClass) not in locals().keys():
                    names['Class_%s' % nameOfClass] = data
                else:
                    names['Class_%s' % nameOfClass] = row_stack((names['Class_%s' % nameOfClass] , data))
                #到这names['Class_%s' % nameOfClass]是矩阵

    for nameOfClass in range(trainStr.numOfClass):
        #array2CSV_Once(names['Class_%s' % nameOfClass][1:list(shape(names['Class_%s' % nameOfClass]))[0],:].A,[],filename =(str(nameOfClass+1)+'.csv'))
        classNumofData = list(shape(names['Class_%s' % nameOfClass]))[0]
        if classNumofData < (trainStr.numOfData * 0.2):
            print(nameOfClass,':',classNumofData)
            print(trainStr.numOfData)
            s = Smote(names['Class_%s' % nameOfClass][:, 1:list(shape(names['Class_%s' % nameOfClass]))[1]], N=300, k=int(classNumofData / 3))
            resampleData = s.over_sampling()
            numOfResampleData = list(shape(resampleData))[0]
            resampleDataLalel = ones((numOfResampleData,1)) * (nameOfClass+1)
            resampleData = column_stack((resampleDataLalel, resampleData))
            names['Class_%s' % nameOfClass] = row_stack((names['Class_%s' % nameOfClass] , resampleData))
            #array2CSV_Once(names['Class_%s' % nameOfClass][1:list(shape(names['Class_%s' % nameOfClass]))[0],:].A,[],filename =(str(nameOfClass+1)+'res.csv'))
    for nameOfClass in range(trainStr.numOfClass):
        if nameOfClass == 0:
            dataAfterResample = names['Class_%s' % nameOfClass]
        else:
            dataAfterResample = row_stack((dataAfterResample,names['Class_%s' % nameOfClass]))
        #print(dataAfterResample)
    #array2CSV_Once(dataAfterResample.A,[],filename ='afterRes.csv')

    numOfDataAfterResample = list(shape(dataAfterResample))[0]
    indexShuffle = list(range(numOfDataAfterResample))
    #print(indexShuffle)
    random.shuffle(indexShuffle)
    #print(indexShuffle)

    for index in indexShuffle:
        if 'dataOutput' not in locals().keys():
            dataOutput = dataAfterResample[index,:]
        else:
            dataOutput = row_stack((dataOutput, dataAfterResample[index,:]))
    #array2CSV_Once(dataOutput.A, [], filename='afterRes_shuffle.csv')
    #print(type(dataOutput))
    return dataOutput
#以下为测试代码
'''train = loadData()[0]
trainStr = ELMDataStruct(train)
SMOTEData(trainStr)'''
