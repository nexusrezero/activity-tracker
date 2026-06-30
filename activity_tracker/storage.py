# STORAGE MODULE
# Handles file read/write system

import os

FILE = "data.txt"

def save_entry(entry):
   # saves activity log
    with open(FILE, "a") as f:
        f.write(entry + "\n")

def load_entries():
     # loads all saved activity logs
    if not os.path.exists(FILE):
        return []
    
    with open(FILE, "r") as f:
        return [line.strip() for line in f.readlines()]