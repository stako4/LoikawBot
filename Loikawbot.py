import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Function to start the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [['🏞️ Attractions', '🍜 Local Cuisine'], ['👥 Ethnic Groups', '🛏️ Accommodation'], ['🗺️ Practical Info', '📅 About Loikaw']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Welcome to LoikawBot! Please select an option from the menu:",
        reply_markup=reply_markup
    )

# Function to show attractions
async def attractions(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    attractions_text = (
        "### Things to Do in Loikaw:\n"
        "1. **Visit authentic Kayan villages** - Experience the daily lives of Kayan women.\n"
        "2. **Learn about ethnic diversity** - Meet various ethnic groups like Palaung, Shan, and Kayah.\n"
        "3. **Explore stunning pagodas** - Visit Taung Kwe Pagoda for breathtaking views.\n"
        "4. **Enjoy local cuisine** - Try rice rolls and other delicious local dishes.\n"
        "5. **Spot domestic elephants** - Witness elephants collecting firewood.\n"
    )
    await update.message.reply_text(attractions_text)

# Function to show local cuisine
async def local_cuisine(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    cuisine_text = (
        "### Unique Local Cuisine:\n"
        "Loikaw is famous for its rice paste-based dishes, including:\n"
        "- **Rice rolls** filled with pork meat.\n"
        "- **Risotto** with minced tuna and vegetables.\n"
        "Experience these delicacies in local eateries!"
    )
    await update.message.reply_text(cuisine_text)

# Function to show ethnic groups
async def ethnic_groups(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    groups_text = (
        "### Ethnic Diversity in Loikaw:\n"
        "Loikaw is home to multiple ethnic groups:\n"
        "- **Kayan** - Known for their long necks.\n"
        "- **Palaung** - Predominantly from Shan State.\n"
        "- **Kayah** - Their women often wear black and red dresses.\n"
        "Exploring these communities is a unique experience!"
    )
    await update.message.reply_text(groups_text)

# Function to show accommodation options
async def accommodation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    accommodation_text = (
        "### Accommodation in Loikaw:\n"
        "- **Budget:** Loikaw Princess Motel - Friendly staff and free bicycle rental.\n"
        "- **Mid-Range:** Kayan Golden Sky Motel - Clean and cozy for couples.\n"
        "Book in advance to secure your stay!"
    )
    await update.message.reply_text(accommodation_text)

# Function to show practical information
async def practical_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    practical_text = (
        "### Practical Information:\n"
        "Loikaw is located 200km south of Inle Lake.\n"
        "Transport options include:\n"
        "- **Mini-bus from Inle Lake** (9-hour journey)\n"
        "- **Buses from Yangon** (16-hour journey)\n"
        "- **Small airport** with flights from Yangon.\n"
    )
    await update.message.reply_text(practical_text)

# Function to provide about information
async def about_loikaw(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    about_text = (
        "### About Loikaw:\n"
        "Loikaw is the capital of Kayah State, known for its rich cultural diversity.\n"
        "Since 2013, it has opened its doors to independent travelers, offering an authentic experience away from mass tourism."
    )
    await update.message.reply_text(about_text)

# Main function to run the bot
def main() -> None:
    bot_token = os.getenv("BOT_TOKEN")

    application = ApplicationBuilder().token(bot_token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("attractions", attractions))
    application.add_handler(CommandHandler("local_cuisine", local_cuisine))
    application.add_handler(CommandHandler("ethnic_groups", ethnic_groups))
    application.add_handler(CommandHandler("accommodation", accommodation))
    application.add_handler(CommandHandler("practical_info", practical_info))
    application.add_handler(CommandHandler("about", about_loikaw))

    application.run_polling()

if __name__ == '__main__':
    main()
