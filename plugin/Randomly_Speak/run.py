from melobot.protocols.onebot.v11.adapter.event import MessageEvent
from melobot.protocols.onebot.v11.handle import on_message,on_event
from melobot import send_text
import random
import asyncio

from .utils.add_sentences import add_sentences
from .utils.get_sentences import get_sentences
from ..Life_Sucks.ignore.run import Checker,Logger,isStartNotPoint


@on_message(checker=Checker)
async def add_into_db(msg:MessageEvent):
    text=msg.text
    if await isStartNotPoint(text):
        add_sentences(text)
    

@on_message(checker=Checker)
async def get_from_db(msg:MessageEvent):
    text=msg.text
    if await isStartNotPoint(text):
        length=len(msg.text)*10
        month=random.randint(0,int(length/119))
    
        if month>=1 and month<=12:
            sentence=get_sentences(2024,12)
            Logger.info("send_from_db")
            await send_text(sentence)
        
        
        
@on_event(checker=Checker)
async def put_off_send():
    if random.randint(0,1119)>409:
        delay=random.randint(0,3600)
        await asyncio.sleep(delay)
        Logger.info("send_from_db_put_off")
        await send_text(get_sentences(2024,12))