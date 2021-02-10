import json
import sqlite3

usr_lst = []
msg_lst = []

j_data = open("chat.json", "rb")
data = json.load(j_data)

conn = sqlite3.connect("chat.db")# change the str to :memory: to work with memory db
cur = conn.cursor() #cursor creator, commands go there
def table_create():
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


def json_digest():
    global usr_lst
    global msg_lst
    for msg in data["messages"]:
        if msg["type"] == "message":
            try:
                usr_lst.append((  msg["from_id"], msg["from"]))
                if type(msg["text"]) == str:
                    msg_lst.append((msg["id"], msg["date"], msg["from_id"], msg["text"].replace("'", "+")))
                    #print("str")
                if type(msg["text"]) == list:
                    try:
                        msg_lst.append((msg["id"], msg["date"], msg["from_id"], msg["text"][0]["text"].replace("'", "+")))
                    except:
                        msg_lst.append((msg["id"], msg["date"], msg["from_id"], msg["text"][1]["text"].replace("'", "+")))
                    #print(msg["text"][0]["text"])

            except Exception as e:
                print("append: ", e, msg)
        else:
            print("not a message.")
    """
    print(set(usr_lst))
    for item in msg_lst:
        print(item[1])
    """

def insert_usr():
    try:
        cur.executemany(f"INSERT INTO Users (usr_id, usr_name) VALUES (?,?)", list(set(usr_lst)))
    except:
        return

def insert_msg():
    for msg in msg_lst:
        try:
            cur.execute(f"INSERT INTO Messages (msg_id, msg_date, from_id, msg_txt) VALUES({msg[0]}, '{msg[1]}', {msg[2]}, '{msg[3]}')")
            #conn.commit()
        except Exception as e:
            print(e)

table_create()
json_digest()
insert_msg()
insert_usr()
conn.commit()

conn.close()
