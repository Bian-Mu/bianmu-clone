from melobot.protocols.onebot.v11 import on_full_match
from melobot import send_text

@on_full_match(".help")
async def USEHELP():
    use_json={
    ".toplace":"关键词/hdu周边查询",
    ".weather":"国区天气查询",
    "本月词云":"计科协当月词云",
    "我的词云":"个人历史词云",
    ".sniff_me":"开始记录个人文字消息",
    ".forget_me":"清除记录的个人文字消息"
    }
    help=[f"'{command}'：{intro}" for command,intro in use_json.items()]
    await send_text("\n".join(help))