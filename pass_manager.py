import hashlib
from cryptography.fernet import Fernet
import time
import db_manager


# if master password = the secret key, provide access

# create key

key = Fernet.generate_key()

crypter = Fernet(key)  # create Fernet object


def add_password():
    print("---------ADD A PASSWORD--------")
    svc = input("Enter Service: ")
    user = input("Enter your username: ")
    pwd = input("Enter your password: ")

    # encode password
    pwd_en = pwd.encode()

    pwd = crypter.encrypt(pwd_en)

    db_manager.db_add(svc, user, pwd)

    # database function, insert(svc, user, pwd)


def update_password():
    print("\n")
    svc = input("Enter the service would you like to update:  ")
    # retrieve data from database/query DB for the service row
    # select from table PW_MANAGER, svc, user, pwd
    option = input(
        "Would you like to update or remove the password from this service?(1/Update, 2/Remove): ")
    if option == 1:

        db_grab(svc)
        # cur_pwd = input("Please enter the current password: ")

    # if cur_pwd = pwd.decrypted, print("correct!")
    # then execute below
    new_pwd = input("Please enter the new password: ")
    con_pwd = input("Please confirm the new password: ")
    # if new_pwd == con_pwd:
    # encode new_password
    # sql.update(pwd, con_pwd)

    # elif option == 2:
    ru_sure = input("Are you sure you want to remove this password? (Y/N): ")
    # if Y,
    # sql.delete, delete row

    # delete password/service from database
    # if N,
    # continue

    # close window

    pass


def retrieve_password():
    svc = input("Enter the service you want to retrieve the password from: ")
    #  select(svc,
    # access database, check if svc matches name of service,
    #  then display to screen
    # integrate closing functionality so window closes
    pass


def display_all():

    db_manager.db_add()

    # closing functionality


# basic functionality

# When user loads program, ask for master password

# when master password is entered, provide other options:
# THE BELOW IS IN THE pass_manager.py script


# remove a password
    # -ask for service to remove
    # -query DB for the service row
    # -ask to enter the password
    # -then ask to confirm to remove


# see list of password
    # display entire db of passwords


# while True:

#     password = input("Please entry a password: ")
#     c_password = input("Please confirm your password: ")

#     if password == c_password:
#         hashed = hashlib.md5(c_password).hexdigest()
#         print(hashed)
#         break
#     else:
#         print("The passwords do not match!")
#         continue


# TODO:
# Decide whether I want store all passwords in DB hidden by master password...
# OR decide whether I want master password, and all passwords under a layer of encryption - research how to do this

# Methods of Encryption

# Kalle takes password, encrypts it, stores in db.
# On retrival, encrypted password is retrived. No decryption process?
# decide levels of encryption

# Other guy adds password to database on selection of menu option, in add password command, he inserts the secret key into DB
# then returns a generated password

# How do secret keys keep original password form

# a salt is used for python to keep the original form?


# THINGS TO ADD:
# connect to Google Chrome API or something, download json of usernames and passwords, or usernames
