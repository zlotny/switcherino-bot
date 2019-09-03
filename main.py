#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" BeetlerBot

The purpose of this bot is to reply a image of a bee similar to Hitler as a response
to any message containing a series of keywords.

Yes, seriously.
"""

import telebot
import time
from datetime import datetime

__author__ = "Andrés Vieira"
__credits__ = ["Alejandro Gutiérrez"]
__version__ = "0.1"
__maintainer__ = "Andrés Vieira"
__email__ = "anvieiravazquez@gmail.com"
__status__ = "Development"

TOKEN = "805668801:AAFvl9lmegBE39tM7qjDMN1CCPPnIcepYxo"

bot = telebot.TeleBot(TOKEN)

KEYWORDS = ["GOLDEN SUN", "LOST AGE", "DARK DAWN"]


@bot.message_handler(commands=['start'])
def send_welcome(message):
    ''' Handle /start '''
    bot.reply_to(message, """\
Hi there, I am the Golden Sun Hype bot!.
Did anyone say Golden Sun?.\
""")


@bot.message_handler(commands=['help', 'info'])
def send_help(message):
    ''' Handle /help and /info '''
    bot.reply_to(
        message, "Just send a message containing any of this words: {}".format(",".join(KEYWORDS)))


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if any(x in message.text.upper() for x in KEYWORDS):
        bot.send_photo(message.chat.id, open('hype.png', 'rb'), 'ALGUIEN HA DICHO... G O L D E N S U N ?')

while True:
    try:
        bot.polling()
    except Exception as e:
        time.sleep(15)
