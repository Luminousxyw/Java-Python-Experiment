while True:
    s = input("请输入一个月份（1~12）：")
    try:
        month = int(s)
    except ValueError:
        print("输入错误，请输入整数月份")
        continue

    if month < 1 or month > 12:
        print("月份超出范围，请输入1~12之间的数字")
        continue

    if 3 <= month <= 5:
        season = "春季"
    elif 6 <= month <= 8:
        season = "夏季"
    elif 9 <= month <= 11:
        season = "秋季"
    else:
        season = "冬季"

    if month == 2:
        days = 28
    elif month in (4, 6, 9, 11):
        days = 30
    else:
        days = 31

    print(f"该月份是{season}，共有{days}天")
    break