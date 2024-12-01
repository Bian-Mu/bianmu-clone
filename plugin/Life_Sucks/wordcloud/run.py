import datetime,random
import os,io
import sqlite3
from wordcloud import WordCloud
from melobot.protocols.onebot.v11 import on_full_match
from melobot import send_image

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



@on_full_match("本月词云")
async def Group_wordcloud():
    currentYear=datetime.datetime.now().year
    currentMonth=datetime.datetime.now().month
    
    file_path=os.path.join(base_dir,f"../../Randomly_Speak/src/kx1/kx1_{currentYear}_{currentMonth}.sqlite")
    
    conn=sqlite3.connect(file_path)
    cursor=conn.cursor()
    
    table_name=f"table_{currentYear}_{currentMonth}"
    cursor.execute(f"SELECT sentence FROM {table_name}")
    words=cursor.fetchall()
    
    text=' '.join(word[0] for word in words if word[0] is not None)
    img=(wordcloud.generate(text=text)).to_image()
    
    pic=io.BytesIO()
    img.save(pic,format="PNG")
    pic.seek(0)
    raw_data=pic.read()
    
    await send_image(name="本月词云",raw=raw_data,mimetype="image/png")
