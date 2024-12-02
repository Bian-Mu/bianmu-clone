import sqlite3
import os

base_dir=os.path.dirname(os.path.abspath(__file__))


def del_sniff_db(qq:int):
    file_path=os.path.join(base_dir,f"../src/{qq}_db.sqlite")
    
    conn=sqlite3.connect(file_path)
    cursor=conn.cursor()
    
    cursor.execute(f"DROP DATABASE {qq}_db.sqlite")    
    cursor.close()
    conn.close()