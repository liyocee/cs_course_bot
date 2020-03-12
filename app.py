from aiohttp import web
from botbuilder.core import (
    BotFrameworkAdapterSettings,
    BotFrameworkAdapter,
    MemoryStorage, UserState, ConversationState)
from botbuilder.core.integration import aiohttp_error_middleware

from bots import Bot
from bots.echo_bot.bot import EchoBot
from config import DefaultConfig

CONFIG = DefaultConfig()

MEMORY = MemoryStorage()
USER_STATE = UserState(MEMORY)
CONVERSATION_STATE = ConversationState(MEMORY)

SETTINGS = BotFrameworkAdapterSettings(CONFIG.APP_ID, CONFIG.APP_PASSWORD)
ADAPTER = BotFrameworkAdapter(SETTINGS)


ADAPTER.on_turn_error = Bot.handle_bot_errors

# Create Echo Bot
ECHO_BOT = EchoBot(ADAPTER)


APP = web.Application(middlewares=[aiohttp_error_middleware])
APP.router.add_post("/api/v1/echo", ECHO_BOT.request_handler())

if __name__ == "__main__":
    try:
        web.run_app(APP, host="localhost", port=CONFIG.PORT)
    except Exception as error:
        raise error
