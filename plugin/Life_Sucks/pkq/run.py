from melobot import send_text
from melobot.protocols.onebot.v11 import on_contain_match

@on_contain_match("皮卡丘")
async def echo_pkq() -> None:
    await send_text("啊？可皮卡丘多得像是路边的野狗耶")