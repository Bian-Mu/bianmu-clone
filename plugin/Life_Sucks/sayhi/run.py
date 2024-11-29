from melobot import send_text
from melobot.protocols.onebot.v11 import on_start_match
from ..ignore.run import Checker

@on_start_match(".sayhi",checker=Checker)
async def echo_hi() -> None:
    await send_text("你好捏")