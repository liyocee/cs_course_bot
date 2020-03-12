from botbuilder.core import TurnContext, StatePropertyAccessor
from botbuilder.dialogs import Dialog, DialogSet, DialogTurnStatus, DialogContext, DialogTurnResult


class DialogHelper:

    @staticmethod
    async def run_dialog(
        dialog: Dialog,
        turn_context: TurnContext,
        accessor: StatePropertyAccessor
    ):
        dialog_set: DialogSet = DialogSet(accessor)
        dialog_set.add(dialog)

        dialog_context: DialogContext = await dialog_set.create_context(turn_context)
        results: DialogTurnResult = await dialog_context.continue_dialog()

        if results.status == DialogTurnStatus.Empty:
            await dialog_context.begin_dialog(dialog.id)
