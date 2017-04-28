from app import app, database
from flask import request, jsonify, abort

usersLoggedIn = {}


@app.route("/login/<username>", methods = ['POST'])
def login(username):
    if username not in usersLoggedIn or usersLoggedIn[username]['code'] != 1:
        database
        usersLoggedIn[username] = {
            'code': 1
        }
        return jsonify({
            'status': 'Successgully Logged In',
            'code': 1
        })
    else:
        return jsonify({
            'status': 'Already Logged In',
            'code': 0
        })


@app.route("/logout/<username>", methods=['GET', 'POST'])
def logout(username):
    if request.method == 'POST':
        if not username in usersLoggedIn:
            return jsonify({
                'status': 'User doesn\'t exist.',
                'code': 0
            })
        elif usersLoggedIn[username]['code'] == 1:
            usersLoggedIn[username]['code'] = 0

            return jsonify({
                'status': 'User succesfully logged out',
                'code': 1
            })
        else:
            return jsonify({
                'status': 'User not logged in',
                'code': 0
            })
    else:
        return abort(403)
