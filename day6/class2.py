# 面向对象编程---类---访问限制
# Python本身没有任何机制阻止你干坏事，一切全靠自觉。

# 表示该类是从object继承而来的
class Student(object):
    # 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
    # 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
    def __init__(self,name,score):
        self.__name=name
        self.__score=score

    def print_score(self):
        print('%s:%s'% (self.__name,self.__score))

    # 如果外部想要获取内部的__name和__score,可以增加函数
    def get_name(self):
        return self.__name
    def get_scote(self):
        return self.__score

    #如果允许外部代码修改内部变量,可以增加函数,这样的方式可以对参数做检查,避免传入无效的参数
    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score=score
        else:
            raise ValueError('bad score')

bart=Student('Bart Simpson',59)
lisa=Student('Lisa Simpson',87)

bart.print_score()
lisa.print_score()

# print('bart name:%s'% bart.__name) #外部是无法访问内部变量的
print('bart name:%s'% bart.get_name()) #以这样的方式来访问内部变量

