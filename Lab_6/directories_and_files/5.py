# 5. Write a Python program to write a list to a file.

def write_list_to_file(file_path, input_list):
    with open(file_path, 'w') as file:
        for item in input_list:
            file.write(str(item) + '\n')
        file.close()

file_path = 'output.txt'
my_list = ['apple', 'banana', 'cherry']
write_list_to_file(file_path, my_list)