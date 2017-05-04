from flask import request, jsonify
from jose import jwt

from app import models, config
from app.crypto import JWT
import time


def restricted(func):
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token and token.startswith('Bearer '):
            try:
                payload = JWT(config.jwt.secret).decrypt(token.replace('Bearer ', ''))
                voter_id = payload.get('voter_id')
                voter = models.VotersDB.get(voter_id)
                if voter and voter.admin:
                    return func(*args, **kwargs)
                return jsonify({
                    'message': 'permission denied'
                }), 403
            except (jwt.JWSError, jwt.ExpiredSignatureError) as e:
                return jsonify({
                    'message': str(e).lower()
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
                token = token.replace('Bearer ', '')
                payload = JWT(config.jwt.secret).decrypt(token)
                voter_id = payload.get('voter_id')
                voter = models.VotersDB.get(voter_id)

                if models.Blacklist.get(token):
                    return jsonify({
                        'message': 'token is not valid'
                    }), 401
                else:
                    models.Blacklist.add(token, payload.get('exp'))

                if voter:
                    json, status_code, *headers = func(*args, **kwargs)
                    time_now = int(time.time())

                    json['token'] = JWT(config.jwt.secret).encrypt({
                        'voter_id': voter_id,
                        'iat': time_now,
                        'exp': time_now + config.tokens.ttl
                    })

                    if headers:
                        return jsonify(json), status_code, headers[0]
                    return jsonify(json), status_code
                return jsonify({
                    'message': 'permission denied'
                }), 403
            except (jwt.JWSError, jwt.ExpiredSignatureError) as e:
                return jsonify({
                    'message': str(e).lower()
                }), 401
        return jsonify({
            'message': 'token not provided'
        }), 401
    return decorator
