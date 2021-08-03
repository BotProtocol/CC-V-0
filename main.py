import constants as keys
from telegram.ext import *
import responses as R

print("CC is Starting .......")

def start_command(update):
  update.message.reply_text('type command for miss cc')

def help_command(update):
  update.message.reply_text('if you need help open your google')

def handle_message(Update):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def error(update):
    print(f"update {update} cause erroe {context.erroe}")

def main():
    updater = Updater(keys.API_KEY,use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()

