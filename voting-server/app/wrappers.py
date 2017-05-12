from flask import session, request, jsonify

from app import models


def restricted(func):
    def decorator(*args, **kwargs):
        voter_id = session.get('voter_id')
        csrf_token = request.headers.get('X-CSRF-Token')
        if not voter_id:
            return jsonify({
                'message': 'voter is not logged in'
            }), 401
        if not csrf_token:
            return jsonify({
                'message': 'The CSRF token is missing.'
            })
        if voter_id and models.SessionsDB.get(voter_id, csrf_token):
            voter = models.VotersDB.get(voter_id)
            if voter and voter.admin:
                return func(*args, **kwargs)
            return jsonify({
                'message': 'permission denied'
            }), 403
        return jsonify({
            'message': 'The CSRF token is invalid.'
        }), 401
    return decorator


def authenticate(func):
    def decorator(*args, **kwargs):
        voter_id = session.get('voter_id')
        csrf_token = request.headers.get('X-CSRF-Token')
        if not voter_id:
            return jsonify({
                'message': 'voter is not logged in'
            }), 401
        if not csrf_token:
            return jsonify({
                'message': 'The CSRF token is missing.'
            }), 403
        if voter_id and models.SessionsDB.get(voter_id, csrf_token):
            return func(*args, **kwargs)
        return jsonify({
            'message': 'The CSRF token is invalid.'
        }), 401
    return decorator
