
import sqlite3 as sql

def create_table():
    con = sql.connect('okul.db')
    cursor = con.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS User(
                id integer PRIMARY KEY,
                name text,
                lastname text,
                username text,
                password text
            )""")
    con.commit()
    con.close()


def insert(name, lastname, username, password):
    con = sql.connect('okul.db')
    cursor = con.cursor()
    
    data = (name, lastname, username, password)
    add_command = """INSERT INTO User(name, lastname, username, password) VALUES (?, ?, ?, ?)"""

    cursor.execute(add_command, data)

    con.commit()
    con.close()


def print_all():
    con = sql.connect('okul.db')
    cursor = con.cursor()

    cursor.execute("""SELECT * from User""")
    list_all = cursor.fetchall()

    for user in list_all:
        print(f"\nİsim: {user[1]}, \nSoyisim: {user[2]}, \nKullanıcı adı: {user[3]}")


    con.close()


def search_username(username):
    con = sql.connect('okul.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM User WHERE username = ?", (username,))
    result = cur.fetchone()
    con.close()
    return result
    
    
def update_password(username,newPassword):
    con = sql.connect('okul.db')
    cursor = con.cursor()

    upd_command = f"""UPDATE User SET PASSWORD = {newPassword} WHERE username = {username}"""
    cursor.execute(upd_command,{newPassword},username,{username})

    con.commit()
    con.close()


def delete_account(username):
    con = sql.connect("okul.db")
    cursor = con.cursor()

    dlt_command = """DELETE from User WHERE username = ?"""
    cursor.execute(dlt_command, (username,))

    con.commit()
    con.close()


def delete_table():
    con = sql.connect("okul.db")
    cursor = con.cursor

    cursor.execute("""DROP TABLE User""")

    con.commit()
    con.close()
