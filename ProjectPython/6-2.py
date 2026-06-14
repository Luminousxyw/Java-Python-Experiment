def tuple_basic():
    t1 = (1, 2, 3, 4, 5)
    t2 = (66,)
    print(f"普通元组: {t1}")
    print(f"单元素元组: {t2}")

    print(f"索引1到3: {t1[1:4]}")
    print(f"第一个元素: {t1[0]}")

    target = int(input("输入要统计的元素: "))
    count = 0
    for item in t1:
        if item == target:
            count = count + 1
    print(f"{target}出现次数: {count}")

    lst = list(t1)
    print(f"转为列表: {lst}")
    lst.append(6)
    print(f"修改后列表: {lst}")
    t3 = tuple(lst)
    print(f"转回元组: {t3}")

def extend():
    coords = ((2, 3), (-1, 5), (-3, -4), (4, -2), (1, 6), (-2, -7))
    print(f"坐标数据: {coords}")
    first_q = []
    third_q = []
    for x, y in coords:
        if x > 0 and y > 0:
            first_q.append((x, y))
        elif x < 0 and y < 0:
            third_q.append((x, y))
    print(f"第一象限坐标: {first_q}")
    print(f"第一象限数量: {len(first_q)}")
    print(f"第三象限坐标: {third_q}")
    print(f"第三象限数量: {len(third_q)}")

if __name__ == "__main__":
    print("基础部分")
    tuple_basic()
    print("\n扩展部分")
    extend()