# 深入理解下装饰器
# http://python.jobbole.com/81683/
a_string = "This is a global variable"
def foo():
    print(locals())  # 函数foo有自己独立的命名空间,虽然暂时命名空间里面什么都还没有
    # print(a_string)
foo()
print(locals())
