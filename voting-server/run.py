#!/usr/bin/python3.5

from app import app
from app import config


app.run(
    host = config.endpoint.host,
    port = config.endpoint.port,
    debug = config.debug,
    ssl_context = (config.https.crt, config.https.key)
)
