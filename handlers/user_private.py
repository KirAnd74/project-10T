from aiogram import types,Router , F
from aiogram.filters import CommandStart,Command , or_f


from kbds import reply


user_private_router = Router()




@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
   await message.answer("Привет я твой бот", reply_markup= reply.start_kb)
@user_private_router.message(or_f(Command('menu'),(F.text.lower() == "menu")))
async def menu(message: types.Message):
   await message.answer("Вот меню")
