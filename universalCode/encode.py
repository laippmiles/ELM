from csv2ListOrMatrix import csv2ListOrMatrix
path1 = r'D:\桌面\ELM' + '\\'
fileName = 'test_Contrast.csv'
path = path1 +fileName
out = csv2ListOrMatrix(path,'list')
print(out)