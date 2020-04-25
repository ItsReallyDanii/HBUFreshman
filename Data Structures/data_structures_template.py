######################################################################################################################
# Name: Daniel Sleiman
# Date: 2/27/2020
# Description: Data Structures
######################################################################################################################

#write your function definitions here

import math

##########################################################
# Main code

#generate myList1 based on the description of Q1.
def numList(number):
    numbers = [0,1,2,3,4,5,6,7,8,9,10]
    if (number in numbers):
        return True
    else:
        return False

evenList = [0,2,4,6,8,10]
myList1 = filter(numList, evenList)
print myList1
############################################################
#generate myList2 based on the description of Q2.
def fact(Nums3):
    return math.factorial(Nums3)
myList2 = map(fact, range (0,10))
print myList2
############################################################
#generate myList3 based on the description of Q3.
def red(i, j):
        return i + j
myList3 = reduce(red, range(0,10001))

print myList3
############################################################
#generate myList4 based on the description of Q4.
myList4 = [math.factorial(x) for x in range (10)]

print myList4
############################################################
#generate the following lists based on the description of Q5.
myList5a = [x + 1 for x in range(9)]
print myList5a

myList5b = [2 * x for x in range(11)]
print myList5b

myList5c = [pow(x,2) for x in range(11)]
print myList5c

myList5d = [pow(x,3) for x in range(11)]
print myList5d


myList5e = [ (x + 1, pow(x + 1, 2)) for x in range(10)]
print myList5e
############################################################
#generate the following dictionaries based on the description of Q6.

myDicta = {x : pow(x,2) for x in range (1,11)}
print myDicta

stringTxt = "superfragilistic"
myDictb = {x : stringTxt[0:x] for x in range(len(stringTxt)) }
print myDictb

############################################################
#generate the form dictionary based on the description of Q7.

form = {'Chelsea': ' W D W W W', 'Tottenham': 'W L W W W', 'ManCity' : 'W W W D D', 'Liverpool': 'W L W W D' }
print form

#Update the form dictionary based on the description of Q7-b
form2 = {'Liverpool': 'L W W D L' }
form.update(form2)
print form

#Update the form dictionary based on the description of Q7-c

form.update({'ManUtd' : 'D W W D W' })
print form
#print form
