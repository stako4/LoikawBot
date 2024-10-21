from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Command functions
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("လွှိုင်ကော် Bot သို့ ကြိုဆိုပါသည်။")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot ၏ အသုံးပြုနည်းနှင့် command များကို သိရှိရန် အကူအညီ။")

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Loikaw Bot ၏ ရည်ရွယ်ချက်နှင့် အကြောင်းအရာကို ဖော်ပြသည်။")

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("လွှိုင်ကော်မြို့အတွက် နောက်ဆုံး ရာသီဥတုအချက်အလက်များကို ရှာဖွေပါ။")

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("လွှိုင်ကော်မြို့အကြောင်း သတင်းအချက်အလက်များကို ရယူပါ။")

async def places(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("လွှိုင်ကော်မြို့ရှိ အထင်ကရနေရာများကို ရှာဖွေပါ။")

async def hotels(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("လွှိုင်ကော်တွင် ရှိသော တည်းခိုရာအဆောင်များကို ရှာဖွေပါ။")

async def restaurants(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("စားသောက်ရန် ကောင်းသော နေရာများကို ရှာဖွေပါ။")

# Main function
async def main():
    application = ApplicationBuilder().token("7259866248:AAGpXN0JldtTnn9ra7qA4-C6fK52NMWmNcw").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("weather", weather))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("places", places))
    application.add_handler(CommandHandler("hotels", hotels))
    application.add_handler(CommandHandler("restaurants", restaurants))

    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())