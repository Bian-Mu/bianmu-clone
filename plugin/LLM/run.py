import json
import os
import random
from .train.ChatModel import ChatModel


from melobot import send_text
from melobot.protocols.onebot.v11 import on_message
from melobot.protocols.onebot.v11.adapter.event import MessageEvent


base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "./path.json")

with open(file_path, 'r', encoding='utf-8') as file:
    path=json.load(file)


LLM_v1 = ChatModel(model_path=path["model_path"], checkpoint_path=path["checkpoint_path"])

@on_message()
async def LLM_v1_Chat(event:MessageEvent)->None:
    roll=random.randint(0,1119)
    if roll<209:
        LLM_v1_instance=LLM_v1
        text=event.text.strip()
        response=LLM_v1_instance.func_chat(text)
        await send_text(response)

