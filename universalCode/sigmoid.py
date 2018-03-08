def sigmoid(inx):
    #inx是一个数
    from numpy import exp
    return 1.0/(1 + exp(-inx))