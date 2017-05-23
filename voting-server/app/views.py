import sqlalchemy
import json

from flask import abort, jsonify, request

from app import app, models, secrets, validators, rsa_utils
from app.wrappers import authenticate, restricted


@app.route('/login', methods = ['POST'])
def login():
    if request.headers.get('Content-Type') == 'application/json':
        voter_id = request.json.get('voter_id')
        password = request.json.get('password')

        if validators.has_valid_body(request.json, models.VotersDB.fields()[:2], models.VotersDB.validators()[:2]):
            voter = models.VotersDB.get(voter_id)
            if voter and voter.verify_password(password):
                token = models.Token({
                    'voter_id': voter_id,
                    'token': secrets.token_urlsafe(64)
                })
                models.TokensDB.add(token)
                return jsonify({
                    'message': 'voter successfully logged in',
                    'token': token.token
                }), 200
            return jsonify({
                'message': 'wrong credentials'
            }), 401
        return jsonify({
            'message': 'validation failed',
            'errors': validators.get_body_errors(request.json, models.VotersDB.fields()[:2], models.VotersDB.validators()[:2])
        }), 422
    return abort(415)


@app.route('/logout', methods = ['POST'], endpoint = 'logout')
@authenticate
def logout(token_voter_id):
    models.TokensDB.remove(token_voter_id)
    return jsonify({
        'message': 'voter successfully logged out'
    }), 200


@app.route('/voters', methods = ['POST'], endpoint = 'create_voter')
@restricted
def create_voter(token_voter_id):
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


@app.route('/voters/<int:voter_id>', methods = ['GET'], endpoint = 'get_voter')
@restricted
def get_voter(token_voter_id, voter_id):
    voter = models.VotersDB.get(voter_id)
    if voter:
        return jsonify(
            voter.to_dict()
        ), 200
    return jsonify({
        'message': 'voter_id not found'
    }), 404


@app.route('/voters', methods = ['GET'], endpoint = 'get_all_voters')
@restricted
def get_all_voters(token_voter_id):
    return jsonify(
        [voter.to_dict() for voter in models.VotersDB.get_all()]
    ), 200


@app.route('/voter', methods = ['GET'], endpoint = 'get_authenticated_voter')
@authenticate
def get_authenticated_voter(token_voter_id):
    return jsonify(
        models.VotersDB.get(token_voter_id).to_dict()
    ), 200


@app.route('/polls', methods = ['POST'], endpoint = 'create_poll')
@restricted
def create_poll(token_voter_id):
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


@app.route('/polls/<int:poll_id>', methods = ['GET'], endpoint = 'get_poll')
@authenticate
def get_poll(token_voter_id, poll_id):
    poll = models.PollsVotersDB.get_voter_poll(token_voter_id, poll_id)
    if poll:
        return jsonify(
            poll.to_dict()
        ), 200
    return jsonify({
        'message': 'poll_id not found'
    }), 404


@app.route('/polls', methods = ['GET'], endpoint = 'get_all_polls')
@authenticate
def get_all_polls(token_voter_id):
    return jsonify(
        [poll.to_dict() for poll in models.PollsVotersDB.get_voter_polls(token_voter_id, all_polls = True)]
    ), 200


@app.route('/vote/<int:poll_id>', methods = ['POST'], endpoint = 'make_vote')
@authenticate
def make_vote(token_voter_id, poll_id):
    if request.headers.get('Content-Type') == 'application/json':
        message = request.json.get('message')
        vote = rsa_utils.decrypt(message)
        vote = models.Vote(json.loads(vote))
        poll = models.PollsVotersDB.get_voter_poll(token_voter_id, poll_id)

        if poll:
            if models.PollsVotersDB.can_vote(poll.poll_id, token_voter_id):
                models.PollsDB.vote(poll.poll_id, token_voter_id)
                models.ItemIdentifiers.add(vote)
                return jsonify({
                    'message': 'vote registered'
                }), 200
            return jsonify({
                'message': 'already voted in this poll!'
            }), 406
        return abort(401)
    return abort(415)
