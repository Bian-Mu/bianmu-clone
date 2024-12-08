from melobot import Plugin
from .run import add_into_db,get_from_db,send_bqb,put_off_send,repeat_speak


class Randomly_speak(Plugin):
    version="1.0.0"
    flows=[add_into_db,get_from_db,send_bqb,put_off_send,repeat_speak]
    
