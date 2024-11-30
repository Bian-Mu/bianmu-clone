import os
import json
from melobot.protocols.onebot.v11.utils import LevelRole,GroupMsgChecker,StartMatcher
from melobot.typ import LogicMode
from melobot.protocols.onebot.v11 import on_message

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "./src/list.json")
with open(file_path, 'r', encoding='utf-8') as file:
    list=json.load(file)


Checker=GroupMsgChecker(LevelRole.NORMAL,list["owner"],list["super_users"],list["white_users"],list["black_users"],list["white_groups"],None)


Matcher=StartMatcher(str,LogicMode.AND)

async def isStartNotPoint(input:str):
    if type(input)=="text":
        if (input.strip())[0]==".":
            return False
    else :
        return True
    
Matcher.match=isStartNotPoint
