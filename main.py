from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode

API_TOKEN = 'YOUR_API_TOKEN'  # BotFather မှရသော API Token ကိုထည့်ပါ

def start(update, context):
    """Welcome Message."""
    welcome_text = (
        "👋 **Loikaw Explorer Bot** မှကြိုဆိုပါတယ်! 🌄\n"
        "Kayah State ရဲ့ အထူးအဆန်းတွေကို စူးစမ်းရှာဖွေပါ။\n\n"
        "သိလိုတာတွေက `/places` 📍 နှင့် `/food` 🍲 လို့ ရေးပြီး လေ့လာနိုင်ပါတယ်။"
    )
    update.message.reply_text(welcome_text, parse_mode=ParseMode.MARKDOWN)

def places(update, context):
    """Information about places to visit in Loikaw."""
    text = (
        "*Loikaw အထူးစွာသွားရောက်သင့်သောနေရာများ*\n"
        "1️⃣ *Taung Kwe Pagoda* – မြို့လေးကိုမြင်ရတဲ့နေရာက ထိပ်ဆုံး!\n"
        "2️⃣ *Kayan Villages* – အားကျစရာ *long-neck* မိန်းကလေးများကို တွေ့ရမည်။\n"
        "3️⃣ *Local Markets* – Palaung, Shan, Kayah စတဲ့ တိုင်းရင်းသားများကို တွေ့နိုင်ပါတယ်။"
    )
    update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN)

def food(update, context):
    """Information about local food."""
    text = (
        "*Loikaw ရဲ့စားဖို့သင့်တော်တဲ့ အစားအစာများ*\n"
        "🍚 *Rice Rolls with Pork* – ထုံးစံအတိုင်း အရသာရှိတဲ့ အစားအစာ။\n"
        "🥗 *Tuna Risotto* – ငါးနဲ့ဆီဖျော်ပြီး အိမ်တွေမှာသာရနိုင်တယ်။\n"
    )
    update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN)

def unknown(update, context):
    """Handle unknown commands."""
    update.message.reply_text("ဤ command ကိုမသိပါဘူး 😅.")

def main():
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("places", places))
    dp.add_handler(CommandHandler("food", food))
    dp.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
