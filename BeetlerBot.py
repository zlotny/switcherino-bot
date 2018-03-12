#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" KofiBot

The purpose of this bot is just to send 'kofipre?' to a chat at 15:50, Monday to Friday.
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

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am BeetlerBot.
Pay me 25 beetcoins or i will kill you.\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):

    cid = message.chat.id
	
    if "BEE" in message.text.upper() or "ABEGA" in message.text.upper()	or "ABEJA" in message.text.upper() or "ABIEGA" in message.text.upper() or "GABEE" in message.text.upper() or "LAZAJAVIER" in message.text.upper() or "OGABIER" in message.text.upper(): 
        bot.send_photo(message.chat.id, open('abega.png', 'rb'),'BZZZZZ')

bot.polling()
