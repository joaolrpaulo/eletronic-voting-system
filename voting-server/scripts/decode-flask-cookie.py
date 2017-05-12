import hashlib
import pprint
import sys

from flask.sessions import TaggedJSONSerializer
from itsdangerous import URLSafeTimedSerializer


def decode_flask_cookie(secret_key, cookie_str):
    salt = 'cookie-session'
    serializer = TaggedJSONSerializer()
    signer_kwargs = {
        'key_derivation': 'hmac',
        'digest_method': hashlib.sha1
    }
    s = URLSafeTimedSerializer(secret_key, salt = salt, serializer = serializer, signer_kwargs = signer_kwargs)
    return s.loads(cookie_str)


print()
with open(sys.argv[1]) as f:
    secret_key = f.read()
cookie_str = input('Paste Cookie String:\n\n')

print()
pp = pprint.PrettyPrinter()
pp.pprint(decode_flask_cookie(secret_key, cookie_str))
