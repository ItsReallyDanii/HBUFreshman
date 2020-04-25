"""#Sub-class - inherits state and behavior from another class called a
#Super-class - gives states and behaviors to subclasses
#This allows us avoid excessive repetition and code duplication."""


#####################################################################


#Example Code.
#You are writing a program to store information about kinds of vehicles that come into mechanics
#garage in a daily basis. You are tracking # of tires, if engine works and cars owner. These
#elements are known as the instance variables to match the attributes of the class.

class Car(object):
    def __init__(self, name):
        self.tires = 4
        self.engine = True
        self.owner = name

    def __str__(self):
        return "Car; owner={}, tires={}, engine={}"\
            .format(self.owner, self.tires, self.engine)
c1 = Car("John")
print c1

#will print Car; owner=John, tires=4, engine=True
class Car(object):
    def __init__(self, name):
        self.tires = 4
        self.engine = True
        self.owner = name
    def __str__(self):
        return "Car; owner={}, tires={}, engine={}"\
                .format(self.owner, self.tires, self.engine)
class Bicycle:
    def __init__(self, name):
        self.tires = 2
        self.engine = False
        self.owner = name
    def __str__(self):
        return "Bicycle; owner={}, tires={}, engine={}"\
                .format(self.owner, self.tires, self.engine)

c1 = Car("John")
b1 = Bicycle("Jane")
print c1
print b1

"""#Output will be Car; owner=John, tires=4, engine=True
            #Bicycle; owner=Jane, tires=2, engine=False
#This method is very ineffective because it creates a new class for each type of Vehicle presented"""
#####################################################################
#In order to avoid confusion presented and make it cohesive, a Vehicle class can be created

class Vehicle(object):
    def __init__(self, name):
        #set to None so that they can be overwritten depending on subclass
        self.tires = None
        #set to None so that they can be overwritten depending on subclass
        self.engine = None
        #set to None so that they can be overwritten depending on subclass
        self.owner = name

    def __str__(self):
        return "owner={}, tires={}, engine={}"\
                .format(self.owner, self.tires, self.engine)

class Car(Vehicle):
#Vehicle superclass is the constructor of each of the subclasses
#This sets the default values for the variables tires and engines.
#The owner of vehicle is passed with instansiating the subclasses and is forwarded
#to the superclass(where it is formally assigned)
#Initialziation of the subclasses is done after call to constructor in superclass (Ex/ tires and engine)
    def __init__(self, name):
        Vehicle.__init__(self, name)
        self.tires = 4
        self.engine = True

    def __str__(self):
        return "Car; " + Vehicle.__str__(self)

class Bicycle(Vehicle):
    def __init__(self, name):
        Vehicle.__init__(self, name)
        self.tires = 2
        self.engine = False

    def __str__(self):
        return "Bicycle; " + Vehicle.__str__(self)

class Motorcycle(Vehicle):
    def __init__(self, name):
        Vehicle.__init__(self, name)
        self.tires = 2
        self.engine = True

    def __str__(self):
        return "Motorcycle; " + Vehicle.__str__(self)

c1 = Car("John")
b1 = Bicycle("Jane")
m1 = Motorcycle("Randy")
print c1
print b1
print m1

"""#The output of the program:
#Car; owner=John, tires=4, engine=True
#Bicycle; owner=Jane, tires=2, engine=False
#Motorcycle; owner=Randy, tires=2, engine=True"""
#####################################################################
"""#This is the same thing as above, except we created a new class called Cycle that inherits
#from the Vehicle class its properties, but defines it own instances that passes on its attributes
#to the bicycle and motorcycle class"""

class Vehicle(object):
    def __init__(self, name):
        self.tires = None
        self.engine = None
        self.owner = name


    def __str__(self):
        return "owner={}, tires={}, engine={}"\
                .format(self.owner, self.tires, self.engine)

class Car(Vehicle):
    def __init__(self, name):
        Vehicle.__init__(self, name)
        self.tires = 4
        self.engine = True

    def __str__(self):
        return "Car; " + Vehicle.__str__(self)

class Cycle(Vehicle):
    def __init__(self, name):
        Vehicle.__init__(self, name)
        self.tires = 2

class Bicycle(Cycle):
    def __init__(self, name):
        """The profound difference is to change constructor body to Cycle.__init__ instead of
        #Vehicle.__init__. You do not have to set self.tires or engine becuase it was set if __name__ == '__main__':
        #the Cycle class."""
        Cycle.__init__(self, name)
        self.engine = False

    def __str__(self):
            return "Bicycle; " + Vehicle.__str__(self)

class Motorcycle(Cycle):
    def __init__(self, name):
        """The profound difference is to change constructor body to Cycle.__init__ instead of
        #Vehicle.__init__. You do not have to set self.tires or engine becuase it was set if __name__ == '__main__':
        #the Cycle class."""
        Cycle.__init__(self, name)
        self.engine = True
    def __str__(self):
        return "Motorcycle; " + Cycle.__str__(self)

c1 = Car("John")
b1 = Bicycle("Jane")
m1 = Motorcycle("Randy")
print c1
print b1
print m1

#####################################################################

"""Abstraction is the ability to ignore the details of parts of a system in order to focus
#attention on a higher detail.
#An object represents a way of abstracting away data and operations into a SINGLE everything
#with the data being the state and the operations being the behavior.
#Programmers just need to know what function to call, what parameters to pass and if return value is expected

#Modularization - Dividing a whole into well-defined parts that can be built and examined seperatley

#Method Lookup- solves the problem of finding the right method to call in a class heirarchy with
#Polymorphisism - idea of having multiple methods with the same name in multiple subclasses
#Example of this includes the __str__ magic method

#Method lookup essentially works if a specifief function is not found at the class, it searches
#for the matching function in the supeclass and goes up hierarchy"""

