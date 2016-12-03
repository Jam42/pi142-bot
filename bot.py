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


def check_even(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('True')
    itembtn2 = types.KeyboardButton('False')
    markup.add(itembtn1, itembtn2)
    even = BOT.send_message(message.chat.id, "Is current week even?", reply_markup=markup)
    return BOT.register_next_step_handler(even, even_handler)


def even_handler(message):
    markup = types.ReplyKeyboardHide(selective=False)
    BOT.send_message(message.chat.id, get_message(read_yaml(), message.text), reply_markup=markup)
    return message.text
    

@BOT.message_handler(WEEKDAYS)
def send_day(message):
    "Send schedule after receive command"
    BOT.send_message(message.chat.id, check_even(message))
    day_name = message.text[1:]
    day_arr = read_yaml()[day_name]
    text = ''.join(get_message(day_arr, check_even(message)))
    BOT.send_message(message.chat.id, text)


@BOT.message_handler(commands=['now'])
def send_today(message):
    "Send schedule after receive command"
    day_arr = read_yaml()[get_weekday()]

    text = ''.join(get_message(day_arr, check_even(message)))
    BOT.send_message(message.chat.id, text)


def get_weekday():
    "Get day of the week"
    return WEEKDAYS[datetime.datetime.today().weekday() - 1]


def get_message(read_yaml, even):
    "Preparing message to sending"
    data_list = []
    for x in range(len(read_yaml)):
        if read_yaml[x]["even"] == even:
            number = 'Number: ' + read_yaml[x]["number"] + "\n"
            lesson = 'Lesson: ' + read_yaml[x]["lesson"] + "\n"
            time = 'Time: ' + read_yaml[x]["time"] + "\n"
            room = 'Room: ' + read_yaml[x]["room"] + "\n"
            data_list.append(number + lesson + time + room + "\n")
    if not data_list:
        return "No lessons"
    return data_list


BOT.polling()
