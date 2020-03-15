import logging

from aiohttp import web
from aiohttp.web import Request, Response
from botbuilder.core import (
    BotFrameworkAdapterSettings,
    BotFrameworkAdapter,
    MemoryStorage, UserState, ConversationState)
from botbuilder.core.integration import aiohttp_error_middleware

from bots import Bot
from bots.courses_bot.bot import CoursesBot
from bots.courses_bot.course_recognizer import CourseRecognizer
from bots.courses_bot.data_models.course import Course
from bots.courses_bot.dialogs.student_profile_dialog import StudentProfileDialog
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

# Load course info
COURSE = Course.load_courses(CONFIG)

# LUIS Recognizer
LUIS_RECOGNIZER = CourseRecognizer(CONFIG)

# Create Courses Bot
COURSES_BOT = CoursesBot(
    ADAPTER,
    USER_STATE,
    CONVERSATION_STATE,
    StudentProfileDialog(USER_STATE, COURSE, LUIS_RECOGNIZER),
    COURSE
)


async def ok(req: Request):
    """
    Health check endpoint
    :param req:
    :return:
    """
    logging.info("Checking app health info")
    return Response(body="OK", status=201)

# Map requests
APP = web.Application(middlewares=[aiohttp_error_middleware])
logging.basicConfig(level=logging.INFO)
APP.router.add_post("/api/v1/echo", ECHO_BOT.request_handler())
APP.router.add_post("/api/v1/course_units", COURSES_BOT.request_handler())
APP.router.add_get("", ok)

if __name__ == "__main__":
    try:
        web.run_app(APP, host="localhost", port=CONFIG.PORT)
    except Exception as error:
        raise error
