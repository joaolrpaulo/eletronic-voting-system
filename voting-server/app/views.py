import time
import uuid

import sqlalchemy
from flask import abort, jsonify, request
from flask_cors import cross_origin

from app import app, config, models, validators
from app.crypto import JWT


@cross_origin()
@app.route('/register', methods = ['POST'])
def register():
    if request.headers.get('Content-Type') == 'application/json':
        if validators.has_valid_body(request.json, models.VotersDB.fields(), models.VotersDB.validators()):
            voter = models.Voter(request.json)
            try:
                voter_id = models.VotersDB.add(voter)
            except sqlalchemy.exc.IntegrityError:
                return jsonify({
                    'message': 'voter_id already exists'
                }), 409
            return jsonify({
                'message': 'voter was successfully registered',
            }), 201, {'Location': '/voters/%d' % voter_id}
        return jsonify({
            'message': 'validation failed',
            'errors': validators.get_body_errors(request.json, models.VotersDB.fields(), models.VotersDB.validators())
        }), 422
    return abort(415)


@cross_origin()
@app.route("/login", methods = ['POST'])
def login():
    if request.headers.get('Content-Type') == 'application/json':
        voter_id = request.json.get('voter_id')
        password = request.json.get('password')

        missing = []
        if not voter_id:
            missing.append('voter_id')
        if not password:
            missing.append('password')

        if not missing:
            voter = models.VotersDB.get(voter_id)
            if voter and voter.verify_password(password):
                models.TokensDB.invalidate_all(voter_id)
                token = models.Token({
                    'token': JWT(config.jwt.secret).encrypt({
                        'voter_id': voter_id,
                        'created_at': int(time.time()),
                        'uuid': uuid.uuid4().hex
                    }),
                    'voter_id': voter_id,
                    'expiration_ts': int(time.time()) + config.tokens.ttl
                })
                models.TokensDB.add(token)
                return jsonify(
                    token.to_dict()
                ), 201
            return jsonify({
                'message': 'wrong credentials'
            }), 401
        return jsonify({
            'message': 'validation failed',
            'errors': {'missing': missing}
        }), 422
    return abort(415)


@cross_origin()
@app.route("/voters/<int:voter_id>", methods = ['GET'])
def voters(voter_id):
    # TODO: Authentication Wrapper
    # TODO: Revalidate Token
    voter = models.VotersDB.get(voter_id)
    if voter:
        return jsonify(
            voter.to_dict()
        ), 200
    abort(404)


@cross_origin()
@app.route("/polls/<int:poll_id>", methods = ['GET', 'POST'])
def polls(poll_id):
    # TODO: Authentication Wrapper
    # TODO: Revalidate Token
    if request.method == 'GET':
        poll = models.PollsDB.get(poll_id)
        if poll:
            return jsonify(
                poll.to_dict()
            ), 200
        abort(404)
    # TODO: Only Admins
    if request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            if validators.has_valid_body(request.json, models.PollsDB.fields(), models.PollsDB.validators()):
                poll = models.Poll(request.json)
                poll_id = models.PollsDB.add(poll)
                return jsonify({
                    'message': 'poll was successfully registered',
                }), 201, {'Location': '/polls/%d' % poll_id}
            return jsonify({
                'message': 'validation failed',
                'errors': validators.get_body_errors(request.json, models.PollsDB.fields(), models.PollsDB.validators())
            }), 422
        return abort(415)
