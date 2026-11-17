CREATE_USER_TABLE = '''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id NOT NULL UNIQUE,
    username TEXT
    )
'''

CREATE_QUESTIONS_TABLE = '''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_text TEXT NOT NULL,
        correct_answer TEXT NOT NULL
    )
'''

CREATE_RESULTS_TABLE = '''
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        question_id INTEGER NOT NULL,
        is_correct BOOLEAN NOT NULL DEFAULT 0,

        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
    )
'''

#---->

CREATE_USER_BY_TG_ID = 'SELECT * FROM users WHERE telegram_id = ?'
INSERT_USER = 'INSERT OR IGNORE INTO users (telegram_id, username) VALUES (?, ?)'
UPDATE_USER = 'UPDATE users SET username = ? WHERE telegram_id = ?'
DELETE_USER = 'DELETE FROM users WHERE telegram_id = ?'

#Вопросы 
GET_ALL_QUESTIONS = 'SELECT * FROM questions'
GET_QUESTION_BY_ID = 'SELECT * FROM questions WHERE id = ?'
INSERT_QUESTIONS  = 'INSERT INTO questions (question_text, correct_answer) VALUES(?, ?)'
UPDATE_QUESTIONS = 'UPDATE questions SET question_text = ?, correct_answer = ? WHERE id = ?'
DELETE_QUESTIONS = 'DELETE FROM questions WHERE id = ?'

#Резултаты 
INSERT_RESULT = 'INSERT INTO results (user_id, question_id, is_correct) VALUES (?, ?, ?)'
GET_RESULT_BY_ID = 'SELECT * FROM results WHERE id = ?'
GET_SCORE_BY_USER_ID = "SELECT COUNT(*) as total, SUM(is_correct) as correct FROM results WHERE user_id = ?"
UPDATE_RESULT = 'UPDATE results SET is_correct = ? WHERE id = ?'
DELETE_RESULT = 'DELETE FROM results WHERE id = ?'

GET_HISTORY = '''
    SELECT q.question_text, r.is_correct
    FROM results AS r
    INNER JOIN users AS u
        ON u.id = r.user_id
    INNER JOIN  questions AS q
        ON q.id = r.question_id
    WHERE u.telegram_id = ?
    ORDER BY r.id
    LIMIT 5
'''
GET_TOP = """
    SELECT u.username,
        COUNT(*) AS total,
        SUM(r.is_correct) AS correct
    FROM results AS r
    INNER JOIN users AS u
        ON u.id = r.user_id
    GROUP BY u.id, u.username
    ORDER BY correct DESC
    LIMIT 3
"""
GET_HARDEST = """
    SELECT q.question_text,
        ROUND(AVG(r.is_correct)*100 ,1) AS succes_rate
    FROM results AS r
    INNER JOIN questions AS q
        ON q.id = r.question_id
    GROUP BY r.question_id
    ORDER BY succes_rate ASC
    LIMIT 1
"""