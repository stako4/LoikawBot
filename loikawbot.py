import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def main() -> None:
    bot_token = os.getenv("7594541731:AAHRfyRJ__6qhTMfDkcthKI8Q6e3nkLrEXU")  # GitHub Secrets ကနေ Token ကိုယူပါ
    updater = Updater(7594541731:AAHRfyRJ__6qhTMfDkcthKI8Q6e3nkLrEXU)
    
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("about", about))
    dispatcher.add_handler(CommandHandler("places", places))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, unknown))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
