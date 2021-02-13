# file to test encrypting

from cryptography.fernet import Fernet
# Generate key; which will be used in our algorithm to create the encryption; then we use the same key to
# revert the encryption into it's actual string content.

# Fernet guarantees that a message encrypted using it cannot be manipualted or read without the key

# Generate key
key = Fernet.generate_key()
key2 = Fernet.generate_key()

crypter = Fernet(key)
crypter2 = Fernet(key)  # create fernet object, pass in key we created

# pass in password, in bytes. data must be in bytes to encrypt
pw = crypter.encrypt(b"Hersheygreen1!")

# decrypt the pw

decrypt_str = crypter2.decrypt(pw)

print(pw)

print(str(decrypt_str, 'utf-8'))


# once we encrypt something, we need to use the same key to decrypt it; can't use a different key

# https://www.youtube.com/watch?v=S-w24LtBub8 / 2:35
# https://cryptography.io/en/latest/fernet.html
