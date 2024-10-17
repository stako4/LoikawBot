from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# /start Command Handler: Bot Introduction နဲ့ Main Menu Keyboard ထည့်ပါ။
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [['🗺 Loikaw အကြောင်း', '📍 အထင်ကရနေရာများ'], ['ℹ️ အကူအညီ']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text(
        "မင်္ဂလာပါ! 😊 LoikawBot မှ ကြိုဆိုပါတယ်။ သင် သိလိုတာတွေကို အောက်က Menu ကနေ ရွေးပါ။",
        reply_markup=reply_markup
    )

# Loikaw အကြောင်း Command
def about(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Loikaw ဟာ Kayah ပြည်နယ်ရဲ့ မြို့တော် ဖြစ်ပြီး တစ်မြို့လုံးမှာ သဘာဝအလှအပနဲ့ ရိုးရာယဉ်ကျေးမှုတွေကြွယ်ဝပါတယ်။\n"
        "ဤမြို့မှာ Kayah လူမျိုးတွေရဲ့ အထိမ်းအမှတ်ပွဲတွေ၊ နိုင်ငံခြားသားတွေရဲ့ အပန်းဖြေခရီးစဉ်တွေဖြစ်လာပါတယ်။\n"
        "အကောင်းဆုံး အချိန်က နှောင်းနှင်းသီးပွင့်ရာသီတုန်းမှာ လာရင် ပိုပြီးအလှမြင်ရပါမယ်။"
    )

# အထင်ကရနေရာများ Command
def places(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "📍 **Loikaw ရဲ့ အထင်ကရနေရာများ:**\n"
        "1. 🏯 **Taung Kwe Pagoda** - မြို့ပြမြင်ကွင်းကို မြင်နိုင်တဲ့ ကမ်းနားပုထိုး။\n"
        "2. 🌊 **Htee Pwint Kan (Umbrella Lake)** - ငြိမ်သက်ပြီး အလှပဆုံး ရေကန်。\n"
        "3. 🏛 **Kayah Cultural Museum** - Kayah ယဉ်ကျေးမှုတွေ စုစည်းထားတဲ့ ပြတိုက်。\n"
        "4. 🛍 **Demawso Market** - Kayah လူမျိုးတို့ရဲ့ ဒေသထွက်ကုန်စည်များ。\n"
        "5. 🏞 **Seven Lakes** - အပန်းဖြေဖို့ သဘာဝလှပတဲ့ ရေကန်များ။"
    )

# အကူအညီ Command
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "မေးမြန်းလိုတာ ရှိရင် ဒီနေရာမှာ ရေးထားခဲ့နိုင်ပါတယ်။\n"
        "သို့မဟုတ် /start နဲ့ Main Menu ကို ပြန်သွားပါ။"
    )

# အလုပ်မလိုက်တဲ့ Input တွေအတွက် Auto Reply
def unknown(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "🤔 ဒီ Command ကို မသိပါဘူး။ Menu ထဲက ရွေးပါကောင်းစွာပြောနိုင်ပါတယ်။"
    )

def main() -> None:
    # BotFather က ရထားတဲ့ Bot Token ထည့်ပါ
    updater = Updater("7594541731:AAHxU60qI2wvDENt1lUyMFM2s61wfnxGQhQ")

    dispatcher = updater.dispatcher

    # Command Handler တွေ သတ်မှတ်ပါ
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("about", about))
    dispatcher.add_handler(CommandHandler("places", places))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # အလုပ်မလိုက်တဲ့ Command တွေအတွက် Handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, unknown))

    # Bot ကို အလုပ်လုပ်စေပါ
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
