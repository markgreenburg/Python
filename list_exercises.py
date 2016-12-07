'''Simple list exercises. All functions print, rather than returning'''

# 1) Sum the numbers
def print_sum_numbers(list_of_nums):
    '''Given a list of numbers, print their sum'''
    print "The sum of the numbers is: %d" % sum(list_of_nums)

# 2) Largest number
def print_largest_number(list_of_nums):
    '''Given a list of numbers, print the largest value'''
    print "The max value in the list is: %d" % max(list_of_nums)

# 3) Smallest number
def print_smallest_number(list_of_nums):
    '''Given a list of numbers, print the smallest value'''
    print "The min value in the list is: %d" % min(list_of_nums)

# 4) Even numbers
def print_even_numbers(list_of_nums):
    '''Given an list of numbers, prints each even number.'''
    list_of_even_nums = []
    for i in range(0, len(list_of_nums)):
        if list_of_nums[i] % 2 == 0:
            list_of_even_nums.append(list_of_nums[i])
    print "The list of even numbers is:"
    print list_of_even_nums

# 5) Positive numbers
def print_positive_numbers(list_of_nums):
    '''prints all positive numbers from a list sequentially'''
    print "The positive numbers in the list are:"
    for i in range(0, len(list_of_nums)):
        if list_of_nums[i] > 0:
            print list_of_nums[i]

# 6) Positive Numbers II
def print_positive_numbers_list(list_of_nums):
    '''prints and returns a list of positive numbers for a given input list'''
    list_of_positive_nums = []
    for i in range(0, len(list_of_nums)):
        if list_of_nums[i] > 0:
            list_of_positive_nums.append(list_of_nums[i])
    print "The list of positive numbers is:"
    print list_of_positive_nums

# 7) Multiply a list
def print_multiply_list(list_of_nums, factor):
    '''Given a list of numbers and a single factor, create a new list
    consisting of each of the numbers in the first list multiplied
    by the factor.'''
    multiplied_list = []
    for i in list_of_nums:
        multiplied_list.append(i * factor)
    print "The new multiplied list of numbers is:"
    print multiplied_list

# 8 Multiply Vectors
def print_multiply_vectors(list_of_nums, list_of_nums_2):
    '''Given two lists of numbers of the same length, creates a new list
    by multiplying the pairs of numbers in corresponding positions in the two
    lists'''
    multiplied_list = []
    if len(list_of_nums) != len(list_of_nums_2):
        print "The two lists need to be the same length!"
        return -1
    else:
        for i in list_of_nums:
            multiplied_list.append(i * list_of_nums_2[list_of_nums.index(i)])
    print "The list of multiplied numbers is:"
    print multiplied_list

# 9 Matrix addition
def print_matrix_addition(matrix_of_nums, matrix_of_nums_2):
    '''Calculate the result of adding the two matrices of the same length'''
    output_matrix = []
    for i in range(len(matrix_of_nums)):
        sub_list = []
        for j in range(len(matrix_of_nums[i])):
            sub_list.append(matrix_of_nums[i][j] + matrix_of_nums_2[i][j])
        output_matrix.append(sub_list)
    print "The summed matrix is:"
    print output_matrix

# 10 De-duping
def print_de_dupe_lists(list_of_nums):
    '''Removes duplicate numbers & strings from a given input list'''
    de_duped_list = []
    for i in list_of_nums:
        if i not in de_duped_list:
            de_duped_list.append(i)
    print "The de-duped list is:"
    print de_duped_list

# 11 Matrix Multiplication (dot product)

# defining testing variables for function args
test_list = [1, 2, 3, 4, 90, -10, 25, 12]
test_list_2 = [25, -10, 90, 4, 3, 2, 1, 11]
test_matrix = [[1, 2, 3, 4, 90, -10, 25, 12], [25, -10, 90, 4, 3, 2, 1, 11]]
test_matrix_2 = [[11, 1, 2, 3, 4, 90, -10, 25], [12, 25, -10, 90, 4, 3, 2, 1, 12]]
test_dedupe_list = [1, 2, 3, 4, 90, -10, 25, 12, 'a', 'b', 'a', 'c', -10]
dot_matrix_1 = [[5, 13], [6, 7]]
dot_matrix_2 = [[3, 9], [8, 3]]
factor_num = 6

# function calls for testing
print_sum_numbers(test_list)
print_largest_number(test_list)
print_even_numbers(test_list)
print_positive_numbers(test_list)
print_positive_numbers_list(test_list)
print_multiply_list(test_list, factor_num)
print_multiply_vectors(test_list, test_list_2)
print_matrix_addition(test_matrix, test_matrix_2)
print_de_dupe_lists(test_dedupe_list)
