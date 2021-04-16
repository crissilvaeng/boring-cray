from config import db


class Course(db.Model):
    code = db.Column(db.String(15), primary_key=True, unique=True)
    name = db.Column(db.String(127), nullable=False)
