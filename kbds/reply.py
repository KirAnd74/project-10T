from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Меню"),
            KeyboardButton(text="ОГЭ"),
        ],
        {
            KeyboardButton(text="ЕГЭ"),
            KeyboardButton(text="Помощь"),
        },
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вас интерисует?",
)
del_kbd = ReplyKeyboardRemove()

oge_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Разбор заданий"),
            KeyboardButton(text="Практика"),
        ],
        {
            KeyboardButton(
                text="Назад",
            ),
        },
    ],
    resize_keyboard=True,
)
oge_razbor_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🖊️1"),
            KeyboardButton(text="🖊️2"),
            KeyboardButton(text="🖊️3"),
        ],
        {
            KeyboardButton(text="🖊️4"),
            KeyboardButton(text="🖊️5"),
            KeyboardButton(text="🖊️6"),
        },
        {
            KeyboardButton(text="🖊️7"),
            KeyboardButton(text="🖊️8"),
            KeyboardButton(text="🖊️9"),
        },
        {
            KeyboardButton(text="🖊️10"),
            KeyboardButton(text="🖊️11"),
            KeyboardButton(text="🖊️12"),
        },
        {
            KeyboardButton(text="🖊️13"),
            KeyboardButton(text="🖊️14"),
            KeyboardButton(text="🖊️15"),
        },
        {
            KeyboardButton(text="🔙Назад"),
        },
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вас интерисует?",
)

oge_practika_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📔1"),
            KeyboardButton(text="📔2"),
            KeyboardButton(text="📔3"),
        ],
        {
            KeyboardButton(text="📔4"),
            KeyboardButton(text="📔5"),
            KeyboardButton(text="📔6"),
        },
        {
            KeyboardButton(text="📔7"),
            KeyboardButton(text="📔8"),
            KeyboardButton(text="📔9"),
        },
        {
            KeyboardButton(text="📔10"),
            KeyboardButton(text="📔11"),
            KeyboardButton(text="📔12"),
        },
        {
            KeyboardButton(text="📔13"),
            KeyboardButton(text="📔14"),
            KeyboardButton(text="📔15"),
        },
        {
            KeyboardButton(text="🔙Назад"),
        },
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вас интерисует?",
)

ege_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✏️Разбор заданий"),
            KeyboardButton(text="✏️Практика"),
        ],
        {
            KeyboardButton(
                text="Назад",
            ),
        },
    ],
    resize_keyboard=True,
)


ege_razbor_str1_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✏️1"),
            KeyboardButton(text="✏️2"),
            KeyboardButton(text="✏️3"),
        ],
        {
            KeyboardButton(text="✏️4"),
            KeyboardButton(text="✏️5"),
            KeyboardButton(text="✏️6"),
        },
        {
            KeyboardButton(text="✏️7"),
            KeyboardButton(text="✏️8"),
            KeyboardButton(text="✏️9"),
        },
        {
            KeyboardButton(text="✏️10"),
            KeyboardButton(text="✏️11"),
            KeyboardButton(text="✏️12"),
        },
        {
            KeyboardButton(text="✏️13"),
            KeyboardButton(text="✏️14"),
            KeyboardButton(text="✏️15"),
        },
        {
            KeyboardButton(text="➡️Далее"),
            KeyboardButton(text="◀️Назад"),
        },
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вас интерисует?",
)
ege_razbor_str2_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✏️16"),
            KeyboardButton(text="✏️17"),
            KeyboardButton(text="✏️18"),
        ],
        {
            KeyboardButton(text="✏️19"),
            KeyboardButton(text="✏️20"),
            KeyboardButton(text="✏️21"),
        },
        {
            KeyboardButton(text="✏️22"),
            KeyboardButton(text="✏️23"),
            KeyboardButton(text="✏️24"),
        },
        {
            KeyboardButton(text="✏️25"),
            KeyboardButton(text="✏️26"),
            KeyboardButton(text="✏️27"),
        },
        {
            KeyboardButton(text="⬅️Назад"),
        },
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вас интерисует?",
)
