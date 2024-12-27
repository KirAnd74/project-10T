from aiogram import types,Router , F
from aiogram.filters import CommandStart,Command

user_private_router = Router()




@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
   await message.answer("it is a command")
@user_private_router.message(Command('menu'))
async def start_cmd(message: types.Message):
   await message.answer("Вот меню")
@user_private_router.message(F.text )
async def echo(message: types.Message):
   await message.answer("Это магический фильтер")
