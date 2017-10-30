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
