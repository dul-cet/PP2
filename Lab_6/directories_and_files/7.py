# 7. Write a Python program to copy the contents of a file to another file.

def copy_file(source, destination):
    with open(source, 'r') as src_file:
        with open(destination, 'w') as dest_file:
            dest_file.write(src_file.read())

source_file = 'source.txt'
destination_file = 'destination.txt'
copy_file(source_file, destination_file)