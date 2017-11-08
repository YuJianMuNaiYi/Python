# 定制类
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a,b

    # 按照下标获取元素     不完善
    def __getitem__(self, item):
        if isinstance(item,int): #item 是索引
            a, b = 0, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item,slice): #item 是切片
            start=item.start
            stop=item.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x >start:
                    L.append(a)
                a,b=b,a+b
            return L


f = Fib()
print('下标为0的元素:%s' % f[0])
print('下标为1的元素:%s' % f[1])

# list神气的切片服务
print(list(range(100))[5:10])

print(f[0:5])
print(f[:10])


