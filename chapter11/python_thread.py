# 对于IO操作为主的程序来说,多线程和多进程性能差别不大
# 甚至多进程还慢,因为线程的调度比起进程来说更加轻量级


# 1.通过Thread类实例化
import threading
import time


def get_detail_html(url):
    print('get detail html started')
    time.sleep(2)
    print('get detail html end')


def get_detail_url(url):
    print('get detail url started')
    time.sleep(4)
    print('get detail url end')


if __name__ == '__main__':
    thread1 = threading.Thread(target=get_detail_html, args=('',))
    thread2 = threading.Thread(target=get_detail_url, args=('',))
    # thread1.setDaemon(True)  # 主线程A启动了子线程B，调用b.setDaemaon(True)，则主线程结束时，会把子线程B也杀死，设置子线程随主线程的结束而结束：
    # thread2.setDaemon(True)
    start_time = time.time()
    thread1.start()
    thread2.start()
    thread1.join()  # 希望子线程执行完毕再执行主线程,堵塞式执行
    thread2.join()

    # 在python中，主线程结束后，会默认等待子线程结束后，主线程才退出。
    print('last time:{}'.format(time.time() - start_time))


# 2. 通过集成Thread来实现多线程
class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url started")
        time.sleep(4)
        print("get detail url end")


if __name__ == "__main__":
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl("get_detail_url")
    start_time = time.time()
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    # 当主线程退出的时候， 子线程kill掉
    print("last time: {}".format(time.time() - start_time))
