from melobot import Bot, Plugin, send_text
from melobot.protocols.onebot.v11 import Adapter, ForwardWebSocketIO, on_start_match
@on_start_match(".sayhi")
async def echo_hi() -> None:
    await send_text("Hello, melobot!")

class MyPlugin(Plugin):
    version = "1.0.0"
    flows = [echo_hi]

if __name__ == "__main__":
    (
        Bot(__name__)
        .add_io(ForwardWebSocketIO("ws://127.0.0.1:8080"))
        .add_adapter(Adapter())
        .load_plugin(MyPlugin())
        .run()
    )