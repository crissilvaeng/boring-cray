from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)


class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]


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


db.create_all()

db.session.add(Course(code='6.0001', name='Introduction to Computer Science Programming in Python'))
db.session.add(Course(code='6.042[J]', name='Mathematics for Computer Science'))
db.session.add(Course(code='6.004', name='Computation Structures'))
db.session.add(Course(code='6.006', name='Introduction to Algorithms'))
db.session.add(Course(code='6.031', name='Elements of Software Construction'))
db.session.commit()

app.run(host='0.0.0.0', port=5000, debug=True)
