#迭代

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k,v in d.items():
    print('key:',k,',value:',v)

#字符串迭代
for ch in 'abcd':
    print(ch)

#如何判断一个对象是可迭代对象?
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))


for i,value in enumerate(['A','B','C']):
    print(i,value)


for x,y in [(1,2),(3,4),(5,6)]:
    print(x,y)