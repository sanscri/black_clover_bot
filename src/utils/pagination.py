from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button


async def change_page(
    callback: CallbackQuery,
    widget: Button,
    dialog_manager: DialogManager,
    **kwargs,
):

    if widget.widget_id in (
        widget_offset := {'previous_item': -1, 'next_item': 1}
    ):
        dialog_manager.start_data['items_page_id'] += widget_offset[
            widget.widget_id
        ]
