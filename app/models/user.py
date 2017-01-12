from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db, login_manager
from .point import Point

ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    points = db.relationship('Point', backref='author', lazy='dynamic')
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, username, email, password, role=ROLE_USER):
        self.username = username
        self.email = email
        self.role = role
        self.password = password

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    def __repr__(self):
        return "=User {0}=".format(self.username)
