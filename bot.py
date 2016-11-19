
import os
import telebot
import yaml

BOT = telebot.TeleBot(os.environ["TELEGRAM_TOKEN"])

def read_yaml():
    "Reading yaml from file"
    with open('schedule.yaml') as stream:
        data = yaml.load(stream)
    return data

@BOT.message_handler(commands=['start', 'help'])
def send_welcome(message):
    "Send welcome message"
    BOT.reply_to(message, "hi")

@BOT.message_handler(commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday'])
def send_day(message):
    "Send schedule after receive command"
    day = yaml.dump(read_yaml()[message.text[1:]], allow_unicode=True)
    BOT.send_message(message.chat.id, day)

BOT.polling()
