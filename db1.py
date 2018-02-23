import sqlite3
import random

db = sqlite3.connect("card.db")
db.text_factory = str
db.row_factory = sqlite3.Row
db.execute("drop table if EXISTS card")
db.execute("create table card(test1 text,test2 int)")

cards = [("d1",1),("d2",2),("d3",3),("d4",4),("d5",5),("d6",6),("d7",7),("d8",8),("d9",9),("d10",10),("dk",10),("dq",10),("dj",10),("da",11),("c1",1),("c2",2),("c3",3),("c4",4),("c5",5),("c6",6),("c7",7),("c8",8),("c9",9),("c10",10),("ck",10),("cq",10),("cj",10),("ca",11),("b1",1),("b2",2),("b3",3),("b4",4),("b5",5),("b6",6),("b7",7),("b8",8),("b9",9),("b10",10),("bk",10),("bq",10),("bj",10),("ba",11),("a1",1),("a2",2),("a3",3),("a4",4),("a5",5),("a6",6),("a7",7),("a8",8),("a9",9),("a10",10),("ak",10),("aq",10),("aj",10),("aa",11),]

db.executemany("insert INTO card VALUES (?,?)", a)
db.commit()
cursor = db.execute("SELECT * FROM card ORDER BY test1")
x = []
y = []
for row in cursor:
    x.append(([(row['test1'])]))
    y.append(([(row['test2'])]))
