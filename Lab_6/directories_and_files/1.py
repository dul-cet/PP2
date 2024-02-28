# 1. Write a Python program to list only directories, files and all directories, files in a specified path. 

import os

def list_directories_files(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return directories, files

path = r'C:\Users\Moldir\VSCodeProjects\githowto\repositories'
directories, files = list_directories_files(path)
print("Directories:", directories)
print("Files:", files)