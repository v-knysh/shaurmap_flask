from flask import render_template

from app import app
from app.models import Point

@app.route('/points/<point_id>')
def point(point_id):

    point = Point.query.filter_by(id=point_id).first_or_404()

    return render_template("point.html", point=point)



@app.route('/points')
def point_list():

    points = Point.query.all()

    return render_template("points_list.html", points=points)