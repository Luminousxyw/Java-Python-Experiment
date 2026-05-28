import random
num=random.randint(1,100)
n=1
while n<=10:
    count=int(input("请输入你猜的数字："))
    if count==num:
        print("恭喜猜对！")
        print(f"正确答案是：{num}")
        break
    elif count>num:
        print("猜大了")
    else:
        print("猜小了")
    n+=1
if n>10:
    print("次数过多，游戏失败")