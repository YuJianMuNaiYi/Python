# 定制类

class Student(object):
    def __init__(self):
        self.name='张三'
    # 避免#1处的问题
    def __getattr__(self, item):
        if item=='score':
            return 99
        if item=='age':
            return lambda :30
        
s=Student()
print(s.name)     #不会报错
print(s.score)   #1报错 AttributeError: 'Student' object has no attribute 'score'
print(s.age())

