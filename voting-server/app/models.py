from app import db
from app import validators
from passlib.hash import pbkdf2_sha512


class Voter:
    def __init__(self, data):
        self.voter_id = data.get('voter_id')
        self.password = data.get('password')
        self.name = data.get('name')
        self.email = data.get('email')
        self.address = data.get('address')
        self.hash = None

    def ok(self):
        fields = [self.voter_id, self.password, self.name, self.email, self.address]
        functions = [validators.voter_id, validators.password, validators.name, validators.email, validators.address]
        return all([bool(field) for field in fields]) and all([v(f) for v, f in zip(functions, fields)])

    def error(self):
        names = ['voter_id', 'password', 'name', 'email', 'address']
        fields = [self.voter_id, self.password, self.name, self.email, self.address]
        functions = [validators.voter_id, validators.password, validators.name, validators.email, validators.address]

        missing, malformed = [], []
        for name, field, func in zip(names, fields, functions):
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
        print(self.hash)

    def verify_password(self):
        return pbkdf2_sha512.verify(self.password, self.hash)


class Voters:
    @staticmethod
    def add(voter_id, hash, salt, name, email, address):
        conn = db.connect()
        return conn.execute("INSERT INTO voters VALUES(?, ?, ?, ?, ?, ?)", [voter_id, hash, salt, name, email, address])

    @staticmethod
    def get(voter_id):
        conn = db.connect()
        return conn.execute("SELECT * FROM voters WHERE voter_id = ?", [voter_id])

    @staticmethod
    def delete(voter_id):
        conn = db.connect()
        return conn.execute("DELETE FROM voters WHERE voter_id = ?", [voter_id])
