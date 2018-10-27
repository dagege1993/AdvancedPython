import time
from multiprocessing import Process, Queue, Manager, Pipe

# 利用queue通信

# def producer(queue):
#     queue.put('a')
#     time.sleep(2)
#
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)


# 共享全局变量通信
# 共享全局变量不能适用于多进程编程,可以适用于多线程
# def producer(a):
#     a += 1
#     time.sleep(2)
#
#
# def consumer(a):
#     print(a)
#
#
# if __name__ == '__main__':
#     queue = Queue(10)
#     a = 1
#     # my_producer = Process(target=producer, args=(queue,))
#     # my_consumer = Process(target=consumer, args=(queue,))
#     my_producer = Process(target=producer, args=(a,))
#     my_consumer = Process(target=consumer, args=(a,))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()  # 线程同步

# multiprocessing中额queue不能用于pool进程池
# pool中的进程间通信需要使用manager中的queue
from multiprocessing.pool import Pool


#
# def producer(queue):
#     queue.put('a')
#     time.sleep(2)
#
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
#
# if __name__ == '__main__':
#     queue = Manager().Queue(10)
#     pool = Pool(2)
#     pool.apply_async(producer, args=(queue,))
#     pool.apply_async(consumer, args=(queue,))
#     pool.close()
#     pool.join()


# 利用pipe实现进程间通信
# pipe性能高于queue,因为queue是用来做进程间同步加了很多锁,就降低了性能
# def producer(pipe):
#     pipe.send('boby')
#
#
# def consumer(pipe):
#     print(pipe.recv())
#
#
# if __name__ == '__main__':
#     recevie_pipe, send_pipe = Pipe()
#     # pipe只能适用于两个进程
#     my_poducer = Process(target=producer, args=(send_pipe,))
#     my_consumer = Process(target=consumer, args=(recevie_pipe,))
#     my_poducer.start()
#     my_consumer.start()
#     my_poducer.join()
#     my_consumer.join()

# 进程间共享内存,用manager().数据类型,一定要注意数据的同步
def add_data(p_dict, key, value):
    p_dict[key] = value


if __name__ == '__main__':
    progress_dict = Manager().dict()
    first_progress = Process(target=add_data, args=(progress_dict, "bobby1", 22))
    send_progress = Process(target=add_data, args=(progress_dict, "bobby2", 23))
    first_progress.start()
    send_progress.start()
    first_progress.join()
    send_progress.join()
    print(progress_dict)
