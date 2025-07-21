# import sqlite3
# from datetime import datetime

# DB_NAME = "predictions.db"

# def init_db():
#     with sqlite3.connect(DB_NAME, check_same_thread=False) as conn:
#         cursor = conn.cursor()
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS predictions (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 disease TEXT,
#                 timestamp TEXT
#         )
#     """)
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS precautions (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             disease TEXT,
#             precaution TEXT,
#             timestamp TEXT
#         )
#     """)
#     conn.commit()
#     conn.close()

# def save_prediction(disease):
#     with sqlite3.connect(DB_NAME, check_same_thread=False) as conn:
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO predictions (disease, timestamp) VALUES (?, ?)",
#                     (disease, datetime.now().isoformat()))
#         conn.commit()
#         conn.close()

# def save_precaution(disease, precaution):
#     with sqlite3.connect(DB_NAME, check_same_thread=False) as conn:
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO precautions (disease, precaution, timestamp) VALUES (?, ?, ?)",
#                     (disease, precaution, datetime.now().isoformat()))
#         conn.commit()
#         conn.close()

# def get_prediction_history():
#     with sqlite3.connect(DB_NAME, check_same_thread=False) as conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT disease, timestamp FROM predictions ORDER BY timestamp DESC")
#         rows = cursor.fetchall()
#         conn.close()
#         return rows

# def get_precaution_history():
#     with sqlite3.connect(DB_NAME, check_same_thread=False) as conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT disease, precaution, timestamp FROM precautions ORDER BY timestamp DESC")
#         rows = cursor.fetchall()
#         conn.close()
#         return rows
import sqlite3
from datetime import datetime

DB_NAME = "predictions.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS prediction (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                disease TEXT,
                timestamp TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS precaution (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                disease TEXT,
                precaution TEXT,
                timestamp TEXT
            )
        """)
        conn.commit()

def save_prediction(disease):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO prediction (disease, timestamp) VALUES (?, ?)", (disease, timestamp))
        conn.commit()

def save_precaution(disease, precaution):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO precaution (disease, precaution, timestamp) VALUES (?, ?, ?)", 
                       (disease, precaution, timestamp))
        conn.commit()

def get_prediction_history():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT disease, timestamp FROM prediction ORDER BY timestamp DESC")
        return cursor.fetchall()

def get_precaution_history():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT disease, precaution, timestamp FROM precaution ORDER BY timestamp DESC")
        return cursor.fetchall()
