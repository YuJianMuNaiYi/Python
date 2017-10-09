#生成器

L=[x * x for x in range(10)]
print(L)

#创建生成器方式一
g=(x * x for x in range(10))
print(g)
for x in g:
    print(x)

#斐波拉契数列

def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b #此处就等于a=b,b=a+b
        n+=1
    return 'done'

print('斐波拉契数列')
fib(10)

#将上面函数编程generator
#如果一个函数定义中包含了yield关键字,那么这个函数就不再是一个普通函数,而是一个generator
def fibGenerator(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b #此处就等于a=b,b=a+b
        n+=1
    return 'done'

f=fibGenerator(10)
print(f)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o=odd()
for x in o:
    print(x)

#但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g=fibGenerator(6)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

#杨辉三角
