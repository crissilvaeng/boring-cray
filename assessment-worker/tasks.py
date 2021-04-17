from celery import Celery

import requests

app = Celery('tasks', broker='pyamqp://broker//')


@app.task
def send_submission_to_evaluation(id, task, course, student):
    service_url = 'http://localhost:5004/api/assessments'
    assessment_data = {
        'id': id,
        'task': task,
        'course': course,
        'student': student,
    }
    response = requests.post(service_url, json=assessment_data)
    return response.json()


@app.task
def send_score_to_submission(id, score):
    service_url = f'http://localhost:5003/api/submissions/{id}'
    submission_data = {
        'score': score,
    }
    response = requests.put(service_url, json=submission_data)
    return response.json()
