from ELMCrossVvalidation import ELMCrossVvalidation
from numpy import shape, savetxt, array
from matrix2CSV import matrix2CSV
wholeTestNum = 10
acc = 0
gmean = 0
trainTime = 0

for i in range(wholeTestNum):
    totalAcc, totalGmean, totalTrainTime, totalRn = ELMCrossVvalidation(20,64)
    if i ==0 :
        Rn = totalRn
    else:
        Rn += totalRn
    acc +=totalAcc
    gmean += totalGmean
    trainTime += totalTrainTime

print('-'*10,'Acc:',acc/wholeTestNum,'-'*10)
print('-'*10,'Gmean:',gmean/wholeTestNum,'-'*10)
print('-'*10,'TrainTime:',trainTime/wholeTestNum,'-'*10)
for i in range(list(shape(Rn))[0]):
    Rn[i] /= wholeTestNum
    print('totalR', i + 1, ':', Rn[i])

matrix2CSV(Rn,['gmean'])