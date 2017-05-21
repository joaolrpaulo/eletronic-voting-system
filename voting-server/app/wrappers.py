from flask import request, jsonify

from app import models


def restricted(func):
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({
                'message': 'The authorization token is missing.'
            }), 401
        token = models.TokensDB.check(token)
        if token:
            voter = models.VotersDB.get(token.voter_id)
            if voter and voter.admin:
                models.TokensDB.update(token.token)
                return func(token_voter_id=token.voter_id, *args, **kwargs)
            return jsonify({
                'message': 'permission denied'
            }), 403
        return jsonify({
            'message': 'The authorization token is invalid.'
        }), 401
    return decorator


def authenticate(func):
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({
                'message': 'The authorization token is missing.'
            }), 401
        token = models.TokensDB.check(token)
        if token:
            models.TokensDB.update(token.token)
            return func(token_voter_id=token.voter_id, *args, **kwargs)
        return jsonify({
            'message': 'The authorization token is invalid.'
        }), 401
    return decorator
