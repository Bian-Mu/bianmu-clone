from melobot.protocols.onebot.v11.adapter.event import MessageEvent
from melobot.protocols.onebot.v11.handle import on_message
from melobot import send_text
import random

from .utils.add_sentences import add_sentences
from .utils.get_sentences import get_sentences
from ..Life_Sucks.ignore.run import Checker

@on_message(checker=Checker)
async def add_into_db(msg:MessageEvent):
    text=msg.text
    add_sentences(text)
    

@on_message(checker=Checker)
async def get_from_db(msg:MessageEvent):
    length=len(msg.text)
    month=random.randint(0,int(length/1119))
    
    if month>=1 and month<=12:
        sentence=get_sentences(24,month)
        await send_text(sentence)