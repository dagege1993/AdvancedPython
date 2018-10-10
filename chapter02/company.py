# class Company(object):
#     def __init__(self, employee_list):
#         self.employee = employee_list
#
#     # 添加魔法函数,类实例化的对象是可迭代的
#     def __getitem__(self, item):
#         return self.employee[item]
#
#
# company = Company(['tom', 'bob', 'jane'])
# print(company)
# emploee = company.employee
# print(emploee)
# for em in company:
#     print(em)


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    # 添加魔法函数,类实例化的对象是可迭代的
    def __str__(self):
        return ','.join(self.employee)


company = Company(['tom', 'bob', 'jane'])
print(company)
