#迭代器
#判断一个对象是否是Iterable对象
from collections import Iterable #导入可迭代对象
from collections import  Iterator #导入迭代器

print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(100,Iterable))

#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

print('迭代器:')
print(isinstance((x for x in range(10)),Iterator))
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance('abc',Iterator))

#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#把list、dict、str等Iterable变成Iterator可以使用iter()函数
print("转换为Iterator:")
print(isinstance(iter([]),Iterator))
print(isinstance(iter('abc'),Iterator))