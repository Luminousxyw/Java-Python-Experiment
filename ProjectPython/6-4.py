def set_basic():
    lst = [1, 2, 2, 3, 4, 4, 5]
    s = set(lst)
    print(f"列表去重后集合: {s}")

    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    print(f"交集: {a & b}")
    print(f"并集: {a | b}")
    print(f"差集a-b: {a - b}")
    print(f"对称差集: {a ^ b}")

    a.add(9)
    print(f"添加9后: {a}")
    a.discard(1)
    print(f"删除1后: {a}")

    num = int(input("输入要判断的元素: "))
    if num in a:
        print(f"{num}在集合中")
    else:
        print(f"{num}不在集合中")

def extend():
    raw1 = input("输入班级1学生姓名(逗号分隔): ")
    raw2 = input("输入班级2学生姓名(逗号分隔): ")

    def clean(names_str):
        result = set()
        for n in names_str.split(","):
            cleaned = n.strip().lower()
            if cleaned:
                result.add(cleaned)
        return result

    c1 = clean(raw1)
    c2 = clean(raw2)

    print(f"共有学生: {c1 & c2}")
    print(f"班级1独有: {c1 - c2}")
    print(f"班级2独有: {c2 - c1}")
    print(f"全体名单: {c1 | c2}")

if __name__ == "__main__":
    print("基础部分")
    set_basic()
    print("\n扩展部分")
    extend()