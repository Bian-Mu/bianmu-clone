from melobot import Plugin
from .run import add_into_db,get_from_db

class Randomly_speak(Plugin):
    version="1.0.0"
    flows=[add_into_db,get_from_db]
    
