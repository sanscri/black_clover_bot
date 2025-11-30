from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.formatting import Bold, as_line, as_list
from aiogram.fsm.state import StatesGroup, State
from aiogram.enums import ParseMode

from keyboards.reply_other_kb import honor_board_kb

honor_board_router = Router()


@honor_board_router.message(F.text == '📜Доска почёта')
async def cmd_honor_board(message: Message, state: FSMContext):
    await state.clear()
    content="Доска почёта"
    await message.answer(content, parse_mode=ParseMode.HTML, reply_markup=honor_board_kb())
    
