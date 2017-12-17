# Python内建模块---contextlib
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的

class Query(object):
    def __init__(self,name):
        self.name=name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type :
            print("Error")
        else :
            print('End')

    def query(self):
        print('Query info about %s ...' % self.name)

# 现在这样就可以把自己写的资源对象用于with语句

with Query("Bob") as q:
    q.query()

# 编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法,上面的代码可以改写如下

from  contextlib import contextmanager

class Query1(object):
    def __init__(self,name):
        self.name=name

    def query(self):
        print("Query1 info about %s ..." % self.name)

@contextmanager
def CreateQuery(name):
    print('Begin')
    q=Query1(name)
    yield q
    print('End')
# @contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了

with CreateQuery('Bob') as q:
    q.query()

    
# 我们希望在某段的代码执行前后自动执行特定代码,也可以用@contextmanager实现

@contextmanager
def tag(name):
    print('<%s>'% name)
    yield
    print('</%s>'% name)

with tag('h1'):
    print('Hello')
    print("world")

# @contextmanager让我们通过编写generator来简化上下文管理。
