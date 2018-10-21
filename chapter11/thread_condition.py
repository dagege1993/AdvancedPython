import threading
from threading import Condition

# 条件变量，用于复杂线程同步
# class XiaoAi(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name='小爱')
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print("{}:在".format(self.name))
#         self.lock.release()
#         self.lock.acquire()
#         print("{}:好啊".format(self.name))
#         self.lock.release()
#
#
# class TianMao(threading.Thread):
#     def __init__(self, lock):
#         self.lock = lock
#         super().__init__(name='天猫精灵')
#
#     def run(self):
#         self.lock.acquire()
#         print("{} : 小爱同学 ".format(self.name))
#         self.lock.release()
#         self.lock.acquire()
#         print("{} : 我们来对古诗吧 ".format(self.name))
#         self.lock.release()
# 通过condition完成协同读诗
from threading import Condition


class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name='小爱')
        self.cond = cond

    def run(self):
        with self.cond:  # 会在这里释放那把锁
            self.cond.wait()
            print("{}:在".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}:好啊".format(self.name))
            self.cond.notify()


class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name='天猫精灵')
        self.cond = cond

    def run(self):
        with self.cond:
            print("{} : 小爱同学 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 我们来对古诗吧 ".format(self.name))
            self.cond.notify()
            self.cond.wait()


if __name__ == '__main__':
    # lock = threading.Lock()
    cond = threading.Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)
    # 启动顺序很重要
    # 在调用with cond之后才能调用wait或者notify方法
    # condition有两层锁， 一把底层锁,会在线程调用了wait方法的时候释放， 上面的锁会在每次调用wait的时候分配一把并放入到cond的等待队列中，等到notify方法的唤醒
    # wait方法只有通过notify才能唤醒
    xiaoai.start()
    tianmao.start()
