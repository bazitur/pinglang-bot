import os
from praw import Reddit as RedditAPI
from pickle import dump

reddit = RedditAPI(
    client_id=os.environ["REDDIT_KEY_PUBLIC"],
    client_secret=os.environ["REDDIT_KEY_PRIVATE"],
    user_agent="Linux:com.myapp.bot:0.0.1"
)

with open("dump.pickle", "wb") as doc:
    dump(reddit.subreddit("language_exchange").new(limit=1000), doc)
