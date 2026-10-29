import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

ADMIN_ID = 6012896505

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("عذراً، هذا البوت خاص بالمدير فقط.")
        return

    await update.message.reply_text(
        "🎮 مرحبا بيك في GAME MODS DZ!\n\n"
        "الأوامر المتاحة:\n"
        "/start - تشغيل البوت\n"
        "/help - المساعدة"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("هذا البوت خاص بالمدير فقط.")
        return

    await update.message.reply_text(
        "🤖 بوت الإدارة راهو في النسخة الأولى.\n"
        "راح نزيدو إدارة الألعاب في الخطوات الجاية."
    )

def main():
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("Missing TELEGRAM_BOT_TOKEN environment variable")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.run_polling()

if __name__ == "__main__":
    main()
