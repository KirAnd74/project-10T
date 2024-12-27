from aiogram.types import ReplyKeyboardMarkup, KeyboardButton ,ReplyKeyboardRemove 
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Menu"),
            KeyboardButton(text="Oge"),
        ],
        {
            KeyboardButton(text="Ege"),
            KeyboardButton(text="Help"),
        },
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вас интерисует?",
)
del_kbd = ReplyKeyboardRemove()


start_kb2 = ReplyKeyboardBuilder()
start_kb2.add(
    KeyboardButton(text="Menu"),
    KeyboardButton(text="Oge"),
    KeyboardButton(text="Ege"),
    KeyboardButton(text="Help"),
)
start_kb2.adjust(2,2)


start_kb3 = ReplyKeyboardBuilder()
start_kb3.attach(start_kb2)
start_kb3.add(KeyboardButton(text="Оставить отзыв"))
start_kb3.adjust(2,2)

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Menu"),
            KeyboardButton(text="🖊️Oge"),
        ],
        {
            KeyboardButton(text="🖊️Ege"),
            KeyboardButton(text="Help"),
        },
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вас интерисует?",
)