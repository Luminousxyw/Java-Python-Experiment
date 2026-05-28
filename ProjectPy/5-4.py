while True:
    year_str = input("请输入一个年份：")
    try:
        year = int(year_str)
        break
    except ValueError:
        print("输入错误，请输入整数年份")

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year,"年是闰年")
else:
    print(year,"年不是闰年")