from melobot import send_text
from melobot.protocols.onebot.v11 import on_start_match
   
@on_start_match(".sayhi")
async def echo_hi() -> None:
    await send_text("你好捏")