import datetime,random
import os,io
import sqlite3
import jieba
from wordcloud import WordCloud
from melobot.protocols.onebot.v11 import on_full_match
from melobot import send_image
from melobot.protocols.onebot.v11.adapter.event import GroupMessageEvent
from melobot.protocols.onebot.v11 import Adapter

base_dir=os.path.dirname(os.path.abspath(__file__))

font_path=os.path.join(base_dir,"./src/SimHei.ttf")
color_list=["#62D1C9","#1B2D26","#E9ACAC","#F47297","#04060F"]
def color_choose(word,font_size,position,orientation,random_state=None,**kwargs):
    return random.choice(color_list)

wordcloud=WordCloud(
    background_color=None,
    mode="RGBA",
    font_path=font_path,
    colormap=None,
    color_func=color_choose,
    width=800,
    height=600
)

stopwords = set([
    "我", "你", "他", "她", "它", "我们", "你们", "他们", "这", "那", "的", "了", "在", "是", "和", "与", "有", "为", "对", "不", "会", "就", "也", "而", "可以","还","啊","吗","吧","什么","能","都","不能"
])

@on_full_match("本月词云")
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


@on_full_match("我的词云")
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