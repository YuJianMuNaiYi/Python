# -*- coding: utf-8 -*-

#定义函数
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type ...')
    if(x>0):
        return x
    else:
        return -x

# 定义空函数
def nop():
    pass #pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来

#返回多个值

import math
def move(x,y,step,angle=0):
    nx=x=step *math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny

#定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#ax2 + bx + c = 0
#两个解。



