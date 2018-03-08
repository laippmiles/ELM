from pickle import dump,load
from shutil import move
def saveFile(data,newpath,fileName):
    fw = open(fileName,'wb')
    #write() argument must be str, not bytes出现这个的时候，将‘w’改为‘wb’即可
    dump(data,fw)
    fw.close()
    move(fileName,newpath + '\\' + fileName)
    #这里字符串前加不加r好像都可以达成目的，不懂为毛

def loadFile(fileName):
    fw = open(fileName,'rb')
    #open的默认模式是'r',ctrl+左键可以看到的
    return load(fw)