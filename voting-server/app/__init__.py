from flask import Flask
from sqlalchemy import create_engine


app = Flask(__name__)
db = create_engine('sqlite:///database/voting-server.db')
with open('database/schema.sql', mode = 'r') as schema, db.begin() as conn:
    conn.execute(schema.read())


# noinspection PyUnresolvedReferences
from app import errors
from app import views
