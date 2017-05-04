import time

import sqlalchemy
from flask import abort, jsonify, request
from flask_cors import cross_origin

from app import app, config, models, validators
from app.crypto import JWT
from app.wrappers import login_required, restricted


@app.route("/login", methods = ['POST'])
@cross_origin()
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
                return jsonify({
                    'token': JWT(config.jwt.secret).encrypt({
                        'voter_id': voter_id,
                        'iat': int(time.time()),
                        'exp': int(time.time()) + config.tokens.ttl
                    }),
                    'expiration_ts': int(time.time())
                }), 201
            return jsonify({
                'message': 'wrong credentials'
            }), 401
        return jsonify({
            'message': 'validation failed',
            'errors': {
                'missing': missing
            }
        }), 422
    return abort(415)


@app.route('/voters', methods = ['POST'], endpoint = 'create_voter')
@cross_origin()
@restricted
@login_required
def create_voter():
    if request.headers.get('Content-Type') == 'application/json':
        if validators.has_valid_body(request.json, models.VotersDB.fields(), models.VotersDB.validators()):
            voter = models.Voter(request.json)
            try:
                voter_id = models.VotersDB.add(voter)
            except sqlalchemy.exc.IntegrityError:
                return {
                    'message': 'voter_id already exists'
                }, 409
            return {
                'message': 'voter was successfully registered',
            }, 201, {'Location': '/voters/%d' % voter_id}
        return {
            'message': 'validation failed',
            'errors': validators.get_body_errors(request.json, models.VotersDB.fields(), models.VotersDB.validators())
        }, 422
    return abort(415)


@app.route("/voters/<int:voter_id>", methods = ['GET'], endpoint = 'get_single_voter')
@cross_origin()
@restricted
@login_required
def get_single_voter(voter_id):
    voter = models.VotersDB.get(voter_id)
    if voter:
        return voter.to_dict(), 200
    return {
        'message': 'voter_id not found'
    }, 404


@app.route("/voters", methods = ['GET'], endpoint = 'get_voter')
@cross_origin()
@login_required
def get_voter():
    token = request.headers.get('Authorization')
    if token and token.startswith('Bearer '):
        token = token.replace('Bearer ', '')
        voter_id = JWT(config.jwt.secret).decrypt(token).get('voter_id')

        return models.VotersDB.get(voter_id).to_dict(), 200


@app.route("/polls", methods = ['POST'], endpoint = 'create_poll')
@cross_origin()
@restricted
@login_required
def create_poll():
    if request.headers.get('Content-Type') == 'application/json':
        if validators.has_valid_body(request.json, models.PollsDB.fields(), models.PollsDB.validators()):
            poll = models.Poll(request.json)
            poll_id = models.PollsDB.add(poll)
            return {
                'message': 'poll was successfully registered',
            }, 201, {'Location': '/polls/%d' % poll_id}
        return {
            'message': 'validation failed',
            'errors': validators.get_body_errors(request.json, models.PollsDB.fields(), models.PollsDB.validators())
        }, 422
    return {
        'message': 'content-type not supported'
    }, 415


@app.route("/polls/<int:poll_id>", methods = ['GET'], endpoint = 'get_poll')
@cross_origin()
@login_required
def get_poll(poll_id):
    poll = models.PollsDB.get(poll_id)
    if poll:
        return poll.to_dict(), 200
    return {
        'message': 'poll_id not found'
    }, 404


@app.route("/polls", methods = ['GET'], endpoint = 'get_all_polls')
@cross_origin()
@login_required
def get_all_polls():
    polls = models.PollsDB.get_all()
    if polls:
        return [poll.to_dict() for poll in polls], 200
    return {
        'message': 'no polls available'
    }, 404
