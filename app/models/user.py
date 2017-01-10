from app import db
from .point import Point

ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    points = db.relationship('Point', backref='author', lazy='dynamic')

    def __init__(self, username, email, role=ROLE_USER):
        self.username = username
        self.email = email
        self.role = role


    def __repr__(self):
        return "=User {0}=".format(self.username)
