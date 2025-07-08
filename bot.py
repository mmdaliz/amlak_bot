from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hiسلام! به ربات املاک اصفهان خوش اومدی 🌟")

if __name__ == '__main__':
    print("ربات با موفقیت اجرا شد ✅")
    TOKEN = "8174394810:AAGAk-D9HhbO3N3F8dV0NE2MrwUfT-pm_lY"
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()