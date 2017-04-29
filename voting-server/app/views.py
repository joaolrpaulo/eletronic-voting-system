import sqlalchemy

from app import app
from app import models
from flask import abort
from flask import jsonify
from flask import request


@app.route("/register", methods = ['POST'])
def register():
    if request.headers['Content-Type'] == 'application/json':
        voter = models.Voter(request.json)
        if voter.ok():
            voter.hash_password()
            try:
                # TODO: add voter to the database
                pass
            except sqlalchemy.exc.IntegrityError:
                return abort(409)
            return jsonify({'message': 'success'})
        return jsonify(voter.error()), 400
    return abort(415)


@app.route("/login", methods = ['POST'])
def login():
    if request.headers['Content-Type'] == 'application/json':
        print(request.json)
        return jsonify({'message': 'success'})
    return abort(415)


@app.route("/logout", methods = ['POST'])
def logout():
    if request.headers['Content-Type'] == 'application/json':
        print(request.json)
        return jsonify({'message': 'success'})
    return abort(415)
