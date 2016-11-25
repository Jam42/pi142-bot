
import os
import telebot
import yaml
import datetime

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
    BOT.send_message(message.chat.id, (get_message(message.text[1:], read_yaml()[message.text[1:]])))


def get_message(message, read_yaml):
    "Preparing message to sending"
    dataList = []
    for x in range(len(read_yaml)):
        number = 'Number: ' + read_yaml[x]["number"] + "\n"
        lesson = 'Lesson: ' + read_yaml[x]["lesson"] + "\n"
        time = 'Time: ' + read_yaml[x]["time"] + "\n"
        room = 'Room: ' + read_yaml[x]["room"] + "\n"
        even = 'Even: ' + read_yaml[x]["even"] + "\n"
        dataList.append(number + lesson + time + room + even + "\n")
    if not dataList:
        return ("No lessons")
    dataString = ''.join(dataList)
    return dataString


BOT.polling()
