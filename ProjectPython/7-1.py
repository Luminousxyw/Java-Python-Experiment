class Employee:
    total_employees = 0
    total_salary = 0
    VALID_POSITIONS = ["经理", "工程师", "专员", "实习生"]

    def __init__(self, emp_id, name, position, basic_salary, years):
        if not self.__validate_id(emp_id):
            raise ValueError(f"员工编号{emp_id}格式错误,必须为8位数字")
        self.__id = emp_id
        self.__name = name
        self.__position = position if position in self.VALID_POSITIONS else "实习生"
        self.__basic_salary = basic_salary if basic_salary >= 0 else 0
        self.__years = years if years >= 0 else 0
        Employee.total_employees += 1
        Employee.total_salary += self.monthly_salary()

    def __validate_id(self, emp_id):
        return len(emp_id) == 8 and emp_id.isdigit()

    def monthly_salary(self):
        return self.__basic_salary + self.__years * 100

    def show_info(self):
        print(f"编号:{self.__id} 姓名:{self.__name} 职位:{self.__position} "
              f"基础工资:{self.__basic_salary} 入职年限:{self.__years} "
              f"月工资:{self.monthly_salary()}")

    def change_position(self, new_pos):
        if new_pos in self.VALID_POSITIONS:
            self.__position = new_pos
            print(f"职位已更新为{new_pos}")
        else:
            print(f"非法职位,可选:{self.VALID_POSITIONS}")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip():
            self.__name = value
        else:
            print("姓名不能为空")

    @property
    def years(self):
        return self.__years

    @years.setter
    def years(self, value):
        if value >= 0:
            old_salary = self.monthly_salary()
            self.__years = value
            Employee.total_salary += self.monthly_salary() - old_salary
        else:
            print("入职年限不能为负")

    @staticmethod
    def is_valid_salary(value):
        return isinstance(value, (int, float)) and value >= 0

    @classmethod
    def print_summary(cls):
        print(f"总员工人数:{cls.total_employees} 总月工资:{cls.total_salary}")


def test():
    print("基础部分")
    e1 = Employee("20240101", "张三", "工程师", 8000, 3)
    e2 = Employee("20240102", "李四", "经理", 12000, 5)
    e3 = Employee("20240103", "王五", "专员", 5000, 1)

    for e in [e1, e2, e3]:
        e.show_info()

    e1.change_position("经理")
    e1.name = "张三丰"
    e1.years = 4
    e1.show_info()

    print("\n扩展部分")
    Employee.print_summary()
    print(f"工资5000是否合法: {Employee.is_valid_salary(5000)}")
    print(f"工资-100是否合法: {Employee.is_valid_salary(-100)}")

    try:
        e4 = Employee("12345", "测试", "工程师", 5000, 1)
    except ValueError as ve:
        print(f"捕获异常: {ve}")

    employees = [
        Employee("20240104", "赵六", "实习生", 3000, 0),
        Employee("20240105", "钱七", "工程师", 9000, 4),
    ]
    print("\n所有员工汇总:")
    for e in employees:
        e.show_info()
    Employee.print_summary()

if __name__ == "__main__":
    test()