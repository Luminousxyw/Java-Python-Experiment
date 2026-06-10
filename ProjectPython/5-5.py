while True:
    s = input("请输入一个学生成绩（0~100）：")
    try:
        score = int(s)
    except ValueError:
        print("输入错误，请输入整数")
        continue

    if score < 0 or score > 100:
        print("成绩输入非法，请输入0~100之间的数字")
        continue

    if score >= 90:
        grade = "优秀"
    elif score >= 80:
        grade = "良好"
    elif score >= 60:
        grade = "及格"
    else:
        grade = "不及格"

    print(f"你的成绩是：{score}，等级是：{grade}")
    break