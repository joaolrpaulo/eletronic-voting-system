from flask import Flask, request
import json

app = Flask(__name__)

usersLoggedIn = {}

def defaultMessage():
    return json.dumps({
        'message': 'This is not what you are expecting hum?'
    })


@app.route("/login/<username>", methods=['GET', 'POST'])
def login(username):
    if request.method == 'POST':
        if not username in usersLoggedIn or usersLoggedIn[username]['code'] != 1:
            usersLoggedIn[username] = {
                'code': 1
            }

            return json.dumps({
                'status': 'Successgully Logged In',
                'code': 1
            })
        else:
            return json.dumps({
                'status': 'Already Logged In',
                'code': 0
            })
    else:
        return defaultMessage()

@app.route("/logout/<username>", methods=['GET', 'POST'])
def logout(username):
    if request.method == 'POST':
        if not username in usersLoggedIn:
            return json.dumps({
                'status': 'User doesn\'t exist.',
                'code': 0
            })
        elif usersLoggedIn[username]['code'] == 1:
            usersLoggedIn[username]['code'] = 0

            return json.dumps({
                'status': 'User succesfully logged out',
                'code': 1
            })
        else:
            return json.dumps({
                'status': 'User not logged in',
                'code': 0
            })
    else:
        return defaultMessage()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000')
