import sqlite3
from db.queries import (
    CREATE_USER_TABLE,
    CREATE_QUESTIONS_TABLE,
    CREATE_RESULTS_TABLE,
    GET_ALL_QUESTIONS,
    INSERT_QUESTIONS
)
from config import DATABASE
from src.questions import QUESTIONS

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn 

def init_db():
    conn = get_db()
    conn.execute(CREATE_USER_TABLE)
    conn.execute(CREATE_RESULTS_TABLE)
    conn.execute(CREATE_QUESTIONS_TABLE)
    #Заполнение бд с вопросами 
    if not conn.execute(GET_ALL_QUESTIONS).fetchall():
        for q_text, q_answer in QUESTIONS:
            conn.execute(INSERT_QUESTIONS, (q_text, q_answer))
    conn.commit()
    conn.close()