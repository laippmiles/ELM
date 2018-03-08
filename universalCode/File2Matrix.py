def File2Matrix(FileMame,NumberOfClass):
    from numpy import zeros
    #好像不用担心重复加载的问题
    File = open(FileMame)
    ArrayOfLines = File.readlines()
    #readline() 和 .readlines() 之间的差异是后者一次读取整个文件，象 .read() 一样。
    # readlines() 自动将文件内容分析成一个行的列表，该列表可以由 Python 的 for ... in ... 结构进行处理。
    # 另一方面，.readline() 每次只读取一行，通常比 .readlines() 慢得多。
    #仅当没有足够内存可以一次读取整个文件时，才应该使用 .readline()。
    NumberOfLines = len(ArrayOfLines)
    ReturnMat = zeros((NumberOfLines, NumberOfClass))
    #这里是两层括号！注意写法
    ClassLabelVector = []
    Index = 0
    for Line in ArrayOfLines:
        Line = Line.strip()
        #strip:用于去掉字符串的首尾字符
        ListFromLine = Line.split('\t')
        #切片
        ReturnMat[Index,:] = ListFromLine[0:NumberOfClass]
        ClassLabelVector.append(int(ListFromLine[-1]))
        Index += 1
    return ReturnMat,ClassLabelVector