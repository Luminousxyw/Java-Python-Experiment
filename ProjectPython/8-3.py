import sqlite3
import threading
import os


class StudentDB:
    def __init__(self, db_name="student_db.sqlite"):
        self.db_name = db_name
        self.lock = threading.Lock()
        self.conn = None
        self.cursor = None
        self.connect()
        self.create_table()

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
            self.conn.execute("PRAGMA foreign_keys = ON")
            self.cursor = self.conn.cursor()
            print(f"数据库{self.db_name}连接成功")
        except sqlite3.Error as e:
            print(f"数据库连接失败: {e}")

    def create_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER CHECK(age BETWEEN 15 AND 30),
            gender TEXT CHECK(gender IN ('男', '女')),
            class TEXT NOT NULL,
            score REAL CHECK(score BETWEEN 0 AND 100)
        )
        """
        try:
            self.cursor.execute(sql)
            self.cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_name ON student(name)"
            )
            self.cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_class ON student(class)"
            )
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"建表失败: {e}")

    def insert(self, name, age, gender, cls, score):
        if not 15 <= age <= 30:
            print("年龄需在15-30之间")
            return False
        if gender not in ("男", "女"):
            print("性别需为男或女")
            return False
        if not 0 <= score <= 100:
            print("成绩需在0-100之间")
            return False
        if not cls.strip():
            print("班级不能为空")
            return False
        sql = "INSERT INTO student (name, age, gender, class, score) VALUES (?, ?, ?, ?, ?)"
        try:
            with self.lock:
                self.cursor.execute(sql, (name, age, gender, cls, score))
                self.conn.commit()
            print(f"插入成功: {name}")
            return True
        except sqlite3.IntegrityError as e:
            print(f"插入失败(约束冲突): {e}")
            return False
        except sqlite3.Error as e:
            print(f"SQL错误: {e}")
            return False

    def batch_insert(self, students):
        sql = "INSERT INTO student (name, age, gender, class, score) VALUES (?, ?, ?, ?, ?)"
        try:
            with self.lock:
                self.cursor.executemany(sql, students)
                self.conn.commit()
            print(f"批量插入{len(students)}条成功")
            return True
        except sqlite3.IntegrityError as e:
            print(f"批量插入失败,回滚: {e}")
            self.conn.rollback()
            return False

    def query(self, cls=None, min_score=None, order="asc", page=1, per_page=10):
        conditions = []
        params = []
        if cls:
            conditions.append("class = ?")
            params.append(cls)
        if min_score is not None:
            conditions.append("score > ?")
            params.append(min_score)
        where = ""
        if conditions:
            where = "WHERE " + " AND ".join(conditions)
        order_clause = f"ORDER BY score {'ASC' if order.lower() == 'asc' else 'DESC'}"
        offset = (page - 1) * per_page

        count_sql = f"SELECT COUNT(*) FROM student {where}"
        data_sql = f"SELECT * FROM student {where} {order_clause} LIMIT ? OFFSET ?"

        try:
            self.cursor.execute(count_sql, params)
            total = self.cursor.fetchone()[0]
            self.cursor.execute(data_sql, params + [per_page, offset])
            rows = self.cursor.fetchall()
            total_pages = (total + per_page - 1) // per_page if total > 0 else 1
            print(f"查询结果(第{page}页/共{total_pages}页,共{total}条):")
            print(f"{'ID':<4} {'姓名':<8} {'年龄':<4} {'性别':<4} {'班级':<12} {'成绩':<6}")
            for r in rows:
                print(f"{r[0]:<4} {r[1]:<8} {r[2]:<4} {r[3]:<4} {r[4]:<12} {r[5]:<6}")
            return rows, total, total_pages
        except sqlite3.Error as e:
            print(f"查询错误: {e}")
            return [], 0, 0

    def update(self, student_id, **kwargs):
        allowed = ["name", "age", "gender", "class", "score"]
        sets = []
        params = []
        for k, v in kwargs.items():
            if k in allowed and v is not None:
                sets.append(f"{k} = ?")
                params.append(v)
        if not sets:
            print("无有效更新字段")
            return False
        params.append(student_id)
        sql = f"UPDATE student SET {', '.join(sets)} WHERE id = ?"
        try:
            with self.lock:
                self.cursor.execute(sql, params)
                self.conn.commit()
            if self.cursor.rowcount > 0:
                print(f"更新成功,影响{self.cursor.rowcount}行")
                return True
            else:
                print("未找到该学生")
                return False
        except sqlite3.Error as e:
            print(f"更新错误: {e}")
            return False

    def delete(self, student_id):
        confirm = input(f"确认删除学号{student_id}? (y/n): ")
        if confirm.lower() != "y":
            print("取消删除")
            return False
        try:
            with self.lock:
                self.cursor.execute("DELETE FROM student WHERE id = ?", (student_id,))
                self.conn.commit()
            if self.cursor.rowcount > 0:
                print(f"删除成功")
                return True
            else:
                print("未找到该学生")
                return False
        except sqlite3.Error as e:
            print(f"删除错误: {e}")
            return False

    def statistics(self):
        sql = """
        SELECT class,
               COUNT(*) as cnt,
               AVG(score) as avg_s,
               MAX(score) as max_s,
               MIN(score) as min_s
        FROM student
        GROUP BY class
        """
        try:
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            print("\n===== 班级统计报表 =====")
            print(f"{'班级':<12} {'人数':<4} {'平均分':<8} {'最高分':<8} {'最低分':<8}")
            for r in rows:
                print(f"{r[0]:<12} {r[1]:<4} {r[2]:<8.2f} {r[3]:<8} {r[4]:<8}")
            return rows
        except sqlite3.Error as e:
            print(f"统计错误: {e}")
            return []

    def backup(self, filename="backup.sql"):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for line in self.conn.iterdump():
                    f.write(line + "\n")
            print(f"备份成功: {filename}")
            return True
        except Exception as e:
            print(f"备份失败: {e}")
            return False

    def restore(self, filename="backup.sql"):
        if not os.path.exists(filename):
            print(f"备份文件{filename}不存在")
            return False
        try:
            with open(filename, "r", encoding="utf-8") as f:
                sql = f.read()
            with self.lock:
                self.cursor.executescript(sql)
                self.conn.commit()
            print(f"恢复成功: {filename}")
            return True
        except Exception as e:
            print(f"恢复失败: {e}")
            return False

    def close(self):
        if self.conn:
            self.conn.close()
            print("数据库连接已关闭")


def menu():
    print("\n===== 学生信息管理系统 =====")
    print("1. 添加学生")
    print("2. 批量插入")
    print("3. 查询学生")
    print("4. 修改学生")
    print("5. 删除学生")
    print("6. 班级统计")
    print("7. 数据库备份")
    print("8. 数据库恢复")
    print("9. 多线程并发测试")
    print("0. 退出")
    return input("选择: ")


def test():
    db = StudentDB()

    while True:
        choice = menu()

        if choice == "1":
            name = input("姓名: ")
            try:
                age = int(input("年龄(15-30): "))
                gender = input("性别(男/女): ")
                cls = input("班级: ")
                score = float(input("成绩(0-100): "))
                db.insert(name, age, gender, cls, score)
            except ValueError:
                print("输入格式错误")

        elif choice == "2":
            students = [
                ("张三", 18, "男", "计算机1班", 85.5),
                ("李四", 19, "女", "计算机1班", 92.0),
                ("王五", 20, "男", "计算机2班", 76.0),
                ("赵六", 18, "女", "计算机2班", 88.5),
                ("钱七", 19, "男", "计算机1班", 66.0),
            ]
            db.batch_insert(students)

        elif choice == "3":
            cls = input("按班级查询(留空跳过): ").strip() or None
            mins = input("最低分数(留空跳过): ").strip()
            min_score = float(mins) if mins else None
            order = input("排序(asc/desc,默认asc): ") or "asc"
            try:
                page = int(input("页码(默认1): ") or "1")
            except ValueError:
                page = 1
            db.query(cls=cls, min_score=min_score, order=order, page=page)

        elif choice == "4":
            try:
                sid = int(input("学号: "))
                print("输入新值(留空不修改):")
                name = input("姓名: ").strip() or None
                age_s = input("年龄: ").strip()
                age = int(age_s) if age_s else None
                gender = input("性别: ").strip() or None
                cls = input("班级: ").strip() or None
                score_s = input("成绩: ").strip()
                score = float(score_s) if score_s else None
                kwargs = {k: v for k, v in [("name", name), ("age", age),
                         ("gender", gender), ("class", cls), ("score", score)]
                         if v is not None}
                db.update(sid, **kwargs)
            except ValueError:
                print("输入格式错误")

        elif choice == "5":
            try:
                sid = int(input("学号: "))
                db.delete(sid)
            except ValueError:
                print("学号需为数字")

        elif choice == "6":
            db.statistics()

        elif choice == "7":
            fname = input("备份文件名(默认backup.sql): ") or "backup.sql"
            db.backup(fname)

        elif choice == "8":
            fname = input("恢复文件(默认backup.sql): ") or "backup.sql"
            db.restore(fname)

        elif choice == "9":
            def worker(name):
                for i in range(3):
                    db.insert(f"{name}_{i}", 20, "男", "测试班", 80.0)
            threads = []
            for tname in ["线程A", "线程B", "线程C"]:
                t = threading.Thread(target=worker, args=(tname,))
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
            print("多线程并发测试完成")
            db.query(cls="测试班")

        elif choice == "0":
            break
        else:
            print("无效选项")

    db.close()
    if os.path.exists(db.db_name):
        os.remove(db.db_name)


if __name__ == "__main__":
    test()
