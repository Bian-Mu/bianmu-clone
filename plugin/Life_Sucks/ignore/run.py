import os
import json
from melobot.protocols.onebot.v11.utils import LevelRole,MsgChecker,StartMatcher
from melobot.typ import LogicMode
from melobot.log import get_logger

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "./src/list.json")
with open(file_path, 'r', encoding='utf-8') as file:
    list=json.load(file)


Checker=MsgChecker(LevelRole.NORMAL,list["owner"],list["super_users"],list["white_users"],list["black_users"],None)



sniff_list_path=os.path.join(base_dir,"../../Stalk_You/sniff_list.json")
with open(sniff_list_path,'r',encoding='utf-8') as f:
    sniff_list=json.load(f)

Sniff_Checker=MsgChecker(LevelRole.NORMAL,list["owner"],list["super_users"],sniff_list,None,None)
# Matcher=StartMatcher(str,LogicMode.AND)

async def isStartNotPoint(input:str):
    if (input.strip())[0]==".":
        return False
    else :
        return True
    
# Matcher.match=isStartNotPoint


Logger=get_logger()