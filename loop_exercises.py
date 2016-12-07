'''Exercise results for loop exercises module'''

# Ex. 1:
# Using a for loop and the range function, print out the numbers
# between 1 and 10 inclusive, one on a line.
def print_one_to_10():
    '''Prints the numbers 1 through 10, one per line'''
    for i in range(1, 11):
        print i


# Ex. 2:
# Prompt uer for the start and end numbers. Otherwise same as above.
def print_user_numbers():
    '''Prints numbers, one per line, from a user-selected range and interval.
    Does NOT handle errors'''
    user_start_num = int(raw_input("At which number would you like to start the counter?> "))
    user_end_num = int(raw_input("At which number would you like to end the counter?> "))
    user_iterator = int(raw_input("Count at what interval?> "))
    for i in range(user_start_num, user_end_num  + 1, user_iterator):
        print i

# Ex. 3.1:
# Print each odd number between 1 and 10, inclusive.
def odd_numbers():
    '''Prints each odd number from 1 to 10, inclusive. Uses range offset to iterate through list.'''
    for i in range(1, 10, 2):
        print i

# Ex. 3.2:
# Print each odd number between 1 and 10, inclusive.
def odd_numbers_modulus():
    '''Prints each odd number from 1 to 10, inclusive. Uses modulus operator to find odds'''
    for i in range(1, 11):
        if i % 2 != 0:
            print i

# Ex. 4:
# Print a 5 x 5 grid of asterisks
def print_asterisk_box():
    '''Prints a 5 x 5 grid of asterisks'''
    for _ in range(5):
        print '*****'

# Ex. 5:
# Print an n * n grid of asterisks per user spec
def print_user_square():
    '''Prints a square grid of asterisks per user's size spec. Does NOT
    handle errors'''
    side = int(raw_input("How big do you want each side of the square?> "))
    for _ in range(side):
        print '*' * side

# Ex. 6:
# Print a box of asterisks per users' dimension specs
def print_user_box():
    '''Prints an empty box of asterisks based on user's input.
    Does NOT error handle'''
    width = int(raw_input("What's your box width?> "))
    height = int(raw_input("What's your box height?> "))
    print "*" * width   #print the top row of the box
    for _ in range(height - 2):   #print the hollow middle rows
        print "*" + " " * (width - 2) + "*"
    print "*" * width   #print the top row of the box

# Ex. 7:
# Print a triangle of a given height
def print_user_triangle():
    '''Prints triangle with user-specified height. Does NOT error handle'''
    height = int(raw_input("What's your triangle's height?> "))
    total_width = 2 * height - 1
    width_counter = 1
    for _ in range(height):
        print " " * ((total_width - width_counter) / 2) + "*" * width_counter
        width_counter += 2
# Ex. 8:
# Print the multiplication tables for numbers from 1 up to 10.
def print_mult_tables():
    '''Prints multiplication tables from 1 to 10'''
    for i in range(1, 11):
        for j in range(1, 11):
            print "%d x %d = %d" % (i, j, i * j)

# Ex. 9:
# Print a banner with user-specified text inside
def print_user_banner():
    '''Prints a banner of asterisks around a user's string'''
    user_string = raw_input("Please enter text to put inside your banner> ")
    banner_inner_width = len(user_string)
    print "*" * (banner_inner_width + 2)
    print "*" + user_string + "*"
    print "*" * (banner_inner_width + 2)

# Ex. 10 Bonus:
# Print all 'triangle' numbers (1, 3, 6, etc.) from 1 to the 100th one
def print_first_100_triangles():
    '''Prints the first 100 triangle numbers'''
    for i in range(1, 101):
        print i * (i + 1) / 2

# Ex. 11 Bonus:
# Print all factors of a given number
def print_factors():
    '''Prints all factors of a number the user specifies. Does NOT error handle'''
    user_number = int(raw_input("Enter a number to see its factors.> "))
    for i in range(1, user_number + 1):
        if user_number % i == 0:
            print i
