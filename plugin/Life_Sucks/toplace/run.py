from melobot import send_text
from melobot.protocols.onebot.v11 import on_start_match
from melobot.protocols.onebot.v11.adapter.event import MessageEvent
import json    
    
from .apikey import key,http_head

from .utils.divide import divide
from .utils.load_dict import load_dict
from .utils.fetch_url import fetch_url

methods=["text?","around?"]
#text为普通关键词搜索
#around为hdu周边关键词搜索

dicts=load_dict()

@on_start_match(".toplace")
async def go_to_someplace(event:MessageEvent):
    input=event.text.strip().removeprefix(".toplace")
    
    if "hdu" in input :
        place="keywords="+(input.replace("hdu","")).strip()
        hdu_location="location=120.34344,30.31526"
        head=http_head+methods[1]
        
        isDistance=True
        
        request=head+hdu_location+"&radius=3000&"+place+"&"+key

    else :
        head=http_head+methods[0]
        isDistance=False
        
        [place,city]=divide(input)
        try:
            if city!="" and place!="":
                city=city.strip()
                adcode=str(dicts[city])
                place="keywords="+place.strip()
            
                request=head+"&"+place+"&region="+adcode+"&"+key
                
            else:
                raise LookupError("Format Error")
        except:
            await send_text("格式有误，应是：'place' in 'xx省/市/区/县 择其一'")
    
    if request:
        response=(await fetch_url(request)).text
        res_json=json.loads(response)
        position=res_json["pois"]
        result=[]
        if isDistance:
            for item in position:
                result.append(item["name"]+" "+item["address"]+" "+item["distance"]+"m")
        else:
            for item in position:
                result.append(item["name"]+" "+item["address"])
        if result!=[]:
            await send_text("\n".join(result))
                
        