from threading import Lock, RLock  # 可重入的锁

# 在同一个线程里面,可以连续调用多次acquire,一定要注意acquire的次数要和release的次数相等
total = 0
lock = Lock()


def add():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total += 1
        lock.release()


def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


import threading

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(total)

# 用锁会影响性能
# 锁会引起死锁
# 死锁情况A(a,b),资源竞争造成死锁
'''
A(a,b)
acquire(a)
acquire(b)

B(a,b)
acquire(a)
acquire(a)

'''
