from loadData import loadData
from dataBagging import dataBagging
from ELMDataStruct import ELMDataStruct
from numpy import column_stack, shape, zeros, sum
from WELM import WELM
from evaluation import accuracy, G_mean
from time import time
from matrix2CSV import matrix2CSV_Once
def bagging_ELM(name,numberofHiddenNeurons,Type='W1', C = 64):
    train,test = loadData(name)
    shapeOfAnswer = []
    numOfBaseClasser = 10
    trainStr = ELMDataStruct(train)
    testStr = ELMDataStruct(test)
    beginTrainTime = time()
    for i in range(numOfBaseClasser):
        print('Begin %d th train' %(i+1))
        baggingTrain = dataBagging(trainStr)
        baggingTrainStr = ELMDataStruct(baggingTrain)
        answer = WELM(numberofHiddenNeurons, baggingTrainStr, testStr, Type, C,baseclasser=True)
        if i == 0 :
            answerMatrix = answer
            shapeOfAnswer = shape(answer)
        else:
            answerMatrix = column_stack((answerMatrix,answer))
    outputAnswer = zeros((shapeOfAnswer))
    endTrainTime = time()
    trainTime = endTrainTime - beginTrainTime

    #matrix2CSV_Once(answerMatrix,[])
    for j in range(shapeOfAnswer[0]):
        voteAnswer = 1
        maxVoteNum = 0
        for k in range(trainStr.numOfClass):
            voteNum = sum(answerMatrix[j,:] == (k+1))
            if voteNum > maxVoteNum:
                maxVoteNum = voteNum
                voteAnswer = k+1
        outputAnswer[j] = voteAnswer
    #print(outputAnswer)
    #input()
    acc = accuracy(answer, testStr.y)
    print('-'*20,'Bagging result','-'*20)
    print('Bagging trainTime:', trainTime)
    gmean, Rn = G_mean(answer, testStr.y, testStr.numOfClass)
    print('-'*20,'Bagging result','-'*20)
    return acc, gmean, Rn, trainTime