from flask import jsonify
from werkzeug.exceptions import default_exceptions, HTTPException

from app import app


def json_error(error):
    response = jsonify(message = str(error))
    response.status_code = error.code if isinstance(error, HTTPException) else 500
    return response

for code in default_exceptions.keys():
    app.register_error_handler(code, json_error)
# app.register_error_handler(Exception, json_error)
