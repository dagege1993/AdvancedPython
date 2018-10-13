# 我们去检查某个类是否有某种方法
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    # 添加魔法函数,类实例化的对象是可迭代的
    # def __str__(self):
    #     return ','.join(self.employee)

    def __len__(self):
        return len(self.employee)


com = Company(['bobby1', 'bobby2'])
print(hasattr(com, '__len__'))  # 在类当中,函数也是她的属性

# 我们在某些情况下希望判定某个对象的类型
from collections.abc import Sized

isinstance(com, Sized)

# print(len(com))

'''
# 我们需要强制某个子类需要实现的某些方法
# 实现了一个web框架,集成cache(redis,cache,memorychache)
# 需要设计一个抽象基类,指定子类必须实现某些方法


# 继承这个类必须要实现的方法,不然会报错
class CacheBase():  # 抽象基类
    def get(self, key):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError


class RedisCache(CacheBase):
    def set(self, key, value):
        pass


redis_cache = RedisCache()
redis_cache.set('key', 'value')
'''
import abc
from collections.abc import *  # python 中已经实现了一些通用的抽象基类,让我们去了解python数据结构的接口


class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisCache(CacheBase):
    def set(self, key, value):
        pass


redis_cache = RedisCache()
