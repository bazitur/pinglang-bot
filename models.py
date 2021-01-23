from manage import db,app

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class RedditPost(db.Model):
    id = db.Column(db.String(6), primary_key=True)
    title = db.Column(db.Text())
    selftext = db.Column(db.Text())
    flair = db.Column(db.String(25))
    timestamp=db.Column(db.DateTime())

    def __repr__(self):
        return '<User %r>' % (self.id)
