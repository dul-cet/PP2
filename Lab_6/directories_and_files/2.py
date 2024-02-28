# 2. Write a Python program to check for access to a specified path.
# Test the existence, readability, writabilityand executability of the specified path.

import os

def check_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    return exists, readable, writable, executable

path = r'C:\Users\Moldir\VSCodeProjects\githowto\repositories'
exists, readable, writable, executable = check_access(path)
print("Existence:", exists)
print("Readability:", readable)
print("Writability:", writable)
print("Executability:", executable)