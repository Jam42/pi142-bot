
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
    BOT.send_message(message.chat.id, get_message(message.text[1:]))


def get_message(message):
    data = []
    for x in range(len(read_yaml()[message])):
        lesson = 'Lesson: ' + str(yaml.dump(read_yaml()[message][x]["lesson"], allow_unicode=True))
        time = 'time: ' + yaml.dump(read_yaml()[message][x]["time"])
        room = 'room: ' + yaml.dump(read_yaml()[message][x]["room"])
        even = 'even: ' + yaml.dump(read_yaml()[message][x]["even"])
        data.append(lesson + time + room + even)
    return data

BOT.polling()
