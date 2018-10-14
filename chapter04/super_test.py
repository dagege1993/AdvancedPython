class A:
    def __init__(self):
        print('A')


class B(A):
    def __init__(self):
        print('B')
        super().__init__()  # 希望调用父类的init方法


from threading import Thread


class MyThread(Thread):
    def __init__(self, name, user):
        self.user = user
        super().__init__(name=name)  # 可以重用父类代码


# 既然我们要重写B的构造函数,为什么还要去调用super
# super到底执行顺序是什么样的

class A:
    def __init__(self):
        print('A')


class B(A):
    def __init__(self):
        print('B')
        super().__init__()  # 希望调用父类的init方法


class C(A):
    def __init__(self):
        print('C')
        super().__init__()  # 希望调用父类的init方法


class D(B, C):
    def __init__(self):
        print('D')
        super(D, self).__init__()  # 希望调用父类的init方法


if __name__ == '__main__':
    print(D.__mro__)
    d = D()
