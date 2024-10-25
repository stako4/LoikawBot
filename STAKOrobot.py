import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Logging configuration
logging.basicConfig(format='%(asctime)s • %(name)s • %(levelname)s • %(message)s', level=logging.INFO)

# Define a command handler function
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your AI chat bot. How can I help you today?')

# Define a message handler function
def reply(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    # Here you would integrate your AI logic (e.g., OpenAI API)
    ai_response = f"You said: {user_message}"  # Placeholder response
    update.message.reply_text(ai_response)

def main():
    # Replace 'YOUR_TOKEN' with your bot's API token
    updater = Updater("7276623409:AAED5cBl8kfJ65b_o2ICpDCxvp1hl_z2mYk")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command and message handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
    
