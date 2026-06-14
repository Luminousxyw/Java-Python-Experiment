def list_basic():
    nums = [3, 1, 4, 1, 5, 9]
    print(f"原始列表: {nums}")

    nums.append(2)
    print(f"append后: {nums}")
    nums.insert(0, 7)
    print(f"insert后: {nums}")

    nums.pop(2)
    print(f"pop索引2后: {nums}")
    nums.remove(1)
    print(f"remove 1后: {nums}")
    del nums[0]
    print(f"del索引0后: {nums}")

    sorted_asc = sorted(nums)
    print(f"升序后: {sorted_asc}")
    sorted_desc = sorted(nums, reverse=True)
    print(f"降序后: {sorted_desc}")
    print(f"原列表不变: {nums}")

    evens = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)
    print(f"偶数列表: {evens}")

def extend():
    scores = []
    for i in range(10):
        while True:
            try:
                s = float(input(f"输入第{i+1}个成绩(0~100): "))
                if 0 <= s <= 100:
                    scores.append(s)
                    break
                else:
                    print("超出范围，重新输入")
            except ValueError:
                print("非数字，重新输入")

    high = scores[0]
    low = scores[0]
    total = 0
    for s in scores:
        total = total + s
        if s > high:
            high = s
        if s < low:
            low = s
    avg = total / len(scores)

    print(f"最高分: {high}")
    print(f"最低分: {low}")
    print(f"平均分: {avg:.2f}")

    for s in scores:
        if s >= 90:
            grade = "优秀"
        elif s >= 80:
            grade = "良好"
        elif s >= 60:
            grade = "及格"
        else:
            grade = "不及格"
        print(f"成绩{s}: {grade}")

if __name__ == "__main__":
    print("基础部分")
    list_basic()
    print("\n扩展部分")
    extend()