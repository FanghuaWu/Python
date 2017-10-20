# import module
from sys import argv

# from the command line read "script" and "input_file" variables.
script, input_file = argv

# define function for read the content of file and print them
def print_all(f):
    print(f.read())

# come back to the beginning of the file
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

# open input_file
current_file = open(input_file)

print("First let's print the whole file:\n")

# read and print
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
