from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
oge_pr_1_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ерш"),
            KeyboardButton(text="Бычок"),
        ],
        {
            KeyboardButton(text="Карась",),
            KeyboardButton(text="Долгопер",),
        },
    ],
    resize_keyboard=True,
)
oge_pr_1_otv_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ерш"),
            KeyboardButton(text="Бычок"),
        ],
        {
            KeyboardButton(text="Карась",),
            KeyboardButton(text="Долгопер",),
        },
    ],
    resize_keyboard=True,
)