import json
import sqlite3

j_data = open("chat.json", "rb")

data = json.load(j_data)

usr_lst = []
msg_lst = []
usr_set = set()

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