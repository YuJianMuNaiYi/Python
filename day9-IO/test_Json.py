# JSON

import  json

d=dict(name='MuNaiYi',age=30,score=100)
# dumps()方法返回一个str，内容就是标准的JSON。
# dump()方法可以直接把JSON写入一个file-like Object。
result=json.dumps(d)
print(result)

# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化

# 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。
obj=json.loads(result)

print(obj)


# JSON进阶

class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

def student2dict(s):
    return {
        'name':s.name,
        'age':s.age,
        'score':s.score
        }
s=Student('zhangSan',20,90)
jsonValue=json.dumps(s,default=student2dict)
print('Student类型的实例序列化:%s' % jsonValue)

# 把JSON反序列化为一个Student对象实例,loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

obj=json.loads(jsonValue,object_hook=dict2student)
print(obj)


o=dict(name='张三',age=29)
t=json.dumps(o,ensure_ascii=True)
print(t)
