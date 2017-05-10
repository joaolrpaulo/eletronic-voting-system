#!/usr/bin/python3.5

from app import app, config

app.run(
    host = config.endpoint.host,
    port = config.endpoint.port,
    debug = config.debug,
    ssl_context = (config.https.crt, config.https.key)
)
