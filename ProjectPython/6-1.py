import re

def string_basic():
    s = input("输入任意字符串: ")
    if s:
        print(f"第一个字符: {s[0]}")
        print(f"最后一个字符: {s[-1]}")

    sent = input("输入英文句子: ")
    print(f"全部大写: {sent.upper()}")
    print(f"全部小写: {sent.lower()}")
    print(f"首字母大写: {sent.title()}")

    s2 = input("输入含空格和a的字符串: ")
    cleaned = s2.strip().replace("a", "b")
    print(f"处理后: {cleaned}")

    s3 = input("输入判断字符串: ")
    print(f"是否纯数字: {s3.isdigit()}")
    keyword = input("输入关键字: ")
    print(f"是否包含关键字: {keyword in s3}")

def filter_text(text):
    result = ""
    upper_count = 0
    lower_count = 0
    for ch in text:
        if ch.isalpha() or ('\u4e00' <= ch <= '\u9fff'):
            result = result + ch
            if ch.isupper():
                upper_count = upper_count + 1
            elif ch.islower():
                lower_count = lower_count + 1
    print(f"过滤后文本: {result}")
    print(f"有效字母总数: {len(result)}")
    print(f"大写字母数量: {upper_count}")
    print(f"小写字母数量: {lower_count}")

def extend():
    while True:
        text = input("输入文本(输入quit退出): ")
        if text.strip().lower() == "quit":
            print("程序退出")
            break
        filter_text(text)

if __name__ == "__main__":
    print("基础部分")
    string_basic()
    print("\n扩展部分")
    extend()