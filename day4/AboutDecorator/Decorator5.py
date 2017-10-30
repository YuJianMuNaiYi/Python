# 嵌套函数


def outer():
    x = 1

    def inner():
        print(x)
    inner()


print(outer())

# 函数是python世界里的一级类对象
# 显而易见，在python里函数和其他东西一样都是对象。
print('int 是否是对象:%s' % issubclass(int, object))


def foo():
    pass


print('foo.__class__:%s' % foo.__class__)

print('函数foo是否是对象:%s' % issubclass(foo.__class__, object))


def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def apply(func, x, y):
    return func(x, y)


result = apply(add, 2, 1)
print(result)

result = apply(sub, 2, 1)
print(result)
