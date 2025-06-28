import os
import django
# Setting up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from api.models import TelegramUser
from asgiref.sync import sync_to_async



BOT_TOKEN = '7563696975:AAGs73GVY6vjQmIvMEUslKL7VwN_HiuZswE'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.from_user.username or update.message.from_user.first_name
    if username:
        await sync_to_async(TelegramUser.objects.get_or_create)(username=username)
        await update.message.reply_text(f"Hello @{username}, welcome to the bot!")
        print(f"Saved : {username}")

    else:
        await update.message.reply_text("Username not found.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is polling and waiting for /start command...")
    app.run_polling()

    