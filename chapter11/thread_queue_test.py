# 通过queue的方式进行线程间同步
from queue import Queue

import time
import threading

from chapter11 import variables

from threading import Condition


# 1. 生产者当生产10个url以后就就等待，保证detail_url_list中最多只有十个url
# 2. 当url_list为空的时候，消费者就暂停

def get_detail_html(queue):
    # 爬取文章详情页
    detail_url_list = variables.detail_url_list
    while True:
        url = queue.get()  # 阻塞方法
        # for url in detail_url_list:
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


def get_detail_url(queue):
    # 爬取文章列表页
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            queue.put("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end")


# 1. 线程通信方式- 共享变量

if __name__ == "__main__":
    detail_url_queue = Queue(maxsize=1000)
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        html_thread.start()
    detail_url_queue.task_done()
    '''task_done()
意味着之前入队的一个任务已经完成。由队列的消费者线程调用。
每一个get()调用得到一个任务，接下来的task_done()调用告诉队列该任务已经处理完毕。
如果当前一个join()正在阻塞，它将在队列中的所有任务都处理完时恢复执行
（即每一个由put()调用入队的任务都有一个对应的task_done()调用）。
'''
    detail_url_queue.join()
    '''
    阻塞调用线程，直到队列中的所有任务被处理掉。
    只要有数据被加入队列，未完成的任务数就会增加。
    当消费者线程调用task_done()（意味着有消费者取得任务并完成任务），未完成的任务数就会减少。
    当未完成的任务数降到0，join()解除阻塞。
    '''
