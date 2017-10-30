# 装饰器


def outer(some_func):
    def inner():
        print('before some_func')
        ret = some_func()
        return ret + 1
    return inner


def foo():
    return 1


decorated = outer(foo)
result = decorated()

print('计算后的值:%s' % result)


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Coord:' + str(self.__dict__)


def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)


def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)


one = Coordinate(100, 200)
two = Coordinate(300, 200)
r = add(one, two)
print('加法运算之后的值:%s' % r)

r = sub(one, two)
print('加法运算之后的值:%s' % r)

three = Coordinate(-100, -100)

r = add(one, three)
print(r)

print('加法运算之后的值:%s' % r)


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

one = Coordinate(100, 200)
two = Coordinate(300, 200)
r = sub(one, two)
print('装饰之后运算的值:%s' % r)
