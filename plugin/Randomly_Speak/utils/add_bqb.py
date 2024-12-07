import os
import json
import httpx

base_dir=os.path.dirname(os.path.abspath(__file__))
list_path=os.path.join(base_dir,"../src/bqb/bqb_list.json")

async def add_bqb(filename:str,url:str):
    with open(list_path,"r") as f:
        bqb_list=json.load(f)
        if filename not in bqb_list:
            bqb_list.append(filename)
            bqb_path=os.path.join(base_dir,f"../src/bqb/image/{filename}.jpg")
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                if response.status_code==200:
                    content = response.read()
                    with open(bqb_path,"wb") as f:
                        f.write(content)
                    with open(list_path,"w") as f2:
                        json.dump(bqb_list,f2,ensure_ascii=False)
           