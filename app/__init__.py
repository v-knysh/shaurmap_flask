from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_login import LoginManager


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:38kv1444@localhost/shaurmap_db'
app.config.from_object('config')
app.debug = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
lm = LoginManager()
lm.init_app(app)

from app import views, models

if __name__ == '__main__':
    app.run()
