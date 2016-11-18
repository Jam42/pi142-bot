# -*- coding: utf-8 -*-
import telebot
import json
import os

bot = telebot.TeleBot(os.environ["TELEGRAM_TOKEN"])

with open('schedule.json') as json_data:
    data = json.load(json_data)
    schedule = data["Monday"][0]["number"] + ": \n" + data["Monday"][0]["lesson"] + "\n" + data["Monday"][0]["time"] + "\n" + data["Monday"][0]["room"]

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "сообщение деньНедели выдает расписание на этот день")

@bot.message_handler(func=lambda message: True)
def send_message(message):
	if (message.text == 'понедельник'):
		bot.send_message(message.chat.id, schedule)
	#else:
		#bot.send_message(message.chat.id, 'что')

bot.polling()