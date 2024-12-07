from melobot import Bot
from melobot.log import Logger, LogLevel
from melobot.protocols.onebot.v11 import Adapter, ForwardWebSocketIO
import os,json

depth=2
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "./src/config.json")
with open(file_path, 'r', encoding='utf-8') as file:
    config=json.load(file)



if __name__ == "__main__":
    logger_bug = Logger(level=LogLevel.DEBUG)
    (
        Bot(__name__, logger=logger_bug)
        .add_io(ForwardWebSocketIO(url=config["url"],access_token=config["access_token"]))
        .add_adapter(Adapter())
        .load_plugin("../plugin/USE_HELP")
        .load_plugin("../plugin/Life_Sucks/pkq", depth)
        .load_plugin("../plugin/Life_Sucks/toplace",depth)
        # .load_plugin("../plugin/LLM",depth)
        .load_plugin("../plugin/Randomly_Speak",depth)
        .load_plugin("../plugin/Life_Sucks/wordcloud",depth)
        .load_plugin("../plugin/Stalk_You",depth)
        .run(debug=True)
    )