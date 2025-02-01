from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import find_dotenv, load_dotenv
import asyncio
import os

load_dotenv(find_dotenv())

from handlers.user_private import user_private_router
from common.bot_cmds_list import private

ALLOWED_UPDATES = ["message , edit_message"]


bot = Bot(token="7700371957:AAGAjFimjK4U_yCy_mCBzgqOH27Ipitglho"#os.getenv("TOKEN") 
          #, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
          )

dp = Dispatcher()
dp.include_router(user_private_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)



try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Bot stopped")
    
