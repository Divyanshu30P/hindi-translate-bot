import os
from telegram.ext import Updater, MessageHandler, Filters
from googletrans import Translator

translator = Translator()

def translate_message(update, context):
    text = update.message.text

    try:
        result = translator.translate(text, dest='hi')
        update.message.reply_text(result.text)
    except:
        update.message.reply_text("Translation failed, try again.")

def main():
    token = os.environ["BOT_TOKEN"]

    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
