import sqlite3
from db.queries import CREATE_USER_TABLE,CREATE_QUESTIONS_TABLE,CREATE_RESULTS_TABLE
from config import DATABASE

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn 

def init_db():
    conn = get_db()
    conn.execute(CREATE_USER_TABLE)
    conn.execute(CREATE_RESULTS_TABLE)
    conn.execute(CREATE_QUESTIONS_TABLE)
    conn.commit()
    conn.close()