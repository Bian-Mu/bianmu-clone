from melobot.protocols.onebot.v11.adapter.event import MessageEvent
from melobot.protocols.onebot.v11.handle import on_message,on_event,on_contain_match
from melobot import send_text,send_image
import random
import asyncio

from .utils.add_sentences import add_sentences
from .utils.get_sentences import get_sentences
from .utils.add_bqb import add_bqb
from .utils.get_bqb import get_bqb
from ..Life_Sucks.ignore.run import Checker,Logger,isStartNotPoint


@on_message(checker=Checker)
async def add_into_db(msg:MessageEvent):
    type=msg.raw["message"][0]["type"]
    if type=="text" and msg.is_group():
        if await isStartNotPoint(msg.text):
            if "词云" not in msg.text:
                add_sentences(msg.text)
                Logger.info("add_into_db")
    elif type=="image":
        data=msg.raw["message"][0]["data"]
        url=data["url"].replace(r"\\u0026",'&')
        if data["summary"]=="[动画表情]":
            await add_bqb(data["filename"],url)
            Logger.info("add_bqb")
            

@on_message(checker=Checker)
async def get_from_db(msg:MessageEvent):
    type=msg.raw["message"][0]["type"]
    if type=="text":
        if await isStartNotPoint(msg.text):
            length=len(msg.text)*10
            month=random.randint(0,int(length/119))
    
            if month>=1 and month<=12:
                sentence=get_sentences(2024,12)
                Logger.info("send_from_db")
                if "http" not in sentence:
                    await send_text(sentence)

@on_contain_match(["笑","草","无敌","吃","乐","？","了","去","6","绷"],checker=Checker)
async def send_bqb():
    if random.randint(0,99)<19:
        Logger.info("send_bqb")
        bqb=await get_bqb()
        await send_image(name="喵喵喵喵～",raw=bqb,mimetype="image/png")
        
        
isWait=False
lock=asyncio.Lock()
@on_message(checker=Checker)
async def put_off_send(msg:MessageEvent):
    global isWait
    async with lock:
        if (msg.user_id+random.randint(0,1119))%30<=11 and not isWait:
            delay=random.randint(300,3600)
            Logger.info(f"start_put_off_{delay}s")
            isWait=True
            await asyncio.sleep(delay)
            await send_text(get_sentences(2024,12))
            Logger.info("send_from_db_put_off")
            isWait=False

ifRepeated=False
repeatWords=""
lock2=asyncio.Lock()            
@on_message(checker=Checker)
async def repeat_speak(msg:MessageEvent):
    global ifRepeated,repeatWords
    async with lock2:
        type=msg.raw["message"][0]["type"]
        if type=="text":
            if await isStartNotPoint(msg.text):
                if repeatWords!=msg.text:
                    repeatWords=msg.text
                    ifRepeated=False
                elif repeatWords==msg.text and not ifRepeated:
                    if random.randint(0,3)<2:
                        await send_text(repeatWords)
                        Logger.info("repeat_speak")
                        ifRepeated=True
                    