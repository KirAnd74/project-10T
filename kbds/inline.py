from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

og_pr1_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1", callback_data="1")],
        [InlineKeyboardButton(text="2", callback_data="2")],
        [InlineKeyboardButton(text="3", callback_data="3")],
        [InlineKeyboardButton(text="4", callback_data="4")],

    ],
    resize_keyboard=True,
)
