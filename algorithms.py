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


if __name__ == "__main__":
    list_to_compare = [0, 4, 45, 7, 767, 7, 787]
    sort(list_to_compare)
    print concat_list(list_to_compare)
