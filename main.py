
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackqueryhandler import CallbackQueryHandler
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

# my apps
import basic_reply_handler
import timerbot

def main_basick_reply_handler_func() -> None:
    # Filters out unknown messages.
    application = Updater("5817335119:AAGWu9d5HHeiPzjjH_dheza7PSweF-oLWJ8", use_context=True)
    application.dispatcher.add_handler(CommandHandler('start', basic_reply_handler.start))
    application.dispatcher.add_handler(CommandHandler('youtube', basic_reply_handler.youtube_url))
    application.dispatcher.add_handler(CommandHandler('help', basic_reply_handler.help))
    application.dispatcher.add_handler(CommandHandler('gmail', basic_reply_handler.gmail_url))
    application.dispatcher.add_handler(CommandHandler('geeks', basic_reply_handler.geeks_url))
    application.dispatcher.add_handler(MessageHandler(Filters.text, basic_reply_handler.unknown))
    application.dispatcher.add_handler(MessageHandler(Filters.command, basic_reply_handler.unknown))  # Filters out unknown commands
    application.dispatcher.add_handler(MessageHandler(Filters.text, basic_reply_handler.unknown_text))
    application.start_polling()

def timerbot_func() :
    application = Updater("5817335119:AAGWu9d5HHeiPzjjH_dheza7PSweF-oLWJ8", use_context=True)
    # on different commands - answer in Telegram
    application.dispatcher.add_handler(CommandHandler(["start", "help"], timerbot.start))
    application.dispatcher.add_handler(CommandHandler("set", timerbot.set_timer))
    application.dispatcher.add_handler(CommandHandler("unset", timerbot.unset))

    # Run the bot until the user presses Ctrl-C
    application.start_polling()
    application.idle()


def main() -> None:
    """Run bot."""
    timerbot_func()

if __name__ == "__main__":
    main()
