from ELMDataStruct import ELMDataStruct
from numpy import ones, linalg, random, tile, shape, max
from getH import getH, getRBF
from csv2ListOrMatrix import csv2ListOrMatrix
from evaluation import accuracy, G_mean
from time import time

def ELM(numberofHiddenNeurons,train, test,ActivationFunction,baseclasser = False):

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
    tempH = inputWeight * trainStr.X.T
    biasMatrix = tile(biasOfHiddenNeurons,(1,trainStr.numOfData))
    tempH = tempH + biasMatrix
    #到tempH为止size是（隐含层节点数，样本数）
    print('ActivationFunction:',ActivationFunction)
    if ActivationFunction == 'rbf':
        H = getRBF(trainStr.X,inputWeight,biasOfHiddenNeurons,numberofHiddenNeurons)
    else:
        H = getH(tempH,ActivationFunction)
    outputWeight = (linalg.pinv(H.T) * trainStr.labelsMatrix.T)
    #outputWeight的尺寸：（NumberofHiddenNeurons，numOfClass）
    endTrainTime = time()
    trainTime = endTrainTime - beginTrainTime

    tempTest = inputWeight * testStr.X.T
    biasMatrixTest = tile(biasOfHiddenNeurons, (1, testStr.numOfData))
    tempTest = tempTest + biasMatrixTest
    if ActivationFunction == 'rbf':
        H_test = getRBF(testStr.X,inputWeight,biasOfHiddenNeurons,numberofHiddenNeurons)
    else:
        H_test = getH(tempTest,ActivationFunction)
    Y = (H_test.T * outputWeight).A
    answer = ones((testStr.numOfData, 1))
    for k in range(testStr.numOfData):
        answer[k, 0] = (Y[k, :].tolist().index(max(Y[k, :]))) + 1

    acc = accuracy(answer,testStr.y)
    print('trainTime:',trainTime)
    gmean, Rn = G_mean(answer,testStr.y,testStr.numOfClass)
    if baseclasser == True:
        return answer
    else:
        return acc , gmean, Rn, trainTime
