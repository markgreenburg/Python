class Animal(object):
    def breed(self):
        return Animal()
    def makeNoise(self):
        print "I am an animal"

class Dog(Animal):
    def __init__(self, numLegs):
        self.numLegs = numLegs
    def woof(self):
        print "Woof...howdy"

class EagerDog(Dog):
    def __init__(self, myWoof, numLegs):
        super(EagerDog, self).__init__(numLegs)
        self.woof = myWoof

ed = EagerDog("wooof woof woof woof", 4)
print ed.numLegs

# class Pomeranian(Dog):
#     def woof(self):
#         print "woof I'm a pomeranian"

    # def woof(self):
    #     # call the super woof
    #     super(EagerDog, self).woof()
    #     # super takes 2 args: class of object in question, the object itself

# class Cat(Animal):
#     def meow(self):
#         print "Meow"
#     def breed(self):
#         return Cat()

# c = Cat()
# d = Dog()
# p = Pomeranian()
# e = EagerDog()
# c.meow()
# d.woof()
# e.woof()
# p.woof()
# kitten = c.breed()
# puppy = d.breed()
# print c.breed()
# print d.breed()
# print p.breed()
