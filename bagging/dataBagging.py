from loadDataToTest import loadDataToTest
from numpy import zeros, column_stack,mat
from random import uniform
from matrix2CSV import matrix2CSV_Once
def dataBagging(name = 'WWP509_2017'):
    trainStr = loadDataToTest('WWP509_2017')[0]
    baggingDataClass = 0
    baggingData = zeros((trainStr.numOfData,trainStr.numOfFeature))
    baggingLabel = zeros((trainStr.numOfData,1))
    #ID = zeros((trainStr.numOfData,1))
    #baggingID = zeros((trainStr.numOfData,1))

    while (baggingDataClass != trainStr.numOfClass):
        for i in range(trainStr.numOfData):
            randIndex = int(uniform(0, trainStr.numOfData))
            baggingData[i] = trainStr.X[randIndex]
            baggingLabel[i] = trainStr.y[randIndex]
            #baggingID[i] = randIndex+1
        baggingDataClassStatus = {}

        for k in range(trainStr.numOfData):
            if baggingLabel[k, 0] not in baggingDataClassStatus:
                baggingDataClassStatus[baggingLabel[k, 0]] = 1
            else:
                baggingDataClassStatus[baggingLabel[k, 0]] += 1
            baggingDataClass = len(baggingDataClassStatus)

    #outputData = mat(column_stack((baggingLabel,baggingData)))
    #print(type(outputData))
    #print(type(trainStr.X))
    #matrix2CSV_Once(outputData,[])