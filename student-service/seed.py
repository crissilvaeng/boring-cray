from model import Student
from config import db

STUDENTS_SEEDS = [
    {'name': 'Albert Einsten', 'email': 'albert.einstein@al.infnet.edu.br'},
    {'name': 'Marie Curie', 'email': 'marie.curie@al.infnet.edu.br'},
    {'name': 'Nicolas Tesla', 'email': 'nicolas.tesla@al.infnet.edu.br'},
]

db.create_all()


def populate():
    for student_seed in STUDENTS_SEEDS:
        student = Student(**student_seed)
        db.session.add(student)
    db.session.commit()
