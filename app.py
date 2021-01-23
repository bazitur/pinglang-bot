from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from praw import Reddit as RedditAPI
from telegram import Bot as TelegramBotAPI
import os
from time import time
from babel.dates import format_datetime as babel_format_datetime
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

####################################
# Flask contents
####################################

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
db = SQLAlchemy(app)
from models import RedditPost

UPDATE_DB_INTERVAL = 86400

reddit = RedditAPI(
    client_id=os.environ["REDDIT_KEY_PUBLIC"],
    client_secret=os.environ["REDDIT_KEY_PRIVATE"],
    user_agent="Linux:com.myapp.bot:0.0.1"
)

@app.template_filter('datetime')
def format_datetime(value, format='medium'):
    if format == 'full':
        format="EEEE, d. MMMM y HH:mm"
    elif format == 'medium':
        format="EE dd.MM.y HH:mm"
    return babel_format_datetime(value, format)

####################################
# Reddit contents
####################################

@app.route('/')
def index():
    return render_template('index.html', reddit_data=RedditPost.query.order_by(desc(RedditPost.timestamp)).limit(10).all())

#@hook up every day
def update_database():
    time_before = int(time()) - UPDATE_DB_INTERVAL - 30 # additional 30 seconds just in case
    return reddit.subreddit("language_exchange").new(limit=200)

####################################
# Telegram contents
####################################
TELEGRAM_KEY = os.environ["TELEGRAM_KEY"]
if __name__ == '__main__':
    app.run()
