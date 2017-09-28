#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" KofiBot

The purpose of this bot is just to send 'kofipre?' to a chat at 15:50, Monday to Friday.
Yes, seriously.
"""

import telebot
import time
from datetime import datetime

__author__ = "Andrés Vieira"
__credits__ = ["Andrés Vieira"]
__version__ = "0.1"
__maintainer__ = "Andrés Vieira"
__email__ = "anvieiravazquez@gmail.com"
__status__ = "Development"

TOKEN = "360303020:AAGT8eyx7mtda99bL79o02g6G9WcbH4N6eY"

bot = telebot.TeleBot(TOKEN)
chat_id = -1
poll_hour = 15
poll_minute = 50


@bot.message_handler(commands=['changehour'])
def bot_changehour(message):
    global chat_id

    if chat_id == -1:
        bot.reply_to(message, "Please /start the bot first.")
        return

    new_time = message.text.split("/changehour ")[1]
    try:
        hours = int(new_time.split(":")[0])
        minutes = int(new_time.split(":")[1])
        if hours in range(0, 24) and minutes in range(0, 60):
            bot.send_message(chat_id, "Changing hour. New time will be: {}:{}".format(str(hours), str(minutes)))
        else:
            raise ValueError('Hours or minutes are not correct')
    except:
        bot.reply_to(message, "Can't change hour. Please write a correct time. Example: /changehour 18:59")


@bot.message_handler(commands=['help'])
def bot_help(message):
    bot.reply_to(message, "This are the available commands:\n\n"
                          "\t/start : Starts the bot. No needed parameters. \n\n"
                          "\t/help : Shows this message. No needed parameters \n\n"
                          "\t/changehour XX:XX : Changes the hour. Example: /changehour 15:20")


@bot.message_handler(commands=['start'])
def bot_start(message):
    """ Starts bot on /start command. Polls time and checks if it has to send a message to the group. """
    global chat_id

    chat_id = message.chat.id
    bot.send_message(chat_id, "Hi there! I'm KofiBot. My only purpose is to print 'kofipre?' at a defined hour Wednesdays and Thursdays.\n\n"
                              "I will say 'kofipre?' each day at {}:{}".format(poll_hour, poll_minute))
    while True:
        time.sleep(20)
        d = datetime.today()
        if d.weekday() in range(2, 4) and d.hour is poll_hour and d.minute is poll_minute:
            bot.send_message(chat_id, "kofipre?")
            time.sleep(100)

print("Started KofiBot")
bot.polling(none_stop=False, interval=0, timeout=20)
