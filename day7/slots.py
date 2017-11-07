# 通常情况下,可以将函数定义在class中,但动态绑定允许我们在程序运行的过程中动态给class加上功能,这在静态语言中很难实现
class Student(object):
    pass

s=Student()
s.name='MuNaiYi' #动态给实例绑定一个属性
print(s.name)

def set_age(self,age): #定义一个函数作为实例方法
    self.age=age

from types import MethodType

s.set_age=MethodType(set_age,s) #给实例绑定一个方法
s.set_age(30) #调用实例方法
print(s.age)

#给一个实例绑定的方法,对另一个实例是不起作用的
s2=Student()
# s2.set_age(25)      #尝试调用方法  报错:AttributeError: 'Student' object has no attribute 'set_age'

#为了给所用实例都绑定方法,可以给class绑定方法
def set_score(self,score):
    self.score=score

Student.set_score=set_score

s.set_score(80)
print(s.score) # 80

s2.set_score(90)
print(s2.score) # 90

# 使用__slots__
# 要显示实例的属性,比如只允许给Student1实例添加name和age属性
# 为了达到限制目的,Python允许在定义class的时候,定义一个特殊的__slots__变量,来显示该class实例添加的属性

class Student1(object):
    __slots__ = ('name','age') #用tuple定义允许绑定的属性名称

student=Student1() #创建实例
student.name='zhangSan'
student.age=30
# student.score=99 # AttributeError: 'Student1' object has no attribute 'score'

print('name:%s,age:%s' % (student.name,student.age))

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
class GraduateStudent(Student1):
    pass

g=GraduateStudent()
g.score=99  #不会报错

print('score:%s' % g.score)



