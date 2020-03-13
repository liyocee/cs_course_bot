from typing import List

from botbuilder.core import UserState, ConversationState, TurnContext, BotFrameworkAdapter, MessageFactory, CardFactory
from botbuilder.dialogs import Dialog
from botbuilder.schema import ChannelAccount, Activity

from bots import Bot
from bots.courses_bot.cards import WELCOME_CARD
from bots.courses_bot.data_models.course import Course
from bots.courses_bot.dialogs.dialog_helper import DialogHelper


class CoursesBot(Bot):

    def __init__(
        self,
        adapter: BotFrameworkAdapter,
        user_state: UserState,
        conversation_state: ConversationState,
        dialog: Dialog,
        course: Course
    ):
        super(CoursesBot, self).__init__(adapter)

        checks = [
            (user_state is None, 'user_state'),
            (conversation_state is None, 'conversation_state'),
            (dialog is None, 'dialog')
        ]

        for check in checks:
            if check[0]:
                raise TypeError(f"[CoursesBot]: Missing parameter. {check[1]} is required but None was given")

        self.conversation_state: ConversationState = conversation_state
        self.user_state: UserState = user_state
        self.dialog = dialog
        self.course = course

    async def on_turn(self, turn_context: TurnContext):
        await super().on_turn(turn_context)
        await self.conversation_state.save_changes(turn_context)
        await self.user_state.save_changes(turn_context)

    async def on_message_activity(self, turn_context: TurnContext):
        await DialogHelper.run_dialog(
            self.dialog,
            turn_context,
            self.conversation_state.create_property("StudentProfileDialogState"),
        )

    async def on_members_added_activity(self, members_added: List[ChannelAccount], turn_context: TurnContext):
        for member_added in turn_context.activity.members_added:
            if member_added.id != turn_context.activity.recipient.id:
                activity: Activity = MessageFactory.attachment(CardFactory.adaptive_card(WELCOME_CARD))
                await turn_context.send_activity(activity)

