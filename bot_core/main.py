from melobot import Bot, Plugin
from melobot.protocols.onebot.v11 import Adapter, ForwardWebSocketIO



class MyPlugin(Plugin):
    version = "1.0.0"
    flows = []

if __name__ == "__main__":
    (
        Bot(__name__)
        .add_io(ForwardWebSocketIO("ws://127.0.0.1:8080"))
        .add_adapter(Adapter())
        .load_plugin("../plugin/Life_Sucks/sayhi")
        # .load_plugin("../plugin/LLM")
        .run()
    )