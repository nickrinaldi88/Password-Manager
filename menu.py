
import time
import pass_manager
import db_manager
import os


def login_success():
    print("----------Welcome to the Menu!----------")
    time.sleep(1)
    print("What would you like to do?")
    print("1. Add ax new password")
    print("2. Update/Remove a password")
    print("3. Retrieve a password")
    print("4. Display all passwords")
    print("5. Exit")
    print("\n")


# only runs if file doesn't exist
if not os.path.exists('master.txt'):
    # the the master file doesn't exist
    # run the first time function, else, run
    pass_manager.first_time()


def grab_master():
    with open('master.txt', 'r') as f:
        for line in f:
            master = line

        return master


pwd = grab_master()

while True:

    if pass_manager.check_master(pwd):
        while True:
            choice = input("Please enter your choice: ")
            print("\n")
            if choice == "1":
                pass_manager.add_password()
            elif choice == "2":
                pass_manager.update_password()
            elif choice == "3":
                pass_manager.retrieve_password()
            elif choice == "4":
                pass_manager.display_all()
            elif choice == "5":
                db_manager.close_db()
                break
    else:
        print("Your master password is not correct. Try Again. ")
        continue
