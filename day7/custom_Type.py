# 使用元类
# 通过type()函数创建的类和直接写class是完全一样的,因为Python解释器遇到class定义时,仅仅是扫描一下class定义的语法,然后调用type()函数创建出class

def fn(self,name='world'):
    print('Hello %s.' % name)


Hello=type('Hello',(object,),dict(hello=fn)) #创建Hello Class
