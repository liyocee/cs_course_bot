from botbuilder.core import MessageFactory, StatePropertyAccessor, UserState
from botbuilder.dialogs import ComponentDialog, TextPrompt, WaterfallDialog, WaterfallStepContext, DialogTurnResult, \
    PromptOptions

from bots.courses_bot.data_models.course import Course


class CourseQueryDialog(ComponentDialog):

    def __init__(self, course: Course, dialog_id: str):
        super(CourseQueryDialog, self).__init__(dialog_id or CourseQueryDialog.__name__)

        self.add_dialog(TextPrompt(TextPrompt.__name__))

        self.add_dialog(
            WaterfallDialog(
                WaterfallDialog.__name__,
                [
                    self.query_step,
                    # self.query_results_step,
                ]
            )
        )

        self.course = course

        self.initial_dialog_id = WaterfallDialog.__name__

    async def query_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        return await step_context.prompt(
            TextPrompt.__name__,
            PromptOptions(prompt=MessageFactory.text("What would you like to find out about the course units?"))
        )


