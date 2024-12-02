import sqlite3
import os

base_dir=os.path.dirname(os.path.abspath(__file__))


def del_sniff_db(qq:int):
    file_path=os.path.join(base_dir,f"../src/{qq}_db.sqlite")
    if os.path.exists(file_path):
        os.remove(file_path)