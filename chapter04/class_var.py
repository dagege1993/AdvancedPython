class A:
    aa = 1  # 类变量

    def __init__(self, x, y):
        self.x = x
        self.y = y


a = A(2, 3)
A.aa = 11
a.aa = 100  # 实例.属性会把值赋给我们实例的属性,类属性是保持不变
print(a.x, a.y, a.aa)  # 属性查找方式,首先会查找对象变量,找不到向上查询到类变量
print(A.aa)  # aa必须要通过类的方式来访问
print(a.aa)
