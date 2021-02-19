# menu will display options onto screen
# terminal or Tkinter GUI?
import time
import pass_manager
import db_manager

print("--------Hello---------")
time.sleep(1)
print("--------Welcome to Your Password Manager----------")
time.sleep(1)


def login_success():
    print("---You're logged in!---")
    print("What would you like to do?")
    print("1. Add a new password")
    print("2. Update/Remove a password")
    print("3. Retrieve a password")
    print("4. Display all passwords")
    print("5. Exit")


while True:
    login_success()
    choice = input("Please enter you1r choice: ")
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
