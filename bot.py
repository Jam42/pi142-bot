# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    	bot.reply_to(message, "команда /деньНедели выдает расписание на этот день")

@bot.message_handler(commands=['понедельник'])
def send_message(message):
	bot.reply_to(message, "1-я неделя: \n 1: Шаталин (лекция) (2к, ауд. 220) \n 2: Шаталин (семинар) (2к, ауд. 220) \n \n2-я неделя: \n 1: Шабалин (семинар) (2к, ауд. 513)\n 2: Шабалин (лекция) (2к, ауд. 513)")

@bot.message_handler(commands=['вторник'])
def send_message(message):
	bot.reply_to(message, "отдыхай, фуфел")

@bot.message_handler(commands=['среда'])
def send_message(message):
	bot.reply_to(message, "1-я неделя: \n 3: Червенчук (лекция) (1к, ауд. 304) \n \n2-я неделя: \n 3: Червенчук (лекция) (1к, ауд. 304)\n 4: Червенчук (семинар) (1к, ауд. 304)")

@bot.message_handler(commands=['четверг'])
def send_message(message):
	bot.reply_to(message, "1-я неделя: \n 2: Стариков (лекция) (1к, ауд. 307) \n 3: Стариков (семинар) (1к, ауд. 402) \n 4: Федотова (лекция) (1к, ауд. 403) \n \n2-я неделя: \n 2: Христосова (лекция) (1к, ауд. 307) \n 3: Стариков (семинар) (1к, ауд. 402) \n 4: Федотова (семинар) (1к, ауд. 402)")

@bot.message_handler(commands=['пятница'])
def send_message(message):
	bot.reply_to(message, "1-я неделя: \n 1: Храпова (лекция) (1к, ауд. 304) \n 2: Храпова (семинар) (1к, ауд. 305) \n 3: окно :( \n 4: Христосова (семинар) (1к, ауд. 401) \n \n2-я неделя: \n 1: Мухаметдиновна (лекция) (1к, ауд. 205а) \n 2: Мухаметдиновна (семинар) (1к, ауд. 401) \n 3: окно :( \n 4: Христосова (семинар) (1к, ауд. 401)")

@bot.message_handler(content_types=['text'])
def echo_all(message):
    bot.send_message(message.chat.id, 'че')

bot.polling()