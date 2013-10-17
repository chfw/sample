from models import db

class test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ab = db.Column(db.Unicode)
