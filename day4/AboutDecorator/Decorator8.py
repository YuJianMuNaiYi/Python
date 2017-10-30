# 使用@标识符将装饰器应用到函数

from day4.AboutDecorator.Decorator7 import wrapper
from day4.AboutDecorator.Decorator7 import Coordinate


@wrapper
def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)


# *args and **kwargs
def one(*args):
    print(args)


one(1, 2, 3)


def two(x, y, *args):
    print(x, y, args)


two('a', 'b', 'c')


def add_test(x, y):
    return x + y


lst = [1, 2]
result = add_test(lst[0], lst[1])

print('result:%s' % result)

result = add_test(*lst)
print('result:%s' % result)


def foo_test(**kwargs):
    print('kwargs: %s' % kwargs)

foo_test()
foo_test(x=1, y=2)

dct = {'x': 1, 'y': 2}


def bar(x, y):
    return x + y


result = bar(**dct)  # 关键字参数
print('result:%s' % result)
