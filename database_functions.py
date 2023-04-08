import os
import sqlite3

database_path = os.path.join('databases', 'database.db')

def init_db():
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    #cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='images'")
    cur.execute('''CREATE TABLE if not exists Posts 
    (id INT, title TEXT, contents TEXT, timeStamp TEXT, categoryId TEXT)''')
    cur.execute('''CREATE TABLE if not exists Categories 
    (id INT, name TEXT)''')
    conn.commit()
    cur.close()
    conn.close()

def create_new_post(id, title, contents, timeStamp, categoryId):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    insert_query = '''INSERT INTO Posts
        (id, title, contents, timeStamp, categoryid) 
        VALUES (?, ?, ?, ?, ?);'''
    data_tuple = (id, title, contents, timeStamp, categoryId)
    cur.execute(insert_query, data_tuple)
    conn.commit()
    cur.close()
    conn.close()

def get_all_posts():
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Posts")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return(data)

def get_post(id):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Posts WHERE id = ?", (id,))
    cur.close()
    conn.close()
    return(data)

def get_all_categories():
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Categories")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return(data)

def update_post(id):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Posts where id=?", (id,))
    data = cur.fetchall()
        #retrieve post and alter with given data
    cur.close()
    conn.close()
    return(data)


def delete_all_posts():
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute("DELETE * FROM Posts")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return(data)

def delete_post(id):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute("DELETE from Posts where id=?", (id,))
    conn.commit()
    cur.close()
    conn.close()
