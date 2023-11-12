from . import db
from datetime import datetime


class Users(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, username, registration_date):
        self.username = username
        self.registration_date = registration_date



