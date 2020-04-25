######################################################################################################################
# Name: Daniel Sleiman
# Date: 11/19/2019
# Description: Fraction Enhancer
######################################################################################################################

def greatestCommonDivisor(numer,denom): #creates function for the greatest common denominator
   while numer != denom: #while num is not equal to denom
       if numer > denom: #under the condition numerator is greater than denominator
         numer = numer - denom #num is = to itself minues denom
       else: #otherwise condition
         denom = denom - numer #denom is set to itself minus num

   return numer #returns the numerator
      

class Fraction(object): #creates a class that takes on the argument of an object

     def __init__(self, numer=1, denom=1):  #magic function initialized
        self._num = 1 #instance variable for num created
        self._den = 1 #instance variable for den created
     
        if numer != 0 : #under condition that if the num is not 0
           self._num = numer #instance variable num is = numerator
           if denom != 0: #if denominator is not equal to 0
             self._num = int(numer / greatestCommonDivisor(abs(numer), abs(denom))) #abs is absolute value function built into python
             self._den = int(denom / greatestCommonDivisor(abs(numer), abs(denom)))
           else:
             self._den = 1 # if is not met, this will execute and set the denominator to 1
        else:
          self._num = 0 #if num is equal to 0, then num is set to 0 to fufill logic
         
      #allows the override of arithmetic operator of adding
     def __add__(self, opp): 
        return Fraction(self._num * opp._den + self._den * opp._num, self._den * opp._den)

      #allows the override of arithmetic operator of subtracting
     def __sub__(self, opp): 
        return Fraction(self._num * opp._den - self._den * opp._num, self._den * opp._den)

      #allows the override of arithmetic operator of dividing
     def __div__(self, opp): 
        return Fraction(self._num * opp._den, self._den * opp._num)

      #allows the override of arithmetic operator of multiplication
     def __mul__(self, opp):
        return Fraction(self._num * opp._num, self._den * opp._den)
      
      #method that returns the floating point representation of a fraction as a string
     def floatingValue(self):
         return str((float)(self._num)/self._den)

      #method that specifies how fractions should be displayed
     def __str__(self):
        return str(self._num) + "/" + str(self._den) + " (" + self.floatingValue() + ")"

      #getter for the numerator
     @property
     def num(self):
        return self._num
    
      #setter for the numerator
     @num.setter
     def num(self,value):
        numer = value
        denom = self._den
        self._num = int(numer / greatestCommonDivisor(abs(numer), abs(denom)))
        self._den = int(denom / greatestCommonDivisor(abs(numer), abs(denom)))

    #getter for the denominator
     @property
     def den(self):
        return self._den

      #setter for the denominator
     @den.setter
     def den(self,value):
        #print "Setter called"
        if value != 0:
          denom = value
          numer = self.num
          self._num = int(numer / greatestCommonDivisor(abs(numer), abs(denom))) 
          self._den = int(denom / greatestCommonDivisor(abs(numer), abs(denom)))
        else:
          self._den = 1
   
    

#create fractions
f1 = Fraction()
f2 = Fraction(5,8)
f3 = Fraction(3,4)
f4 = Fraction(1,0)

#display them
print "f1:", f1
print "f2:", f2
print "f3:", f3
print "f4:", f4

#play around
f3.num = 5
f3.den = 8
f1 = f2 + f3
f4.den = 88
f2 = f1 - f1
f3 = f1 * f1
f4 = f4 / f3

#display them again
print
print "f1:", f1
print "f2:", f2
print "f3:", f3
print "f4:", f4