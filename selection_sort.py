'''
Example of selection sort on a (pseudo-)randomly-shuffled list
'''

import random
import time

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

def selection_sort(random_list):
    '''
    For given input list, sort the list in ascending order
    '''
    for index_value in range(len(random_list)):
        new_min = find_min_index(random_list, index_value)
        swap_values(random_list, index_value, new_min)
    print random_list

def test():
    '''
    Test the selection sort code with random input
    '''
    user_list = range(10000)
    random.shuffle(user_list)
    # Copy same shuffled list for other sort comparisons
    ul2 = user_list
    # Timed execution of our selection sort
    start_time = time.time()
    selection_sort(user_list)
    print "Selection sort took %s seconds" % (time.time() - start_time)
    # Compare our results to the internal sort function
    start_time = time.time()
    ul2.sort()
    print "Python's sort function took %s seconds" % (time.time() - start_time)
    # No surprise...Python's

#
if __name__ == "__main__":
    test()
