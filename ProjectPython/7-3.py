from abc import ABC, abstractmethod
import json
import csv
import os


class FileProcessor(ABC):
    """抽象父类"""

    @abstractmethod
    def read_file(self, filepath):
        pass

    @abstractmethod
    def write_file(self, filepath, data):
        pass

    @abstractmethod
    def count_content(self, filepath):
        """统计文件内容"""
        pass


class TxtProcessor(FileProcessor):
    def read_file(self, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            print(f"TXT读取: {content[:50]}...")
            return content
        except FileNotFoundError:
            print("文件不存在")
        except PermissionError:
            print("权限不足")
        return ""

    def write_file(self, filepath, data):
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(data)
            print(f"TXT写入成功: {filepath}")
        except PermissionError:
            print("写入权限不足")

    def count_content(self, filepath):
        content = self.read_file(filepath)
        lines = content.count("\n") + 1 if content else 0
        chars = len(content)
        print(f"TXT统计: {lines}行, {chars}字符")
        return lines, chars


class CsvProcessor(FileProcessor):
    def read_file(self, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                rows = [row for row in reader]
            print(f"CSV读取: {len(rows)}行")
            return rows
        except FileNotFoundError:
            print("文件不存在")
        except PermissionError:
            print("权限不足")
        return []

    def write_file(self, filepath, data):
        try:
            with open(filepath, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(data)
            print(f"CSV写入成功: {filepath}")
        except PermissionError:
            print("写入权限不足")

    def count_content(self, filepath):
        rows = self.read_file(filepath)
        total_cells = sum(len(row) for row in rows)
        print(f"CSV统计: {len(rows)}行, {total_cells}单元格")
        return len(rows), total_cells


class JsonProcessor(FileProcessor):
    def read_file(self, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            print(f"JSON读取: {type(data).__name__}")
            return data
        except FileNotFoundError:
            print("文件不存在")
        except json.JSONDecodeError:
            print("JSON格式错误")
        except PermissionError:
            print("权限不足")
        return {}

    def write_file(self, filepath, data):
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"JSON写入成功: {filepath}")
        except PermissionError:
            print("写入权限不足")
        except TypeError:
            print("数据类型不可序列化")

    def count_content(self, filepath):
        data = self.read_file(filepath)
        if isinstance(data, dict):
            keys = len(data.keys())
            print(f"JSON统计: {keys}个键")
            return keys
        elif isinstance(data, list):
            print(f"JSON统计: {len(data)}个元素")
            return len(data)
        return 0


class XmlProcessor(FileProcessor):
    def read_file(self, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            print(f"XML读取: {len(content)}字符")
            return content
        except FileNotFoundError:
            print("文件不存在")
        except PermissionError:
            print("权限不足")
        return ""

    def write_file(self, filepath, data):
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(data)
            print(f"XML写入成功: {filepath}")
        except PermissionError:
            print("写入权限不足")

    def count_content(self, filepath):
        content = self.read_file(filepath)
        tag_count = content.count("<") - content.count("</") * 2
        print(f"XML统计: {len(content)}字符, 约{tag_count}个标签")
        return len(content), tag_count


def auto_select_processor(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".txt":
        return TxtProcessor()
    elif ext == ".csv":
        return CsvProcessor()
    elif ext == ".json":
        return JsonProcessor()
    elif ext == ".xml":
        return XmlProcessor()
    else:
        print(f"未识别的格式: {ext}")
        return None


def process_file(processor, filepath, action, data=None):
    """统一处理函数,多态调用"""
    if action == "read":
        return processor.read_file(filepath)
    elif action == "write":
        processor.write_file(filepath, data)
    elif action == "count":
        processor.count_content(filepath)


def test():
    print("基础部分")
    txt = TxtProcessor()
    csv_p = CsvProcessor()
    json_p = JsonProcessor()

    test_txt = "test.txt"
    txt.write_file(test_txt, "Hello World\n你好世界")
    process_file(txt, test_txt, "read")
    process_file(txt, test_txt, "count")

    test_csv = "test.csv"
    csv_p.write_file(test_csv, [["姓名", "年龄"], ["张三", "20"], ["李四", "21"]])
    process_file(csv_p, test_csv, "read")
    process_file(csv_p, test_csv, "count")

    test_json = "test.json"
    json_p.write_file(test_json, {"name": "张三", "age": 20})
    process_file(json_p, test_json, "read")
    process_file(json_p, test_json, "count")

    print("\n扩展部分")
    xml_p = XmlProcessor()
    test_xml = "test.xml"
    xml_p.write_file(test_xml, "<root><item>内容</item></root>")
    process_file(xml_p, test_xml, "read")
    process_file(xml_p, test_xml, "count")

    print("\n自动选择处理器:")
    for f in ["data.txt", "data.csv", "data.json", "data.xml"]:
        proc = auto_select_processor(f)
        if proc:
            print(f"  {f} -> {type(proc).__name__}")

    for f in [test_txt, test_csv, test_json, test_xml]:
        if os.path.exists(f):
            os.remove(f)


if __name__ == "__main__":
    test()