from flask import render_template, redirect, url_for, Blueprint, request, session, flash
from .models import Users
from datetime import datetime
from . import db

login_blueprint = Blueprint('login', __name__)
register_blueprint = Blueprint('register', __name__)
dashboard_blueprint = Blueprint('dashboard', __name__)
logout_blueprint = Blueprint('logout', __name__)


@login_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        user = Users.query.filter_by(username=username).first()
        if user:
            session['username'] = username
            return redirect(url_for('dashboard.dashboard'))
        else:
            flash("Invalid username !")
    return render_template('login.html')


@register_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        new_user = Users(username=username, registration_date=datetime.utcnow())
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login.login'))
    return render_template('register.html')


@dashboard_blueprint.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    if 'username' in session:
        user = Users.query.filter_by(username=session['username']).first()
        days_registered = (datetime.utcnow() - user.registration_date).days
        return render_template('dashboard.html', username=session['username'], days_registered=days_registered)


@logout_blueprint.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
        session.pop('registration_date', None)
        flash('You have been logged out!')
    return redirect(url_for('login.login'))
