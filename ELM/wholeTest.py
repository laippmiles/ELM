from ELMCrossVvalidation import ELMCrossVvalidation
from numpy import shape
from matrix2CSV import matrix2CSV, CSVDeleteSpace
from mailToMe import mailToMe
#写文件名要用的
from datetime import datetime
from re import sub
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


subjectName = 'TestAnawer_' + sub('[:.\s]','_',str(datetime.now()))
fileName = subjectName + '.csv'
filePath = r'D:\桌面\ELM' + '\\'
matrix2CSV(['Gmean'],filePath+fileName)
for i in range(list(shape(Rn))[0]):
    matrix2CSV(Rn[i],filePath+fileName)
#写入CSV的示例
CSVDeleteSpace(filePath+fileName)

subject = subjectName
content = '暂时HelloWorld'
mailToMe(subject,content,filePath,fileName)