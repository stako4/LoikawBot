import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [['🗺 Loikaw အကြောင်း', '📍 အထင်ကရနေရာများ'], ['ℹ️ အကူအညီ']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "မင်္ဂလာပါ! 😊 LoikawBot မှ ကြိုဆိုပါတယ်။ သင် သိလိုတာတွေကို အောက်က Menu ကနေ ရွေးပါ။",
        reply_markup=reply_markup
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Loikaw ဟာ Kayah ပြည်နယ်ရဲ့ မြို့တော် ဖြစ်ပြီး သဘာဝနဲ့ ယဉ်ကျေးမှုအလှတွေကို စုစည်းထားပါတယ်။"
    )

async def places(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "📍 **Loikaw ရဲ့ အထင်ကရနေရာများ:**\n"
        "1. 🏯 **Taung Kwe Pagoda**\n"
        "2. 🌊 **Htee Pwint Kan (Umbrella Lake)**\n"
        "3. 🏛 **Kayah Cultural Museum**\n"
        "4. 🛍 **Demawso Market**\n"
        "5. 🏞 **Seven Lakes**"
    )

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🤔 ဒီ Command ကို မသိပါဘူး။ Menu ထဲက ပြန်ရွေးပါ။")

def main() -> None:
    bot_token = os.getenv("BOT_TOKEN")

    if not bot_token:
        raise ValueError("BOT_TOKEN is not set. Check your GitHub Secrets configuration.")

    application = ApplicationBuilder().token(bot_token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("places", places))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown))

    application.run_polling()

if __name__ == '__main__':
    main()
