from ELMDataStruct import ELMDataStruct
from numpy import ones, linalg, random, tile, exp, max
from csv2ListOrMatrix import csv2ListOrMatrix
from evaluation import accuracy, G_mean
from time import time

def ELM(name, numberofHiddenNeurons, i=1):
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
    tempH = inputWeight * trainStr.X.T
    biasMatrix = tile(biasOfHiddenNeurons,(1,trainStr.numOfData))
    tempH = tempH + biasMatrix
    #到tempH为止size是（隐含层节点数，样本数）
    H =  1 / (1 + exp(-tempH))
    outputWeight = (linalg.pinv(H.T) * trainStr.labelsMatrix.T)
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
    gmean, Rn = G_mean(answer,testStr.y,testStr.numOfClass)
    return acc , gmean, Rn, trainTime