import sqlalchemy
import time

from app import app, secretContext
from app import models
from app.crypto import Encryption, TTL
from flask import abort
from flask import jsonify
from flask import request
from flask_cors import cross_origin


@app.route("/register", methods=['POST'])
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


@app.route("/login", methods=['POST'])
@cross_origin()
def login():
    if request.headers['Content-Type'] == 'application/json':
        voter_id = request.json.get('voter_id')
        voter_password = request.json.get('password')

        if voter_id and voter_password:
            voter = models.Voters.get(voter_id)
            if voter and voter.verify_password(voter_password):
                # invalidate all previous tokens from the requested user
                models.Tokens.invalidate_all(voter_id)

                time_now = int(time.time())
                jwt = Encryption(secretContext)

                token = jwt.encrypt({
                    'voter_id': voter_id,
                    'expiration_ts': time_now + TTL
                })

                models.Tokens.add(voter_id, token, time_now + TTL)

                return jsonify({
                    'token' : token
                })

        if voter:
            return abort(401)
        else:
            return abort(404)

    return abort(415)


@app.route("/logout", methods=['POST'])
@cross_origin()
def logout():
    if request.headers['Content-Type'] == 'application/json':
        token = request.json.get('token')
        token_db = models.Tokens.get(token)

        if token_db:
            if token_db['expiration_ts'] <= int(time.time()):
                models.Tokens.invalidate(token)

            if token_db['expiration_ts'] == 0:
                return jsonify({'message': 'token already expired'})

            models.Tokens.invalidate(token)
            return jsonify({'message': 'success'})
        else:
            return abort(404)

    return abort(415)


@app.route("/user", methods=['POST'])
@cross_origin()
def user():
    if request.headers['Content-Type'] == 'application/json':
        token = request.json.get('token')
        token_db = models.Tokens.get(token)

        if token_db:
            if token_db['expiration_ts'] <= int(time.time()) or token_db['expiration_ts'] == 0:
                return abort(401)

            voter_id = token_db['voter_id']
            user = models.Voters.get(voter_id)

            return jsonify({
                'voter_id': user.voter_id,
                'name': user.name,
                'email': user.email,
                'city': user.city
            })
        else:
            return abort(404)
