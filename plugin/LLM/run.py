from .train.ChatModel import ChatModel
from private.path import model_path,checkpoint_path
from melobot import send_text
from melobot.protocols.onebot.v11 import on_message
from melobot.protocols.onebot.v11.adapter.event import GroupMessageEvent

LLM_v1 = None


async def init_model():
    global LLM_v1
    if LLM_v1 is None:
        LLM_v1 = ChatModel(model_path=model_path, checkpoint_path=checkpoint_path)
    return LLM_v1

@on_message()
async def LLM_v1_Chat(event:GroupMessageEvent)->None:
    
    LLM_v1_instance = await init_model()
    
    text=event.text.strip()
    response=LLM_v1_instance.func_chat(text)
    await send_text(response)

