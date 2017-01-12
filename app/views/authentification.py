from flask import render_template, redirect, flash
from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Email
from flask_login import login_user, login_required, logout_user

from app import app, login_manager
from app.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect("/")
        flash("invalid username or password")
        # login_user()
        return redirect('/login')
    return render_template('auth/login.html', form=form)

@app.route('/log_out')
@login_required
def logout():
    logout_user()
    return redirect('/')
