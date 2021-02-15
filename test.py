# generate a secret key master password:
from cryptography.fernet import Fernet
import time

key = Fernet.generate_key()  # create key

# a bytes key

# take in user input for password

pw = input("Please enter your password: ")
pw_en = pw.encode()  # convert to bytes


crypter = Fernet(key)  # Fernet object
encrypted_pw = crypter.encrypt(pw_en)


# encrypt password

with open("our_pass.txt", "wb") as f:
    f.write(encrypted_pw)

print("Your encrypted password is: " + str(encrypted_pw) +
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
                print(line)

                decrypted_pw = crypter.decrypt(line)
                if decrypted_pw != "":
                    break

    return decrypted_pw


decrypter = view_pw()
print(decrypter)

# store in database
# retrieve password
# decrypt
