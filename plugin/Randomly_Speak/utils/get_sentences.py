import sqlite3
import os
import random

base_dir = os.path.dirname(os.path.abspath(__file__))

def get_sentences(Year,Month):
    
    file_path = os.path.join(base_dir, f"../src/kx1/kx1_{Year}_{Month}.sqlite")
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT MIN(id), MAX(id) FROM table_{Year}_{Month}")
    result = cursor.fetchone()

    min_id, max_id = result if result else (None, None)
    
    index=random.randint(min_id,max_id)
    
    cursor.execute(f"SELECT * FROM table_{Year}_{Month} WHERE id = ?", (index,))
    sentence=cursor.fetchone()
    
    conn.close()
    return sentence