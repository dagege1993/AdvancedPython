import time
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED


# 线程池,为什么要线程池
# 需求:1,主线程中可以获取某一个线程的状态,或者某一个任务的状态和返回值
# 需求:2,当一个线程完成的时候,主线程能立即知道
# futures 可以让多线程和多进程编码接口一致

def get_html(times):
    time.sleep(times)
    print('got page{} success'.format(times))
    return times


executor = ThreadPoolExecutor(max_workers=1)
# 通过submit函数提交执行的函数到线程池中,submit是立即返回,非租塞
# task1 = executor.submit(get_html, (3))
# task2 = executor.submit(get_html, (2))

# 要获取已经成功的task的返回
urls = [2, 3, 4]
all_tasks = [executor.submit(get_html, (url)) for url in urls]
wait(all_tasks, return_when=FIRST_COMPLETED)
print('main')
# for futere in as_completed(all_tasks):
#     data = futere.result()
#     print("get {} page".format(data))
# 通过executor.map获取已经完成的task的值
# for data in executor.map(get_html, urls):
# data = futer.result()
# print("get {} page".format(data))
# done方法用于判定某个任务是否完成
# print(task1.done())
# print(task2.cancel())
# time.sleep(3)
# print(task1.done())
# # result方法可以获取task的执行结果
# print(task1.result())  # 阻塞方法,
