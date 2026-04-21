# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:30:05 2026

@author: Carson

This demo will print out the sha256 hash for all of the files in the same directory as the python program itself.
It will also compare against the given list called "badHashes"
Limitiations:
    Only finds files that are inside the same directory as the python program, not the whole computer.
    I did not check that it is propery hashing the files as I have no example to compare to.
    It is not able to distnguish between a file and a folder, and it can not hash folders.
"""

import hashlib
from pathlib import Path
import sys

print("\nProgram Started.\n")

# This boolean will control whether debug information will be printed to console
debug = False

# This is the list of hashes we will look for.
badHashes = ["b4632f7be15b114d20d46b7c304561c68cd15fb9ed9b2a36bb4fa46ce8501f4b", "0e60f8569d61c6fa15bf9b7fface2478ccd518f2ae26c72540729275f3d11deb", "a31e05e237314081b7f5b1ccc2f5fc768ddbb97bb8888e7be371d072cc8f6193", "668f0ec4a4969abdacc651ca5c4f509661ae75b78d71181decd6c8dfb9210ee9"]

# Couple of counters for the end of program summary
amountOfBadFiles = 0
amountOfUnopenableFiles = 0

# Getting all directories and files in the current directory
allDirs = Path(".").rglob("*")

# Iterate over all files
for directory in allDirs:
    
    if debug:
        print("File name: " + str(directory))
    
    # We use a try because some folders can not be opended
    try:
        
        # Read the file in as bytes
        data = directory.read_bytes()
        
        # Hash it using SHA256
        hash_object = hashlib.sha256(data)
        
        # Converting data to hex for the sake of printing.
        hex_digest = hash_object.hexdigest()
        
        if debug:
            print("Hash Code: " + hex_digest)
        
        # If this is a bad file
        if hex_digest in badHashes:
            
            amountOfBadFiles += 1
            
            if debug:
                print("------------------------------- /\ BAD /\ -------------------------------")
            else:
                print("Found a bad file!")
                print("Directory: " + str(directory))
                print("Hash Code: " + hex_digest)
                print()

    # Some files can not be opened
    except (PermissionError):
        amountOfUnopenableFiles += 1
        if debug:
            print("Unable to open file")

# Summary
if debug:
    print()
print("----------------------------- Summary --------------------------\n")

print("Total bad files found: " + str(amountOfBadFiles))
print("Total amount fo files that can not be opened: " + str(amountOfUnopenableFiles))

