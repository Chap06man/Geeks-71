from db.database import get_db
from db.queries import (
    GET_ALL_QUESTIONS, 
    GET_QUESTION_BY_ID,
    UPDATE_QUESTIONS,
    DELETE_QUESTIONS
    )

def get_all_questions():
    conn = get_db()
    rows = conn.execute(GET_ALL_QUESTIONS).fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_question(question_id: int):
    conn = get_db()
    row = conn.execute(GET_QUESTION_BY_ID, (question_id, )).fetchone()
    conn.close()
    return dict(row) if row else None

def update_question(question_id: int,question_text: str, correct_answer: bool):
    conn = get_db()
    conn.execute(UPDATE_QUESTIONS, (question_id, question_text, correct_answer))
    conn.commit()
    conn.close()
    return get_question(question_id)

def delete_question(question_id: int):
    conn = get_db()
    conn.execute(DELETE_QUESTIONS, (question_id, ))
    conn.commit()
    conn.close()