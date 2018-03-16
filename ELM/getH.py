from numpy import nonzero, exp, zeros,shape,sin

def getH(tempH,type = 'sig'):
    shapeOfH = list(shape(tempH))
    H = zeros((shapeOfH[0], shapeOfH[1]))

    if type == 'sig':
        H = 1 / (1 + exp(-tempH))
    elif type == 'hardlim':
        tempH[ list(nonzero( tempH.A > 0 ))[0] ] = 1
        tempH[ list(nonzero( tempH.A <=0 ))[0] ] = 0
        H = tempH
    elif type == 'tribas':
        for i in range(shapeOfH[0]):
            for j in range(shapeOfH[1]):
                if ((tempH[i,j] <= -1) and (tempH[i,j] >= 1)):
                    H[i,j] = 1 - abs(tempH[i,j])
        H = tempH
    elif type == 'sin':
        H = sin(tempH)
    return H