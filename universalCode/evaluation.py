from numpy import shape, zeros, true_divide
from math import pow
def accuracy(answer,labels):
    error = 0.0
    testDataNum = list(shape(answer))[0]
    for k in range(testDataNum):
        if answer[k, 0] != labels[k, 0]:
            # print('classify:', Answer[k, 0], 'Actral:', testStr.y[k, 0])
            error += 1
    acc = float(1 - error / testDataNum)
    print('acc:', acc)
    return acc

def G_mean(answer, labels, numOfClass):
    error = 0.0
    testDataNum = list(shape(answer))[0]
    TP = zeros((numOfClass,1))
    expectedClass = zeros((numOfClass,1))
    for k in range(testDataNum):
        for j in range(numOfClass):
            Class = j+1
            if (labels[k, 0] == Class):
                expectedClass[j] += 1
                if(answer[k, 0] == Class):
                    TP[j] += 1
    Rn = true_divide(TP , expectedClass)
    R = 1
    for Ri in Rn:
        R = R * Ri
    gmean = pow(R,1/numOfClass)
    #print('TP:', TP)
    #print('expectedClass:', expectedClass)
    #print('gmean:', gmean)
    for i in range(list(shape(Rn))[0]):
        print('R',i+1,':',Rn[i])
    return gmean , Rn