from config import db


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(127), nullable=False)
    course = db.Column(db.String(15), nullable=False)
    submissions = db.relationship('Submission')


class Submission(db.Model):
    __tablename__ = 'submission'
    id = db.Column(db.Integer, primary_key=True)
    student = db.Column(db.String(127), nullable=False)
    score = db.Column(db.Integer, default=0)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
