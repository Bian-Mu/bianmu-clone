from melobot.protocols.onebot.v11 import on_full_match,on_message
from melobot.protocols.onebot.v11.adapter.event import GroupMessageEvent
from melobot.protocols.onebot.v11 import Adapter
import os,json

from .utils.add_sniff_db import add_sniff_db
from .utils.del_sniff_db import del_sniff_db
from ..Life_Sucks.ignore.run import Checker

base_dir=os.path.dirname(os.path.abspath(__file__))
list_path=os.path.join(base_dir,"./sniff_list.json")

@on_full_match(".sniff_me",checker=Checker)
async def start_stalk(event:GroupMessageEvent,adapter:Adapter):
    prey_qq=event.user_id
    with open(list_path,'r') as f:
        sniff_list1=json.load(f)
        if prey_qq == sniff_list1[0]:
            await adapter.send_reply("ฅ是主人捏ฅ")
        elif prey_qq in sniff_list1:
            await adapter.send_reply("已经被小狗记住了")
        else:
            sniff_list1.append(prey_qq)
            add_sniff_db(prey_qq,"你好，小狗")
            with open(list_path,'w',encoding='utf-8') as f2:
                json.dump(sniff_list1,f2,ensure_ascii=False)
            await adapter.send_reply("小狗很高兴认识你")
        
@on_full_match(".forget_me",checker=Checker)
async def refuse_stalk(event:GroupMessageEvent,adapter:Adapter):
    prey_qq=event.user_id
    with open(list_path,'r') as f:
        sniff_list2=json.load(f)
        if prey_qq==sniff_list2[0]:
            await adapter.send_reply("ฅ小狗认主ฅ")
        elif prey_qq in sniff_list2:
            sniff_list2.remove(prey_qq)
            del_sniff_db(prey_qq)
            with open(list_path,'w',encoding="utf-8") as f2:
                    json.dump(sniff_list2,f2,ensure_ascii=False)
            await adapter.send_reply("你在小狗的剧本里杀青了")
        else:
            await adapter.send_reply("你谁？（犬牙差互）")

        
@on_message(checker=Checker)
async def write_down_prey_sentence(event:GroupMessageEvent):
    prey_qq=event.user_id
    with open(list_path,'r') as f:
        sniff_list1=json.load(f)
        if prey_qq in sniff_list1:
            add_sniff_db(prey_qq,event.text.strip())