'''Basic string manipulation exercises'''

# 1.) Reverse a String:
def reverse_string(string):
    '''Takes input string and prints the reverse. Does not return any values.'''
    reversed_string = ""
    for i in range(1, len(string) + 1):
        reversed_string += string[len(string) - i]
    print reversed_string

# 2.1) Ceasar Cypher
# This method is expensive, so commented out in favor of caesar_cypher_faster
# def caesar_encrypt(string, offset):
#     '''Encrypts the input string by offsetting by the offset amount'''
#     plaintext = "abcdefghijklmnopqrstuvwxyz"
#     encrypted = plaintext[offset:] + plaintext[:offset]
#     encryption_key = {}
    #here we're using a range to iterate through. Should be using object
    # iteration instead
    # for i in range(len(plaintext) - 1):
    #     encryption_key.update({plaintext[i]: encrypted[i]})
    # print encryption_key
    # plaintext_string = string.lower()
    # encrypted_string = ""
    # for j in range(len(plaintext_string)):
    #     if encryption_key.get(plaintext_string[j]):
    #         encrypted_string += encryption_key[plaintext_string[j]]
    #     else:
    #         encrypted_string += plaintext_string[j]
    # print encrypted_string

# 2.2) Ceasar Cypher
# This method is better...
def caesar_encrypt_faster(string, offset):
    '''Encrypts the input string by offsetting by the offset amount'''
    special_chars = " ~!@#$%^&*()-+_=[]|:;"'<>,.?/'",.0123456789"
    plaintext = "abcdefghijklmnopqrstuvwxyz"
    encrypted = plaintext[offset:] + plaintext[:offset] + special_chars
    plaintext += special_chars
    encrypted_string = ''
    for char in string:
        encrypted_string += encrypted[plaintext.index(char.lower())]
    print encrypted_string

caesar_encrypt_faster("some such, string. 123@#$23423|]", 13)
