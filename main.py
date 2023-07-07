#!/usr/bin/python
# -*- coding: UTF-8 -*-
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.auth_widget import check_token
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, InputFile
from aiogram.types.web_app_info import WebAppInfo
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import BoundFilter
import json, asyncio, logging, random, time, sqlite3, os
#################################################################################################################################
storage = MemoryStorage()
bot = Bot(token='6221891379:AAH2WvzJw-PTr9izMSsjcZFKTBGKx8rxW6I', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s', level=logging.INFO,)
#################################################################################################################################
# Получение данных о пользователе (ID: int, Username: str)
async def get_user_data(message: types.Message):
	return [message.from_user.id, (message.from_user.username if message.from_user.username is not None else 'no_@_username')]


def kb_menu():
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(KeyboardButton('Test', web_app=WebAppInfo(url='https://flowsidee-github-io.vercel.app')))
	return keyboard


#################################################################################################################################
@dp.message_handler(CommandStart())
async def mm_start(message: types.Message, state: FSMContext):
	gg=await get_user_data(message)
	uid, uum = gg[0], gg[1]

	await message.answer('test by flowside', reply_markup=kb_menu())

@dp.message_handler(content_types='web_app_data')
async def web_app_handler(webAppMes):
	#{"message_id": 12, "from": {"id": 5749609907, "is_bot": false, "first_name": "flowside", "username": "flowside", "language_code": "ru"}, "chat": {"id": 5749609907, "first_name": "flowside", "username": "flowside", "type": "private"}, "date": 1688738873, "web_app_data": {"button_text": "Test", "data": "items"}}
	md=webAppMes.web_app_data.data
	uid=webAppMes.chat.id
	print(webAppMes)
	print(md)
	await bot.send_message(uid, f'Работник отправлен на поле:\n{md}')




"""@dp.message_handler(content_types=['web_app_data'])
async def buy_nigger(message: types.Message):
	await bot.send_invoice(web_app_message.chat.id, title='Title', description='Title', provider_token='f', currency='rub', need_email=True, need_phone_number=True, prices=LabeledPrice(label='Nigger', amount=696969), start_parameter='example', payload='some_invoice')
"""
############################################ CALLBACKQUERY ######################################################################


#################################################################################################################################
async def on_startup(dp):
	global bot_info
	bot_info=await bot.get_me()
	async def set_default_commands(dp):
		await dp.bot.set_my_commands([types.BotCommand("start", "Запустить бота")])
	await set_default_commands(dp)

if __name__ == "__main__":
	executor.start_polling(dp, on_startup=on_startup)