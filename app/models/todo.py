from ..utils.dbo import db
from datetime import datetime

class Todo(db.Model):
    __tablename__ = "ttodos"
    todoid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    desc = db.Column(db.String(200))
    status = db.Column(db.String(10))
    userid = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, title, desc, userid, status='ongoing'):
        self.title = title
        self.desc = desc
        self.userid = userid
        self.status = status

    def json(self):
        return {"todoid": self.todoid, "title":self.title, "desc":self.desc, "status": self.status}
