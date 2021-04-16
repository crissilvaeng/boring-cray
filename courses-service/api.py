import seed

from model import Course, Session, Term
from config import app, ma
from flask import jsonify


class SessionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Session
        fields = ['code', 'start', 'end']


class TermSchema(ma.SQLAlchemyAutoSchema):
    session = ma.Nested(SessionSchema)

    class Meta:
        model = Term
        fields = ['code', 'professor', 'session']


class CourseSchema(ma.SQLAlchemyAutoSchema):
    terms = ma.Nested(TermSchema, many=True)

    class Meta:
        model = Course
        fields = ['code', 'name', 'terms']


single_course_schema = CourseSchema()
all_course_schema = CourseSchema(many=True)


@app.route("/api/courses", methods=["GET"])
def course_list():
    courses = Course.query.all()
    schema = all_course_schema.dump(courses)
    return jsonify(schema)


@app.route("/api/courses/<course_code>", methods=["GET"])
def course_detail(course_code):
    course = Course.query.get(course_code)
    schema = single_course_schema.dump(course)
    return jsonify(schema)


if __name__ == '__main__':
    seed.populate()
    app.run(host='0.0.0.0', port=5001, debug=True)
