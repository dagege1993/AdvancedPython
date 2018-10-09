a = 1
# print(type(a))
# print(type(int))


# type ->int ->1
# type ->class ->obj
# object是最顶层基类
# type也是一个类,同时type也是一个对象
class Student:
    pass


stu = Student()
print(type(stu))
print(type(Student))
print(Student.__bases__)  # 查看基类
print(type.__bases__)
print(type(object))
print(1, type(type))
print(object.__bases__)  # object的基类为空
