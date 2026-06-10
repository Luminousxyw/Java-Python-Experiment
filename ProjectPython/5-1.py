while True:
    num_str = input("请输入一个整数：")
    try:
        num = int(num_str)
        break
    except ValueError:
        print("输入错误，请输入整数")
if num > 0:
    print("该数是正数")