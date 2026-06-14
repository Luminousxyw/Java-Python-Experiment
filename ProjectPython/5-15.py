students = []
pass_count = 0

for i in range(5):
    while True:
        score = float(input(f"请输入第{i + 1}个学生的成绩（0~100）："))
        if 0 <= score <= 100:
            break
        print("成绩非法，请重新录入！")

    if score >= 90:
        grade = "优秀"
    elif score >= 80:
        grade = "良好"
    elif score >= 60:
        grade = "及格"
    else:
        grade = "不及格"

    if score >= 60:
        pass_count += 1

    students.append((score, grade))

print("\n成绩汇总：")
for i, (score, grade) in enumerate(students, 1):
    print(f"学生{i}：成绩={score}，等级={grade}")

print(f"\n及格人数：{pass_count}")