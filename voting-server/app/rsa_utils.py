import sys
import base64

from Crypto.PublicKey import RSA

from app import configs

# Import configs
config = configs.parser(sys.argv[1])

# Import Private key for content decrypting
with open(config.rsa.privkey, mode = 'rb') as privatefile:
    keydata = privatefile.read()
privkey = RSA.importKey(keydata)

def decrypt(message):
    b64_content = base64.b64decode(message)
    uncrypted = privkey.decrypt(b64_content)
    return remove_padding(uncrypted.decode("utf-8", "backslashreplace"))

def remove_padding(message):
    return '{' + message.split('{')[-1]

