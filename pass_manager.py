import hashlib
from cryptography.fernet import Fernet
import time
import db_manager
import hash_script


# if master password = the secret key, provide access

# create key for master PW?

key = Fernet.generate_key()

crypter = Fernet(key)  # create Fernet object


def add_password():
    print("---------ADD A PASSWORD--------")
    svc = input("Enter Service: ")
    user = input("Enter your username: ")
    pwd = input("Enter your simple password: ")

    # encode values
    svc = svc.encode()
    pwd = pwd.encode()

    # make hex

    pwd_hex = hash_script.make_password(svc, pwd)

    # add service, username, and hexed pwd to database

    db_manager.db_add(svc, user, pwd_hex)


def update_password():
    print("\n")
    svc = input("Enter the service would you like to update:  ")

    # encode the service into bytes again

    svc = svc.encode()
    option = input(
        "Would you like to update or remove the password from this service?(1/Update, 2/Remove): ")

    if option == "1":
        # update :
        print("You would like to update the password for " +
              svc.decode('utf-8') + ".")
        print("------------------------------------------")
        new_pwd = input("Enter new plain-text password: ")
        new_pwd = new_pwd.encode()
        new_pwd_hex = hash_script.make_password(svc, new_pwd)
        db_manager.db_update(svc, new_pwd_hex)
        time.sleep(1)
        print("The password for " + svc.decode("utf-8") +
              " has been updated to: " + str(new_pwd_hex))

    elif option == "2":
        # remove

        print("You would like to remove this service from the database..")
        print("------------------------------------------")
        time.sleep(1)
        ru_sure = input(
            "Are you sure you want to remove this password? (Y/N): ")
        if ru_sure == 'y':
            time.sleep(1)
            db_manager.db_remove(svc)
            print(svc.decode("utf-8") + " has been successfully removed!")
        elif ru_sure == 'n':
            print("Returning to menu...")


def retrieve_password():

    while True:
        svc = input(
            "Enter the service you want to retrieve the password from: ")

        db_manager.db_grab(svc)
        exit = input("Would you like to exit? ")

        if exit == "y":
            break
        else:
            continue
    #  select(svc,
    # access database, check if svc matches name of service,
    #  then display to screen
    # integrate closing functionality so window closes


def display_all():

    db_manager.display_db()

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
