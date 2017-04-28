import os

from flask import Flask


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE = os.path.join(app.root_path, 'voting-server.db'),
    SECRET_KEY = 'voting-server',
    USERNAME = 'admin',
    PASSWORD = 'admin'
))
app.config.from_json('config/config.json', silent = True)


# noinspection PyUnresolvedReferences
from app import errors, users, database
