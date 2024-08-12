from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_TOKEN_HERE' with your actual bot token
TELEGRAM_TOKEN = '6811996280:AAHapr6EmUERcGI3FRKg0QpFLSAhubofGp4'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! This is your mini Telegram bot.')

def main() -> None:
    updater = Updater(TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
