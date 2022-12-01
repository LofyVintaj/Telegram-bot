from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackqueryhandler import CallbackQueryHandler
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

"""
    reply_text - Это что-то вроде ответа на сообщение. 
                 Он пересылает в тот же директ ответ на какое-то действие
"""

updater = Updater("5817335119:AAGWu9d5HHeiPzjjH_dheza7PSweF-oLWJ8", use_context=True)

def start(update: Update, context: CallbackQueryHandler):
    update.message.reply_text(
        "Hello sir, Welcome to the Bot.Please write\
        /help to see the commands available.")


def help(update: Update, context: CallbackQueryHandler):
    update.message.reply_text("""Available Commands :-
    /youtube - To get the youtube URL
    /linkedin - To get the LinkedIn profile URL
    /gmail - To get gmail URL
    /geeks - To get the GeeksforGeeks URL""")


def gmail_url(update: Update, context: CallbackQueryHandler):
    update.message.reply_text(
        "Your gmail link here (I am not\
        giving mine one for security reasons)")


def youtube_url(update: Update, context: CallbackQueryHandler):
    update.message.reply_text("Youtube Link =>\
    https://www.youtube.com/")


def geeks_url(update: Update, context: CallbackQueryHandler):
    update.message.reply_text(
        "GeeksforGeeks URL => https://www.geeksforgeeks.org/")


def unknown(update: Update, context: CallbackQueryHandler):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackQueryHandler):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)