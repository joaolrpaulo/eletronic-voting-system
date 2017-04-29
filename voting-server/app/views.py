import sqlalchemy
from app import app
from app import models
from flask import request, jsonify, abort


@app.route("/register", methods = ['POST'])
def register():
    if request.headers['Content-Type'] == 'application/json':
        voter = models.Voter(request.json)
        if voter.ok():
            voter.hash_password()
        else:
            print(voter.error())
        # v = request.json
        # if validator.validate_voter(v):
        #     hash = ''
        #     salt = ''
        #     try:
        #         models.Voters.add(v['voter_id'], hash, salt, v['name'], v['email'], v['address'])
        #         return jsonify({'message': 'success'})
        #     except sqlalchemy.exc.IntegrityError:
        #         return abort(409)
        # else:
        #     return abort(400)
        return jsonify({"test": "test"})
    else:
        return abort(415)


@app.route("/login", methods = ['POST'])
def login():
    if request.headers['Content-Type'] == 'application/json':
        print(request.json)
        return jsonify({'message': 'success'})
    else:
        return abort(415)


@app.route("/logout", methods = ['POST'])
def logout():
    return abort(403)
