import sqlite3
import datetime
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

def add_sentences(sentence:str):
    currentYear=datetime.datetime.now().year
    currentMonth=datetime.datetime.now().month
    
    file_path = os.path.join(base_dir, f"../src/kx1/kx1_{currentYear}_{currentMonth}.sqlite")
    
    conn=sqlite3.connect(file_path)
    cursor=conn.cursor()
    
    table_name = f"table_{currentYear}_{currentMonth}"
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sentence TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute(f"INSERT INTO {table_name} (sentence) VALUES (?)", (sentence,))
    
    conn.commit()
    conn.close()
