import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('လွှိုင်ကော် Bot သို့ ကြိုဆိုပါသည်။')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        'Bot ၏ အသုံးပြုနည်းနှင့် command များကို သိရှိရန် အကူအညီ။\n'
        '/start - လွှိုင်ကော် Bot သို့ ကြိုဆိုပါသည်။\n'
        '/help - Bot ၏ အသုံးပြုနည်းနှင့် command များကို သိရှိရန် အကူအညီ။\n'
        '/about - Loikaw Bot ၏ ရည်ရွယ်ချက်နှင့် အကြောင်းအရာကို ဖော်ပြသည်။\n'
        '/weather - လွှိုင်ကော်မြို့အတွက် နောက်ဆုံး ရာသီဥတုအချက်အလက်များကို ရှာဖွေပါ။\n'
        '/info - လွှိုင်ကော်မြို့အကြောင်း သတင်းအချက်အလက်များကို ရယူပါ။\n'
        '/places - လွှိုင်ကော်မြို့ရှိ အထင်ကရနေရာများကို ရှာဖွေပါ။\n'
        '/hotels - လွှိုင်ကော်တွင် ရှိသော တည်းခိုရာအဆောင်များကို ရှာဖွေပါ။\n'
        '/restaurants - စားသောက်ရန် ကောင်းသော နေရာများကို ရှာဖွေပါ။'
    )

def about(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Loikaw Bot ၏ ရည်ရွယ်ချက်မှာ လွှိုင်ကော်မြို့အကြောင်း သတင်းအချက်အလက်များကို ရှာဖွေရန် ဖြစ်သည်။')

def weather(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('လွှိုင်ကော်မြို့အတွက် နောက်ဆုံး ရာသီဥတုအချက်အလက်များ: 25°C, clear sky.')

def info(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('လွှိုင်ကော်မြို့သည် မြန်မာနိုင်ငံ၏ ကယားပြည်နယ်၏ မြို့တော်ဖြစ်သည်။')

def places(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('လွှိုင်ကော်မြို့ရှိ အထင်ကရနေရာများ: Naung Tone, Kyat Ko, စသည်တို့ ဖြစ်သည်။')

def hotels(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('လွှိုင်ကော်တွင် ရှိသော တည်းခိုရာအဆောင်များ: Hotel A, Hotel B.')

def restaurants(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('စားသောက်ရန် ကောင်းသော နေရာများ: Restaurant A, Restaurant B.')

def main() -> None:
    token = os.getenv('TELEGRAM_TOKEN')
    updater = Updater(token)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(CommandHandler('about', about))
    updater.dispatcher.add_handler(CommandHandler('weather', weather))
    updater.dispatcher.add_handler(CommandHandler('info', info))
    updater.dispatcher.add_handler(CommandHandler('places', places))
    updater.dispatcher.add_handler(CommandHandler('hotels', hotels))
    updater.dispatcher.add_handler(CommandHandler('restaurants', restaurants))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()