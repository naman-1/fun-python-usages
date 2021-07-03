import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

path = 'xyz'
fileName = os.listdir(path)
def multiFiles():
    with open('jpg', 'rb') as file:
        original = file.read()

encrypted = fernet.decrypt(original)

with open('jpg', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)