
import os
import telebot
import yaml

bot = telebot.TeleBot(os.environ["TELEGRAM_TOKEN"])

with open('schedule.yaml') as stream:
    data = yaml.load(stream)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "hi")

@bot.message_handler(commands=['monday','tuesday','wednesday','thursday','friday'])
def send_day(message):
	day = yaml.dump(data[message.text[1:]], allow_unicode=True)
	bot.send_message(message.chat.id, day)

bot.polling()