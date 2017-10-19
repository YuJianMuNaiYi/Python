# 深入理解下装饰器
# http://python.jobbole.com/81683/

# 作用域
a_string = "This is a global variable"

def foo():
    # 本地作用域
    print(locals())  # 函数foo有自己独立的命名空间,虽然暂时命名空间里面什么都还没有
    # print(a_string)
foo()

print(locals())  # 全局作用域

# 变量解析规则

def foo1():
    a_string = 'test'  # 此处实际上新创建了一个局部变量,隐藏全局作用域中的同名变量
    # print(a_string)
    print(locals())

foo1()

print(a_string)  # 此处的全局变量并没有在foo1()函数中被修改

#  变量生存周期
#  变量不仅是生存在一个个的命名空间内,他们都有自己的生存周期

def foo2():
    x = 1  # 函数foo2的命名空间随着函数调用开始而开始,结束而销毁

# 函数参数
# python允许我们向函数传递参数,参数会变成本地变量存在于函数内部
# 函数的参数可以有名称和位置。这意味着在函数的定义和调用的时候会稍稍在理解上有点不同。我们可以只给定义了位置参数的函数传递命名参数(实参),反之亦然
def foo3(x):
    print(locals())
foo3(1)

# 嵌套函数
def outer():
    x=1
    def inner():
        print(x)
    inner()

print(outer())

# 函数是python世界里的一级类对象
# 显而易见，在python里函数和其他东西一样都是对象。
print(issubclass(int, object))

def foo5():
    pass

print(foo5.__class__)

print(issubclass(foo5.__class__, object))

def add(x, y):
    return x+y
def sub(x, y):
    return x-y

def apply(func, x, y):
    return func(x,y)

result= apply(add,2,1)
print(result)

result= apply(sub,2,1)
print(result)

# 闭包
# 嵌套定义在非全局作用域里面的函数能够记住它在被定义的时候它所处的封闭命名空间

def outer1():
    x = 1
    def inner1():
        print(x)
    return inner1

r=outer1()
# print(r.func_closure)

# 装饰器
def outer2(some_func):
    def inner():
        print('before some_func')
        ret = some_func()
        return ret + 1
    return inner

def foo6():
    return 1

# decorated=outer2(foo6)
# decorated()

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Coord:' + str(self.__dict__)

def add (a, b):
    return Coordinate(a.x + b.x, a.y + b.y)
def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)

one = Coordinate(100, 200)

two = Coordinate(300, 200)

r = add(one, two)
print(r)

r = sub(one, two)
print(r)

three = Coordinate(-100, -100)

r = add(one, three)
print(r)


def wrapper(func):
    def checker(a, b):
        if a.x < 0 or a.y < 0:
            a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
        if b.x < 0 or b.y < 0:
            b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
        ret = func(a, b)
        if ret.x < 0 or ret.y < 0:
            ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
        return ret
    return checker

add = wrapper(add)
sub = wrapper(sub)

# one = Coordinate(100, 200)
# two = Coordinate(300, 200)
r = sub(one, two)
print(r)











