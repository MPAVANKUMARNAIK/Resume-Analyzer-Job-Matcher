import sqlite3

conn = sqlite3.connect("users.db", check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')

def register_user(u, p):
    c.execute("INSERT INTO users VALUES (?,?)", (u, p))
    conn.commit()

def login_user(u, p):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (u, p))
    return c.fetchone() is not None