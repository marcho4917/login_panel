from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
    app.config['SECRET_KEY'] = 'klucz_tajny'
    db.init_app(app)

    from .main import login_blueprint, logout_blueprint, dashboard_blueprint, register_blueprint
    app.register_blueprint(login_blueprint)
    app.register_blueprint(logout_blueprint)
    app.register_blueprint(dashboard_blueprint)
    app.register_blueprint(register_blueprint)

    with app.app_context():
        db.create_all()

    return app
