from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [['🗺 Loikaw အကြောင်း', '📍 အထင်ကရနေရာများ'], ['ℹ️ အကူအညီ']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text(
        "မင်္ဂလာပါ! 😊 LoikawBot မှ ကြိုဆိုပါတယ်။ သင် သိလိုတာတွေကို အောက်က Menu ကနေ ရွေးပါ။",
        reply_markup=reply_markup
    )

def about(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Loikaw ဟာ Kayah ပြည်နယ်ရဲ့ မြို့တော်ဖြစ်ပြီး ရိုးရာယဉ်ကျေးမှုတွေနဲ့ သဘာဝအလှတရားတွေအတွက် နာမည်ကြီးပါတယ်။"
    )

def places(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "📍 **Loikaw ရဲ့ အထင်ကရနေရာများ:**\n"
        "1. 🏯 **Taung Kwe Pagoda**\n"
        "2. 🌊 **Htee Pwint Kan (Umbrella Lake)**\n"
        "3. 🏛 **Kayah Cultural Museum**\n"
        "4. 🛍 **Demawso Market**\n"
        "5. 🏞 **Seven Lakes**"
    )

def unknown(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("🤔 ဒီ Command ကို မသိပါဘူး။ Menu ထဲက ပြန်ရွေးပါ။")

def main() -> None:
    updater = Updater("7594541731:AAHxU60qI2wvDENt1lUyMFM2s61wfnxGQhQ")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("about", about))
    dispatcher.add_handler(CommandHandler("places", places))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, unknown))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
