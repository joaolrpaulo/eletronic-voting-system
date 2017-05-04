from flask import request, jsonify

from app import models, config
from app.crypto import JWT


def authorization(func):
    def authorize(*args, **kwargs):
        token = request.headers.get('Authorization').split('Bearer ')[1]
        token_decrypted = JWT(config.jwt.secret).decrypt(token)
        voter_id = token_decrypted.get('voter_id')

        if voter_id is None:
            return jsonify(token_decrypted), 401

        role = models.VotersDB().get(voter_id).role
        path = request.path.split('/')[1][:-1]

        if role != 'admin' and request.method == 'POST':
            return jsonify({
                'message': 'No permissions to create a new %s' % path
            }), 401
        return func(*args, **kwargs)
    return authorize


def authentication(func):
    def authenticate(*args, **kwargs):
        token = request.headers.get('Authorization').split('Bearer ')[1]
        token_decrypted = JWT(config.jwt.secret).decrypt(token)
        voter_id = token_decrypted.get('voter_id')

        if voter_id is None:
            return jsonify(token_decrypted), 401

        voter = models.VotersDB().get(voter_id)

        if not voter:
            return jsonify({
                'message': 'No such user found, please try another way to break the system.'
            }), 401
        return func(*args, **kwargs)
    return authenticate
