from loadData import loadData
from ELMDataStruct import ELMDataStruct
from numpy import column_stack, row_stack, shape,zeros
from array2CSV import array2CSV_Once

def SMOTEData(trainStr):
    names = locals()
    for nameOfClass in range(trainStr.numOfClass):
        names['indexOfClass_%s' % nameOfClass] = []
        names['Class_%s' % nameOfClass] = zeros((1, (trainStr.numOfFeature+1) ))
    for i in range(trainStr.numOfData):
        for j in range(trainStr.numOfClass):#range（x）里头包含0~（x-1）的迭代对象
            if trainStr.y[i] == j+1 :
                names['indexOfClass_%s' % j] .append(i)

    for i in range(trainStr.numOfData):
        for nameOfClass in range(trainStr.numOfClass):  # range（x）里头包含0~（x-1）的迭代对象
            if i in names['indexOfClass_%s' % nameOfClass]:
                data = column_stack((trainStr.y[i],trainStr.X[i,:]))
                names['Class_%s' % nameOfClass] = row_stack((names['Class_%s' % nameOfClass] , data))
                #到这names['Class_%s' % nameOfClass]是矩阵

    for nameOfClass in range(trainStr.numOfClass):
        array2CSV_Once(names['Class_%s' % nameOfClass][1:list(shape(names['Class_%s' % nameOfClass]))[0],:].A,[],filename =(str(nameOfClass+1)+'.csv'))

#以下为测试代码
train = loadData()[0]
trainStr = ELMDataStruct(train)
SMOTEData(trainStr)