# 4. Write a Python program to count the number of lines in a text file.

def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

file_path = 'input.txt'
line_count = count_lines(file_path)
print("Number of lines in the file:", line_count)