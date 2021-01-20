from praw import Reddit as RedditAPI
from telegram import Bot as TelegramBotAPI
from flask import Flask, render_template
import os

TELEGRAM_KEY = os.environ["TELEGRAM_KEY"] if "TELEGRAM_KEY" in os.environ else None

app = Flask(__name__)

# A welcome message to test our server
@app.route('/')
def index():
    return render_template('index.html', TOPSECRET=TELEGRAM_KEY)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
