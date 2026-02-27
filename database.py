import sqlite3


def init_db():
    conn = sqlite3.connect("scorvanta.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT,
        plan TEXT DEFAULT 'free'
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        score INTEGER,
        industry TEXT,
        revenue INTEGER,
        employees INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_score(username, score, industry, revenue, employees):
    conn = sqlite3.connect("scorvanta.db")
    c = conn.cursor()

    c.execute("""
    INSERT INTO scores (username, score, industry, revenue, employees)
    VALUES (?, ?, ?, ?, ?)
    """, (username, score, industry, revenue, employees))

    conn.commit()
    conn.close()


def get_user_history(username):
    conn = sqlite3.connect("scorvanta.db")
    c = conn.cursor()

    c.execute("""
    SELECT score, timestamp FROM scores
    WHERE username = ?
    ORDER BY timestamp
    """, (username,))

    data = c.fetchall()
    conn.close()
    return data


def get_report_count(username):
    conn = sqlite3.connect("scorvanta.db")
    c = conn.cursor()

    c.execute("""
    SELECT COUNT(*) FROM scores
    WHERE username = ?
    """, (username,))

    count = c.fetchone()[0]
    conn.close()
    return count


def upgrade_user(username):
    conn = sqlite3.connect("scorvanta.db")
    c = conn.cursor()

    c.execute("""
    UPDATE users
    SET plan = 'pro'
    WHERE username = ?
    """, (username,))

    conn.commit()
    conn.close()


def get_user_plan(username):
    conn = sqlite3.connect("scorvanta.db")
    c = conn.cursor()

    c.execute("""
    SELECT plan FROM users
    WHERE username = ?
    """, (username,))

    result = c.fetchone()

    conn.close()

    if result:
        return result[0]
    else:
        return "free"