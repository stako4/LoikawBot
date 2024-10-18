from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from dotenv import load_dotenv
import os
from telegram.ext import ApplicationBuilder

TOKEN = os.getenv("TELEGRAM_TOKEN")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.run_polling()

# Start command with a warm and engaging message
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📜 Loikaw သမိုင်း", callback_data='history')],
        [InlineKeyboardButton("🏞 အထင်ကရနေရာများ", callback_data='places')],
        [InlineKeyboardButton("🎭 ယဉ်ကျေးမှုနှင့် အစဉ်အလာ", callback_data='culture')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_message = (
        "🎉 **မင်္ဂလာပါ!** 🎉\n\n"
        "🌄 **LoikawBot** မှ ကြိုဆိုပါသည်။ ကယားပြည်နယ်၏ လှပသောမြို့လေး "
        "Loikaw အကြောင်း အားလုံးကို ဒီမှာ လေ့လာနိုင်ပါတယ်။\n\n"
        "ဘာကို သိချင်ပါသလဲ? 👇 ရွေးချယ်ပါ:"
    )
    await update.message.reply_text(welcome_message, reply_markup=reply_markup, parse_mode='Markdown')

# Callback function for button interactions
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'history':
        await query.edit_message_text(
            "📜 **Loikaw သမိုင်း**:\n\n"
            "Loikaw သည် ကယားပြည်နယ်၏ မြို့တော်ဖြစ်ပြီး အလွန်စိတ်ဝင်စားဖွယ်ရာသော သမိုင်းများဖြင့် ပြည့်နေပါသည်။"
        )

    elif query.data == 'places':
        await query.edit_message_text(
            "🏞 **အထင်ကရနေရာများ**:\n\n"
            "- နန်းမြို့စေတီ\n"
            "- ဖားလေးရေတံခွန်\n"
            "- ဒုလ်လေါင်တောင် 🌄\n\n"
            "ဒီနေရာတွေကို သွားရောက်လည်ပတ်ဖို့ မမေ့နဲ့နော်!"
        )

    elif query.data == 'culture':
        await query.edit_message_text(
            "🎭 **ယဉ်ကျေးမှုနှင့် အစဉ်အလာ**:\n\n"
            "Loikaw တွင် တိုင်းရင်းသားများ၏ ယဉ်ကျေးမှုများ၊ အားကစားပွဲများနှင့် "
            "ဖျော်ဖြေပွဲများကို အစဉ်အတိုင်း ကျင်းပလေ့ရှိပါတယ်။ 💃"
        )

# Main function to run the bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("LoikawBot by STAKO is running... 🚀")
    app.run_polling()
