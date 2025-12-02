import os
import threading
from telegram.ext import Updater, MessageHandler, Filters
from deep_translator import GoogleTranslator
from flask import Flask

# -------------------- Telegram Bot --------------------
def translate_message(update, context):
    text = update.message.text
    try:
        # Translate text to Hindi
        result = GoogleTranslator(source='auto', target='hi').translate(text)
        update.message.reply_text(result)
    except Exception as e:
        # Catch any errors
        update.message.reply_text("Translation failed. Try again.")

def run_bot():
    token = os.environ["BOT_TOKEN"]  # Bot token from Railway variable
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_message))

    updater.start_polling()
    updater.idle()

# -------------------- Flask Keep-Alive --------------------
app = Flask(__name__)

@app.route("/")
def index():
    return "Bot is alive"

def run_flask():
    port = int(os.environ.get("PORT", 8080))  # Railway assigns PORT automatically
    app.run(host="0.0.0.0", port=port)

# -------------------- Start Both --------------------
if __name__ == "__main__":
    # Start Flask in a separate thread
    threading.Thread(target=run_flask).start()
    # Start Telegram bot
    run_bot()
