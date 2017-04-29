from flask import Flask
from sqlalchemy import create_engine
from flask_cors import CORS


# Initialize the App
app = Flask(__name__)
# CORS Support
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

# Connects to DB
db = create_engine('sqlite:///database/voting-server.db')

# Initialize Voters table
with open('database/voters.sql', mode = 'r') as schema, db.begin() as conn:
    conn.execute(schema.read())

# Initialize Tokens table
with open('database/tokens.sql', mode='r') as schema, db.begin() as conn:
    conn.execute(schema.read())

secretContext = open('certs/secret.jwt').read()

# noinspection PyUnresolvedReferences
from app import errors
from app import views
