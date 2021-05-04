import time
import pass_manager
import db_manager
import os

def show_menu():

    print("----------Welcome to the Menu!----------")
    time.sleep(1)
    print("What would you like to do?")
    print("1. Add a new password")
    print("2. Update/Remove a password")
    print("3. Retrieve a password")
    print("4. Display all passwords")
    print("5. Exit")
    print("\n")

def startup():

    if not os.path.exists('master.txt'):
        pass_manager.first_time()
        db_manager.create_table()

    if pass_manager.check_master():
        print("----------You're in!----------")
        time.sleep(0.5)
        print("-"*30)
        time.sleep(0.5)

        while True:

            show_menu()
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

if __name__ == '__main__':
    startup()
