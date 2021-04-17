from config import app, ma, db, broker
from flask import jsonify, request
from model import Task, Submission

import seed


class SubmissionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Submission
        fields = ['id', 'student', 'score']


class TaskSchema(ma.SQLAlchemyAutoSchema):
    submissions = ma.Nested(SubmissionSchema, many=True)

    class Meta:
        model = Task
        fields = ['id', 'description', 'course', 'submissions']


class AllTaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        fields = ['id', 'description', 'course']


single_submission_schema = SubmissionSchema()
single_task_schema = TaskSchema()
all_tasks_schema = AllTaskSchema(many=True)


@app.route('/api/tasks', methods=['GET'])
def task_list():
    tasks = Task.query.all()
    schema = all_tasks_schema.dump(tasks)
    return jsonify(schema)


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def task_detail(task_id):
    task = Task.query.get(task_id)
    schema = single_task_schema.dump(task)
    return jsonify(schema)


@app.route('/api/tasks/<int:task_id>/submissions', methods=['POST'])
def send_submission(task_id):
    task = Task.query.get(task_id)
    payload = request.json
    submission = Submission(**payload)
    task.submissions.append(submission)
    db.session.commit()
    broker.send_task('tasks.send_submission_to_evaluation', args=[
        submission.id,
        task.id,
        task.course,
        submission.student,
    ], kwargs={})
    schema = single_submission_schema.dump(submission)
    return jsonify(schema)


@app.route('/api/submissions/<int:submission_id>', methods=['PUT'])
def update_submission(submission_id):
    payload = request.json
    submission = Submission.query.get(submission_id)
    submission.score = payload.get('score')
    db.session.commit()
    schema = single_submission_schema.dump(submission)
    return jsonify(schema)


if __name__ == '__main__':
    seed.populate()
    app.run(host='0.0.0.0', port=5003, debug=True)
