from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Command handler for /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('လွှိုင်ကော် Bot သို့ ကြိုဆိုပါသည်။')

# Command handler for /help
def help_command(update: Update, context: CallbackContext) -> None:
    help_text = (
        "Commands:\n"
        "/start - လွှိုင်ကော် Bot သို့ ကြိုဆိုပါသည်။\n"
        "/help - Bot ၏ အသုံးပြုနည်းနှင့် command များကို သိရှိရန် အကူအညီ။\n"
        "/about - Loikaw Bot ၏ ရည်ရွယ်ချက်နှင့် အကြောင်းအရာကို ဖော်ပြသည်။\n"
        "/weather - လွှိုင်ကော်မြို့အတွက် နောက်ဆုံး ရာသီဥတုအချက်အလက်များကို ရှာဖွေပါ။\n"
        "/info - လွှိုင်ကော်မြို့အကြောင်း သတင်းအချက်အလက်များကို ရယူပါ။\n"
        "/places - လွှိုင်ကော်မြို့ရှိ အထင်ကရနေရာများကို ရှာဖွေပါ။\n"
        "/hotels - လွှိုင်ကော်တွင် ရှိသော တည်းခိုရာအဆောင်များကို ရှာဖွေပါ။\n"
        "/restaurants - စားသောက်ရန် ကောင်းသော နေရာများကို ရှာဖွေပါ။"
    )
    update.message.reply_text(help_text)

# Command handler for /about
def about(update: Update, context: CallbackContext) -> None:
    about_text = "Loikaw Bot သည် လွှိုင်ကော်မြို့အတွက် သတင်းအချက်အလက်များနှင့် အထောက်အကူများ ပေးရန် ရည်ရွယ်သည်။"
    update.message.reply_text(about_text)

# Main function to run the bot
def main() -> None:
    # Replace 'YOUR_SECRET_TOKEN' with your bot token
    updater = Updater("YOUR_SECRET_TOKEN")

    # Register handlers
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("help", help_command))
    updater.dispatcher.add_handler(CommandHandler("about", about))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()