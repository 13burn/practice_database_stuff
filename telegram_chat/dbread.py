import sqlite3

conn = sqlite3.connect("chat.db")
cur = conn.cursor()

def db_reader():
    try:
        cur.execute("SELECT * FROM Messages JOIN Users WHERE Messages.from_id=Users.usr_id")
        #cur.fetchone()
        #cur.fetchmany(<limit>)
        #cur.fetchall()
        for entry in cur.fetchmany(50):
            print(f"{entry[1]}\t{entry[5]}\t\t{entry[3]}")#this reads the date, sander name and message
    except:
        print("can't read table")

db_reader()

conn.commit()

conn.close()
