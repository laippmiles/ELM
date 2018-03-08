from csv2ListOrMatrix import *
from numpy import matrix, ones, shape, linalg, random, tile, exp, max
NumberofHiddenNeurons = 20
#载入数据
path = r'D:\桌面\ELM\dataSet\diabetes'
trainSet = r'\diabetes-train1.csv'
testSet = r'\diabetes-test1.csv'
train = csv2ListOrMatrix(path + trainSet)
test = csv2ListOrMatrix(path + testSet)
#trainData = train[:,1:]
#trainLabel = train[:,0]
trainData = train[:,1:]
trainLabel = train[:,0]
numOfTrainData = list(shape(trainData))[0]
numOfTrainFeature = list(shape(trainData))[1]
dataClass = []
for k in range(numOfTrainData):
    if trainLabel[k,0] not in dataClass:
        dataClass.append(trainLabel[k,0])
numOfClass = len(dataClass)
temptrainLabel = ones((numOfClass,numOfTrainData)) * -1
for k in range(numOfTrainData):
    i = int(trainLabel[k,0] - 1)
    temptrainLabel[i,k] = 1
print(temptrainLabel)
testData = test[:,1:]
testLabel = test[:,0]
numOftestData = list(shape(testData))[0]

inputWeight = random.random(size=(NumberofHiddenNeurons, numOfTrainFeature))*2-1
biasOfHiddenNeurons = random.random(size=(NumberofHiddenNeurons, 1))
tempH = inputWeight * trainData.T
biasMatrix = tile(biasOfHiddenNeurons,(1,numOfTrainData))
tempH = tempH + biasMatrix
#到tempH为止size是（隐含层节点数，样本数）
#print(shape(tempH))
#print('-'*50)
H =  1 / (1 + exp(-tempH))
outputWeight = (linalg.pinv(H.T) * temptrainLabel.T)
print(shape(outputWeight))

tempTest = inputWeight * testData.T
print(shape(tempTest))
biasMatrixTest = tile(biasOfHiddenNeurons,(1,numOftestData))
print(shape(biasMatrixTest))
tempTest = tempTest + biasMatrixTest
H_test = 1 / (1 + exp(-tempTest))
Y = (H_test.T * outputWeight).A
Answer = ones((numOftestData,1))
for k in range(numOftestData):
    Answer[k,0] = (Y[k,:].tolist().index(max(Y[k,:])))+1
error = 0.0
for k in range(numOftestData):
    if Answer[k,0] != testLabel[k,0]:
        print('classify:',Answer[k,0], 'Actral:',testLabel[k,0])
        error += 1
print('acc:', float(1-error/numOftestData))