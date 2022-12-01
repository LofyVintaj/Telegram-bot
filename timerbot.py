from telegram.ext.updater import Updater, ContextTypes
from telegram.update import Update
from telegram.ext.callbackqueryhandler import CallbackQueryHandler

from telegram.ext import CommandHandler, ContextTypes, MessageHandler, filters, Job


def start(update: Update, context: ContextTypes.context ) -> None:
    """Sends explanation on how to use the bot."""
    update.message.reply_text("Hi! Use /set <seconds> to set a timer")


def alarm(context: ContextTypes.context) -> None:
    """Send the alarm message."""
    print('context job', context.job)
    job = context.job
    # data = job.data
    # chat_id = job.chat_id
    chat_id = 692256842
    data = '5'
    context.bot.send_message(chat_id, text=f"Beep! {data} seconds are over!")


def remove_job_if_exists(name: str, context: ContextTypes.context) -> bool:
    """Remove job with given name. Returns whether job was removed."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


def set_timer(update: Update, context: ContextTypes.context) -> None:
    """Add a job to the queue."""
    chat_id = update.effective_message.chat_id
    print('chat id -', chat_id)
    # try:
    # args[0] should contain the time for the timer in seconds
    due = float(context.args[0])
    print('due ', due)
    if due < 0:
        update.effective_message.reply_text("Sorry we can not go back to future!")
        return
    print(' removed job for exists  ')
    job_removed = remove_job_if_exists(str(chat_id), context)
    # context.job_queue.run_once(alarm, due, chat_id=chat_id, name=str(chat_id), data=due)
    print(' job queue run once ')
    context.job_queue.run_once(callback=alarm, when=due, name=str(chat_id))

    text = "Timer successfully set!"
    if job_removed:
        text += " Old one was removed."
    update.effective_message.reply_text(text)

    #except (IndexError, ValueError):
        #update.effective_message.reply_text("Usage: /set <seconds>")


def unset(update: Update, context: ContextTypes.context) -> None:
    """Remove the job if the user changed their mind."""
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = "Timer successfully cancelled!" if job_removed else "You have no active timer."
    update.message.reply_text(text)