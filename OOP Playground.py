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

a = Animal()

    
