from app import db


class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=False, nullable=False)
    address = db.Column(db.String(100))
    lat = db.Column(db.Float(precision=10, scale=16))
    lng = db.Column(db.Float(precision=10, scale=16))
    description = db.Column(db.Text, nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __init__(self, name, adress, lat, lng, user):
        self.name = name
        self.address = adress
        self.lat = lat
        self.lng = lng
        self.author_id = user.id
