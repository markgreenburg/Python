'''
A few basic algorithm exercises
'''
import time
# import random

# 1) Write an algorithm that takes in a string and reverses all the characters
#    in that string
def reverse_characters(string):
    '''
    Reverses a given string. Prints the reversed string.
    '''
    # Make the string input into a list so that we can reassing indiv. chars
    str_list = list(string)
    # Calculate the ending index in the list
    end_x_range = (len(string) - 1) / 2
    current_last_index = len(string) - 1
    # Loop through the list, replacing each evaluated char with the char
    # at the last evaluated index. Then increment evaluated char's index,
    # decrement evaluated last index
    for indx in xrange(end_x_range):
        str_list[indx], str_list[current_last_index] = str_list[current_last_index], str_list[indx]
        current_last_index -= 1
    return "".join(str_list)
    # print reversed_string

# 2) Write a function that takes in a paragraph of text and reverses each word #    in the paragraph
def reverse_words(string):
    '''
    Reverses each string block denoted by a space in place. Prints the reversed
    string. Orders of magnitude slower than the base reverse() method, even
    with string-to-list conversion time factored in.
    '''
    # Split the string on each space
    words_in_string = string.rsplit()
    for indx in xrange(len(words_in_string) - 1):
        words_in_string[indx] = reverse_characters(words_in_string[indx])
    return " ".join(words_in_string)

def average_runtime(num_loops, subfunct_args):
    '''
    Tests a given function's runtime, with input string to test and num of
    loops as args
    '''
    start_time = time.time()
    for _ in xrange(num_loops):
        # insert function to test here(subfunct_args)
        # reverse_characters(subfunct_args)
        reverse_words(subfunct_args)
    avg_time = ((time.time() - start_time)) / num_loops
    print "The average run time for this sample is: %s" % str(avg_time)

# 3) Find the kth largest element in an unsorted array.
#    First, define some selection sort helper methods...
def find_min_index(random_list, starting_index):
    '''
    For a given sublist starting at the starting_index and ending at the
    end of the list, find the index of the min. value
    '''
    # Initialize current minimum value
    min_index = starting_index
    # loop through the rest of the list to find smallest value
    for index in range(starting_index + 1, len(random_list)):
        if random_list[min_index] > random_list[index]:
            min_index = index
    return min_index

def swap_values(random_list, current_index, min_index):
    '''
    Swaps the values of two list items passed in as arguments.
    '''
    if random_list[current_index] > random_list[min_index]:
        temp_value_hold = random_list[current_index]
        random_list[current_index] = random_list[min_index]
        random_list[min_index] = temp_value_hold
    return random_list

#   Then, modify Selection Sort to only sort as many items as needed.
def xth_selection_sort(random_list, xth_largest):
    '''
    Find the xth largest value for a given list. Prints value.
    '''
    for index_value in range(len(random_list) - (xth_largest - 1)):
        new_min = find_min_index(random_list, index_value)
        swap_values(random_list, index_value, new_min)
    print random_list[len(random_list) - xth_largest]

# 4) Validate special characters:
#    Given a string containing just the characters '(', ')', '{', '}', '[' and
#    ']', determine if all parens are closed.
#    Note: This solution doesn't respect valid order, it just checks that all
#    parens are closed.
def check_pairs(string, pair):
    '''
    Checks through string and counts the number of unclosed 'pairs' of inputs.
    I.e., each '(' should have a corresponding number of subsequent ')', etc.
    '''
    unclosed_pair = 0
    for char in string:
        if char == pair[0]:
            unclosed_pair += 1
        if char == pair[1]:
            unclosed_pair -= 1
        if unclosed_pair < 0:
            # Exit immediately upon finding the first unclosed pair
            return False
    # To catch unclosed pairs at the end of the string
    return unclosed_pair == 0

def validate_string(string):
    '''
    Runs pair validation on all types of legal inputs (parens, brackets, braces)
    '''
    return check_pairs(string, "()") and check_pairs(string, "[]") and check_pairs(string, "{}")

# 5) Convert string to integer
def chunk_string(string):
    '''
    Intelligently converts string to int, being sure to account for null /
    empty strings, white space, +/- signs, calculating real values, and
    handling min / max
    '''
    # Initialize valid characters
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    special_chars = ['+', '-']
    # Convert string to list for processing with pop()
    l_of_str = list(string)
    # Initialize an empty list to hold chunked results
    list_of_chars = []
    # Iterate through string and add each chunk as item to list
    for _ in xrange(len(string)):
        if l_of_str[0] in nums:
            # If the current item is a number, check if another number comes
            # directly after it.
            substring = ""
            for _ in xrange(len(string)):
                if len(l_of_str) == 0:
                    # If no chars left in string to check, return chunked list
                    list_of_chars.append(substring)
                    return list_of_chars
                elif l_of_str[0] in nums:
                    # Append the current number chunk to the list
                    substring += l_of_str.pop(0)
                else:
                    # Break out as soon as the first non-number is encountered
                    break
            # Append the current number sequence string to the chunked list
            list_of_chars.append(substring)
        elif l_of_str[0] in special_chars:
            # If the current char is a + or -, append it as its own list item
            list_of_chars.append(l_of_str.pop(0))
        else:
            # If invalid char is encountered, pop it out and ignore
            l_of_str.pop(0)
        if len(l_of_str) == 0:
            # Once nothing is left to process in the string, return the new
            # list
            return list_of_chars
    return list_of_chars

def parse_strings(num_list):
    '''
    Takes a list of chunked strings and converts them to int, performs basic
    math on them if + or - operator encountered.
    '''
    # Combine strings with operators where possible
    for item in xrange(1, len(num_list) - 1):
        if num_list[item - 1] in ['-', '+']:
            num_list[item] += num_list.pop(item - 1)
    print num_list


def test_functions():
    '''
    Test our functions
    '''
    # # Define a test string for our tests
    # long_txt_file = open("big.txt")
    # test_string = long_txt_file.read()
    # test_string = "The quick brown fox jumps over the lazy dog"
    # Test string character reversal
    # average_runtime(100, test_string)
    # new_string = reverse_characters(test_string)
    # reverse_words(test_string)
    # test_string = "The quick brown fox jumps over the lazy dog"
    # reverse_words(test_string)
    # Test our xth largest value finder
    # user_list = range(10000)
    # random.shuffle(user_list)
    # xth_selection_sort(user_list, 10)
    special_string = "j-123 48+7395-09;"
    # validate_string(special_string)
    chunked_string = chunk_string(special_string)
    print chunked_string
    parse_strings(chunked_string)

if __name__ == "__main__":
    test_functions()
