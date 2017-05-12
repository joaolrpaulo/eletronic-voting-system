import base64
import os


def token_urlsafe(nbytes = 32):
    token = os.urandom(nbytes)
    return base64.urlsafe_b64encode(token).rstrip(b'=').decode('ascii')
