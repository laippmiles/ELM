import csv
from numpy import shape
def array2CSV(matrix , path = 'D:\桌面\ELM'+'\\',filename = 'test.csv'):
    #python2可以用file替代open
    with open(path+filename,"at") as csvfile:
        writer = csv.writer(csvfile,dialect='excel')
        #先写入columns_name
        #writer.writerow(indexName)
        #写入多行用writerows
        writer.writerow(matrix)

def CSVDeleteSpace(path = 'D:\桌面\ELM'+'\\',filename = 'test.csv'):
    with open(path+filename, 'rt')as fin:  # 读有空行的csv文件，舍弃空行
        lines = ''
        for line in fin:
            if line != '\n':
                lines += line
    with open(path+filename, 'wt')as fout:  # 再次文本方式写入，不含空行
        fout.write(lines)

def array2CSV_Once(matrix ,indexName, path = 'D:\桌面\ELM'+'\\',filename = 'test.csv'):
    # python2可以用file替代open
    with open(path+filename, "wt") as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        # 先写入columns_name
        writer.writerow(indexName)
        # 写入多行用writerows
        writer.writerows(matrix)

    with open(path+filename, 'rt')as fin:  # 读有空行的csv文件，舍弃空行
        lines = ''
        for line in fin:
            if line != '\n':
                lines += line
    with open(path+filename, 'wt')as fout:  # 再次文本方式写入，不含空行
        fout.write(lines)

#测试
from loadData import loadData
from numpy import mat
train = loadData()[0].A
array2CSV_Once(train,[])