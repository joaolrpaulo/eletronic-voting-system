from passlib.hash import pbkdf2_sha512

from app import db
from app import validators


def cursor_to_json(query, data):
    return dict(zip(tuple(query.keys()), data))


class Voter:
    def __init__(self, data):
        self.voter_id = data.get('voter_id')
        self.password = data.get('password')
        self.hash = data.get('hash')
        self.name = data.get('name')
        self.email = data.get('email')
        self.city = data.get('city')
        self.functions = [validators.voter_id, validators.password, validators.name, validators.email, validators.city]

    def ok(self):
        fields = [self.voter_id, self.password, self.name, self.email, self.city]
        return all([bool(field) for field in fields]) and all([v(f) for v, f in zip(self.functions, fields)])

    def error(self):
        names = ['voter_id', 'password', 'name', 'email', 'city']
        fields = [self.voter_id, self.password, self.name, self.email, self.city]

        missing, malformed = [], []
        for name, field, func in zip(names, fields, self.functions):
            if not field:
                missing.append(name)
            elif not func(field):
                malformed.append(name)
        if missing:
            return {"missing": missing}
        if malformed:
            return {"malformed": malformed}
        return {}

    def hash_password(self):
        self.hash = pbkdf2_sha512.encrypt(self.password, rounds=200000, salt_size=16)

    def verify_password(self, password):
        return pbkdf2_sha512.verify(password, self.hash)


class Voters:
    @staticmethod
    def add(voters):
        conn = db.connect()
        return conn.execute("INSERT INTO voters VALUES(?, ?, ?, ?, ?)",
                            [voters.voter_id, voters.hash, voters.name, voters.email, voters.city])

    @staticmethod
    def get(voter_id):
        conn = db.connect()
        query = conn.execute("SELECT * FROM voters WHERE voter_id = ?", [voter_id])

        user = query.cursor.fetchone()

        if user:
            return Voter(cursor_to_json(query, user))
        else:
            return None

    @staticmethod
    def delete(voter_id):
        conn = db.connect()
        return conn.execute("DELETE FROM voters WHERE voter_id = ?", [voter_id])


class Tokens:
    @staticmethod
    def add(voter_id, token, expiration_ts):
        conn = db.connect()
        return conn.execute("INSERT INTO tokens(voter_id, token, expiration_ts) VALUES(?, ?, ?)", [voter_id, token, expiration_ts])

    @staticmethod
    def get(token):
        conn = db.connect()
        query = conn.execute("SELECT * FROM tokens WHERE token = ?", [token])

        token_user = query.cursor.fetchone()

        if token_user:
            return cursor_to_json(query, token_user)
        else:
            return None

    @staticmethod
    def invalidate(token):
        conn = db.connect()
        return conn.execute("UPDATE tokens SET expiration_ts = 0 WHERE token = ?", [token])

    @staticmethod
    def invalidate_all(voter_id):
        conn = db.connect()
        return conn.execute("UPDATE tokens SET expiration_ts = 0 WHERE voter_id = ? AND expiration_ts <> 0", [voter_id])
