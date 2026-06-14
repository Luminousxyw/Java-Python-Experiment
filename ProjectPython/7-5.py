import json
import os


class Book:
    def __init__(self, title, author, isbn, stock):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.stock = stock

    def show_info(self):
        return f"《{self.title}》作者:{self.author} ISBN:{self.isbn} 库存:{self.stock}"

    def change_stock(self, delta):
        new_stock = self.stock + delta
        if new_stock < 0:
            raise ValueError(f"库存不足,当前库存{self.stock}")
        self.stock = new_stock


class Reader:
    MAX_BORROW = 3

    def __init__(self, name, reader_id):
        self.name = name
        self.reader_id = reader_id
        self.borrowed = []

    def borrow_book(self, book):
        if len(self.borrowed) >= self.MAX_BORROW:
            raise Exception(f"借阅数量已达上限({self.MAX_BORROW}本)")
        book.change_stock(-1)
        self.borrowed.append(book.isbn)

    def return_book(self, book):
        if book.isbn not in self.borrowed:
            raise Exception(f"未借阅《{book.title}》,无法归还")
        book.change_stock(1)
        self.borrowed.remove(book.isbn)

    def show_info(self):
        print(f"读者:{self.name} ID:{self.reader_id} 已借:{len(self.borrowed)}本")


class Librarian(Reader):
    def __init__(self, name, reader_id, admin_level):
        super().__init__(name, reader_id)
        self.admin_level = admin_level
        self.MAX_BORROW = 10

    def manage_books(self):
        print(f"管理员{self.name}权限等级{self.admin_level}")


class Library:
    total_books_count = 0
    total_borrow_count = 0

    def __init__(self, name):
        self.name = name
        self.books = []
        self.readers = []
        self.data_file = "library_data.json"

    def add_book(self, title, author, isbn, stock):
        book = Book(title, author, isbn, stock)
        self.books.append(book)
        Library.total_books_count += stock
        print(f"添加书籍: {book.show_info()}")

    def register_reader(self, name, reader_id, is_librarian=False, admin_level=0):
        if is_librarian:
            r = Librarian(name, reader_id, admin_level)
        else:
            r = Reader(name, reader_id)
        self.readers.append(r)
        print(f"注册读者: {r.name}")
        return r

    def find_book(self, keyword):
        results = []
        for b in self.books:
            if keyword.lower() in b.title.lower() or \
               keyword.lower() in b.author.lower() or \
               keyword in b.isbn:
                results.append(b)
        return results

    def borrow(self, reader, isbn):
        for b in self.books:
            if b.isbn == isbn:
                reader.borrow_book(b)
                Library.total_borrow_count += 1
                print(f"{reader.name}借阅《{b.title}》成功")
                return
        print(f"未找到ISBN:{isbn}的书籍")

    def return_book(self, reader, isbn):
        for b in self.books:
            if b.isbn == isbn:
                reader.return_book(b)
                print(f"{reader.name}归还《{b.title}》成功")
                return
        print(f"未找到ISBN:{isbn}的书籍")

    def save_data(self):
        data = {
            "books": [{"title": b.title, "author": b.author,
                       "isbn": b.isbn, "stock": b.stock} for b in self.books],
            "readers": [{"name": r.name, "reader_id": r.reader_id,
                         "borrowed": r.borrowed} for r in self.readers]
        }
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"数据已保存到{self.data_file}")

    def load_data(self):
        if not os.path.exists(self.data_file):
            print("数据文件不存在,使用空库")
            return
        with open(self.data_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        for b_data in data.get("books", []):
            self.add_book(b_data["title"], b_data["author"],
                          b_data["isbn"], b_data["stock"])
        for r_data in data.get("readers", []):
            r = self.register_reader(r_data["name"], r_data["reader_id"])
            r.borrowed = r_data.get("borrowed", [])
        print(f"数据已加载,{len(self.books)}本书,{len(self.readers)}位读者")

    def show_status(self):
        print(f"\n===== {self.name} =====")
        print(f"总藏书量:{Library.total_books_count} 总借阅次数:{Library.total_borrow_count}")
        for b in self.books:
            print(f"  {b.show_info()}")
        for r in self.readers:
            print(f"  {r.name} 已借:{r.borrowed}")


def test():
    print("=== 基础部分 ===")
    lib = Library("中心图书馆")
    lib.add_book("Python编程", "张三", "ISBN001", 3)
    lib.add_book("数据结构", "李四", "ISBN002", 2)
    lib.add_book("算法导论", "王五", "ISBN003", 1)

    r1 = lib.register_reader("小明", "R001")
    r2 = lib.register_reader("小红", "R002")

    try:
        lib.borrow(r1, "ISBN001")
        lib.borrow(r1, "ISBN002")
        lib.borrow(r1, "ISBN003")
        lib.borrow(r1, "ISBN001")
    except Exception as e:
        print(f"借阅异常: {e}")

    try:
        lib.return_book(r2, "ISBN001")
    except Exception as e:
        print(f"归还异常: {e}")

    try:
        lib.borrow(r2, "ISBN003")
    except Exception as e:
        print(f"借阅异常: {e}")

    print("\n查询:")
    for b in lib.find_book("Python"):
        print(f"  找到: {b.show_info()}")

    print("\n=== 扩展部分 ===")
    admin = lib.register_reader("管理员", "A001", is_librarian=True, admin_level=3)
    admin.manage_books()
    lib.borrow(admin, "ISBN001")
    lib.borrow(admin, "ISBN001")
    lib.borrow(admin, "ISBN001")

    lib.show_status()
    lib.save_data()

    lib2 = Library("分馆")
    lib2.load_data()
    lib2.show_status()

    if os.path.exists("library_data.json"):
        os.remove("library_data.json")


if __name__ == "__main__":
    test()
