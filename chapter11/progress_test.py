import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor


# # 多进程编程
# # 耗CPU的操作,用多进程编程,对于IO操作来收,使用多线程编程
# # 进程切换代价要高于线程
#
# # 1. 对于耗费cpu的操作,多进程优于多线程
# import time
#
#
# def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# if __name__ == '__main__':
#
#     with ThreadPoolExecutor(3) as executor:
#         all_tasks = [executor.submit(fib, (num)) for num in range(25, 40)]
#         start_time = time.time()
#         for futere in as_completed(all_tasks):
#             data = futere.result()
#             print("exe result: {} ".format(data))
#         print('end_time is :{} '.format(time.time() - start_time))


# 对于IO操作来说,多线程优于多进程
def random_sleep(n):
    time.sleep(n)
    return n


if __name__ == '__main__':

    with ThreadPoolExecutor(3) as executor:
    # with ProcessPoolExecutor(3) as executor:
        all_tasks = [executor.submit(random_sleep, (num)) for num in [2] * 30]
        start_time = time.time()
        for futere in as_completed(all_tasks):
            data = futere.result()
            print("exe result: {} ".format(data))
        print('end_time is :{} '.format(time.time() - start_time))
