import sqlite3
import sys

from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine

from app import configs

# Parse app configs
config = configs.parser(sys.argv[1])


# Initialize the app
app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
# app.config['SESSION_COOKIE_SECURE'] = True
# app.config['PERMANENT_SESSION_LIFETIME'] = config.sessions.ttl
with open(config.sessions.secret, mode = 'r') as secret_key:
    app.config['SECRET_KEY'] = secret_key.read()

cors = CORS(app)

# Connect to database
db = create_engine('sqlite:///' + config.database.location)

# Setup database
with open(config.database.schema, mode = 'r') as schema, sqlite3.connect(config.database.location) as conn:
    cursor = conn.cursor()
    cursor.executescript(schema.read())

# noinspection PyUnresolvedReferences
from app import errors
# noinspection PyUnresolvedReferences
from app import views
# noinspection PyUnresolvedReferences
from app import schedulers

@app.before_first_request
def start_threads():
    schedulers.scheduler.start()
