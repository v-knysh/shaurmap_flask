from app import db

class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    address = db.Column()
    lat = db.Column(db.Float(precision=10, scale=16))
    lng = db.Column(db.Float(precision=10, scale=16))
    # type
    #
    # def
