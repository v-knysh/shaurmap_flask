import json
from functools import reduce

from flask import jsonify, request

from app import app, db
from app.models import Point, PointSchema

point_schema = PointSchema()


# @app.route('/api/points/test')
# def api_test():
#     points = Point.query.
#     dict = {"a": 1}
#     return jsonify([dict]*4)

@app.route('/api/most_rated')
def api_most_rated_points():
    point_query = Point.query
    if request.args:
        params = ['max_lat', 'min_lat', 'max_lng', 'min_lng']
        param_dict = {param: request.args.get(param) for param in params}
        validate = reduce(lambda x, y: x and y, param_dict.values())
        if not validate:
            params_need = [param for param in params if not request.args.get(param)]
            return jsonify({"errors": ["required parameters " + str(params_need)]}), 400
        point_query = point_query.filter(Point.lat > param_dict['min_lat'])
        point_query = point_query.filter(Point.lat < param_dict['max_lat'])
        point_query = point_query.filter(Point.lng > param_dict['min_lng'])
        point_query = point_query.filter(Point.lng < param_dict['max_lng'])


    points = []

    for point in point_query.order_by(Point.rating.desc()).limit(20).all():
        points.append({
            'name': point.name,
            'lat': point.lat,
            'lng': point.lng,
        })


    # response = {'points': [point_schema.dump(point).data for point in points]}
    response = {"points": points}
    return jsonify(response)


@app.route('/api/points/point_<point_id>')
def api_point(point_id):
    point = Point.query.get_or_404(point_id)
    return jsonify({"point": point_schema.dump(point).data})


#
# @app.route('/api/points/point_<point_id>')
# def api_point(point_id):
#     point = Point.query.get_or_404(point_id)
#     return point_schema.jsonify(point)
