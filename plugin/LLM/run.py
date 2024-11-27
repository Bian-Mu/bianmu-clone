from .train.ChatModel import ChatModel
from .path import model_path,checkpoint_path
from melobot import send_text
from melobot.protocols.onebot.v11 import on_message
from melobot.protocols.onebot.v11.adapter.event import MessageEvent

# LLM_v1 = None


# async def init_model():
#     global LLM_v1
#     if LLM_v1 is None:
#         LLM_v1 = ChatModel(model_path=model_path, checkpoint_path=checkpoint_path)
#         print("_________________________init完毕——————————————————————")
#     return LLM_v1

LLM_v1 = ChatModel(model_path=model_path, checkpoint_path=checkpoint_path)

@on_message()
async def LLM_v1_Chat(event:MessageEvent)->None:
    
    # LLM_v1_instance = await init_model()
    LLM_v1_instance=LLM_v1
    text=event.text.strip()
    response=LLM_v1_instance.func_chat(text)
    await send_text(response)

