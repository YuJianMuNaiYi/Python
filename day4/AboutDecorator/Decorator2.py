# 变量解析规则
a_string = "This is a global variable"


def foo1():
    a_string = 'test'  # 此处实际上新创建了一个局部变量,隐藏全局作用域中的同名变量
    # print(a_string)
    print(locals())


foo1()

print('a_string:%s' % a_string )  # 此处的全局变量并没有在foo1()函数中被修改
