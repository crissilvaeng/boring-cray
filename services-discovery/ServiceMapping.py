import requests


class ServiceHandler:
    endpoint = ""
    payload = {}

    def get(self, **kwargs):
        req = requests.get(self.endpoint, params=self.payload)
        return req.json()


class CourseServiceHandler(ServiceHandler):
    endpoint = 'http://localhost:5001/api/courses/'

    def __init__(self, **kwargs):
        course_code = kwargs.get('course_code')
        self.endpoint = f'{self.endpoint}/{course_code}''
