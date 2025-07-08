from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8174394810:AAGAk-D9HhbO3N3F8dV0NE2MrwUfT-pm_lY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات املاک اصفهان فعال است.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ ربات با موفقیت اجرا شد...")
    app.run_polling()
