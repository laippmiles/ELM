from numpy import nonzero, exp, zeros,shape,sin, tile, power, multiply,column_stack, mat

def getH(tempH,Type):
    shapeOfH = list(shape(tempH))
    H = zeros((shapeOfH[0], shapeOfH[1]))

    if Type == 'sig':
        H = 1 / (1 + exp(-tempH))
    elif Type == 'hardlim':
        tempH[ list(nonzero( tempH.A > 0 ))[0] ] = 1
        tempH[ list(nonzero( tempH.A <=0 ))[0] ] = 0
        H = tempH
    elif Type == 'tribas':
        for i in range(shapeOfH[0]):
            for j in range(shapeOfH[1]):
                if ((tempH[i,j] <= -1) and (tempH[i,j] >= 1)):
                    H[i,j] = 1 - abs(tempH[i,j])
        H = tempH
    elif Type == 'sin':
        H = sin(tempH)
    # 到这是numberofHiddenNeurons*numOfData
    return H

def getRBF(X,inputWeight,biasOfHiddenNeurons,numberofHiddenNeurons):
    numOfData = list(shape(X))[0]
    numOfFeature = list(shape(X))[1]
    for i in range(numberofHiddenNeurons):
        weight = inputWeight[i,:]
        weightMatrix = tile(weight, (numOfData,1))
        temp = power((X - weightMatrix),2) + 2 * -1
        tempV = zeros((numOfData,1))
        #到这是numOfData*numOfFeature
        for j in range(numOfFeature):
            tempV += temp[:,j]
        if i == 0:
            V = tempV
        else:
            V = column_stack((V,tempV))
    biasMatrix = tile(biasOfHiddenNeurons, (1,numOfData))
    V = multiply(V,biasMatrix.T)
    H = mat(exp(V).T)
    # 到这是numOfData*numberofHiddenNeurons
    return H