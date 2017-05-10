import sqlalchemy
from secrets import token_urlsafe

from flask import abort, jsonify, request, session
from flask_cors import cross_origin

from app import app, models, validators
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
                session.permanent = True
                _csrf_token = token_urlsafe(64)
                print(session.get('_csrf_token'))

                if session.get('voter_id') and models.SessionsDB.exists(voter_id, session.get('_csrf_token')):
                    return jsonify({
                        'message': 'voter already logged in!'
                    }), 200

                session['voter_id'] = voter.voter_id
                session['_csrf_token'] = _csrf_token
                models.SessionsDB.add(voter_id, _csrf_token)

                return jsonify({
                    'message': 'voter successfully logged in!'
                }), 200
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


@app.route("/logout", methods = ['POST'], endpoint = 'logout')
@cross_origin()
@login_required
def logout():
    if session.get('voter_id'):
        session.clear()
        return jsonify({
            'message': 'voter successfully logged out!'
        })
    return abort(401)


@app.route('/voters', methods = ['POST'], endpoint = 'create_voter')
@cross_origin()
@restricted
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
def get_single_voter(voter_id):
    voter = models.VotersDB.get(voter_id)
    if voter:
        return jsonify(
            voter.to_dict()
        ), 200
    return jsonify({
        'message': 'voter_id not found'
    }), 404


@app.route("/voters", methods = ['GET'], endpoint = 'get_all_voters')
@cross_origin()
@restricted
def get_all_voters():
    return jsonify(
        [voter.to_dict() for voter in models.VotersDB.get_all()]
    ), 200


@app.route("/voter", methods = ['GET'], endpoint = 'get_voter')
@cross_origin()
@login_required
def get_voter():
    return jsonify(
        models.VotersDB.get(session.get('voter_id')).to_dict()
    ), 200


@app.route("/polls", methods = ['POST'], endpoint = 'create_poll')
@cross_origin()
@restricted
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
    poll = models.PollsVotersDB.get_voter_poll(session.get('voter_id'), poll_id)
    if poll:
        return jsonify(
            poll.to_dict()
        ), 200
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
