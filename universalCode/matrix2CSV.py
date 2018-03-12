import csv
from numpy import shape
def matrix2CSV(matrix , path = r"D:\桌面\ELM\test.csv"):
    #python2可以用file替代open
    with open(path,"at") as csvfile:
        writer = csv.writer(csvfile,dialect='excel')

        #先写入columns_name
        #writer.writerow(indexName)
        #写入多行用writerows
        writer.writerow(matrix)

def CSVDeleteSpace(path = r"D:\桌面\ELM\test.csv"):
    with open(path, 'rt')as fin:  # 读有空行的csv文件，舍弃空行
        lines = ''
        for line in fin:
            if line != '\n':
                lines += line
    with open(path, 'wt')as fout:  # 再次文本方式写入，不含空行
        fout.write(lines)

def matrix2CSV_Once(matrix ,indexName, path = r"D:\桌面\ELM\test1.csv"):
    # python2可以用file替代open
    with open(path, "wt") as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        # 先写入columns_name
        writer.writerow(indexName)
        # 写入多行用writerows
        writer.writerows(matrix)

    with open(path, 'rt')as fin:  # 读有空行的csv文件，舍弃空行
        lines = ''
        for line in fin:
            if line != '\n':
                lines += line
    with open(path, 'wt')as fout:  # 再次文本方式写入，不含空行
        fout.write(lines)