import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS scores (user TEXT, score REAL)''')
    conn.commit()
    conn.close()

def save_score(user, score):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO scores VALUES (?,?)", (user, score))
    conn.commit()
    conn.close()

def get_scores(user):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT score FROM scores WHERE user=?", (user,))
    rows = c.fetchall()
    conn.close()
    return [r[0] for r in rows]