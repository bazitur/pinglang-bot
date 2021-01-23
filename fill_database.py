from app import app, db
from models import RedditPost
from pickle import load
from datetime import datetime

with open("dump.pickle", "rb") as doc:
    data = load(doc)

for sub in list(data)[2:]:
    u = RedditPost(
        id=sub.id,
        title=sub.title,
        flair=sub.link_flair_text,
        selftext=sub.selftext,
        timestamp=datetime.fromtimestamp(sub.created_utc)
    )
    print("post added", u)
    db.session.add(u)
db.session.commit()
