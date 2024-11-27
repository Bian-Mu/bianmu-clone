from melobot import Plugin
from .run import LLM_v1_Chat

class LLM(Plugin):
    version="1.0.0"
    flows=[LLM_v1_Chat]
