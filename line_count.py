'''
Checks for the count of lines in a file passed in via argv
'''
# Write a program which when given the name of a file as a command line
# Argument, will print the number of lines there are in the file
from sys import argv

# Get file name from user
script, user_file = argv

# open the file and read contents into memory
open_file = open(user_file)
file_contents = open_file.read()

# count the newline chars in the file, print them
file_lines = file_contents.count('\n')
print file_lines
