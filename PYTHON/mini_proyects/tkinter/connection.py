import sqlite3

class Connect():
    def __init__(self):
        try:
            self.conn = sqlite3.connect('users.db')
            self.CreateTables()
        except Exception as ex:
            print(ex)
    
    def CreateTables(self):
        sql_create_table = '''CREATE TABLE IF NOT EXISTS users
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL);'''
        cur = self.conn.cursor()
        cur.execute(sql_create_table)
        cur.close()

        self.CreateAdmin()

    def CreateAdmin(self):
        try:
             sql_create_admin = '''INSERT INTO users(name,username,email,password) VALUES ('Admin','admin','admin@gmail.com','admin')'''
        except Exception as ex:
            print(ex)

        cur = self.conn.cursor()
        cur.execute(sql_create_admin)
        self.conn.commit()
        

conn = Connect()


        