# 匿名函数
list(map(lambda x: x*x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# 上面的lambda x: x*x 相当于
def f(x):
    return x*x

# 匿名函数作为返回值返回
def build(x, y):
    return x*x + y*y

