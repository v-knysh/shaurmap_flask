from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://testdbuser:password@localhost/myveryfirstdbtest002'
app.debug = True
db = SQLAlchemy(app)

from app import views, models


if __name__ == '__main__':
    app.run()
