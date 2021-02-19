# generate a secret key master password:
from cryptography.fernet import Fernet
import time
import hashlib
import binascii

def make_password(salt, pwd):
    return hashlib.sha256(salt+pwd).hexdigest()

# encrypt password

with open("our_pass.txt", "wb") as f:
    f.write(new_pw.encode())

print("Your encrypted password is: " + str(new_pw) +
      "\n" + "and has been added to the database." + "\n" + "The original password is: " + pw)


def view_pw():

    while True:
        # ask for password
        retrieve = input("Want password?: ")

        if retrieve != "y":
            break
        else:
            f = open("our_pass.txt", "rb")
            for line in f:
                the_pwd = line

    return the_pwd


result = view_pw()

print(type(result))
