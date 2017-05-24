import time

from passlib.hash import pbkdf2_sha512

from app import config, db, validators


def result_to_json(result, first = False, last = False):
    json = [dict(zip(tuple(result.keys()), data)) for data in result.cursor]
    if first:
        return json[0] if len(json) > 0 else None
    if last:
        return json[-1] if len(json) > 0 else None
    return json


class Voter:
    def __init__(self, data):
        self.voter_id = data.get('voter_id')
        self.admin = data.get('admin')
        if data.get('password'):
            self.pw_hash = pbkdf2_sha512.encrypt(data.get('password'), rounds = 200000, salt_size = 16)
        else:
            self.pw_hash = data.get('pw_hash')
        self.email = data.get('email')
        self.name = data.get('name')
        self.city = data.get('city')

    def verify_password(self, password):
        return pbkdf2_sha512.verify(password, self.pw_hash)

    def to_dict(self):
        return {
            'voter_id': self.voter_id,
            'email': self.email,
            'name': self.name,
            'city': self.city
        }


class VotersDB:
    @staticmethod
    def add(voter):
        conn = db.connect()
        result = conn.execute(
            "INSERT INTO voters(voter_id, pw_hash, email, name, city, admin) VALUES(?, ?, ?, ?, ?, ?)",
            [voter.voter_id, voter.pw_hash, voter.email, voter.name, voter.city, 0]
        )
        return result.lastrowid

    @staticmethod
    def get(voter_id):
        conn = db.connect()
        result = conn.execute(
            "SELECT * FROM voters WHERE voter_id = ?",
            [voter_id]
        )
        json = result_to_json(result, first = True)
        return Voter(json) if json else None

    @staticmethod
    def get_all():
        conn = db.connect()
        result = conn.execute(
            "SELECT * FROM voters"
        )
        json = result_to_json(result)
        return [Voter(voter) for voter in json] if json else []

    @staticmethod
    def delete(voter_id):
        with db.begin() as conn:
            conn.execute(
                "DELETE FROM polls_voters WHERE voter_id = ?",
                [voter_id]
            )
            result = conn.execute(
                "DELETE FROM voters WHERE voter_id = ?",
                [voter_id]
            )
        return result.rowcount

    @staticmethod
    def fields():
        return ['voter_id', 'password', 'email', 'name', 'city']

    @staticmethod
    def validators():
        return [validators.voter_id, validators.password, validators.email, validators.name, validators.city]


class Poll:
    def __init__(self, data):
        self.poll_id = data.get('poll_id')
        self.title = data.get('title')
        self.description = data.get('description')
        self.image = data.get('image')
        self.begin_ts = data.get('begin_ts')
        self.end_ts = data.get('end_ts')
        self.available_at = data.get('available_at')

    def to_dict(self):
        return {
            'poll_id': self.poll_id,
            'title': self.title,
            'description': self.description,
            'image': self.image,
            'begin_ts': self.begin_ts,
            'end_ts': self.end_ts,
            'available_at': self.available_at,
            'items': [item.to_dict() for item in PollsItemsDB.get_poll_items(self.poll_id)]
        }


