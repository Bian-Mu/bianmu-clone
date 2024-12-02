from melobot import Plugin
from .run import start_stalk,refuse_stalk,write_down_prey_sentence

class Stalk_You(Plugin):
    version="1.0.0"
    flows=[start_stalk,refuse_stalk,write_down_prey_sentence]
    
