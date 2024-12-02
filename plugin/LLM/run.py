import json
import os
import random
from .train.ChatModel import ChatModel
from ..Life_Sucks.ignore.run import Logger,isStartNotPoint

from melobot import send_text
from melobot.protocols.onebot.v11 import on_message
from melobot.protocols.onebot.v11.adapter.event import MessageEvent
from melobot.log import GenericLogger

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "./path.json")

with open(file_path, 'r', encoding='utf-8') as file:
    path=json.load(file)


LLM_v1 = ChatModel(model_path=path["model_path"], checkpoint_path=path["checkpoint_path"])


@on_message()
async def LLM_v1_Chat(event:MessageEvent)->None:
    type=event.raw["message"][0]["type"]
    if type=="text":
        if await isStartNotPoint(event.text):
            roll=random.randint(0,1119)
            if roll<119:
                LLM_v1_instance=LLM_v1
                response=LLM_v1_instance.func_chat(event.text)
                Logger.info("send_from_LLM")
                await send_text(response)

