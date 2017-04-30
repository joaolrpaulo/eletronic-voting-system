from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine


# Initialize the app
app = Flask(__name__)

# Remove sorted objects
app.config['JSON_SORT_KEYS'] = False

# CORS support
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)


# Connect to database
db = create_engine('sqlite:///database/voting-server.db')

# Setup voters table
with open('database/voters.sql', mode = 'r') as schema, db.begin() as conn:
    conn.execute(schema.read())

# Setup tokens table
with open('database/tokens.sql', mode = 'r') as schema, db.begin() as conn:
    conn.execute(schema.read())


# Fetch JWT secret
with open('certs/secret.jwt', mode = 'r') as secret:
    jwt_secret = secret.read()


# noinspection PyUnresolvedReferences
from app import errors
# noinspection PyUnresolvedReferences
from app import views
