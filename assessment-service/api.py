from config import app, ma, db, broker
from model import Assessment
from flask import jsonify, request


class AssessmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Assessment
        fields = ['id', 'task', 'course', 'student', 'score']


single_assessment_schema = AssessmentSchema()
all_assessment_schema = AssessmentSchema(many=True)


@app.route('/api/assessments', methods=['GET'])
def assessment_list():
    assessments = Assessment.query.all()
    schema = all_assessment_schema.dump(assessments)
    return jsonify(schema)


@app.route('/api/assessments/<int:assessment_id>', methods=['GET'])
def assessment_detail(assessment_id):
    assessment = Assessment.query.get(assessment_id)
    schema = single_assessment_schema.dump(assessment)
    return jsonify(schema)


@app.route('/api/assessments', methods=['POST'])
def assessment_submit():
    payload = request.json
    assessment = Assessment(**payload)
    db.session.add(assessment)
    db.session.commit()
    schema = single_assessment_schema.dump(assessment)
    return jsonify(schema)


@app.route('/api/assessments/<int:assessment_id>', methods=['PUT'])
def assessment_update(assessment_id):
    payload = request.json
    assessment = Assessment.query.get(assessment_id)
    assessment.score = payload.get('score')
    db.session.commit()
    broker.send_task('tasks.send_score_to_submission', args=[
        assessment.id,
        assessment.score
    ], kwargs={})
    schema = single_assessment_schema.dump(assessment)
    return jsonify(schema)


if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5004, debug=True)
