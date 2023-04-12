from ..utils.dbo import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "tusers"
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    email = db.Column(db.String(30))
    pwd = db.Column(db.String(200))
    imgpath = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, username, email, pwd):
        self.username = username
        self.email = email
        self.pwd = pwd

    def json(self):
        return {"username":self.username, "email":self.email}
