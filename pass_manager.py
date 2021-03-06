import time
import db_manager
import hash_script
import pyperclip
import os


def first_time():
    print("--------Hello---------")
    time.sleep(1)
    print("--------Welcome to Your Password Manager----------")
    time.sleep(1)
    master = "Please enter a master password (Keep this safe!): "
    with open('master.txt', "w") as f:
        f.write(master)


def check_master(pwd):
    with open('master.txt', "r") as f:
        for line in f:
            if pwd == line:
                return True
        return False


def add_password():
    print("---------ADD A PASSWORD--------")
    # take inputs
    svc = input("Enter Service: ")
    user = input("Enter your username: ")
    pwd = input("Enter your simple password: ")

    # encode values
    svc_en = svc.encode()
    pwd_en = pwd.encode()

    # make hex
    pwd_hex = hash_script.make_password(svc_en, pwd_en)

    # add service, username, and hexed pwd to database

    db_manager.db_add(svc, user, pwd_hex)
    time.sleep(1)

    print("The password for " + svc + " has been added!")
    print("------------------------------------------")
    print("\n")
    time.sleep(1)


def update_password():

    while True:
        svc = input("Enter the service would you like to update:  ")

        time.sleep(1)
        # check if svc exists in db
        if db_manager.db_chek(svc) == False:
            break
        else:
            pass

        # except:
        #     print("there's an error")
        #     break
        print("------------------------------------------")
        option = input(
            "Would you like to update or remove the password from this service? (1/Update, 2/Remove): ")

        if option == "1":

            print("------------------------------------------")

            print("You would like to update the password for " + svc + "."
                  )

            # update :

            print("------------------------------------------")

            new_pwd = input("Enter new plain-text password: ")
            print("------------------------------------------")
            new_pwd = new_pwd.encode()
            new_svc_en = svc.encode()
            new_pwd_hex = hash_script.make_password(new_svc_en, new_pwd)
            db_manager.db_update(svc, new_pwd_hex)
            time.sleep(1)
            print("The password for " + svc +
                  " has been updated to: " + str(new_pwd_hex))
            print("\n")
            time.sleep(2)

            break

        elif option == "2":
            # remove
            print("------------------------------------------")
            print("You would like to remove this service from the database..")
            print("------------------------------------------")
            time.sleep(1)
            ru_sure = input(
                "Are you sure you want to remove this password? (y/n): ")
            if ru_sure == 'y':
                time.sleep(1)
                db_manager.db_remove(svc)
                print("------------------------------------------")
                print(svc + " has been successfully removed!")
                print("\n")
                time.sleep(2)
            elif ru_sure == 'n':
                print("------------------------------------------")
                print("Returning to menu...")
                print("\n")
                time.sleep(2)

            break


def retrieve_password():

    while True:
        svc = input(
            "Enter the service you want to retrieve the password from: ")
        print("------------------------------------------")
        time.sleep(1)
        try:
            db_manager.db_chek(svc)
            print("------------------------------------------")

            time.sleep(1)
        except:
            print("------------------------------------------")
            print("There's an error!")

        db_manager.db_grab(svc)
        exit = input("Would you like to exit? (y/n) ")

        if exit == "y":
            break
        else:
            continue


def display_all():

    while True:

        time.sleep(1)

        db_manager.display_db()
        time.sleep(1)

        exit = input("Would you like to exit?(y/n) ")

        if exit == "y":
            print("\n")

            break
        else:
            continue

    # closing functionality
