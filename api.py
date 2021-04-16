from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)


class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]


class Assessment(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(127), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    course_code = db.Column(db.Integer, db.ForeignKey('course.code'),
                            nullable=False)
    course = db.relationship('Course',
                             backref=db.backref('assessments', lazy=True))

    def serialize(self):
        return Serializer.serialize(self)

    def __repr__(self):
        return '<Assessment %r>' % self.name


class Course(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(15), nullable=False)
    name = db.Column(db.String(127), nullable=False)

    def serialize(self):
        return Serializer.serialize(self)

    def __repr__(self):
        return '<Course %r>' % self.name


@app.route('/courses/<course_code>')
def get_course(course_code):
    course = Course.query.filter_by(code=course_code).first()
    return jsonify(course.serialize())


@app.route('/courses')
def list_courses():
    courses = Course.query.all()
    return jsonify(Course.serialize_list(courses))


@app.route('/assessments')
def list_assessments():
    assessments = Assessment.query.all()
    return jsonify(Assessment.serialize_list(assessments))


@app.route('/courses/<course_code>/assessments')
def list_assessments_by_course(course_code):
    assessments = Assessment.query.filter_by(course_code=course_code).all()
    return jsonify(Assessment.serialize_list(assessments))


db.create_all()

cs50 = Course(code='CS50', name='Introduction to Computer Science')
cs50.assessments.append(Assessment(title='Problem Set 0'))
cs50.assessments.append(Assessment(title='Problem Set 1'))
cs50.assessments.append(Assessment(title='Quiz 1'))
cs50.assessments.append(Assessment(title='Problem Set 2'))
cs50.assessments.append(Assessment(title='Problem Set 3'))
cs50.assessments.append(Assessment(title='Quiz 2'))
cs50.assessments.append(Assessment(title='Test 1'))
cs50.assessments.append(Assessment(title='Problem Set 4'))
cs50.assessments.append(Assessment(title='Problem Set 5'))
cs50.assessments.append(Assessment(title='Quiz 3'))
cs50.assessments.append(Assessment(title='Problem Set 6'))
cs50.assessments.append(Assessment(title='Problem Set 7'))
cs50.assessments.append(Assessment(title='Quiz 4'))
cs50.assessments.append(Assessment(title='Test 2'))
cs50.assessments.append(Assessment(title='Final Project'))
db.session.add(cs50)
db.session.add(Course(code='6.0001', name='Introduction to Computer Science Programming in Python'))
db.session.add(Course(code='6.042[J]', name='Mathematics for Computer Science'))
db.session.add(Course(code='6.004', name='Computation Structures'))
db.session.add(Course(code='6.006', name='Introduction to Algorithms'))
db.session.add(Course(code='6.031', name='Elements of Software Construction'))
db.session.commit()

app.run(host='0.0.0.0', port=5000, debug=True)
