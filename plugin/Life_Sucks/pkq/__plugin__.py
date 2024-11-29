from melobot import Plugin
from .run import echo_pkq

class Pkq(Plugin):
    version="1.0.0"
    flows=[echo_pkq]
    
