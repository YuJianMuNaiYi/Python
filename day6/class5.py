# 面向对象编程---类---实例属性和类属性

class Student(object):
    # def __init__(self,name):
       # self.name=name
    name='Student'

s=Student() #创建实例s
print(s.name) #打印name属性,因为实例并没有name属性,所以会继续查找class的name属性Student
print(Student.name) #打印类的name属性
s.name='Michael'# 给实例绑定name属性
print(s.name)# 由于实例属性优先级比类属性高,因此,他会屏蔽类的name属性
print(Student.name)# 但是类属性并未消失,用Student.name任然可以访问
del s.name  #如果删除实例的name属性
print(s.name) # 再次调用s.name,由于实例的name属性并未找到,类的name属性就显示出来了

