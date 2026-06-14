scores = []

while True:
    score_input = input("请输入学生成绩（0~100，输入-1停止）：")
    score = float(score_input)

    if score == -1:
        break

    if score < 0 or score > 100:
        print("成绩非法，不存入")
        continue

    scores.append(score)

if len(scores) == 0:
    print("未录入任何有效成绩！")
else:
    total_count = len(scores)
    total_sum = sum(scores)
    avg_score = round(total_sum / total_count, 2)
    max_score = max(scores)
    min_score = min(scores)

    excellent = good = pass_ = fail = 0
    for s in scores:
        if s >= 90:
            excellent += 1
        elif s >= 80:
            good += 1
        elif s >= 60:
            pass_ += 1
        else:
            fail += 1

    if avg_score >= 85:
        class_grade = "优秀"
    elif avg_score >= 70:
        class_grade = "良好"
    elif avg_score >= 60:
        class_grade = "及格"
    else:
        class_grade = "不及格"

    print("\n成绩统计：")
    print(f"总人数：{total_count}")
    print(f"总分：{total_sum}")
    print(f"平均分：{avg_score}")
    print(f"最高分：{max_score}")
    print(f"最低分：{min_score}")
    print(f"优秀人数：{excellent}")
    print(f"良好人数：{good}")
    print(f"及格人数：{pass_}")
    print(f"不及格人数：{fail}")
    print(f"班级整体等级：{class_grade}")