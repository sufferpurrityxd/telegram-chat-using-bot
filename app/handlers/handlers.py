from database.execute import execute_command
from profanity_filter.filter import profainty_filter
from aiogram import types


async def cmd_start(message: types.Message):
    await execute_command(message=message, adduser=True)
    await message.reply("Hi i'm an anonymous chat bot!\nWrite the /start command and chat with people from all over the world")


async def cmd_startchat(message: types.Message):
    execute = await execute_command(message=message, startchat=True)
    if execute == 0:
        await message.reply("You are already chatting")
    elif execute == 1:
        await message.reply("You are already waiting")
    else:
        await message.bot.send_message(execute['chatting_with'], "I found a chat for you")
        await message.bot.send_message(execute['request_user'], "I found a chat for you")
    

async def cmd_stopchat(message: types.Message):
    execute = await execute_command(message=message, stopchat=True)
    if execute == 0:
        await message.reply("You dont have any chats")
    elif execute == 1:
        await message.reply("You are put on hold. When a suitable chat is found, I will let you know")
    else:
        await message.bot.send_message(execute['chatting_with'], "Interlocutor ended the chat")
        await message.bot.send_message(execute['request_user'], "You have completed the chat")


async def chat(message: types.Message):
    execute = await execute_command(message=message, chat=True)
    if execute == 0:
        await message.reply("Please type /startchat")
    elif execute == 1:
        await message.reply("You are put on hold. When a suitable chat is found, I will let you know")
    elif execute == 3:
        await message.reply("You are allready chatting")
    else:
        await message.bot.send_message(execute['chatting_with'], profainty_filter(execute["message"]))
