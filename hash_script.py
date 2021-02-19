from cryptography.fernet import Fernet
import time
import hashlib
import binascii
import string


def make_password(salt, pwd):
    return hashlib.sha256(salt+pwd).hexdigest()


alphabet = string.ascii_letters + string.digits + string.punctuation

print(alphabet)
