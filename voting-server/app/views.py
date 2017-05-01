import time

import sqlalchemy
from flask import abort
from flask import jsonify
from flask import request
from flask_cors import cross_origin

from app import app, config
from app import models
from app.crypto import Encryption


@app.route("/register", methods=['POST'])
@cross_origin()
def register():
    if request.headers.get('Content-Type') == 'application/json':
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
    if request.headers.get('Content-Type') == 'application/json':
        voter_id = request.json.get('voter_id')
        voter_password = request.json.get('password')

        if voter_id and voter_password:
            voter = models.Voters.get(voter_id)
            if voter and voter.verify_password(voter_password):
                # invalidate all previous tokens from the requested user
                models.Tokens.invalidate_all(voter_id)

                time_now = int(time.time())
                jwt = Encryption(config.jwt.secret)

                token = jwt.encrypt({
                    'voter_id': voter_id,
                    'expiration_ts': time_now + config.tokens.ttl
                })

                models.Tokens.add(voter_id, token,
                                  time_now + config.tokens.ttl)

                return jsonify({
                    'token': token
                })

            if voter:
                return abort(401)

            return abort(404)

        return abort(400)

    return abort(415)


@app.route("/logout", methods=['POST'])
@cross_origin()
def logout():
    has_auth = request.headers.get('Authorization')
    if has_auth and has_auth.startswith('Bearer '):
        token = has_auth.split('Bearer ')[1]
        token_db = models.Tokens.get(token)

        if token_db:
            if token_db['expiration_ts'] <= int(time.time()):
                models.Tokens.invalidate(token)

            if token_db['expiration_ts'] == 0:
                return jsonify({'message': 'token already expired'})

            models.Tokens.invalidate(token)
            return jsonify({'message': 'success'})

        return abort(404)

    return abort(415)


@app.route("/user", methods=['GET'])
@cross_origin()
def user():
    has_auth = request.headers.get('Authorization')
    if has_auth and has_auth.startswith('Bearer '):
        token = has_auth.split('Bearer ')[1]
        token_db = models.Tokens.get(token)

        if token_db:
            time_now = int(time.time())
            if token_db.get('expiration_ts') <= time_now or\
               token_db.get('expiration_ts') == 0:

                return abort(401)

            voter_id = token_db['voter_id']
            user = models.Voters.get(voter_id)
            models.Tokens.revalidate(token, time_now + config.tokens.ttl)

            return jsonify({
                'voter_id': user.voter_id,
                'name': user.name,
                'email': user.email,
                'city': user.city
            })

        return abort(404)

    return abort(400)


@app.route("/polls", methods=['GET', 'POST'])
@cross_origin()
def polls():
    has_auth = request.headers.get('Authorization')
    if has_auth and has_auth.startswith('Bearer '):
        token = has_auth.split('Bearer ')[1]
        time_now = int(time.time())
        models.Tokens.revalidate(token, time_now + config.tokens.ttl)

        if request.method == 'POST':
            if request.headers.get('Content-Type') == 'application/json':

                poll = models.Poll(request.json)

                if poll.ok():
                    poll_id = models.Polls.add_poll(poll.title,
                                                    poll.description,
                                                    poll.image,
                                                    poll.begin_ts,
                                                    poll.end_ts,
                                                    poll.available_at)[0]

                    return jsonify({'poll_id': poll_id})

                return jsonify(poll.error()), 400

            return abort(415)

        return jsonify(models.Polls.get_polls(token))

    return abort(400)
