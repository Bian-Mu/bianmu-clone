import os,json
from melobot import send_text
from melobot.protocols.onebot.v11 import on_at_qq
from melobot.protocols.onebot.v11 import Adapter
from melobot.protocols.onebot.v11.adapter.event import MessageEvent

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "../ignore/src/list.json")
with open(file_path, 'r', encoding='utf-8') as file:
    list=json.load(file)


@on_at_qq(list["white_users"][0])
async def hate_you(event:MessageEvent,adapter:Adapter):
    if event.user_id in list["black_users"]:
        await adapter.send_reply("...zv lu ye ka-i di")