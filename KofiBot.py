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


def main():
    tb = telebot.TeleBot(TOKEN)
    chat_id = None
    while chat_id is None:
        updates = tb.get_updates()
        if len(updates) > 0:
            chat_id = updates[-1].message.chat.id
        else:
            print "No updates.\n"

    print "Achieved a chat id, which is {}".format(chat_id)
    tb.send_message(chat_id, "Hi there! I'm going to post 'kofipre?' every Monday to Friday at 15:50")
    while True:
        time.sleep(20)
        d = datetime.today()
        if d.weekday() in range(0, 5) and d.hour is 15 and d.minute is 50:
            print "hi"
            tb.send_message(chat_id, "kofipre?")
            time.sleep(100)


if __name__ == '__main__':
    main()
