'''
Basic exercises to build familiarity with functions and classes. The Person
class has been pre-defined.
'''
class Person(object):
    '''
    Creates a person with some basic properties.
    '''
    def __init__(self, name, email, phone):
        '''
        Initializes each person object with name, email, & phone number passed
        in as args.
        '''
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique_people_greeted = []

    def __repr__(self):
        '''
        We're returning object's string representation with some basic info
        about the Person.
        '''
        return '%s; %s; %s; %s; %s' % (self.name, self.email, self.phone,
                                       self.friends, self.greeting_count)

    def greet(self, other_person):
        '''
        Greets another person object by name and announces the current person
        object's name. Prints to console. Then increments the greeting counter
        and increments the unique people greeted counter if the greeting is
        to a unique Person
        '''
        # Print greeting to console
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        # Increment the count of greetings
        self.greeting_count += 1
        # Add recipient's name to the list of people who have been greeted.
        # only if they're not in there already
        if other_person not in self.unique_people_greeted:
            self.unique_people_greeted.append(other_person)


    def print_contact_info(self):
        '''
        Prints a given Person object's contact info
        '''
        print "%s's email: %s, %s's phone number: %s" % (self.name, self.email,
                                                         self.name, self.phone)

    def add_friend(self, other_person):
        '''
        Adds a person object to the friends list of a person
        '''
        if other_person not in self.friends:
            self.friends.append(other_person)
        else:
            print "%s is already %s's friend." % (other_person.name, self.name)

    def num_friends(self):
        '''
        prints the length of a Person object's friends list.
        '''
        print len(self.friends)

    def num_unique_people_greeted(self):
        '''
        Prints the number of unique people greeted
        '''
        print len(self.unique_people_greeted)
        print "the list of unique people greeted is: "
        print self.unique_people_greeted

# 1) Instantiate an instance object of Person with name of 'Sonny', email of
#    'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable
#    sonny.
#       - Added answer to test method at bottom of script

# 2) Instantiate another person with the name of 'Jordan', email of
#    'jordan@aol.com', and phone of '495-586-3456', store it in the variable
#    'jordan'.
#       - Added answer to test method at bottom of script

# 3) Have Sonny greet Jordan using the greet method
#       - Added answer to test method at bottom of script

# 4) Have jordan greet sonny using the greet method.
#       - Added answer to test method at bottom of script

# 5) Write a print statement to print the contact info (email and phone) of
#    Sonny.
#        - Added answer to test method at bottom of script

# 6) Write another print statement to print the contact info of Jordan.
#        - Added answer to test method at bottom of script

# 7) Make your own class:
#    Create a class Vehicle. A vehicle object will have 3 attributes: make,
#    model, and year
class Vehicle(object):
    '''
    Create a Vehicle class that includes make, model, and year. Since there's
    only one public method here, in reality we probably wouldn't need to make
    a class for this...
    '''
    def __init__(self, make, model, year):
        '''
        Have make, model, and year defined for each Vehicle through args
        '''
        self.make = make
        self.model = model
        self.year = year

# 8) Add a print_info method to the Vehicle class. It will print out the
#    Vehicle's class. It will print out the info as: "2015 Nissan Leaf"
    def print_info(self):
        '''
        Prints the year, make, and model of a given Vehicle object
        '''
        print "%s %s %s" % (self.year, self.make, self.model)

# 9) Go back to the Person class. Add a print_contact_info method to the Person
#    class that will print out the contact info for a object instance of
#    Person. You will use it thus: Sonny's email: sonny@hotmail.com, Sonny's
#    phone number: 483-485-4948.
#       - Answer added above in Person class methods

# 10) Add a friends instance variable (attribute) to the Person class. Once
#     you've done this you should be able to add a friend to a person using
#     list's append method.

# 11) The fact that a person's friends attribute is a list is an implementation
#     detail of the Person class. It is often desired to hide implementation
#     details from the users of your object/class. Implement an add_friend
#     method to Person.
#       - Answer above in Person class methods

# 12) Similarly, to get the number of friends a person has, we'd like to hide
#     the implementation detail that there is a friends attribute which is a
#     list. Implement a num_friends method which returns the number of friends
#     the person currently has.
#       - Answer above in Person class methods

# 13) We want to count the number of times a person has greeted someone. To do
#     this, we'll add another attribute, call it say greeting_count, and
#     initialize it to 0. Then each time the greet method is called, we'll
#     increment greeting_count by 1.
#       - Answer above in Person methods

# Testing some of the code...
def test_objects():
    '''
    Test each of the methods defined to ensure we get back expected output.
    Print helpers to console to easily parse what's going on at each step.
    '''
    print "Instantiating sonny instance of Person class..."
    sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
    print "Instantiating jordan instance of Person class..."
    jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
    print "jordan greeting sonny using each's name..."
    jordan.greet(sonny)
    print "sonny greeting jordan using each's name..."
    sonny.greet(jordan)
    print "printing contact info for sonny, then jordan..."
    print "Name: %s; Email: %s; Phone: %s" % (sonny.name, sonny.email,
                                              sonny.phone)
    print "Name: %s; Email: %s; Phone: %s" % (jordan.name, jordan.email,
                                              jordan.email)
    print "Appending Sonny to Jordan's friend list..."
    jordan.friends.append(sonny)
    print "Appending Jordan to Sonny's friend list..."
    sonny.friends.append(jordan)
    print "Printing the length of Jordan's friend list..."
    print len(jordan.friends)
    print "Printing the number of greetings Jordan has issued..."
    print jordan.greeting_count
    print "Instantiating abe_lincoln instance of Person class..."
    abe_lincoln = Person("Abe", "abe@gmail.com", "483-485-4948")
    print "Instantiating andy instance of Person class..."
    andy = Person("Andrew", "andylolz@gmail.com", "123-456-789")
    print "Instantiating tommy instance of Person class..."
    tommy = Person("Thomas", "t_jefferson@gmail.com", "234-567-8910")
    print "adding tommy object to andy's friend list..."
    andy.add_friend(tommy)
    print "andy greeting tommy using each's name..."
    andy.greet(tommy)
    print "andy greeting abe_lincoln using each's name..."
    andy.greet(abe_lincoln)
    print "andy greeting abe_lincoln using each's name, again..."
    andy.greet(abe_lincoln)
    print "printing the number of greetings andy has issued..."
    print andy.greeting_count
    print "printing the number of unique people andy has greeted..."
    andy.num_unique_people_greeted()

if __name__ == "__main__":
    test_objects()
