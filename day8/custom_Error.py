# 自定义错误类型
# 只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。

class Custom_Error(ValueError):
    pass

def foo(s):
    n=int(s)
    if n==0:
        raise Custom_Error('invalid value:%s' % s)
    return 10/n

foo('0')

