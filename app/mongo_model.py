import datetime
from flask_mongoengine import MongoEngine
db = MongoEngine()


class Mongo:
    def __init__(
        self,
        app
    ) -> None:
        app.config['MONGODB_SETTINGS'] = {
            'db': 'local',
            'host': 'datagran_db',
            'port': 27017,
            'username': 'root-datagran',
            'password': 'password-datagran'
        }

        db.init_app(app)
        self.db = db


class CmdDoc(db.Document):
    name = db.StringField()
    status = db.StringField()
    creation_date = db.DateTimeField(default=datetime.datetime.utcnow)
