import sqlalchemy

from app import app
from app import models
from app.crypto import Encryption
from flask import abort
from flask import jsonify
from flask import request
from flask_cors import cross_origin


@app.route("/register", methods = ['POST'])
@cross_origin()
def register():
    if request.headers['Content-Type'] == 'application/json':
        voter = models.Voter(request.json)
        if voter.ok():
            voter.hash_password()
            try:
                models.Voters.add(voter)
            except sqlalchemy.exc.IntegrityError:
                return abort(409)
            return jsonify({'message': 'success'})
        return jsonify(voter.error()), 400
    return abort(415)


@app.route("/login", methods = ['POST'])
@cross_origin()
def login():
    if request.headers['Content-Type'] == 'application/json':
        voter_id = request.json.get('voter_id')
        voter_password = request.json.get('password')

        if voter_id and voter_password:
            voter = models.Voters.get(voter_id)
            if voter and voter.verify_password(voter_password):
                # TODO: Generate Token
                e = Encryption('secretToken')

                return jsonify({'token': e.encrypt({'voter_id': voter_id})})

        if voter:
            return abort(401)
        else:
            return abort(404)
    return abort(415)


@app.route("/logout", methods = ['POST'])
@cross_origin()
def logout():
    if request.headers['Content-Type'] == 'application/json':
        print(request.json)
        return jsonify({'message': 'success'})
    return abort(415)
