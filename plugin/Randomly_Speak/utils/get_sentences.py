import sqlite3
import os
import random

base_dir = os.path.dirname(os.path.abspath(__file__))

def get_sentences(Year,Month):
    
    file_path = os.path.join(base_dir, f"../src/kx1/kx1_{Year}_{Month}.sqlite")
    try:
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT MIN(id), MAX(id) FROM table_{Year}_{Month}")
        result = cursor.fetchone()

        min_id, max_id = result if result else (None, None)

        if min_id is None or max_id is None:
            return "启动自毁程序"

        index = random.randint(min_id, max_id)

        cursor.execute(f"SELECT sentence FROM table_{Year}_{Month} WHERE id = ?", (index,))
        sentence = cursor.fetchone()
        
        conn.close()
        return sentence[0]

    except sqlite3.Error:
        print(f"Database file {file_path} does not exist or is not accessible.")
        return "找不到记录..."
    