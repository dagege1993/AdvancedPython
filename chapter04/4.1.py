class Cat():
    def say(self):
        print('i am a cat')


class Dog():
    def say(self):
        print('i am a dos')


class Duck():
    def say(self):
        print('i am a duck')


animal = Cat
animal().say()
# 所有的类都实现了一个共同的方法,方法名一样,这些类可以归为一种类型
# 以此达到python中多态
animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    # 添加魔法函数,类实例化的对象是可迭代的
    def __getitem__(self, item):
        return self.employee[item]


a = ['bobby1', 'bobby2']
b = ['bobby1', 'bobby']
name_tuple = ['bobby3', 'bobby4']
name_set = set()
name_set.add('bobby5')
name_set.add('bobby6')
# a.extend(b)
# a.extend(name_tuple)
company = Company(['tom', 'bob', 'jane'])
a.extend(company)
# a.extend(name_set)  # 要求传参为iterable就行,不一定要指定列表
print(a)
