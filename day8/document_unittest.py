# 文档测试
# Python内置的"文档测试"(doctest)模块可以直接提取注释中的代码并执行

def abs(n):
    '''
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)
