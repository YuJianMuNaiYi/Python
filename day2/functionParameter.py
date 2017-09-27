# -*- coding: utf-8 -*-

# 位置参数,调用函数时,传入的两个值按照位置顺序依次赋给参数x和y
def power(x:int,n:int):
    s=1
    while n>0:
        n-=1
        s*=x
    return s


#可变参数
def clacvalue(*numbers):
    sum=0
    for n in numbers:
        sum+=n*n
    return sum


result=clacvalue(1,2,3,4,5)
print(result)

nums=[4,5,6]
print(clacvalue(*nums))

#关键字参数
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)


person('zhangsan',30)
person('zhangsan',30,city='lanzhou',address='兰州市城关区')
extra = {'city': 'Beijing', 'job': 'Engineer'}

person('zhangsan',30,city=extra['city'],job=extra['job'])
person('zhangsan',30,**extra)


#命名关键字参数
def person1(name,age,**kw):
    if 'city' in kw and 'job' in kw:
        print('name:', name, ',age:', age, ',city:',kw['city'],',job',kw['job'])

person1('lis',30,city=extra['city'],job=extra['job'])

#参数组合
def f1(a,b,c=0,*args,**kw):#必选参数,默认参数,可变参数,关键字参数
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=0,*,d,**kw):
    print('a =',a,'b =',b,'c =',c,'d=',d,'kw =',kw)

f1(1,2)
f1(1,2,3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
f2(1, 2, d=99, ext=None)


args=(1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args,**kw)

args=(1,2,3)
kw={'d':99,'x':'#'}
f2(*args,**kw)