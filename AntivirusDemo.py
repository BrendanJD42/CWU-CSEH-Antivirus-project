# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:30:05 2026

@author: Carson

This demo will print out the sha256 hash for all of the files in the same directory as the python program itself.
Limitiations:
    Only finds files that are inside the same directory as the python program, not the whole computer.
    I did not check that it is propery hashing the files as I have no example to compare to.
    It is not able to distnguish between a file and a folder, and it can not hash folders.
"""

import hashlib
from pathlib import Path

# Getting all directories and files in the current directory
allDirs = Path(".").rglob("*")

# Iterate over all files
for directory in allDirs:
    
    # Print the file name
    print("File name: " + str(directory))
    
    # If it can be opened, print the hash code of the file
    try:
        # Read the file in as bytes
        data = directory.read_bytes()
        
        # Hash it using SHA256
        hash_object = hashlib.sha256(data)
        
        # Converting data to hex for the sake of printing.
        hex_digest = hash_object.hexdigest()
        print("Hash code: " + str(hex_digest))

    # If unable to open file, just print.
    except (PermissionError):
        print("Unable to open file")
    
    
