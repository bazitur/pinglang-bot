from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from praw import Reddit as RedditAPI
from telegram import Bot as TelegramBotAPI
from flask import Flask, render_template
import os

TELEGRAM_KEY = os.environ["TELEGRAM_KEY"]

reddit = RedditAPI(
    client_id=os.environ["REDDIT_KEY_PUBLIC"],
    client_secret=os.environ["REDDIT_KEY_PRIVATE"],
    user_agent="Linux:com.myapp.bot:0.0.1"
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
db = SQLAlchemy(app)

from models import User

@app.route('/')
def index():
    return render_template('index.html', reddit_data=reddit.subreddit("language_exchange").new(limit=10))

@app.route('/add/')
def webhook():
    return "yeeehaw!!!"
    name = "ram2"
    email = "ram2@ram.com"
    u = User(nickname = name, email = email)
    print("user created", u)
    db.session.add(u)
    db.session.commit()
    return "user created"

@app.route('/delete/')
def delete():
    u = User.query.get(i)
    db.session.delete(u)
    db.session.commit()
    return "user deleted"

if __name__ == '__main__':
    app.run()
