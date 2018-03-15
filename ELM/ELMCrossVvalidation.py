from WELM import *
from ELM import *
def ELMCrossVvalidation(name,type, numberofHiddenNeurons = 50, C = 64):
    CrossVvalidatioNum = 5
    totalAcc = 0
    totalGmean = 0
    totalTrainTime = 0
    for i in range(CrossVvalidatioNum):
        k = i+1
        path = r'D:\桌面\ELM\dataSet' + '\\' + name
        trainSet = '\\' + name + '-train' + str(k) + '.csv'
        testSet = '\\' + name + '-test' + str(k) + '.csv'
        train = csv2ListOrMatrix(path + trainSet)
        test = csv2ListOrMatrix(path + testSet)

        acc, gmean, Rn, trainTime = WELM(numberofHiddenNeurons, train, test, type, C)
        #acc, gmean, Rn, trainTime = ELM( 145,train, test)
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
    print('CVAcc:',totalAcc)
    print('CVGmean:',totalGmean)
    print('CVTrainTime:',totalTrainTime)
    for i in range(list(shape(totalRn))[0]):
            totalRn[i] /= CrossVvalidatioNum
            print('CVR', i+1 ,':',totalRn[i])
    return totalAcc, totalGmean, totalTrainTime, totalRn

#ELMCrossVvalidation('WWP509_2017','W1', numberofHiddenNeurons = 50, C = 64)