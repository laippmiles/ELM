from aWholeTest import aWholeTest
from matrix2CSV import matrix2CSV, CSVDeleteSpace
from csv2ListOrMatrix import csv2ListOrMatrix
from numpy import shape, zeros
from Mail import mailFromLZY
#写文件名要用的
from datetime import datetime
from re import sub
numberofHiddenNeuronsList = list(range(5,10,5))
CParaList = list(range(0,2)) ; CList = []
for i in range(len(CParaList)):
    CList.append(2**CParaList[i])

# 载入数据
subjectName = 'TestAnawer_' + sub('[:.\s]', '_', str(datetime.now()))
fileName = subjectName + '.csv'
filePath = r'D:\桌面\ELM' + '\\'

name = 'WWP509_2017'
info1 = ['name', name]
matrix2CSV(info1, filePath + fileName)

Wtype = 'W1'
info2 = ['WType', Wtype]
matrix2CSV(info2, filePath + fileName)

ActivationFunction = 'sig'
info3 = ['ActivationFunction', ActivationFunction]
matrix2CSV(info3, filePath + fileName)

for i in range(len(numberofHiddenNeuronsList)):
    for j in range(len(CList)):
        print(numberofHiddenNeuronsList[i],CList[j])
        acc, gmean, trainTime, Rn = aWholeTest(name, Wtype, numberofHiddenNeuronsList[i], CList[j])
        if i == 0 and j == 0:
            nameList = ['NumberofHiddenNeurons', 'C', 'trainTime', 'acc', 'Gmean']
            for Ri in range(list(shape(Rn))[0]):
                nameList.append('R'+str(Ri+1))
            matrix2CSV(nameList, filePath + fileName)
        answer = zeros((5+list(shape(Rn))[0]))
        answer[0] = numberofHiddenNeuronsList[i]
        answer[1] = CList[j]
        answer[2] = trainTime
        answer[3] = acc
        answer[4] = gmean
        for ans in range(list(shape(Rn))[0]):
            answer[5+ans] = Rn[ans]
        matrix2CSV(answer, filePath + fileName)

#写入CSV的示例
CSVDeleteSpace(filePath+fileName)

subject = '笨蛋，你的实验跑完了。'
content = '赶快回来。'
mailFromLZY(subject,content,filePath,fileName)