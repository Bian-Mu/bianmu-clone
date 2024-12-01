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


# Matcher=StartMatcher(str,LogicMode.AND)

async def isStartNotPoint(input:str):
    if (input.strip())[0]==".":
        return False
    else :
        return True
    
# Matcher.match=isStartNotPoint


Logger=get_logger()