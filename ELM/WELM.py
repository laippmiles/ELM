from ELMDataStruct import ELMDataStruct
from numpy import ones, linalg, random, tile, exp, max, zeros, eye, shape
from getH import getH
from csv2ListOrMatrix import csv2ListOrMatrix
from evaluation import accuracy, G_mean
from time import time
def WELM(numberofHiddenNeurons,train, test, type='W1',ActivationFunction = 'sig', C = 64,baseclasser = False):

    if baseclasser == False:
        trainStr = ELMDataStruct(train)
        testStr = ELMDataStruct(test)
    else:
        trainStr = train
        testStr = test
    #(trainStr.labelsMatrix)
    #print(testStr.labelsMatrix)
    beginTrainTime = time()
    inputWeight = random.random(size=(numberofHiddenNeurons, trainStr.numOfFeature))*2-1
    biasOfHiddenNeurons = random.random(size=(numberofHiddenNeurons, 1))
    W = getWMatrix(trainStr.y,trainStr.numOfData,trainStr.dataClassStatus,type)
    tempH = inputWeight * trainStr.X.T
    biasMatrix = tile(biasOfHiddenNeurons,(1,trainStr.numOfData))
    tempH = tempH + biasMatrix
    #到tempH为止size是（隐含层节点数，样本数）
    H = getH(tempH, ActivationFunction)
    tempWeight = H * W * H.T
    tempEye = eye(list(shape(tempWeight))[0])
    outputWeight = linalg.pinv(tempWeight/C + H * W * H.T) * H * W * trainStr.labelsMatrix.T
    #outputWeight的尺寸：（NumberofHiddenNeurons，numOfClass）
    endTrainTime = time()
    trainTime = endTrainTime - beginTrainTime

    tempTest = inputWeight * testStr.X.T
    biasMatrixTest = tile(biasOfHiddenNeurons, (1, testStr.numOfData))
    tempTest = tempTest + biasMatrixTest
    H_test = getH(tempTest, ActivationFunction)
    Y = (H_test.T * outputWeight).A
    answer = ones((testStr.numOfData, 1))
    for k in range(testStr.numOfData):
        answer[k, 0] = (Y[k, :].tolist().index(max(Y[k, :]))) + 1
    acc = accuracy(answer,testStr.y)
    print('trainTime:',trainTime)
    gmean ,Rn = G_mean(answer,testStr.y,testStr.numOfClass)
    #print(trainStr.dataClassStatus)
    if baseclasser == True:
        return answer
    else:
        return acc , gmean, Rn, trainTime

def getWMatrix(y,numberofData,dataClassStatus,type = 'W1'):
    D = zeros((numberofData,1))
    numOfClass = len(dataClassStatus)
    if type == 'W1':
        for i in range(numberofData):
            for j in range(numOfClass):
                dataClass = j+1
                if y[i] == dataClass:
                    D[i] = 1/dataClassStatus[dataClass]
    else:#W2法
        avg = int(numberofData / numOfClass)
        for i in range(numberofData):
            for j in range(numOfClass):
                dataClass = j+1
                if y[i] == dataClass:
                    if dataClassStatus[dataClass] > avg:
                        D[i] = 0.618/dataClassStatus[dataClass]
                    else:
                        D[i] = 1 / dataClassStatus[dataClass]
    W = zeros((numberofData,numberofData))
    for i in range(numberofData):
        W[i,i] = D[i]
    return W
'''
    DClassStatus = {}
    for k in range(len(D)):
        if D[k,0] not in DClassStatus:
            DClassStatus[D[k,0]] = 1
        else:
            DClassStatus[D[k,0]] += 1
    #print(DClassStatus)
'''
