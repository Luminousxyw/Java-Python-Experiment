def dict_basic():
    stu = {"姓名": "张三", "年龄": 20, "成绩": 85}
    print(f"学生信息: {stu}")

    print(f"姓名: {stu['姓名']}")
    print(f"get年龄: {stu.get('年龄')}")
    print(f"get不存在的键: {stu.get('地址', '未找到')}")

    stu["班级"] = "计算机1班"
    print(f"新增班级后: {stu}")
    stu["成绩"] = 90
    print(f"修改成绩后: {stu}")
    del stu["年龄"]
    print(f"删除年龄后: {stu}")

    print("遍历键:")
    for k in stu.keys():
        print(k, end=" ")
    print()
    print("遍历值:")
    for v in stu.values():
        print(v, end=" ")
    print()
    print("遍历键值对:")
    for k, v in stu.items():
        print(f"{k}: {v}")

def extend():
    students = {}

    while True:
        print("\n1 添加学生 2 查询 3 修改 4 统计平均分 5 退出")
        choice = input("选择: ")

        if choice == "1":
            name = input("姓名: ")
            scores = []
            for subj in ["语文", "数学", "英语"]:
                while True:
                    try:
                        s = float(input(f"{subj}成绩: "))
                        scores.append(s)
                        break
                    except ValueError:
                        print("输入数字")
            students[name] = scores
            print(f"已添加{name}")

        elif choice == "2":
            name = input("查询姓名: ")
            if name in students:
                print(f"{name}成绩: {students[name]}")
            else:
                print("未找到")

        elif choice == "3":
            name = input("修改姓名: ")
            if name in students:
                subj = input("科目: ")
                if subj == "语文":
                    idx = 0
                elif subj == "数学":
                    idx = 1
                elif subj == "英语":
                    idx = 2
                else:
                    print("无此科目")
                    continue
                try:
                    new_s = float(input("新分数: "))
                    students[name][idx] = new_s
                    print("修改成功")
                except ValueError:
                    print("输入数字")
            else:
                print("未找到")

        elif choice == "4":
            for name, sc in students.items():
                avg = sum(sc) / len(sc)
                print(f"{name}平均分: {avg:.2f}")

        elif choice == "5":
            break
        else:
            print("无效选项")

if __name__ == "__main__":
    print("基础部分")
    dict_basic()
    print("\n扩展部分")
    extend()