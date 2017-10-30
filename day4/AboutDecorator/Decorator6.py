# 闭包
# 嵌套定义在非全局作用域里面的函数能够记住它在被定义的时候它所处的封闭命名空间


def outer1():
    x = 1

    def inner1():
        print(x)
    return inner1


r = outer1()
print(r.func_closure)
