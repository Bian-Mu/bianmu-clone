import os
import json
import random
import io
from PIL import Image

base_dir=os.path.dirname(os.path.abspath(__file__))
list_path=os.path.join(base_dir,"../src/bqb/bqb_list.json")

async def get_bqb():
    with open(list_path,"r") as f:
        bqb_list=json.load(f)
    choice=random.randint(0,len(bqb_list))
    bqb_path=os.path.join(base_dir,f"../src/bqb/image/{bqb_list[choice]}")
    with Image.open(bqb_path) as img:
        byte_io=io.BytesIO()
        img.save(byte_io, format='PNG') 
        byte_io.seek(0) 
        bqb = byte_io.read()
        
        return bqb