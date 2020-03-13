from botbuilder.core import MessageFactory, Recognizer, RecognizerResult, TurnContext
from botbuilder.dialogs import ComponentDialog, TextPrompt, WaterfallDialog, WaterfallStepContext, DialogTurnResult, \
    PromptOptions

from bots.courses_bot.course_intent_handlers import CourseIntentHandlers
from bots.courses_bot.data_models.course import Course


class CourseQueryDialog(ComponentDialog):

    def __init__(self, course: Course, luis_recognizer: Recognizer, dialog_id: str = None):
        super(CourseQueryDialog, self).__init__(dialog_id or CourseQueryDialog.__name__)

        self.add_dialog(TextPrompt(TextPrompt.__name__))

        self.add_dialog(
            WaterfallDialog(
                WaterfallDialog.__name__,
                [
                    self.query_step,
                    self.query_results_step
                ]
            )
        )

        self.course = course
        self.luis_recognizer = luis_recognizer

        self.initial_dialog_id = WaterfallDialog.__name__

        self.intent_handlers = CourseIntentHandlers.get_handlers(course)

    async def query_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        courses = list(map(lambda x: x.code, self.course.course_units))
        return await step_context.prompt(
            TextPrompt.__name__,
            PromptOptions(prompt=MessageFactory.text(f"What would you like to find out about the course units: {','.join(courses)}?"))
        )

    async def query_results_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        query_string = step_context.result

        results: RecognizerResult = await self.luis_recognizer.recognize(step_context.context)

        await self.process_search_results(step_context, results)

        # loop  through the query interface
        return await step_context.replace_dialog(CourseQueryDialog.__name__)

    async def process_search_results(self, step_context: WaterfallStepContext, search_results: RecognizerResult) -> None:
        entities = search_results.entities.get("CourseUnits", [[]])[0]
        intent = search_results.get_top_scoring_intent()

        if intent is None or len(entities) == 0:
            await step_context.context.send_activity(MessageFactory.text(f'No details were found for your query'))
            return

        intent_handler = self.intent_handlers.get(intent.intent, None)

        if intent_handler is None:
            await step_context.context.send_activity(MessageFactory.text(f'Could not process your query'))
            return

        await step_context.context.send_activity(MessageFactory.text(intent_handler(entities[0])))
