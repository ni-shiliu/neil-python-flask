from models.mysql_db import db
from neil_app import NeilApp


def init_app(app: NeilApp):
    db.init_app(app)
    