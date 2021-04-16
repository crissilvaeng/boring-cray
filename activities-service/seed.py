from model import Task, Submission
from config import db

COURSE_CODE = '6.0001'

STUDENTS = [
    'albert.einstein@al.infnet.edu.br',
    'marie.curie@al.infnet.edu.br',
    'nicolas.tesla@al.infnet.edu.br',
]

TASKS = [
    {'description': 'What is computation?', 'course': COURSE_CODE},
    {'description': 'Branching and Iteration', 'course': COURSE_CODE},
    {'description': 'String Manipulation, Guess and check, Approximations, Bisection', 'course': COURSE_CODE},
    {'description': 'Decomposition, Abstractions, Functions', 'course': COURSE_CODE},
    {'description': 'Tuples, Lists, Aliasing, Mutability, Cloning', 'course': COURSE_CODE},
    {'description': 'Testing, Debugging, Exceptions, Assertions', 'course': COURSE_CODE},
    {'description':  'Object Oriented Programming', 'course': COURSE_CODE}
]

SUBMISSIONS = [({'student': student}) for student in STUDENTS]

db.create_all()


def populate():
    for task_seed in TASKS:
        task = Task(**task_seed)
        for submission_seed in SUBMISSIONS:
            task.submissions.append(Submission(**submission_seed))
        db.session.add(task)
    db.session.commit()
