from flask import request, jsonify
from jose import jwt

from app import models, config
from app.crypto import JWT


def restricted(func):
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token and token.startswith('Bearer '):
            try:
                payload = JWT(config.jwt.secret).decrypt(token.replace('Bearer ', ''))
                voter_id = payload.get('voter_id')
                voter = models.VotersDB.get(voter_id)
                if voter and voter.role == 'admin':
                    return func(*args, **kwargs)
                return jsonify({
                    'message': 'permission denied'
                }), 403
            except (jwt.JWSError, jwt.ExpiredSignatureError) as e:
                return jsonify({
                    'message': str(e)
                }), 401
        return jsonify({
            'message': 'token not provided'
        }), 401
    return decorator


def login_required(func):
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token and token.startswith('Bearer '):
            try:
                payload = JWT(config.jwt.secret).decrypt(token.replace('Bearer ', ''))
                voter_id = payload.get('voter_id')
                voter = models.VotersDB.get(voter_id)
                if voter:
                    return func(*args, **kwargs)
                return jsonify({
                    'message': 'permission denied'
                }), 403
            except (jwt.JWSError, jwt.ExpiredSignatureError) as e:
                return jsonify({
                    'message': str(e)
                }), 401
        return jsonify({
            'message': 'token not provided'
        }), 401
    return decorator
