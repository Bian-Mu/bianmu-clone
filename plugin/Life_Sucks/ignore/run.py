import os
import json
from melobot.protocols.onebot.v11 import on_event
from melobot.protocols.onebot.v11.utils import LevelRole,GroupMsgChecker
from melobot.protocols.onebot.v11.adapter.event import Event

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "./src/list.json")
with open(file_path, 'r', encoding='utf-8') as file:
    list=json.load(file)

Checker=GroupMsgChecker(LevelRole(list["role"]),list["owner"],list["super_users"],list["white_users"],list["black_users"],list["white_groups"],None)