class PollsDB:
    @staticmethod
    def add(poll):
        conn = db.connect()
        result = conn.execute(
            "INSERT INTO polls(title, description, image, begin_ts, end_ts, available_at) VALUES (?, ?, ?, ?, ?, ?)",
            [poll.title, poll.description, poll.image, poll.begin_ts, poll.end_ts, poll.available_at]
        )
        return result.lastrowid

    @staticmethod
    def get(poll_id):
        conn = db.connect()
        result = conn.execute(
            "SELECT * FROM polls WHERE poll_id = ?",
            [poll_id]
        )
        json = result_to_json(result, first = True)
        return Poll(json) if json else None

    @staticmethod
    def get_all():
        conn = db.connect()
        result = conn.execute(
            "SELECT * FROM polls"
        )
        json = result_to_json(result)
        return [Poll(poll) for poll in json] if json else []

    @staticmethod
    def delete(poll_id):
        with db.begin() as conn:
            conn.execute(
                "DELETE FROM polls_items WHERE poll_id = ?",
                [poll_id]
            )
            conn.execute(
                "DELETE FROM polls_voters WHERE poll_id = ?",
                [poll_id]
            )
            result = conn.execute(
                "DELETE FROM polls WHERE poll_id = ?",
                [poll_id]
            )
        return result.rowcount

    @staticmethod
    def vote(poll_id, voter_id, message):
        with db.begin() as conn:
            conn.execute(
                "UPDATE polls_voters SET voted = 1 WHERE poll_id = ? AND voter_id = ?",
                [poll_id, voter_id]
            )
            result = conn.execute(
                "INSERT INTO messages(poll_id, message) VALUES(?, ?)",
                [poll_id, message]
            )
        return result.rowcount

    @staticmethod
    def fields():
        return ['title', 'description', 'image', 'begin_ts', 'end_ts', 'available_at']

    @staticmethod
    def validators():
        return [validators.title, validators.description, validators.image, validators.ts, validators.ts, validators.ts]


class PollItem:
    def __init__(self, data):
        self.item_id = data.get('item_id')
        self.poll_id = data.get('poll_id')
        self.title = data.get('title')
        self.description = data.get('description')

    def to_dict(self):
        return {
            'item_id': self.item_id,
            'title': self.title,
            'description': self.description,
            'item_identifiers': [item.to_dict() for item in ItemIdentifiers.get(self.item_id)]
        }


class PollsItemsDB:
    @staticmethod
    def add(item):
        conn = db.connect()
        result = conn.execute(
            "INSERT INTO polls_items(poll_id, title, description) SELECT ?, ?, ? FROM polls WHERE poll_id = ?",
            [item.poll_id, item.title, item.description, item.poll_id]
        )
        return result.lastrowid

    @staticmethod
    def get(item_id):
        conn = db.connect()
        result = conn.execute(
            "SELECT * FROM polls_items WHERE item_id = ?",
            [item_id]
        )
        json = result_to_json(result, first = True)
        return PollItem(json) if json else None

    @staticmethod
    def get_poll(item_id):
        conn = db.connect()
        result = conn.execute(
            "SELECT * FROM polls WHERE poll_id IN (SELECT poll_id FROM polls_items WHERE item_id = ?)",
            [item_id]
        )
        json = result_to_json(result, first = True)
        return Poll(json) if json else None

    @staticmethod
    def get_poll_items(poll_id):
        conn = db.connect()
        result = conn.execute(
            "SELECT * FROM polls_items WHERE poll_id = ?",
            [poll_id]
        )
        json = result_to_json(result)
        return [PollItem(item) for item in json] if json else []

    @staticmethod
    def get_all():
        conn = db.connect()
        result = conn.execute(
            "SELECT * FROM polls_items"
        )
        json = result_to_json(result)
        return [PollItem(item) for item in json] if json else []

    @staticmethod
    def delete(item_id):
        conn = db.connect()
        result = conn.execute(
            "DELETE FROM polls_items WHERE item_id = ?",
            [item_id]
        )
        return result.rowcount

    @staticmethod
    def delete_poll_items(poll_id):
        conn = db.connect()
        result = conn.execute(
            "DELETE FROM polls_items WHERE poll_id = ?",
            [poll_id]
        )
        return result.rowcount

    @staticmethod
    def fields():
        return ['title', 'description']

    @staticmethod
    def validators():
        return [validators.title, validators.description]


