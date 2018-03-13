from ELMCrossVvalidation import ELMCrossVvalidation
from numpy import shape

def aWholeTest(name, type, numberofHiddenNeurons, C):
    wholeTestNum = 10
    acc = 0
    gmean = 0
    trainTime = 0
    for i in range(wholeTestNum):
        totalAcc, totalGmean, totalTrainTime, totalRn = ELMCrossVvalidation(name, type, numberofHiddenNeurons, C)
        if i ==0 :
            Rn = totalRn
        else:
            Rn += totalRn
        acc +=totalAcc
        gmean += totalGmean
        trainTime += totalTrainTime

    acc /= wholeTestNum
    gmean /= wholeTestNum
    trainTime /= wholeTestNum
    print('-'*10,'Acc:',acc,'-'*10)
    print('-'*10,'Gmean:',gmean,'-'*10)
    print('-'*10,'TrainTime:',trainTime,'-'*10)
    for i in range(list(shape(Rn))[0]):
        Rn[i] /= wholeTestNum
        print('totalR', i + 1, ':', Rn[i])

    return acc,gmean,trainTime,Rn
