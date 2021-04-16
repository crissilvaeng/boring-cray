from model import Course
from config import db

COURSES_SEEDS = [
    {'code': '6.0001', 'name': 'Introduction to Computer Science Programming in Python'},
    {'code': '6.042[J]', 'name': 'Mathematics for Computer Science'},
    {'code': '6.004', 'name': 'Computation Structures'},
    {'code': '6.006', 'name': 'Introduction to Algorithms'},
    {'code': '6.031', 'name': 'Elements of Software Construction'},
]

db.create_all()


def populate():
    for course_seed in COURSES_SEEDS:
        course = Course(**course_seed)
        db.session.add(course)
    db.session.commit()
