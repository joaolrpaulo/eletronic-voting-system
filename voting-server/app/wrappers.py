from flask import session, abort, request

from app import models


def restricted(func):
    def decorator(*args, **kwargs):
        voter_id = session.get('voter_id')

        if voter_id and models.SessionsDB.exists(voter_id, request.headers.get('X-EVS-TOKEN')):
            voter = models.VotersDB.get(voter_id)
            if voter and voter.admin:
                return func(*args, **kwargs)

            return abort(403)
        return abort(401)
    return decorator


def login_required(func):
    def decorator(*args, **kwargs):
        voter_id = session.get('voter_id')

        if voter_id and models.SessionsDB.exists(voter_id, request.headers.get('X-EVS-TOKEN')):
            return func(*args, **kwargs)

        return abort(401)
    return decorator
