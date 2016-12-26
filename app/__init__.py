from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:38kv1444@localhost/shaurmap_db'
app.config.from_object('config')
app.debug = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views, models


if __name__ == '__main__':
    app.run()
