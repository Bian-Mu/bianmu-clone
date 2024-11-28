import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "../src/adcode.json")

def load_dict():
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    
