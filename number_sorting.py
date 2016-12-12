'''
Example of sorting algorithms on (pseudo-)randomly-shuffled lists
'''
import random
import time

# Selection Sort
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
    return random_list

# Bubble sort
def bubble_sort(random_list):
    '''
    Uses bubble sort algorithm to sort a randomized list taken in as an arg.
    Returns sorted list.
    '''
    iteration_range = len(random_list) - 1
    swap = True
    while swap:
        swap = False
        for i in range(1, iteration_range):
            if random_list[i - 1] > random_list[i]:
                random_list[i - 1], random_list[i] = random_list[i],\
                random_list[i - 1]
                swap = True
        # We know that each pass sorts at least the last item in the list into
        # correct position
        iteration_range -= 1
    return random_list

def test():
    '''
    Test the selection sort code with random input
    '''
    # user_list = [4, 3, 1, 8, 3, 1, 2, 9]
    user_list = range(1000)
    random.shuffle(user_list)
    copy_1 = user_list
    copy_2 = user_list
    copy_3 = user_list
    start_time = time.time()
    bubble_sort(copy_1)
    print "Normal bsort took %s seconds" % (time.time() - start_time)
    start_time = time.time()
    bubble_sort(copy_2)
    print "Optimized bsort took %s seconds" % (time.time() - start_time)
    start_time = time.time()
    selection_sort(copy_3)
    print "Selection sort took %s seconds" % (time.time() - start_time)
    # random.shuffle(user_list)
    # # Copy same shuffled list for other sort comparisons
    # ul2 = user_list
    # # Timed execution of our selection sort

    # # Compare our results to the internal sort function
    # start_time = time.time()
    # ul2.sort()
    # print "Python's sort function took %s seconds" % (time.time() - start_time)
    # # No surprise...Python's


if __name__ == "__main__":
    test()
