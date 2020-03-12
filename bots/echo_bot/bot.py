from typing import List

from botbuilder.core import TurnContext
from botbuilder.schema import ChannelAccount

from bots import Bot


class EchoBot(Bot):
    __name__ = 'EchoBot'

    async def on_message_activity(self, turn_context: TurnContext):
        return await super().on_message_activity(turn_context)

    async def on_members_added_activity(self, members_added: List[ChannelAccount], turn_context: TurnContext):
        for member_added in turn_context.activity.members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(f"Hello and welcome to {self.__name__}")
