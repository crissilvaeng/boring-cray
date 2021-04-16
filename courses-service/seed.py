from model import Course, Session, Term
from datetime import datetime
from config import db

DATETIME_ISO_FORMAT = '%Y-%m-%dT%H:%M:%S%zZ'

COURSES_SEEDS = [
    {'code': '6.0001', 'name': 'Introduction to Computer Science Programming in Python'},
    {'code': '6.042[J]', 'name': 'Mathematics for Computer Science'},
    {'code': '6.004', 'name': 'Computation Structures'},
    {'code': '6.006', 'name': 'Introduction to Algorithms'},
    {'code': '6.031', 'name': 'Elements of Software Construction'},
]

SESSIONS_SEEDS = [
    {'code': 'Spring2021', 'start': '2021-03-01T00:00:00+0000Z', 'end': '2021-05-31T23:59:59+0000Z'},
    {'code': 'Summer2021', 'start': '2021-06-01T00:00:00+0000Z', 'end': '2021-08-31T23:59:59+0000Z'},
    {'code': 'Fall2021', 'start': '2021-09-01T00:00:00+0000Z', 'end': '2021-11-30T23:59:59+0000Z'},
    {'code': 'Winter2021', 'start': '2021-12-01T00:00:00+0000Z', 'end': '2022-02-28T23:59:59+0000Z'},
]

TERMS_SEEDS = [
    {'code': '6.0001_Spring2021', 'professor': 'Eric Grimson', 'course': '6.0001', 'session': 'Spring2021'},
    {'code': '6.0001_Summer2021', 'professor': 'Eric Grimson', 'course': '6.0001', 'session': 'Summer2021'},
    {'code': '6.042[J]_Summer2021', 'professor': 'Tom Leighton', 'course': '6.042[J]', 'session': 'Spring2021'},
]

db.create_all()


def populate():
    for course_seed in COURSES_SEEDS:
        course = Course(**course_seed)
        db.session.add(course)
    for session_seed in SESSIONS_SEEDS:
        session_seed['start'] = datetime.strptime(session_seed['start'], DATETIME_ISO_FORMAT)
        session_seed['end'] = datetime.strptime(session_seed['end'], DATETIME_ISO_FORMAT)
        _session = Session(**session_seed)
        db.session.add(_session)
    for term_seed in TERMS_SEEDS:
        term = Term(**term_seed)
        db.session.add(term)
    db.session.commit()
