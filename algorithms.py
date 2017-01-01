"""
Given a list of non negative integers, arrange them such that they form the largest number.
For example, given [3, 20, 34, 5, 9], the largest formed number is 9534320. (Note: The result may be very large, so you need to return a string instead of an integer.)
"""

def compare(cur_num, prev_num):
    """
    Compares two ints to determine is swap is needed
    """
    cur_pos = int(str(prev_num) + str(cur_num))
    swp_pos = int(str(cur_num) + str(prev_num))
    if swp_pos > cur_pos:
        return True
    return False

def sort(int_list):
    """
    Swaps positions of numbers in a list according to the output of the compare
    helper function.
    """
    iteration_range = len(int_list)
    swap = True
    while swap:
        swap = False
        for position in range(1, iteration_range):
            if compare(int_list[position], int_list[position - 1]):
                int_list[position], int_list[position - 1] = int_list[position - 1]\
                , int_list[position]
                swap = True
        iteration_range -= 1
    return int_list

def concat_list(int_list):
    """
    Concats all ints in the list in position to form a single number (returned as string)
    """
    num_string = ""
    for num in int_list:
        num_string += str(num)
    return num_string

"""
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.
"""

def main(user_list, comparator):
    """
    Main function - pseudocode
    """
    subarray_sum = 0
    subarray_len = 1
    range_end = len(user_list)
    subrange = range_end
    iterate = True
    while iterate:
        for position in range(subrange):
            subarray_sum = sum(user_list[position:(position + subarray_len)])
            if subarray_sum >= comparator:
                return subarray_len
        subrange -= 1        
        subarray_len += 1
        if subarray_len > range_end:
            return 0
    # take a slice of the list
    # total = largest sum of the slice
    # add the slice together
    # if greater than passed in num, return len
    # else, keep iterating with longer subarrays



if __name__ == "__main__":
    list_to_compare = [5, 4, 45, 7, 76, 7, 27]
    # sort(list_to_compare)
    # print concat_list(list_to_compare)
    main(list_to_compare, 800)
