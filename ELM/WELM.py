from ELMDataStruct import ELMDataStruct
from numpy import ones, linalg, random, tile, exp, max, zeros, eye, shape
from csv2ListOrMatrix import csv2ListOrMatrix
from evaluation import accuracy, G_mean
from time import time

def WELM(name, numberofHiddenNeurons, C = 64, i=1):
    path = r'D:\桌面\ELM\dataSet'+ '\\' + name
    trainSet = '\\' + name + '-train' + str(i) + '.csv'
    testSet = '\\' + name + '-test' + str(i) +'.csv'
    train = csv2ListOrMatrix(path + trainSet)
    test = csv2ListOrMatrix(path + testSet)
    trainStr = ELMDataStruct(train)
    testStr = ELMDataStruct(test)
    #(trainStr.labelsMatrix)
    #print(testStr.labelsMatrix)

    beginTrainTime = time()
    inputWeight = random.random(size=(numberofHiddenNeurons, trainStr.numOfFeature))*2-1
    biasOfHiddenNeurons = random.random(size=(numberofHiddenNeurons, 1))
    W = getWMatrix(trainStr.y,trainStr.numOfData,trainStr.dataClassStatus)
    tempH = inputWeight * trainStr.X.T
    biasMatrix = tile(biasOfHiddenNeurons,(1,trainStr.numOfData))
    tempH = tempH + biasMatrix
    #到tempH为止size是（隐含层节点数，样本数）
    H =  1 / (1 + exp(-tempH))
    tempWeight = H * W * H.T
    tempEye = eye(list(shape(tempWeight))[0])
    outputWeight = linalg.pinv(tempWeight/C + H * W * H.T) * H * W * trainStr.labelsMatrix.T
    #outputWeight的尺寸：（NumberofHiddenNeurons，numOfClass）
    endTrainTime = time()
    trainTime = endTrainTime - beginTrainTime

    tempTest = inputWeight * testStr.X.T
    biasMatrixTest = tile(biasOfHiddenNeurons, (1, testStr.numOfData))
    tempTest = tempTest + biasMatrixTest
    H_test = 1 / (1 + exp(-tempTest))
    Y = (H_test.T * outputWeight).A
    answer = ones((testStr.numOfData, 1))
    for k in range(testStr.numOfData):
        answer[k, 0] = (Y[k, :].tolist().index(max(Y[k, :]))) + 1
    acc = accuracy(answer,testStr.y)
    print('trainTime:',trainTime)
    gmean ,Rn = G_mean(answer,testStr.y,testStr.numOfClass)
    #print(trainStr.dataClassStatus)
    return acc , gmean, Rn, trainTime

def getWMatrix(y,numberofData,dataClassStatus):
    D = zeros((numberofData,1))
    for i in range(numberofData):
        for j in range(len(dataClassStatus)):
            dataClass = j+1
            if y[i] == dataClass:
                D[i] = 1/dataClassStatus[dataClass]
    W = zeros((numberofData,numberofData))
    for i in range(numberofData):
        W[i,i] = D[i]


    DClassStatus = {}
    for k in range(len(D)):
        if D[k,0] not in DClassStatus:
            DClassStatus[D[k,0]] = 1
        else:
            DClassStatus[D[k,0]] += 1
    #print(DClassStatus)
    return W