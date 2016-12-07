'''Simple dictionary exercises.'''

# 1 Print Elizabeth's phone number
def print_phone_number(dictionary, first_name):
    '''Print a phone number for given person's name, in a given dictionary'''
    print "%s's phone number is: %s" % (first_name, dictionary[first_name])

# 2 Add an entry to the directory
def add_entry_to_dic(dictionary, entry):
    '''Adds a user-specified entry to a user-specified dictionary'''
    dictionary.update(entry)
    return dictionary

# 3 Delete an entry from the directory
def delete_entry_from_dic(dictionary, entry):
    '''Deletes a given entry from a given dictionary. Takes dict and key as
    input'''
    del dictionary[entry]
    return dictionary

# 4 Update an entry in the directory
def update_entry_in_dic(dictionary, entry):
    '''Updates values for a key in a given dictionary'''
    dictionary.update(entry)
    return dictionary

# 5 Print all the phone numbers in the directory
def print_all_values_in_dic(dictionary):
    '''prints all values in the directory'''
    print dictionary.values()

# 6 Get email address of a friend
def get_stuff_from_dic(dictionary):
    '''Gets specific items from a dictionary'''
    # Get Aditi's email
    print dictionary['friends'][1]['email']
    # Get Aditi's interests
    print dictionary['friends'][1]['interests'][0]
    # Get Jasmine's email
    print dictionary['friends'][0]['email']
    # Get Aditi's second interest
    print dictionary['friends'][1]['interests'][1]

# 7 Read in the text of a .txt file and count word frequency
def word_count(user_file):
    '''Given an input .txt file, counts frequency of each word in the file'''
    contents = open(user_file).read()
    list_of_all_words = contents.split(' ')
    list_of_unique_words = []
    word_frequency_dictionary = {}
    for word in list_of_all_words:
        if word not in list_of_unique_words:
            list_of_unique_words.append(word)
    for unique_word in list_of_unique_words:
        word_frequency_dictionary[unique_word] = list_of_all_words.count(unique_word)
    return word_frequency_dictionary

#Define variables for function args
phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}

ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
            'name': 'Jasmine',
            'email': 'jasmine@yahoo.com',
            'interests': ['photography', 'tennis']
        },
        {
            'name': 'Aditi',
            'email': 'Aditi@hotmail.com',
            'interests': ['movies', 'tv']
        }
    ]
}

my_entry = {'Mark': '111-123-4567'}
alice = 'Alice'
bob_new = {'Bob': '968-345-2345'}

# Call functions for testing
print_phone_number(phonebook_dict, "Elizabeth")
add_entry_to_dic(phonebook_dict, my_entry)
delete_entry_from_dic(phonebook_dict, alice)
update_entry_in_dic(phonebook_dict, bob_new)
print_all_values_in_dic(phonebook_dict)

# Test of nested dictionary value extraction
get_stuff_from_dic(ramit)

# Test programmer's blues
word_count('programmers_blues.txt')
