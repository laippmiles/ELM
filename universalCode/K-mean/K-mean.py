from loadData import loadData
from ELMDataStruct import ELMDataStruct
from numpy import column_stack,row_stack, shape
import random
from array2CSV import array2CSV_Once
from sklearn.cluster import birch
from sklearn.cluster import KMeans

train = loadData()[0]
trainStr = ELMDataStruct(train)
names = locals()
for nameOfClass in range(trainStr.numOfClass):
    names['indexOfClass_%s' % nameOfClass] = []
for i in range(trainStr.numOfData):
    for j in range(trainStr.numOfClass):  # range（x）里头包含0~（x-1）的迭代对象
        if trainStr.y[i] == j + 1:
            names['indexOfClass_%s' % j].append(i)

for i in range(trainStr.numOfData):
    for nameOfClass in range(trainStr.numOfClass):  # range（x）里头包含0~（x-1）的迭代对象
        if i in names['indexOfClass_%s' % nameOfClass]:
            data = column_stack((trainStr.y[i], trainStr.X[i, :]))
            if 'Class_' + str(nameOfClass) not in locals().keys():
                names['Class_%s' % nameOfClass] = data
            else:
                names['Class_%s' % nameOfClass] = row_stack((names['Class_%s' % nameOfClass], data))
                # 到这names['Class_%s' % nameOfClass]是矩阵

clf = KMeans(n_clusters=2)#大类对半分
for nameOfClass in range(trainStr.numOfClass):  # range（x）里头包含0~（x-1）的迭代对象
    classNumofData = list(shape(names['Class_%s' % nameOfClass]))[0]
    if classNumofData > (trainStr.numOfData * 0.2):
        kmeanMetrix = names['Class_%s' % nameOfClass][:,1:list(shape(names['Class_%s' % nameOfClass]))[1]]
        yKmean = clf.fit_predict(kmeanMetrix)
        for i in range(list(shape(yKmean))[0]):
            if yKmean[i] == 0:
                yKmean[i] = nameOfClass + 1
            else:
                yKmean[i] = trainStr.numOfClass + nameOfClass +1
        #print(yKmean)
        names['Class_%s' % nameOfClass] = column_stack((yKmean, kmeanMetrix))

for nameOfClass in range(trainStr.numOfClass):
    if nameOfClass == 0:
        dataAfterKmean = names['Class_%s' % nameOfClass]
    else:
        dataAfterKmean = row_stack((dataAfterKmean,names['Class_%s' % nameOfClass]))

numOfDataAfterKmean = list(shape(dataAfterKmean))[0]
#print(numOfDataAfterKmean)
indexShuffle = list(range(numOfDataAfterKmean))
#print(indexShuffle)
random.shuffle(indexShuffle)
#print(indexShuffle)

for index in indexShuffle:
    if 'dataOutput' not in locals().keys():
        dataOutput = dataAfterKmean[index,:]
    else:
        dataOutput = row_stack((dataOutput, dataAfterKmean[index,:]))

array2CSV_Once(dataOutput.A, [], filename='Kmean_shuffle.csv')