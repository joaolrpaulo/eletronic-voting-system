from jose import jwt

TTL = 300


class Encryption:
    def __init__(self, secret):
        self.secret = secret

    def encrypt(self, data = {}, algorithm = 'HS256'):
        return jwt.encode(data, self.secret, algorithm = algorithm)

    def decrypt(self, token = None, algorithm = ['HS256']):
        if not token:
            raise Exception('No data to decrypt.')
        return jwt.decode(token, self.secret, algorithms = algorithm)