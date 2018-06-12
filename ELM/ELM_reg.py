from numpy import ones, linalg, random, tile, shape, max
from getH import getH, getRBF
from time import time

def ELM_reg(train, test,numberofHiddenNeurons,ActivationFunction):
    i = 0
    #0:BOD   1:COD

    train_X = train[:,2:]
    train_y = train[:,i]#预测BOD
    [train_numOfData,train_numOfFeature] = list(shape(train_X))

    test_X = test[:,2:]
    test_y = test[:,i]
    test_numOfData = list(shape(test_X))[0]

    beginTrainTime = time()
    inputWeight = random.random(size=(numberofHiddenNeurons, train_numOfFeature))*2-1
    biasOfHiddenNeurons = random.random(size=(numberofHiddenNeurons, 1))
    tempH = inputWeight * train_X.T
    biasMatrix = tile(biasOfHiddenNeurons,(1,train_numOfData))
    tempH = tempH + biasMatrix
    #到tempH为止size是（隐含层节点数，样本数）
    print('ActivationFunction:',ActivationFunction)
    if ActivationFunction == 'rbf':
        H = getRBF(train_X,inputWeight,biasOfHiddenNeurons,numberofHiddenNeurons)
    else:
        H = getH(tempH,ActivationFunction)
    outputWeight = (linalg.pinv(H.T) * train_y)
    #outputWeight的尺寸：（NumberofHiddenNeurons，numOfClass）
    endTrainTime = time()
    trainTime = endTrainTime - beginTrainTime

    tempTest = inputWeight * test_X.T
    biasMatrixTest = tile(biasOfHiddenNeurons, (1, test_numOfData))
    tempTest = tempTest + biasMatrixTest
    if ActivationFunction == 'rbf':
        H_test = getRBF(train_X,inputWeight,biasOfHiddenNeurons,numberofHiddenNeurons)
    else:
        H_test = getH(tempTest,ActivationFunction)
    Y = (H_test.T * outputWeight).A

    target = [1.5, 2.1, 3.3, -4.7, -2.3, 0.75]
    prediction = [0.5, 1.5, 2.1, -2.2, 0.1, -0.5]

    error = []
    for i in range(test_numOfData):
        error.append(test_y[i] - Y[i])

    #print("Errors: ", error)
    #print(error)
    #print(Y)
    squaredError = []
    absError = []
    for val in error:
        squaredError.append(val * val)  # target-prediction之差平方
        absError.append(abs(val))  # 误差绝对值

    #print("Square Error: ", squaredError)
    #print("Absolute Value of Error: ", absError)
    MSE = sum(squaredError) / len(squaredError)
    print("MSE = ", MSE)  # 均方误差MSE

    from math import sqrt
    RMSE = sqrt(sum(squaredError) / len(squaredError))
    print("RMSE = ", RMSE)  # 均方根误差RMSE
    MAE = sum(absError) / len(absError)
    print("MAE = ", MAE)  # 平均绝对误差MAE

    return MSE,RMSE,MAE,trainTime