class PollsVotersDB:
    @staticmethod
    def add(poll_id, voter_id):
        conn = db.connect()
        result = conn.execute(
            "INSERT INTO polls_voters(poll_id, voter_id) SELECT ?, ? FROM polls, voters \
            WHERE poll_id = ? AND voter_id = ?",
            [poll_id, voter_id, poll_id, voter_id]
        )
        return result.lastrowid

    @staticmethod
    def get_voter_poll(voter_id, poll_id):
        conn = db.connect()
        result = conn.execute(
            "SELECT * FROM polls WHERE poll_id IN \
            (SELECT poll_id FROM polls_voters WHERE voter_id = ? AND poll_id = ?)",
            [voter_id, poll_id]
        )
        json = result_to_json(result, first = True)
        return Poll(json) if json else None

    @staticmethod
    def get_voter_polls(voter_id, all_polls = False):
        conn = db.connect()
        if all_polls:
            result = conn.execute(
                "SELECT * FROM polls WHERE poll_id IN (SELECT poll_id FROM polls_voters WHERE voter_id = ?)",
                [voter_id]
            )
        else:
            time_now = int(time.time())
            result = conn.execute(
                "SELECT * FROM polls WHERE poll_id IN (SELECT poll_id FROM polls_voters WHERE voter_id = ?) \
                AND begin_ts <= ? AND end_ts > ?",
                [voter_id, time_now, time_now]
            )
        json = result_to_json(result)
        return [Poll(poll) for poll in json] if json else []

    @staticmethod
    def can_vote(poll_id, voter_id):
        conn = db.connect()
        result = conn.execute(
            "SELECT * FROM polls_voters WHERE poll_id = ? AND voter_id = ? AND voted = 0",
            [poll_id, voter_id]
        )
        json = result_to_json(result, first = True)
        return json

    @staticmethod
    def delete(poll_id, voter_id):
        conn = db.connect()
        result = conn.execute(
            "DELETE FROM polls_voters WHERE poll_id = ? AND voter_id = ?",
            [poll_id, voter_id]
        )
        return result.rowcount

    @staticmethod
    def delete_poll_voters(poll_id):
        conn = db.connect()
        result = conn.execute(
            "DELETE FROM polls_voters WHERE poll_id = ?",
            [poll_id]
        )
        return result.rowcount


class Token:
    def __init__(self, data):
        self.voter_id = data.get('voter_id')
        self.token = data.get('token')
        self.expiration_ts = data.get('expiration_ts')


class TokensDB:
    @staticmethod
    def add(token):
        conn = db.connect()
        result = conn.execute(
            "INSERT OR REPLACE INTO tokens(voter_id, token, expiration_ts) VALUES(?, ?, ?)",
            [token.voter_id, token.token, int(time.time()) + config.sessions.ttl]
        )
        return result.rowcount

    @staticmethod
    def check(token):
        conn = db.connect()
        result = conn.execute(
            "SELECT * FROM tokens WHERE token = ? AND expiration_ts > ?",
            [token, int(time.time())]
        )
        json = result_to_json(result, first = True)
        return Token(json) if json else None

    @staticmethod
    def update(token):
        conn = db.connect()
        result = conn.execute(
            "UPDATE tokens SET expiration_ts = ? WHERE token = ?",
            [int(time.time()) + config.sessions.ttl, token]
        )
        return result.rowcount

    @staticmethod
    def remove(voter_id):
        conn = db.connect()
        result = conn.execute(
            "DELETE FROM tokens WHERE voter_id = ?",
            [voter_id]
        )
        return result.rowcount


class Vote:
    def __init__(self, json):
        self.item = json.get('item')
        self.identifier = json.get('identifier')

    def to_dict(self):
        return self.identifier


class ItemIdentifiers:
    @staticmethod
    def add(vote):
        conn = db.connect()
        result = conn.execute(
            "INSERT INTO item_votes(item, identifier) VALUES(?, ?)",
            [vote.item, vote.identifier]
        )
        return result.rowcount

    @staticmethod
    def get(item):
        conn = db.connect()
        result = conn.execute(
            "SELECT * FROM item_votes WHERE item = ?",
            [item]
        )
        items = result_to_json(result)
        return [Vote(item) for item in items]
