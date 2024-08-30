from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

# Define your command handler
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I'm your bot. Send me any message, and I'll echo it back to you.")

# Define your message handler (echo)
def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

def main():
    # Replace 'YOUR_TOKEN' with your actual bot token
    updater = Updater("7526285280:AAH2TVqFCFgmDp2znNIQBGsuFbPo4O5eLsE", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the /start command handler
    dp.add_handler(CommandHandler("start", start))

    # Register a message handler to echo back user messages
    dp.add_handler(MessageHandler(filters.text & ~filters.command, echo))

    # Start the bot
    updater.start_polling()

    # Keep the bot running until you stop it manually
    updater.idle()

if __name__ == '__main__':
    main()
