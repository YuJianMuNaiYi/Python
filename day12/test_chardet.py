# 常用第三方模块---chardet
from pip._vendor.requests.packages import chardet

result=chardet.detect(b'Hello, world!')
print(result)

# gbk
data = '离离原上草，一岁一枯荣'.encode('gbk')
result=chardet.detect(data)
print(result)

#utf-8
data = '离离原上草，一岁一枯荣'.encode('utf-8')
result=chardet.detect(data)
print(result)

#对日文进行检测
data = '最新の主要ニュース'.encode('euc-jp')
result=chardet.detect(data)
print('日文:%s' % result)
