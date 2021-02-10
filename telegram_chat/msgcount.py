import json
import matplotlib.pyplot as plt

count = {}
keys = []
vals = []

try:
    file_name = input("write the file name: ")#json file goes here
    chat_file = open(file_name, "rb")#rb solves encoding issues
    chat_json = json.load(chat_file)
except Exception as e:
    print(e)

for item in chat_json["messages"]:
    try:
        count[item["from"]] = count.get(item["from"], 0) + 1
    except Exception as e:
        print(e)

for item in list(count.keys()):
    keys.append(item)
    vals.append(count[item])

plt.bar(keys, vals)
plt.xticks(rotation=90)
plt.show()
