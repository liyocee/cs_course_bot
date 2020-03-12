from botbuilder.core import UserState, StatePropertyAccessor, MessageFactory
from botbuilder.dialogs import (
    ComponentDialog,
    WaterfallDialog,
    TextPrompt,
    ChoicePrompt,
    ConfirmPrompt,
    AttachmentPrompt,
    WaterfallStepContext,
    DialogTurnResult,
    PromptOptions,
    Choice,
    PromptValidatorContext)

from bots.courses_bot.data_models.course_unit import CourseUnit
from bots.courses_bot.data_models.student_profile import StudentProfile, StudentProfileAttributes


class StudentProfileDialog(ComponentDialog):

    def __init__(self, user_state: UserState, dialog_id: str = None):
        super(StudentProfileDialog, self).__init__(dialog_id or StudentProfileDialog.__name__)

        # create accessor
        self.student_profile_accessor: StatePropertyAccessor = user_state.create_property("StudentProfile")

        # add dialogs
        self.add_dialog(
            WaterfallDialog(
                WaterfallDialog.__name__,
                [
                    self.name_step,
                    self.admission_number_step,
                    self.picture_step,
                    self.courses_step,
                    self.summary_step
                ]
            )
        )

        self.add_dialog(TextPrompt(TextPrompt.__name__))
        self.add_dialog(ChoicePrompt(ChoicePrompt.__name__))
        self.add_dialog(ConfirmPrompt(ConfirmPrompt.__name__))
        self.add_dialog(AttachmentPrompt(AttachmentPrompt.__name__, StudentProfileDialog.picture_prompt_validator))

        self.initial_dialog_id = WaterfallDialog.__name__

    @staticmethod
    async def name_step(step_context: WaterfallStepContext) -> DialogTurnResult:
        return await step_context.prompt(
            TextPrompt.__name__,
            PromptOptions(prompt=MessageFactory.text("Please enter your name?"))
        )

    @staticmethod
    async def admission_number_step(step_context: WaterfallStepContext) -> DialogTurnResult:
        step_context.values[StudentProfileAttributes.NAME.value] = step_context.result

        await step_context.context.send_activity(MessageFactory.text(f'Hello {step_context.result}'))

        return await step_context.prompt(
            TextPrompt.__name__,
            PromptOptions(prompt=MessageFactory.text("Please enter your admission number?"))
        )

    @staticmethod
    async def picture_step(step_context: WaterfallStepContext) -> DialogTurnResult:
        step_context.values[StudentProfileAttributes.ADMISSION_NUMBER.value] = step_context.result
        name = step_context.values[StudentProfileAttributes.NAME.value]

        msg = f'Hello {name}, thanks for providing us with admission number: {step_context.result}'

        await step_context.context.send_activity(MessageFactory.text(msg))

        prompt_options = PromptOptions(
            prompt=MessageFactory.text(
                "Please attach a profile picture. "
            ),
            retry_prompt=MessageFactory.text(
                "The attachment must be a jpeg/png image file. Please attach again"
            ),
        )
        return await step_context.prompt(AttachmentPrompt.__name__, prompt_options)

    @staticmethod
    async def courses_step(step_context: WaterfallStepContext) -> DialogTurnResult:
        step_context.values[StudentProfileAttributes.PICTURE.value] = step_context.result[0]
        name = step_context.values[StudentProfileAttributes.NAME.value]

        await step_context.context.send_activity(
            MessageFactory.text(f"Hello {name}, your profile picture has been uploaded"))

        await step_context.context.send_activity(
            MessageFactory.attachment(
                step_context.result[0], f"Hello {name}, your profile picture has been uploaded"
            )
        )

        return await step_context.prompt(
            ChoicePrompt.__name__,
            PromptOptions(
                prompt=MessageFactory.text("Please select the course you are interested in"),
                choices=[Choice("CS 101"), Choice("CS 102"), Choice("CS 103")]
            )
        )

    async def summary_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        student_profile: StudentProfile = await self.student_profile_accessor.get(
            step_context.context, StudentProfile)

        student_profile.name = step_context.values[StudentProfileAttributes.NAME.value]
        student_profile.admission_number = step_context.values[StudentProfileAttributes.ADMISSION_NUMBER.value]
        student_profile.picture = step_context.values[StudentProfileAttributes.PICTURE.value]
        student_profile.course_unit = CourseUnit(step_context.result.value)

        msg = (
            f"Hello {student_profile.name}, your details have been captured as: "
            f"Admission number: {student_profile.admission_number} "
            f"Course unit: {student_profile.course_unit.name} "
        )

        await step_context.context.send_activity(
            MessageFactory.attachment(
                student_profile.picture, "This is your profile picture."
            )
        )

        await step_context.context.send_activity(MessageFactory.text(msg))

        return await step_context.end_dialog()

    @staticmethod
    async def picture_prompt_validator(prompt_context: PromptValidatorContext) -> bool:
        if not prompt_context.recognized.succeeded:
            await prompt_context.context.send_activity(MessageFactory.text("No attachments received."))

            return False

        attachments = prompt_context.recognized.value

        valid_images = [
            attachment
            for attachment in attachments
            if attachment.content_type in ["image/jpeg", "image/png"]
        ]

        prompt_context.recognized.value = valid_images

        return len(valid_images) > 0
