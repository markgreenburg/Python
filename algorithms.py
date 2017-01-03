"""
Given a list of non negative integers, arrange them such that they form the
largest number. For example, given [3, 20, 34, 5, 9], the largest formed number
is 9534320. (Note: The result may be very large, so you need to return a string
instead of an integer.)
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
Given an array of n positive integers and a positive integer s, find the 
minimal length of a subarray of which the sum >= s. If there is not one return 
0 instead.
"""

def find_len(user_list, comparator):
    """
    takes a given positive int list and value to compare against. Returns len
    of the shortest sublist that is >= the comparator value.
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

"""
Given an array of strings, return all groups of strings that are anagrams. 
Example: ['dome','node', 'done','mode','help','demo'] Should return:[['node',
'done'],['mode','dome','demo']] because node and done both have 'D-E-N-O' demo, 
mode and dome have 'D-E-M-O'
"""

def compare_words(word_1, word_2):
    """
    Takes two strings as arguments. Returns True if strings are anagrams of each other.
    """
    return sorted(list(word_1)) == sorted(list(word_2))

def find_anagrams(strings_list):
    """
    Takes a list of strings as arg. Returns list of sublists of all anagrams
    within the original list.
    """
    anagrams = []
    subrange_start = 1
    for word in strings_list[:len(strings_list) -1]:
        sublist = []
        for subword in strings_list[subrange_start:]:
            if compare_words(word, subword):
                if word not in sublist and not any(word in anagram for anagram \
                in anagrams):
                    sublist.append(word)
                if not any(subword in anagram for anagram in anagrams):
                    sublist.append(subword)
        if len(sublist) > 0:
            anagrams.append(sublist)
        subrange_start += 1
    return anagrams
# any(2 in i for i in a)
def test():
    """
    Calls functions above to test with sample inputs
    """
    # list_to_compare = [5, 4, 45, 7, 76, 7, 27]
    # sort(list_to_compare)
    # print concat_list(list_to_compare)
    # find_len(list_to_compare, 800)
    list_of_strings = ['dome', 'node', 'done', 'mode', 'help', 'demo']
    print find_anagrams(list_of_strings)

if __name__ == "__main__":
    test()
