from WELM import *
from ELM import *
def ELMCrossVvalidation(name,type, numberofHiddenNeurons = 50, C = 64):
    CrossVvalidatioNum = 5
    totalAcc = 0
    totalGmean = 0
    totalTrainTime = 0
    for i in range(CrossVvalidatioNum):
        k = i+1
        acc, gmean, Rn, trainTime = WELM(name, numberofHiddenNeurons,type, C,i=k)
        #acc, gmean, Rn, trainTime = ELM('WWP509_2017', 145,  i=k)
        totalAcc += acc
        totalGmean += gmean
        totalTrainTime += trainTime
        if i == 0 :
            totalRn = Rn
        else:
            totalRn += Rn

    totalAcc /= CrossVvalidatioNum
    totalGmean /= CrossVvalidatioNum
    totalTrainTime /= CrossVvalidatioNum
    #print('totalAcc:',totalAcc)
    #print('totalGmean:',totalGmean)
    #print('totalTrainTime:',totalTrainTime)
    for i in range(list(shape(totalRn))[0]):
            totalRn[i] /= CrossVvalidatioNum
            #print('totalR', i+1 ,':',totalRn[i])
    return totalAcc, totalGmean, totalTrainTime, totalRn
