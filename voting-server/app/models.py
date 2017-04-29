from app import db
from app import validators
from passlib.hash import pbkdf2_sha512


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
        self.hash = pbkdf2_sha512.encrypt(self.password, rounds = 200000, salt_size = 16)

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
            return Voter(dict(zip(tuple(query.keys()), user)))
        else:
            return None

    @staticmethod
    def delete(voter_id):
        conn = db.connect()
        return conn.execute("DELETE FROM voters WHERE voter_id = ?", [voter_id])
