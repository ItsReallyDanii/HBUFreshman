class Greeting(object):
    def __init__(self, mainString):

        self.superString = mainString

    @property
    def superString(self):
        return self._superString

    @superString.setter
    def superString(self, mainString):
        self._superString = mainString

    def get_Greeting(self):
        return self.superString.lower()

    def print_Greeting(self):
        return "{}".format(self.superString.upper())



class HBUGreeting(Greeting):
    def __init__(self, mainString):

        self.superString = mainString

    @property
    def superString(self):
        return self._superString

    @superString.setter
    def superString(self, mainString):
        self._superString = mainString

    def get_Greeting(self):
        return self.superString.lower()

    def print_Greeting(self):
        return "Welcome to HBU, here is our greeting to you: {}".format(self.superString)






GreetMessage = raw_input("Greet Me! \n")

c1 = Greeting(GreetMessage)
c2 = HBUGreeting(GreetMessage)


t2 = c1.print_Greeting()
t3 = c2.print_Greeting()


t4 = c1.get_Greeting()
t5 = c2.get_Greeting()

print
print "print_Greeting() results"
print "-------------------------"
print t2
print t3
print
print "get_Greeting() results"
print "-------------------------"
print t4
print t5
