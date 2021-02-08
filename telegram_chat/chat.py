import json
import sqlite3

usr_lst = []
msg_lst = []

j_data = open("chat.json", "rb")
data = json.load(j_data)

conn = sqlite3.connect("chat.db")# change the str to :memory: to work with memory db
cur = conn.cursor() #cursor creator, commands go there
cur.execute("""
CREATE TABLE IF NOT EXISTS "Messages" (
	"msg_id"	INTEGER NOT NULL UNIQUE,
	"msg_date"	TEXT NOT NULL,
	"from_id"	INTEGER NOT NULL,
	"msg_txt"	TEXT,
	PRIMARY KEY("msg_id")
);
""")
cur.execute("""
CREATE TABLE IF NOT EXISTS "Users" (
	"usr_id"	INTEGER NOT NULL UNIQUE,
	"usr_name"	INTEGER NOT NULL,
	PRIMARY KEY("usr_id")
);

""")#msg table command AND usr table command



for msg in data["messages"]:
    if msg["type"] == "message":
        try:
            usr_lst.append((  msg["from_id"], msg["from"]))
            msg_lst.append((msg["id"], msg["date"], msg["from_id"], msg["text"]))
        except Exception as e:
            print(e)
"""
print(set(usr_lst))
for item in msg_lst:
    print(item[1])
"""

def insert_usr():
    for usr in usr_lst:
        try:
            cur.execute(f"INSERT INTO Users ('usr_id', 'usr_name') VALUES('{usr[0]}','{usr[1]}')")
            #conn.commit()
        except Exception as e:
            print()

def insert_msg():
    for msg in msg_lst:
        try:
            cur.execute(f"INSERT INTO Messages (msg_id, msg_date, from_id, msg_txt) VALUES({msg[0]}, '{msg[1]}', {msg[2]}, '{msg[3]}')")
            #conn.commit()
        except Exception as e:
            print(e, msg[1])

insert_msg()
insert_usr()
conn.commit()