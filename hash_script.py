import time
import hashlib
import string


def make_password(salt, pwd):
    return hashlib.sha256(salt+pwd).hexdigest()
