# 面向对象编程---类---获取对象信息
# 当我们拿到一个对象的引用时,如何知道这个对象是什么类型?有哪些方法呢?
import  types

#使用type()
#基本类型都可以用type()判断
print(type(123))
print(type('str'))
print(type(None))

print(type(abs))

result=type(123)==type(456)
print('123的类型是否跟456的类型是一致的:%s'% result)
result=type(123)==int
print('123的类型是否是int:%s'% result)
result=type('abc')==str
print('abc的类型是否是str:%s' % result)
result=type('abc')==type(123)
print('abc的类型是否与123的类型是一致的: %s ' % result)

# 如何判断一个对象是否是函数?

def fn():
    pass

result=type(fn)==types.FunctionType
print(result) # True

result=type(abs)==types.BuiltinFunctionType     #内置函数
print(result) # True

result=type(lambda x:x )==types.LambdaType
print(result) # True
result=type(x for x in range(10))==types.GeneratorType
print(result) # True

# 使用isinstance()
# isinstance()判断的是一个对象是否是该类型本身,或者位于该类型的父继承链上

# 使用dir()
# 如果要获得一个对象的所有属性和方法,可以使用dir()函数,它返回已包含字符串的list

print(dir('abc'))

class MyObject(object):
    def __init__(self):
        self.x=9

    def power(self):
        return self.x * self.x

obj=MyObject()

result=hasattr(obj,'x') # 有属性'x'吗？
print(result)   # True

result=hasattr(obj,'y') # 有属性'y'吗？
print(result)  # False

setattr(obj,'y',19) #设置一个属性'y'
result=hasattr(obj,'y') # 有属性'y'吗？
print(result)  # True
print('obj.y:%s'% obj.y)

result=getattr(obj,'y') # 获取属性'y'
print(result) # 19

result=obj.y # 获取属性'y'
print(result) # 19

# 获取属性'z'，如果不存在，返回默认值404
result=getattr(obj,'z',404)
print(result) # 404

# 也可以获取对象的方法

result=hasattr(obj,'power')
print(result)    # True

result=getattr(obj, 'power') # 获取属性'power'
print(result)
