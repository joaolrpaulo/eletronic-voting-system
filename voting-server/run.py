#!/usr/bin/python3.5

from app import app
from flask_cors import CORS

app.run(
    host = '0.0.0.0',
    port = 443,
    debug = True,
    ssl_context = ('certs/voting-server.crt', 'certs/voting-server.key')
)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)
