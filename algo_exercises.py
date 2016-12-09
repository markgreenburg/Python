'''
A few basic algorithm exercises
'''
import time

# 1) Write an algorithm that takes in a string and reverses all the characters
#    in that string
def reverse_characters(string):
    '''
    Reverses a given string. Prints the reversed string.
    '''
    # Make the string input into a list so that we can reassing indiv. chars
    str_list = list(string)
    # Initialize the starting and ending indicies in the list
    end_x_range = (len(string) - 1) / 2
    # end_x_range = (len(str_list) - 1) / 2
    # Loop through the list, replacing each evaluated char with the char
    # at the last evaluated index. Then increment evaluated char's index,
    # decrement evaluated last index
    for indx in xrange(end_x_range):
        current_last_indx = end_x_range - indx
        str_list[indx], str_list[current_last_indx] = str_list[current_last_indx], str_list[indx]
    return "".join(str_list)
    # print reversed_string

# def reverse_words(string):
#     '''
#     Reverses each string block denoted by a space in place. Prints the reversed
#     string.
#     '''
#     # Split the string on each space
#     words_in_string = " ".split(string)
#     print words_in_string

def average_runtime(num_loops, subfunct_args):
    '''
    Tests a given function's runtime, with input string to test and num of
    loops as args
    '''
    total_time = 0
    for _ in xrange(num_loops):
        start_time = time.time()
        # insert function to test here(subfunct_args)
        reverse_characters(subfunct_args)
        total_time += (time.time() - start_time)
    avg_time = total_time / num_loops
    print "The average run time for this sample is: %s" % str(avg_time)

def test_reverse():
    '''
    Test our algos
    '''
    # Define a test string for our tests
    long_txt_file = open("big.txt")
    test_string = long_txt_file.read()
    # Test string character reversal
    average_runtime(20, test_string)
    # new_string = reverse_characters(test_string)
    # reverse_words(test_string)

if __name__ == "__main__":
    test_reverse()
