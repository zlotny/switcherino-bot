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

__author__ = "Alejandro Gutiérrez"
__credits__ = ["Andrés Vieira"]
__version__ = "0.1"
__maintainer__ = "Alejandro Gutiérrez"
__email__ = "agutierreznovoa90@gmail.com"
__status__ = "Development"

TOKEN = "527579098:AAGtle1dXS7DBwG3fjnNOZBpS-5YxJn4LpY"

bot = telebot.TeleBot(TOKEN)
cid = -1

KEYWORDS = ["BEE",
            "ABEGA",
            "ABEJA",
            "ABIEGA",
            "GABEE",
            "LAZAJAVIER",
            "OGABIER"]


@bot.message_handler(commands=['start'])
def send_welcome(message):
    ''' Handle /start '''
    bot.reply_to(message, """\
Hi there, I am BeetlerBot.
Pay me 25 beetcoins or i will kill you.\
""")


@bot.message_handler(commands=['help', 'info'])
def send_help(message):
    ''' Handle /help and /info '''
    bot.reply_to(
        message, "Just send a message containing any of this words: {}".format(KEYWORDS))


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):

    cid = message.chat.id

    if any(x in message.text.upper() for x in KEYWORDS):
        bot.send_photo(message.chat.id, open('abega.png', 'rb'), 'BZZZZZ')


bot.polling()
