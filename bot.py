
import os
import datetime
import telebot
import yaml

BOT = telebot.TeleBot(os.environ["TELEGRAM_TOKEN"])

weekdays=['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

def read_yaml():
    "Reading yaml from file"
    with open('schedule.yaml') as stream:
        data = yaml.load(stream)
    return data

@BOT.message_handler(weekdays)
def send_day(message):
    "Send schedule after receive command"
    day_name = message.text[1:]
    day_arr = read_yaml()[day_name]
    text = get_message(day_arr)
    BOT.send_message(message.chat.id, text)

@BOT.message_handler(commands=['now'])
def send_today(message):
    "Send schedule after receive command"
    day_arr = read_yaml()[get_weekday()]
    text = get_message(day_arr)
    BOT.send_message(message.chat.id, text)

def get_weekday():
    "Get day of the week"
    return weekdays[datetime.datetime.today().weekday() - 1]

def get_message(read_yaml):
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
