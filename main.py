#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Switcherino Bot

Bot made to participate in a telegram group

"""

import telebot
import time
from datetime import datetime
from random import choice

__author__ = "Andrés Vieira"
__credits__ = ["Alejandro Gutiérrez"]
__version__ = "0.1"
__maintainer__ = "Andrés Vieira"
__email__ = "anvieiravazquez@gmail.com"
__status__ = "Development"

TOKEN = "7940099208:AAHmZkDjg-iUhVHD0e02r7DskLvAe0BkkW0"

bot = telebot.TeleBot(TOKEN)

KEYWORDS_GS = ["GOLDEN SUN", "LOST AGE", "DARK DAWN"]
KEYWORDS_SOIBER = ["SOIBER", "OTERO", "AMBROA", "SOIBERIA", "SOIBERIANA", "SOIBERIANO", "SOIBERIANAS", "SOIBERIANOS"]
PICS_GS = ["hype1.png", "hype2.jpg"]
PICS_SOIBER = ["soiber1.png"]


@bot.message_handler(commands=['start'])
def send_welcome(message):
    ''' Handle /start '''
    bot.reply_to(message, """\
    Unga bunga?.\
""")


@bot.message_handler(commands=['help', 'info'])
def send_help(message):
    ''' Handle /help and /info '''
    bot.reply_to(
        message, "Just send a message containing any of this words: {}".format(",".join(KEYWORDS_GS+KEYWORDS_SOIBER)))


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    ''' Handle all other messages '''
    if any(x in message.text.upper() for x in KEYWORDS_GS):
        bot.send_photo(message.chat.id, open(choice(PICS_GS), 'rb'), 'ALGUIEN HA DICHO... G O L D E N S U N ?')
    elif any(x in message.text.upper() for x in KEYWORDS_SOIBER):
        bot.send_photo(message.chat.id, open(choice(PICS_SOIBER), 'rb'), 'Soiber, awesome content, You deserve more views')

while True:
    try:
        bot.polling()
    except Exception as e:
        time.sleep(15)
