# 定制类__call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用
# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
class Student(object):
    def __init__(self,name):
        self.name=name

    def __call__(self):
        print('My Name is %s.'% self.name)

s=Student('张三')
s()# self参数不要传入

# 如何判断一个变量是函数还是对象?
# 判断一个对象是否能被调用,能被调用的对象就是一个Callable对象

print(callable(Student))
print(callable(max))
print(callable([1,2,3]))
print(callable(None))
print(callable('str'))
        
