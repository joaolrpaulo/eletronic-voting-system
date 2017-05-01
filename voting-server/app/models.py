from passlib.hash import pbkdf2_sha512

from app import db
from app import validators


def cursor_to_json(query):
    return [dict(zip(tuple(query.keys()), data)) for data in query.cursor]


class Poll:
    def __init__(self, data):
        self.title = data.get('title')
        self.description = data.get('description')
        self.image = data.get('image')
        self.begin_ts = data.get('begin_ts')
        self.end_ts = data.get('end_ts')
        self.available_at = data.get('available_at')
        self.functions = [validators.title, validators.description, validators.image, validators.ts,  validators.ts, validators.ts]
        self.fields = [self.title, self.description, self.image, self.begin_ts, self.end_ts, self.available_at]
        self.names = ['title', 'description', 'image', 'begin_ts', 'end_ts', 'available_at']

    def ok(self):
        return all([bool(field) for field in self.fields]) and all([v(f) for v, f in zip(self.functions, self.fields)])

    def error(self):
        missing, malformed = [], []
        for name, field, func in zip(self.names, self.fields, self.functions):
            print(field)
            if field is None:
                missing.append(name)
            elif not func(field):
                malformed.append(name)
        if missing:
            return {"missing": missing}
        if malformed:
            return {"malformed": malformed}
        return {}


class Voter:
    def __init__(self, data):
        self.voter_id = data.get('voter_id')
        self.password = data.get('password')
        self.hash = data.get('hash')
        self.name = data.get('name')
        self.email = data.get('email')
        self.city = data.get('city')
        self.functions = [validators.voter_id, validators.password, validators.name, validators.email, validators.city]
        self.fields = [self.voter_id, self.password, self.name, self.email, self.city]
        self.names = ['voter_id', 'password', 'name', 'email', 'city']

    def ok(self):
        return all([bool(field) for field in self.fields]) and all([v(f) for v, f in zip(self.functions, self.fields)])

    def error(self):
        missing, malformed = [], []
        for name, field, func in zip(self.names, self.fields, self.functions):
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
        cursor = cursor_to_json(query)

        return Voter(cursor[0]) if len(cursor) else None

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
        cursor = cursor_to_json(query)

        return cursor[0] if len(cursor) else None

    @staticmethod
    def revalidate(token, expiration_ts):
        conn = db.connect()
        return conn.execute("UPDATE tokens SET expiration_ts = ? WHERE token = ?", [expiration_ts, token])

    @staticmethod
    def invalidate(token):
        conn = db.connect()
        return conn.execute("UPDATE tokens SET expiration_ts = 0 WHERE token = ?", [token])

    @staticmethod
    def invalidate_all(voter_id):
        conn = db.connect()
        return conn.execute("UPDATE tokens SET expiration_ts = 0 WHERE voter_id = ? AND expiration_ts <> 0", [voter_id])


class Polls:
    @staticmethod
    def add_poll(title, description, image, begin_ts, end_ts, available_at):
        conn = db.connect()
        with db.begin() as conn:
            conn.execute("INSERT INTO polls(title, description, image, begin_ts, end_ts, available_at) VALUES (?, ?, ?, ?, ?, ?)", [title, description, image, begin_ts, end_ts, available_at])
            return_id = conn.execute("SELECT last_insert_rowid() FROM polls").cursor.fetchone()

        return return_id

    @staticmethod
    def add_voter_to_poll(voter_id, poll_id):
        conn = db.connect()
        return conn.execute("INSERT INTO voters_polls(voter_id, poll_id) VALUES(?, ?)", [voter_id, poll_id])

    @staticmethod
    def add_items_to_poll(poll_id, title, description):
        conn = db.connect()
        return conn.execute("INSERT INTO items_polls(poll_id, title, description) VALUES(?, ?, ?)", [poll_id, title, description])

    @staticmethod
    def get_polls(token):
        conn = db.connect()
        query = conn.execute("SELECT * FROM polls WHERE id in (SELECT poll_id FROM voters_polls WHERE voter_id in (SELECT voter_id FROM tokens WHERE token = ?))", [token])
        polls = cursor_to_json(query)

        return polls if polls else None

    @staticmethod
    def get_items_poll(poll_id):
        conn = db.connect()
        query = conn.execute("SELECT * FROM items_polls WHERE poll_id = ?", [poll_id])
        items = cursor_to_json(query)

        return items if items else None
