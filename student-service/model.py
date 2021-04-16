from config import db


class Student(db.Model):
    email = db.Column(db.String(127), primary_key=True, unique=True)
    name = db.Column(db.String(127), nullable=False)
