# 协程 generator

#consumer()函数就是一个generator
def consumer():
    r=''
    while True:
        n=yield r
        if not n:
            return
        print('[Consumer] Consuming %s ...'% n)
        r='200 OK'

def produce(C):
    c.send(None)
    n=0
    while n <5:
        n=n+1
        print('[Produce] Producing %s ...' % n)
        r=c.send(n)
        print('[Produce] Consumer return :%s' % r)
    c.close()

c=consumer()
produce(c)
