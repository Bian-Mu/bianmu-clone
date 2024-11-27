from melobot import Plugin
from .run import echo_hi

class Sayhi(Plugin):
    version="1.0.0"
    flows=[echo_hi]
    
