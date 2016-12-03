# -*- coding: utf-8 -*-

import os
import datetime
import telebot
import yaml
from telebot import types

BOT = telebot.TeleBot(os.environ["TELEGRAM_TOKEN"])

WEEKDAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']


def read_yaml():
    "Reading yaml from file"
    with open('schedule.yaml') as stream:
        data = yaml.load(stream)
    return data


@BOT.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('True')
    itembtn2 = types.KeyboardButton('False')
    markup.add(itembtn1, itembtn2)
    even = BOT.send_message(message.chat.id, "Is current week even?", reply_markup=markup)
    return even
    markup = types.ReplyKeyboardHide(selective=False)
    BOT.send_message(message.chat.id, message, reply_markup=markup)


@BOT.message_handler(WEEKDAYS)
def send_day(message):
    "Send schedule after receive command"
    day_name = message.text[1:]
    day_arr = read_yaml()[day_name]
    text = ''.join(get_message(day_arr))
    BOT.send_message(message.chat.id, text)


@BOT.message_handler(commands=['now'])
def send_today(message):
    "Send schedule after receive command"
    day_arr = read_yaml()[get_weekday()]
    text = ''.join(get_message(day_arr))
    BOT.send_message(message.chat.id, text)


def get_weekday():
    "Get day of the week"
    return WEEKDAYS[datetime.datetime.today().weekday() - 1]


def get_message(read_yaml):
    "Preparing message to sending"
    data_list = []
    for x in range(len(read_yaml)):
        if (read_yaml[x]["even"] == "true"): 
            number = 'Number: ' + read_yaml[x]["number"] + "\n"
            lesson = 'Lesson: ' + read_yaml[x]["lesson"] + "\n"
            time = 'Time: ' + read_yaml[x]["time"] + "\n"
            room = 'Room: ' + read_yaml[x]["room"] + "\n"
            even = 'Even: ' + read_yaml[x]["even"] + "\n"
            data_list.append(number + lesson + time + room + even + "\n")
    if not data_list:
        return "No lessons"
    return data_list


BOT.polling()
