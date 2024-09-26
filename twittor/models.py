from datetime import datetime
from twittor import db  # from init

# Want database (twitter.db) to be in twittor folder (absolute path)
# which was done in config.py


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    # interacting with other classes/tables
    # upper 'T' -> link to entire class/table
    tweets = db.relationship('Tweet', backref='author', lazy='dynamic')

    def __repr__(self):  # for debugging
        return "id={}, username={}, email={}, password_hash={}".format(
            self.id, self.username, self.email, self.password_hash
        )


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    # lower 'u' - link to specific column in another table/class
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):  # for debugging
        return "id={}, body={}, create_time={}, user_id={}". format(
            self.id, self.body, self.create_time, self.user_id
        )
