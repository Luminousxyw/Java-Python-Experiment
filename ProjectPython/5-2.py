while True:
    a_str = input("请输入整数 a：")
    try:
        a = int(a_str)
        break
    except ValueError:
        print("输入错误，请输入整数")
while True:
    b_str = input("请输入整数 b：")
    try:
        b = int(b_str)
        break
    except ValueError:
        print("输入错误，请输入整数")
if a > b:
    print("a大于b")
else:
    print("a不大于b")