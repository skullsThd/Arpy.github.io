#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Let's find some files

files = []

for file in os.listdir():
    if file == "v3voost.py" or file == "theKey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("theKey.key", "rb") as key:
    secretkey = key.read()

print(files)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
