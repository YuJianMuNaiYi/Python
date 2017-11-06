# 面向对象编程---类
# 面向对象的设计思想是抽象出Class,根据Class创建Instance
# 面向对象的抽象程度又比函数要高,因为一个Class既包含数据,又包含数据的方法
# 万变不离其宗,面向对象始终围绕数据封装,继承和多态

# 表示该类是从object继承而来的
class Student(object):

    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print('%s:%s'% (self.name,self.score))

    def get_grade(self):
       if self.score >= 90:
           return 'A'
       elif self.score>=60:
           return 'B'
       else:
           return 'C'

bart=Student('Bart Simpson',59)
lisa=Student('Lisa Simpson',87)

bart.print_score()
result=bart.get_grade()
print(result)

lisa.print_score()
result=lisa.get_grade()
print(result)

bart.age=20
print('bart age:%s'% bart.age)
print('lisa age:%s'% lisa.age)     #则会报错
