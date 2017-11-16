# 写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
# 要写入特定编码的文本文件,请给open()函数传入encoding参数,将字符串自动转换成指定编码

import PIL.image as pic

path='./test.txt'

def writeTxtFile():
    with open(path,'w') as file:
        file.write('Hello,Python.')

def readTxtFile():
    with open(path,'r') as file:
        print(file.read())

writeTxtFile()
readTxtFile()
