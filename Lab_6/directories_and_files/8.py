# 8. Write a Python program to delete file by specified path.
# Before deleting check for access and whether a given path exists or not.

import os

def delete_file(file_path):
    exists = os.path.exists(file_path)
    if exists:
        os.remove(file_path)
        return True
    else:
        return False

file_path = 'file_to_delete.txt'
deleted = delete_file(file_path)
if deleted:
    print("File deleted successfully.")
else:
    print("File does not exist.")