from melobot import Plugin
from .run import hate_you

class Hate(Plugin):
    version="1.0.0"
    flows=[hate_you]
    
