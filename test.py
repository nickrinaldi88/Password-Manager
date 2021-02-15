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

with open("our_pass.txt", "w+") as f:
    f.write(str(encrypted_pw))

print("Your encrypted password is: " + str(encrypted_pw) +
      "\n" + "and has been added to the database." + "\n" + "The original password is: " + pw)

time.sleep(2)


def view_pw():

    while True:
        retrieve = input("Want password?: ")
        if retrieve != "y":
            break
        else:
            f = open("our_pass.txt", "r")
            for line in f:
                decrypted_pw = crypter.decrypt(line.encode())
                if decrypted_pw != "":
                    break

    return decrypted_pw


decrypter = view_pw()
print(decrypter)

# store in database
# retrieve password
# decrypt
