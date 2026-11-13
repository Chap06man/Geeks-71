from db.database import get_db
from db.queries import INSERT_RESULT, GET_SCORE_BY_USER_ID, UPDATE_RESULT, DELETE_RESULT, GET_RESULT_BY_ID

def save_result(user_id: int, question_id: int, is_correct: bool):
    conn = get_db()
    conn.execute(INSERT_RESULT, (user_id, question_id, int(is_correct)))
    conn.commit()
    conn.close()

def get_score(user_id: int):
    conn = get_db()
    row = conn.execute(GET_SCORE_BY_USER_ID, (user_id, )).fetchone()
    conn.close()
    return dict(row) if row else {'total': 0, 'correct': 0}

def get_result(result_id: int):
    conn = get_db()
    result = conn.execute(GET_RESULT_BY_ID, (result_id,)).fetchone()
    conn.close()
    return dict(result) if result else None

def update_result(result_id: int, is_correct: bool):
    conn = get_db()
    conn.execute(UPDATE_RESULT, (int(is_correct), result_id))
    conn.commit()
    conn.close()
    return get_result(result_id)

def delete_result(result_id: int):
    conn = get_db()
    conn.execute(DELETE_RESULT, (result_id,))
    conn.commit()
    conn.close()