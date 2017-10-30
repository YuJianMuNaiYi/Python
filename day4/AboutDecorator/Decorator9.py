
# 更通用的装饰器


def logger(func):
    #  inner函数,能够接受任意数量和类型的参数并把它们传递给被包装的方法
    def inner(*args, ** kwargs):
        print('Arguments were:可变参数:%s,关键字参数:%s' % (args, kwargs))
        return func(*args, **kwargs)
    return inner


@logger
def foo_test(x, y=1):
    return x * y


@logger
def foo_test2():
    return 2


result = foo_test(5, 4)
print(result)

result = foo_test(1)
print(result)


result = foo_test2()
print(result)
