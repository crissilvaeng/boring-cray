from config import db


class Course(db.Model):
    __tablename__ = 'course'
    code = db.Column(db.String(15), primary_key=True, unique=True)
    name = db.Column(db.String(127), nullable=False)
    terms = db.relationship('Term', back_populates='course_ref')


class Session(db.Model):
    __tablename__ = 'session'
    code = db.Column(db.String(15), primary_key=True, unique=True)
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    terms = db.relationship('Term', back_populates='session_ref')


class Term(db.Model):
    __term__ = 'term'
    code = db.Column(db.String(15), primary_key=True, unique=True)
    professor = db.Column(db.String(127), primary_key=True)
    course = db.Column(db.String(15), db.ForeignKey('course.code'))
    session = db.Column(db.String(15), db.ForeignKey('session.code'))
    course_ref = db.relationship('Course', back_populates='terms')
    session_ref = db.relationship('Session', back_populates='terms')
