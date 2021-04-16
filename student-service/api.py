import seed

from model import Student
from config import app, ma
from flask import jsonify


class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        fields = ['name', 'email']


single_student_schema = StudentSchema()
all_student_schema = StudentSchema(many=True)


@app.route("/api/students", methods=["GET"])
def student_list():
    students = Student.query.all()
    schema = all_student_schema.dump(students)
    return jsonify(schema)


@app.route("/api/students/<student_email>", methods=["GET"])
def student_detail(student_email):
    student = Student.query.get(student_email)
    schema = single_student_schema.dump(student)
    return jsonify(schema)


if __name__ == '__main__':
    seed.populate()
    app.run(host='0.0.0.0', port=5002, debug=True)