#####################################################################

#Polymorphisism example
class Shape(object):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def draw(self):
        for i in range(self.width):
            print "* " * self.length

class Rectangle(Shape):
    def __init__(self, l, w):
        Shape.__init__(self, l , w)

class Square(Shape):
    #constructor has only one argument
    def __init__(self, l):
        Shape.__init__(self, l, l)

class Triangle(Shape):
    def __init__(self, l):
        Shape.__init__(self, l, l)
#Has its own draw function since the shape is different
    def draw(self):
        for i in range(self.width):
            print "* " * (self.width - i)

r1 = Rectangle(12,4)
r1.draw()
print
s1 = Square(6)
s1.draw()
print
t1 = Triangle(7)
t1.draw()

#####################################################################
#Single inhertiance is when a class inherits traits from a single superclass
#Multiple inheritance is when a class inhereits traits from 2 or more superclasses.

#Take the example of a banana class that stems from Fruit Class with features such as
#origin and if it is fresh. Another class it stems from is SaleItem with price,
#inventory and location as instance variables. This would look like This

"""class Banana(Fruit, SaleItem)"""

#If there are superclasses with the same function name, it inherits from the first one listed
#####################################################################
"""#An abstract metod in a class is a way of promisimg that any subclass of some superclass
#will provide implementation details for that method. This means that it has a method
#lined up, but details will come from subclasses specific to their instances"""

#Abstract methods can RAISE an error known as NotImplementedError.
#This occurs wehn a subclass does not implement a function defined as abstract in the superclass
#and an object reference of the subclass tries to call it, the error will be raised.
#This terminates the program

class Animal(object):
#Animal class has constructor and abstract function called communicate.
#Making the function abstract is a way of enforcing that all subclasses have an actal implementation
#of it (instead of hoping whoever is working on that class remembers to implement it)
    def __init__(self):
    #Constructs a new Animal
    #Pass OR """ ___ """ is for skipping a function for when a program will return to it. Fun fact!
        """ Constructs a new Animal """
    def communicate(self):

        """ How an animal communicates """
        raise NotImplementedError("Abstract method communicate not implemented in subclass!")

class Bird(Animal):
    def __init__(self):

        """ Constructs a new Bird """

#Bird class has not implemented the communicate function for this example. Therefore the
#statement b.communicate() causes the NotImplementedError. We can use method lookup to
#see that it seeks the Animal class communicate functuon that raises the error
b = Bird()
b.communicate()
#####################################################################

""" #Another way of implementing abstract method is by using Abstract Base Class (abc)
#library that is packged with Python that marks a method as abstract the same way you can use
#mutators and accescors. The difference is the decorator used to mark the function @abc.abstractmethod
#This method ensures tha a TypeError will be raised immediatley upon the instansiation
#of a subclass if the abstract method is not implemented in the subclass """

#Imports the ABC library (Abstract Base Class)
import abc

class Animal(object):
    #Statement that must be declared to be used as a decorator
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """ Constructs a new Animal """

    #To implement TypeError if subclass if the abstract method is not implemented
    @abc.abstractmethod
    def communicate(self):
        """ How an animal communicates """

class Bird(Animal):
    def __init__(self):
            """ Constructs a new Bird """

b = Bird()
b.communicate()

#Error will be as follows

""" Traceback (most recent call last):
 File "...\02 More on Objects\code\abstract3.py", line 17, in <module>
 b = Bird()
TypeError: Can't instantiate abstract class Bird with abstract methods communicate """

#This program would work if the abstract method is implemented with the Bird class
#as follows
"""
def communicate(self):
    #How an animal communicates
    print "A Bird communicates!" """

#####################################################################

#Abstract classes are best used qt the bottom of the heirarchy since they are
#specific enough to each category you are creating.

#Abstract classes are designed to soley be used as superclasses and never instansiated
#instandiated means used in code.

#Abstract classes are ALWAYS used with the ABC library
#If you just want to make one or more functions in a class abstract but not the entire class,
#then use the first method. raise NotImplementedError("Abstract method communicate not implemented in subclass!")

import abc

class Animal(object):
    #Statement that must be declared to be used as a decorator
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """ Constructs a new Animal """

    #To implement TypeError if subclass if the abstract method is not implemented
    @abc.abstractmethod
    def communicate(self):
        """ How an animal communicates """

class Bird(Animal):
    def __init__(self):
            """ Constructs a new Bird """

    def communicate(self):
        #How an animal communicates
        print "A Bird communicates!"

#Attempt to declare and instance of the Animal class
a = Animal()

#This program basically locks the Animal class since communicate function is locked
#Abstrct classes are a framework for the subclasses that it has to check and follow
#Concrete classes are those that can be instansiated
#####################################################################
#Unit - reasonable self contained compoenent of a program
#Example includes class or function depending on the level of abstraction

#Coupling refers to the links between the seperate unites of a program
#Example:// if 2 classes closeley depend on each other then they are tightly coupled
#We try to avoid tight coupling.


#Cohesion refers to # and diveristy of taks a unit is responsible for
#Example:// if unit is responsible for single task then it has high cohesion
#Multiple tasks = low cohesion
