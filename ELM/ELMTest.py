from WELM import *
from ELM import *
testnum = 5
totalAcc = 0
totalGmean = 0
totalTrainTime = 0
for i in range(testnum):
    k = i+1
    acc, gmean, Rn, trainTime = WELM('WWP509_2017',50, C=64,i=k)
    #acc, gmean, Rn, trainTime = ELM('WWP509_2017', 145,  i=k)
    totalAcc += acc
    totalGmean += gmean
    totalTrainTime += trainTime
    if i == 0 :
        totalRn = Rn
    else:
        totalRn += Rn

print('totalAcc:',totalAcc/testnum)
print('totalGmean:',totalGmean/testnum)
print('totalTrainTime:',totalTrainTime/testnum)
for i in range(list(shape(totalRn))[0]):
        print('totalR', i+1 ,':',totalRn[i]/testnum)
