#!/usr/bin/python3.5

from app import app


app.run(host = '0.0.0.0', port = 8000, debug = True,
        ssl_context = ('certs/voting-server.crt', 'certs/voting-server.key'))
