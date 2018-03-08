from matplotlib import pyplot
from numpy import array, shape, arange

def plotData(inputData, inputLabel):
    #arange是numpy里头的函数，返回一个数组，画图要用到
    data = array(inputData)
    numOfData = list(shape(data))[0]
    xcord1 = [] ; ycord1 = []
    xcord2 = [] ; ycord2 = []
    #python中分号基本就这么用了

    for i in range(numOfData):
        if int(inputLabel[i]) == 1:
            #第i个样本是第一类数据
            xcord1.append(inputData[i,0]) ; ycord1.append(inputData[i,1])
        else:
            xcord2.append(inputData[i,0]); ycord2.append(inputData[i, 1])

    fig = pyplot.figure()
    #创建一幅图
    ax = fig.add_subplot(111)
    #只有一幅图
    ax.scatter(xcord1,ycord1, s = 30 , color= 'red',marker= 's')
    #散点尺寸；颜色；样式
    ax.scatter(xcord2, ycord2, s=30, color='blue')
    #画出决策线
    pyplot.xlabel('X1') ; pyplot.ylabel('X2')
    #设定坐标轴名称
    pyplot.show()
    print('show')