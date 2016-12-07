'''Basic string manipulation exercises'''

# 1.) Reverse a String:
def reverse_string(string):
    '''Takes input string and prints the reverse. Does not return any values.'''
    reversed_string = ""
    for i in range(1, len(string) + 1):
        reversed_string += string[len(string) - i]
    print "reversed string: %s" % reversed_string

# 2.1) Ceasar Cypher
# Encrypt a message with using the Caesar Cypher
def caesar_encrypt_faster(string, offset):
    '''Encrypts the input string by offsetting by the offset amount'''
    string = string.upper()
    plaintext_key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_key = plaintext_key[offset:] + plaintext_key[:offset]
    encrypted_string = ''
    for char in string:
        if char.isalpha():
            encrypted_string += encrypted_key[plaintext_key.index(char)]
        else:
            encrypted_string += char
    print "encrypted string: %s" % encrypted_string

def leetspeak(string):
    '''Replaces certain alpha characters with their leetspeak num equivalents.
    Prints translated string and outputs nothing.'''
    # treat all characters as uppercase
    string = string.upper()
    plaintext_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    leetspeak_key = '4BCD3F6H1JKLMN0PQR57UVWXYZ'
    translated_text = ''
    for char in string:
        if char.isalpha():
            translated_text += leetspeak_key[plaintext_key.index(char)]
        else:
            translated_text += char
    print "leetspeak text: %s" % translated_text

reverse_string("some such 1234 $#@ nonsense")
caesar_encrypt_faster("some such 1234 $#@ nonsense",13)
leetspeak("some such 1234 $#@ nonsense")
