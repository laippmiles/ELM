from csv2ListOrMatrix import csv2ListOrMatrix
from Mail import mailToMe, mailFromLZY
#写文件名要用的
subject = '笨蛋，你的实验跑完了'
content = '赶快回来。'
fileName = 'TestAnawer_2018-03-13_20_52_52_915519.csv'
filePath = r'D:\桌面\ELM' + '\\'
mailFromLZY(subject,content,filePath,fileName)

path1 = r'D:\桌面\ELM' + '\\'
fileName = 'test_Contrast.csv'
path = path1 +fileName
out = csv2ListOrMatrix(path,'list')
print(out)