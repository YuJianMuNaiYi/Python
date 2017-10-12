# 装饰器
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2017-10-12')

print(now())
print(now.__name__)

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2017-10-12')

print(now())
print(now.__name__)


# def log(text=''):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('begin call', text)
#             func(*args, **kw)
#             print('end call')
#         return wrapper
#     return decorator
#
# @log
# def f():
#     print('f')


