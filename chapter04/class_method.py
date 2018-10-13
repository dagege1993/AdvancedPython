class Date:
    # 构造函数
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)

    @staticmethod
    def parse_from_string(date_str):  # 静态方法是硬编码,一旦类名变了静态方法也跟着要变
        year, month, day = tuple(data_str.split('-'))
        return Date(int(year), int(month), int(day))

    @staticmethod
    # 要判断字符串是否合法
    def valid_str(data_str):
        year, month, day = tuple(data_str.split('-'))
        if int(year) > 0 and (int(month) > 0 and month <= 12):
            return True
        else:
            return False

    @classmethod
    def from_str(cls, date_str):  # cls只是命名规范,阅读代码的时候知道这是类,优点这样可以防止静态方法的缺点,硬编码
        year, month, day = tuple(data_str.split('-'))
        return cls(int(year), int(month), int(day))


if __name__ == '__main__':
    new_day = Date(2018, 12, 31)
    new_day.tomorrow()  # python会自动传为tomorrow(new_day)
    print(new_day)

    # 2018-12-31
    data_str = '2018-12-31'
    result = data_str.split('-')
    print(result)
    # year, month, day = tuple(data_str.split('-'))
    # new_day = Date(int(year), int(month), int(day))
    print(new_day)

    # 用staticmethod完成初始化
    new_day = Date.parse_from_string(data_str)
    print(new_day)

    # 用classmethod完成初始化
    new_day = Date.from_str(data_str)
    print(new_day)

    print(Date.valid_str('2018-12-31'))
