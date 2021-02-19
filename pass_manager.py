import hashlib
from cryptography.fernet import Fernet
import time
import db_manager
import test
import hash_script


# if master password = the secret key, provide access

# create key

key = Fernet.generate_key()

crypter = Fernet(key)  # create Fernet object


def add_password():
    print("---------ADD A PASSWORD--------")
    svc = input("Enter Service: ")
    user = input("Enter your username: ")
    pwd = input("Enter your simple password: ")

    # encode password
    svc = svc.encode()
    pwd = pwd.encode()

    # encrypt

    pwd_hex = hash_script.make_password(svc, pwd)

    db_manager.db_add(svc, user, pwd_hex)

    # database function, insert(svc, user, pwd)


# def print_key():
#     print(key)


def update_password():
    print("\n")
    svc = input("Enter the service would you like to update:  ")
    option = input(
        "Would you like to update or remove the password from this service?(1/Update, 2/Remove): ")

    if option == 1:

        new_pwd = input("Enter new password: ")

        time.sleep(1)
        print("The password for " + svc + " has been updated to: " + new_pwd)

        db_manager.db_update(svc)

    elif option == 2:

        print("You would like to remove this service from the database..")
        time.sleep(1)
        ru_sure = input(
            "Are you sure you want to remove this password? (Y/N): ")
        if ru_sure == 'y':
            time.sleep(1)
            db_manager.db_remove(svc)
            print(svc + " has been successfully removed!")
        elif ru_sure == 'n':
            print("Returning to menu...")

def retrieve_password():
    svc = input("Enter the service you want to retrieve the password from: ")

    db_manager.db_grab(svc)
    #  select(svc,
    # access database, check if svc matches name of service,
    #  then display to screen
    # integrate closing functionality so window closes


def display_all():

    db_manager.db_add()

    # closing functionality


# Create master password which will equal our secret key

# encrypt passwords our selves

# Encryption instructions:
# 1. take in password
# 2. provide salt + plaintext pw
# 3. pass combo through hash algo
# 4. output hashed password
# 5. copy to clipboard
# 4. store hash algo

# Storing the plaintext password in DB makes no sense, because it's still easy to hack. A password manager exists to house all your encrypted passwords.
