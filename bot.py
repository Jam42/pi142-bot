"Schedule bot"
import os
import datetime
import telebot
import yaml

BOT = telebot.TeleBot(os.environ["TELEGRAM_TOKEN"])

WEEKDAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def read_yaml():
    "Reading yaml from file"
    with open('schedule.yaml') as stream:
        data = yaml.load(stream)
    return data


def check_even():
    "Return type of week (even / odd)"
    week_number = datetime.datetime.utcnow().isocalendar()[1]
    if week_number % 2 != 0:
        return True
    else:
        return False


@BOT.message_handler(WEEKDAYS)
def send_day(message):
    "Send schedule after receive command"
    day_name = message.text[1:]
    day_arr = read_yaml()[day_name]
    text = ''.join(get_message(day_arr, check_even()))
    BOT.send_message(message.chat.id, text)


@BOT.message_handler(commands=['now'])
def send_today(message):
    "Send schedule after receive command"
    day_arr = read_yaml()[get_weekday()]
    text = ''.join(get_message(day_arr, check_even()))
    BOT.send_message(message.chat.id, text)


@BOT.message_handler(commands=['tomorrow'])
def send_tomorrow(message):
    "Send schedule for tomorrow"
    tomorrow = WEEKDAYS[datetime.datetime.today().weekday() + 1]
    day_arr = read_yaml()[tomorrow]
    text = ''.join(get_message(day_arr, check_even()))
    BOT.send_message(message.chat.id, text)


def get_weekday():
    "Get day of the week"
    return WEEKDAYS[datetime.datetime.today().weekday()]


def get_message(yaml, even):
    "Preparing message to sending"
    data_list = []
    for x in range(len(yaml)):
        if yaml[x]['even'] == even:
            number = 'Number: ' + yaml[x]["number"] + "\n"
            lesson = 'Lesson: ' + yaml[x]["lesson"] + "\n"
            time = 'Time: ' + yaml[x]["time"] + "\n"
            room = 'Room: ' + yaml[x]["room"] + "\n"
            data_list.append(number + lesson + time + room + "\n")
    if not data_list:
        return "No lessons"
    return data_list


BOT.polling(none_stop=True)
