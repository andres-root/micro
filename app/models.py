#!/usr/bin/env python
from datetime import datetime
from hashlib import md5
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login

followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.uid')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.uid'))
)

class User(UserMixin, db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    bio = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    followed = db.relationship(
        'User',
        secondary=followers,
        primaryjoin=(followers.c.follower_id == uid),
        secondaryjoin=(followers.c.followed_id == uid),
        backref=db.backref('followers', lazy='dynamic')
    , lazy='dynamic')

    def __repr__(self):
        return 'User {}'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        return self.uid
    
    def gravatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'http://gravatar.com/avatar/{0}?d=identicon&s={1}'.format(digest, size)
    
    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
    
    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)
    
    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.uid).count() > 0

    def followed_posts(self):
        followed = Post.query.join(
            followers,
            (followers.c.followed_id == Post.user_id)
        ).filter(followers.c.follower_id == self.uid)
        
        return followed.union(self.posts).order_by(Post.timestamp.desc())


@login.user_loader
def load_user(uid):
    return User.query.get(int(uid))


class Post(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(64), index=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.uid'))

    def __repr__(self):
        return 'Post {}'.format(self.body)
