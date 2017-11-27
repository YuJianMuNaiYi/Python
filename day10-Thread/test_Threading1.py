 # Lock
import time,threading

# 假定银行存款
balance=0
lock=threading.Lock()

def change_it(n):
    # 先存后取,结果应该为0
    global balance
    balance+=n
    #print('balance+:%s' % balance)
    balance-=n
    #print('balance-:%s' % balance)

def run_thread(n):
    for i in range(100000):
        # 先要获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 改完了一定要释放锁
            lock.release()


t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(8,))

t1.start()
t2.start()

t1.join()
t2.join()

print(balance)
