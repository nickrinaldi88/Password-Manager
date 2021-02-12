import hashlib


def add_password():
    svc = input("Enter Service: ")
    user = input("Enter your username: ")
    pwd = input("Enter your password: ")

    # -Take password, encode, run through hashing algorithm, and store in database
    # -Access function in database script to add to DB


def update_password():
    svc = input("Enter the service would you like to update:  ")
    # retrieve data from database/query DB for the service row
    cur_pwd = input("Please enter the current password for this service: ")
    option = input(
        "Would you like to update or remove the password from this service?(1/Update, 2/Remove): ")
    # if option == 1:
    new_pwd = input("Please enter the new password: ")
    con_pwd = input("Please confirm the new password: ")
    # if cur_pwd == the pwd from the DB:
    # executve this line
    # if new_pwd == con_pwd:
    # encode new_password
    # run through hash algo
    # update password
    # update new pwd in DB
    # elif option == 2:
    ru_sure = input("Are you sure you want to remove this password? (Y/N): ")
    # if Y,

    # delete password/service from database
    # if N,
    # continue

    # close window

    pass


def retrieve_password():
    svc = input("Enter the service you want to retrieve the password from: ")
    # access database, check if svc matches name of service, then display to screen
    # integrate closing functionality so window closes
    pass


def display_all():
    # retrieve complete table from database
    # display onto screen
    # closing functionality
    pass

# This script will execute the essential functionality of our password manager
# Take in 4 inputs,
# username
# password
# website
# email
# provide ability to open PW_Manager to see how many passwords exist


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
