# 定制类
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a,b

    # 按照下标获取元素
    def __getitem__(self, item):
        a, b = 0, 1
        for x in range(item):
            a, b = b, a + b
        return a

f = Fib()
print('下标为0的元素:%s' % f[0])
print('下标为1的元素:%s' % f[1])



