
from datetime import datetime

from flask import Flask, request
from celery import Celery
from mongo_model import Mongo, CmdDoc

app = Flask(__name__)

celery = Celery(
    'postman',
    broker='redis://datagran_redis:6379',
    backend='redis://datagran_redis:6379',
)
db = Mongo(app).db


@app.route('/new_task', methods=['POST'])
def new_task():
    request_data = request.get_json()
    cmd = request_data['cmd']
    cmd_doc = CmdDoc(
        name=cmd,
        status="Created",
        creation_date=datetime.utcnow()
    )
    cmd_doc.save()
    celery.send_task('execute_task', (str(cmd_doc.id), cmd))
    print("test sending CELERY")
    return {'id': str(cmd_doc.id)}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
