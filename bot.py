from telegram.ext import Updater, MessageHandler, Filters
from deep_translator import GoogleTranslator
import os

def translate_message(update, context):
    text = update.message.text
    try:
        result = GoogleTranslator(source='auto', target='hi').translate(text)
        update.message.reply_text(result)
    except:
        update.message.reply_text("Translation failed")

def main():
    token = os.environ["BOT_TOKEN"]
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
