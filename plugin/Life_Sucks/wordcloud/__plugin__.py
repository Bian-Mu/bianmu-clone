from melobot import Plugin
from .run import Group_wordcloud

class wordcloud(Plugin):
    version="1.0.0"
    flows=[Group_wordcloud]
