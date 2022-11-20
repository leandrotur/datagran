import time
import os
from celery import Celery
from mongo_model import Mongo, CmdDoc
from flask import Flask
# Wait for rabbitmq to be started
time.sleep(15)

app = Celery(
    'postman',
    broker='redis://datagran_redis:6379',
    backend='redis://datagran_redis:6379',
)
app_f = Flask(__name__)
db = Mongo(app_f).db

@app.task(name='execute_task')  # Named task
def execute_task(id:str, cmd:str):
    cmddoc = CmdDoc.objects(id=id)
    try:
        status = os.system(cmd)
        
        if not status:
            cmddoc.update(status="Executed")
        else:
            cmddoc.update(status="Failed")
        print(f'task id:{id} executed with result code {status}')
    except Exception as e:
        print(e)
        cmddoc.update(status="Failed")

