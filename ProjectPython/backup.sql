BEGIN TRANSACTION;
CREATE TABLE student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER CHECK(age BETWEEN 15 AND 30),
            gender TEXT CHECK(gender IN ('男', '女')),
            class TEXT NOT NULL,
            score REAL CHECK(score BETWEEN 0 AND 100)
        );
INSERT INTO "student" VALUES(1,'a',20,'男','1',100.0);
CREATE INDEX idx_name ON student(name);
CREATE INDEX idx_class ON student(class);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('student',1);
COMMIT;
