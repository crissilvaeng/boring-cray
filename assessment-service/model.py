from config import db

class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.Integer, nullable=False)
    course = db.Column(db.String(15), nullable=False)
    student = db.Column(db.String(127), nullable=False)
    score = db.Column(db.Integer, default=0)
