from numpy import zeros, column_stack,matrix
from random import uniform
from random import uniform

from numpy import zeros, column_stack, matrix


def dataBagging(trainStr):
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

    outputData = (column_stack((baggingLabel,baggingData)))
    #print(type(outputData))
    #print(type(trainStr.X))
    #matrix2CSV_Once(outputData,[])
    return matrix(outputData)
#dataBagging('WWP509_2017')
#测试指令