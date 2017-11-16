# 读文件

def readFile():
    try:
        file = open('./test.txt', 'r')
        content = file.read()
        print(content)
    except IOError as e:
        print('出错了')
    finally:
        if file:
            file.close()

# 上面函数的简写
# 和上面的try ... finally是一样的,只是代码更简洁,并且不必调用file.close()
def readFile1():
    with open('./test.txt', 'r') as  file:
        print(file.read())

readFile()
readFile1()

# 读取二进制文件
# 要读取二进制文件,比如图片,视频等等,用'rb'模式打开文件即可

def readFile2():
    with open('./test.jpg','rb') as file:
        print(file.read())    # 十六进制表示的字节

readFile2()

# 字符编码
# 要读取非UTF-8编码的文本文件,需要给open()函数传入encoding参数,例如,读取GBK编码的文件
def readFileGbk():
    with open('./test.txt','r',encoding='gbk')as file:
        print(file.read())

readFileGbk()

# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：

def readFileUnicodeDecode():
    with open('./test.txt','r',encoding='gbk',errors='innore') as file:
        print(file.read())

readFileUnicodeDecode()





