from aiogram.fsm.state import StatesGroup, State

class menu(StatesGroup):
    start = State()
    menu = State()
    

class Work(StatesGroup):
    process = State()