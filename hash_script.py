import hashlib

import string
import secrets
# secrets is used for generating cryptographically strong random numbers for managing such such as passwords, etc.


our_list = [x for x in range(11)]

# variable to hold the alphabet

alphabet = string.ascii_letters + string.digits + string.punctuation

# print(alphabet)

password = ''.join(secrets.choice(alphabet) for i in range(8))

print(password)

# print(password)

m = hashlib.sha256()
m.update(b"hello")

print(m)

# any entered password must be 'encoded' before we hash it
# look up how to encode a string

# Might not need to use hashlib, cryptography library may do own encryption

# Do I want database to store string password or encrypted password?
# - Google
# Do I need to encrypt every password, or just encrypt one master password

# does encryption take place, then variable sent to DB?
