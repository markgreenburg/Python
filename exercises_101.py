'''Series of simple exercises for Python 101. Each exercise should be commented out except the one you want to run'''

# 1.) Hello, you!
# name = raw_input("What is your name?> ")
# print "Hello, %s!" % name

# 2.) Hello, in all CAPS
# name = raw_input("What is your name?> ").upper()
# print "Hello, %s!" % name

# 3.) How many letters in the name?
# name = raw_input("What is your name?> ")
# print "Hello, %s!" % name
# print "Your name has %s letters in it!" % len(name)

# 4.) Madlib
sentence = "'s favorite subject in school is "
name = raw_input("What's a name?> ")
subject = raw_input("What's a subject?> ")

print name + sentence + subject





# '''Simple script to calculate a per-person tip / check total amount to pay.'''
#
# total_bill = float(raw_input("What's the bill total?> "))
# service = raw_input("Was your service good, fair, or bad?> ")
#
# while (service == 'good' or service == 'fair' or service == 'poor') is False:
#     service = raw_input("That's not a valid service level. Please choose good, fair, or poor.> ")
#
# split = int(raw_input("How many ways do you want to split the bill?> "))
#
#
# if service == 'good':
#     tip_percent = .20
# elif service == 'fair':
#     tip_percent = .15
# else:
#     tip_percent = .1
#
# tip_amount = round(total_bill * tip_percent, 2)
# total_with_tip = round(total_bill + tip_amount, 2)
# total_with_tip_per_person = round(total_with_tip / split, 2)
#
# print "The total tip amount is: $%f" % tip_amount
# print "The total bill with tip is: $%f" % total_with_tip
# print "The total amount per person is: $%f" % total_with_tip_per_person
