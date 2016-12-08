'''
OOP 101 notes / scratchpad
'''

class Person(object): # name of class, inherits (object)
    '''
    Makes a person with name and life
    '''
    alive = True
    def __init__(self, fname, lname, user_info={}): # change constructor to
                                                    # pass in what we want. Be
                                                    # careful with empty
                                                    # dictionary here....
        '''
        Sets name of each instance of the Person class to janice
        '''
        self.name = user_info.get("name", "")
        self.user_name = user_info.get('user_name', "")
        self.gender = user_info.get("gender", "")
        self.fname = fname
        self.lname = lname
    def greet(self): # the self parameter refers to the object itself
        '''
        Greets an instance of the Person object
        '''
        print 'Hello, %s!' % self.name
        print 'Hello, %s!' % self.fname
    def kill(self):
        '''
        Sets life to False and print who we killed
        '''
        self.alive = False
        print "We just killed %s" % self.name
        print "We just killed %s" % self.fname
