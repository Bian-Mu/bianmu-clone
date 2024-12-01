from melobot import Plugin
from .run import go_to_someplace,get_weather

class Toplace(Plugin):
    version="1.0.0"
    flows=[go_to_someplace,get_weather]
    
