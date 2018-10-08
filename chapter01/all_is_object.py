def ask(name='bobby1'):
    print(name)


class Person:
    def __init__(self):
        print('jack')


obj_list = []
obj_list.append(ask, Person)

# my_func = ask
# my_func('bobby')

my_class = Person
my_class()
