# Semaphore 是用于控制数量的锁
# 文件读写,写一般是一个线程写,读可以允许有多个
# 做爬虫,控制爬虫的数量
import threading
import time


class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print('got html text success')
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()  # 会减一,数为零时会停在这里
            html_thread = HtmlSpider('https://baidu.com/{}'.format(i), self.sem)
            html_thread.start()


if __name__ == '__main__':
    sem = threading.Semaphore(3)
    url_producer = UrlProducer(sem)
    url_producer.start()
