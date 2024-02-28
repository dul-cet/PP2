# 3. Write a Python program to test whether a given path exists or not.
# If the path exist find the filename and directory portion of the given path. 

import os

def path_info(path):
    exists = os.path.exists(path)
    if exists:
        directory = os.path.dirname(path)
        filename = os.path.basename(path)
        return True, directory, filename
    else:
        return False, None, None

path = r'C:\Users\Moldir\VSCodeProjects\githowto\repositories'
exists, directory, filename = path_info(path)
if exists:
    print("Path exists.")
    print("Directory:", directory)
    print("Filename:", filename)
else:
    print("Path does not exist.")