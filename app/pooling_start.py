from aiogram import Dispatcher, Bot, executor
from pooling_settings import token
from handlers.handlers import cmd_start, cmd_startchat, cmd_stopchat, chat
bot = Bot(token=token)
dp = Dispatcher(bot=bot)
dp.register_message_handler(cmd_start, commands=['start'])
dp.register_message_handler(cmd_startchat, commands=['startchat'])
dp.register_message_handler(cmd_stopchat, commands=['stopchat'])
dp.register_message_handler(chat)
if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
