from app import app
from flask import jsonify
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions


def json_error(error):
    response = jsonify(message=str(error))
    response.status_code = error.code if isinstance(error, HTTPException) else 500
    return response

for code in default_exceptions.keys():
    app.register_error_handler(code, json_error)
