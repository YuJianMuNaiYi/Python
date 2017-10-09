#列表生成式

result=list(range(1,11))
print(result)

result=[x*x for x in list(range(1,11))]
print(result)

result=[x*x for x in list(range(1,11)) if x%2==0]
print(result)

#两层循环,可以生成全排列
result=[m+n for m in 'ABC' for n in 'XYZ']
print(result)

#列出当前目录下的所有文件和目录名
import os #导入os模块
print([d for d in os.listdir('.')]) #os.listdir可以列出文件和目录

#for循环其实可以同时使用两个甚至多个变量,比如dict的items()可以同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.items():
    print(k,'=',v)

temp=[k+'='+v for k,v in d.items()]
print(temp)

#把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
l=[s.lower() for s in L]
print(l)

#如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
L1 = ['Hello', 'World', 18, 'Apple', None]

L2=[s.lower() for s in L1 if isinstance(s,str)==True]

print(L2)
