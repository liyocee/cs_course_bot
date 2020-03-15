import logging
import sys
import traceback
from datetime import datetime
from typing import Callable, Awaitable

from aiohttp.abc import StreamResponse
from aiohttp.web import Request, Response, json_response
from botbuilder.core import ActivityHandler, BotFrameworkAdapter, TurnContext
from botbuilder.schema import Activity, ActivityTypes


class Bot(ActivityHandler):
    __name__ = 'Bot'

    def __init__(self, adapter: BotFrameworkAdapter) -> None:
        super(Bot, self).__init__()
        self.bot_adapter = adapter

    def request_handler(self) -> Callable[[Request], Awaitable[StreamResponse]]:

        async def router(req: Request) -> Response:
            # Main bot message handler.
            return await self.process_bot_request(req)

        return router

    async def process_bot_request(self, req: Request) -> Response:
        if "application/json" in req.headers["Content-Type"]:
            body = await req.json()
        else:
            return Response(status=415)

        activity = Activity().deserialize(body)
        auth_header = req.headers["Authorization"] if "Authorization" in req.headers else ""

        try:
            response = await self.bot_adapter.process_activity(activity, auth_header, self.on_turn)
            if response:
                return json_response(data=response.body, status=response.status)
            return Response(status=201)
        except Exception as exception:
            raise exception

    @staticmethod
    async def handle_bot_errors(context: TurnContext, error: Exception) -> None:
        # Handle bot errors
        logging.error(f"\n [on_turn_error] unhandled error: {error}", file=sys.stderr)
        traceback.print_exc()

        # Send a message to the user
        await context.send_activity("The bot encountered an error or bug.")
        await context.send_activity(
            "To continue to run this bot, please fix the bot source code."
        )
        # Send a trace activity if we're talking to the Bot Framework Emulator
        if context.activity.channel_id == "emulator":
            # Create a trace activity that contains the error object
            trace_activity = Activity(
                label="TurnError",
                name="on_turn_error Trace",
                timestamp=datetime.utcnow(),
                type=ActivityTypes.trace,
                value=f"{error}",
                value_type="https://www.botframework.com/schemas/error",
            )
            # Send a trace activity, which will be displayed in Bot Framework Emulator
            await context.send_activity(trace_activity)

