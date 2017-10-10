#高阶函数

#变量可以指向函数

print(abs(-10))
f=abs #将函数本身赋值给变量 即变量可以指向函数

print(f(23))

#一个最简单的高阶函数
def add(x,y,f):
    return f(x)+f(y)

result=add(-5,6,abs)
print(result)

#map
def f(x):
    return x * x

r=map(f,[1,2,3,4,5,6,7,8,9])   #由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
print(list(r))

print(list(map(str,[1,2,3,4,5,6,7,8,9])))

#reduce
#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

from functools import reduce
def add(x,y):
    return x+y

result=reduce(add,[1,3,5,7,9])
print(result)
#把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    return name.capitalize()
L1 = ['adam', 'LISA', 'barT']
L2=list(map(normalize,L1))
print(L2)
#编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(l):
    def multiply(x,y):
        return x*y
    return reduce(multiply,l)

result=prod([3,5,7,9])
print(result)

