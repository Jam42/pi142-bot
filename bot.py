# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    	bot.reply_to(message, "Hi!")

@bot.message_handler(commands=['понедельник'])
def send_message(message):
	bot.reply_to(message, "1-я неделя: \n 1-я пара: Шабалин (2к, 5 этаж) \n 2-я пара: Шабалин (2к, 5 этаж)\n \n 2-я неделя: \n 1-я пара: Шаталин (2к, 2 этаж)\n 2-я пара: Шаталин (2к, 2 этаж)")

@bot.message_handler(content_types=['text'])
def echo_all(message):
    bot.send_message(message.chat.id, ')')

bot.polling()