from melobot import Bot
from melobot.log import Logger, LogLevel
from melobot.protocols.onebot.v11 import Adapter, ForwardWebSocketIO


if __name__ == "__main__":
    logger = Logger(level=LogLevel.DEBUG)
    (
        Bot(__name__, logger=logger)
        .add_io(ForwardWebSocketIO("ws://127.0.0.1:8080"))
        .add_adapter(Adapter())
        # .load_plugin("../plugin/Life_Sucks/sayhi")
        # .load_plugin("../plugin/Life_Sucks/toplace")
        .load_plugin("../plugin/LLM")
        .run(debug=True)
    )