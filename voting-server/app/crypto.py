from jose import jwt


class JWT:
    def __init__(self, secret):
        with open(secret, mode = 'r') as f:
            self.secret = f.read()

    def encrypt(self, data, algorithm = 'HS256'):
        return jwt.encode(data, self.secret, algorithm = algorithm)

    def decrypt(self, token, algorithm = ['HS256']):
        try:
            return jwt.decode(token, self.secret, algorithms = algorithm)
        except Exception as e:
            return {
                'message': str(e)
            }
