from flask import render_template
from app import app
from app.models import User, Point

@app.route('/users/<user_id>')
def userpage(user_id):

    user = User.query.filter_by(id=user_id).first_or_404()
    # print(user)
    # user = {
    #     'id': user_id,
    #     'name': 'name {}'.format(user_id),
    # }
    return render_template("user.html", user=user)

@app.route('/users')
def users_list():

    users = User.query.all()
    # print(users)
    return render_template("users_list.html", users=users)
