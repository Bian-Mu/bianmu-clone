from melobot.protocols.onebot.v11.adapter.event import MessageEvent
from melobot.protocols.onebot.v11.handle import on_message,on_event
from melobot import send_text
import random
import asyncio

from .utils.add_sentences import add_sentences
from .utils.get_sentences import get_sentences
from ..Life_Sucks.ignore.run import Checker,Matcher

@on_message(checker=Checker,matcher=Matcher)
async def add_into_db(msg:MessageEvent):
    text=msg.text
    add_sentences(text)
    

@on_message(checker=Checker,matcher=Matcher)
async def get_from_db(msg:MessageEvent):
    length=len(msg.text)*4
    month=random.randint(0,int(length/1119))
    
    if month>=1 and month<=12:
        sentence=get_sentences(24,month)
        print("send_from_db")
        await send_text(sentence)
        
        
        
@on_event(checker=Checker,matcher=Matcher)
async def put_off_send():
    if random.randint(0,1119)>1000:
        delay=random.randint(0,7200)
        await asyncio.sleep(delay)
        await send_text(get_sentences(24,random.randint(1,12)))