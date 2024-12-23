import datetime,random
import os,io
import sqlite3
import jieba
from wordcloud import WordCloud
from melobot.protocols.onebot.v11 import on_full_match
from melobot import send_image
from melobot.protocols.onebot.v11.adapter.event import GroupMessageEvent
from melobot.protocols.onebot.v11 import Adapter
from ..ignore.run import Logger,Checker
base_dir=os.path.dirname(os.path.abspath(__file__))

font_path=os.path.join(base_dir,"./src/SimHei.ttf")
color_list=["#62D1C9","#1B2D26","#E9ACAC","#F47297","#04060F"]
def color_choose(word,font_size,position,orientation,random_state=None,**kwargs):
    return random.choice(color_list)

wordcloud=WordCloud(
    background_color="white",
    mode="RGBA",
    font_path=font_path,
    colormap=None,
    color_func=color_choose,
    width=800,
    height=600
)

stoptxt_path=os.path.join(base_dir,"./src/chineseStopWords.txt")
stopwords=[line.strip() for line in open(stoptxt_path,encoding="utf-8").readlines()]
@on_full_match("本月词云",checker=Checker)
async def Group_wordcloud():
    currentYear=datetime.datetime.now().year
    currentMonth=datetime.datetime.now().month
    
    file_path=os.path.join(base_dir,f"../../Randomly_Speak/src/kx1/kx1_{currentYear}_{currentMonth}.sqlite")
    
    conn=sqlite3.connect(file_path)
    cursor=conn.cursor()
    
    table_name=f"table_{currentYear}_{currentMonth}"
    cursor.execute(f"SELECT sentence FROM {table_name}")
    sentences=cursor.fetchall()
    
    text = []

    for sentence in sentences:
        if sentence[0]:
            words = jieba.cut(sentence[0])
            text.extend([word for word in words if word not in stopwords])
    text = ' '.join(text)
    
    img=(wordcloud.generate(text=text)).to_image()
    
    pic=io.BytesIO()
    img.save(pic,format="PNG")
    pic.seek(0)
    raw_data=pic.read()
    
    await send_image(name="本月词云",raw=raw_data,mimetype="image/png")
    Logger.info("wordcloud")


@on_full_match("我的词云",checker=Checker)
async def Solo_wordcloud(event:GroupMessageEvent,adapter:Adapter):
    prey_qq=event.user_id
    file_path=os.path.join(base_dir,f"../../Stalk_You/src/{prey_qq}_db.sqlite")
    if os.path.exists(file_path):
        conn=sqlite3.connect(file_path)
        cursor=conn.cursor()
    
        table_name=f"table_data"
        cursor.execute(f"SELECT sentence FROM {table_name}")
        sentences=cursor.fetchall()
    
        text = []

        for sentence in sentences:
            if sentence[0]:
                words = jieba.cut(sentence[0])
                text.extend([word for word in words if word not in stopwords])
        text = ' '.join(text)
    
        img=(wordcloud.generate(text=text)).to_image()
    
        pic=io.BytesIO()
        img.save(pic,format="PNG")
        pic.seek(0)
        raw_data=pic.read()
    
        await send_image(name="历史词云",raw=raw_data,mimetype="image/png")
    else:
        await adapter.send_reply("先sniff再慢慢认识嗷")
        Logger.info("wordcloud")
        