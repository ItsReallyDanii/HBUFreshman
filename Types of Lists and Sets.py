#Manual Way
#################################################################################
Letters = ["a","z","i","o","c","e"]
Vowels = []

for i in Letters:
    if (i == "a" or i == "e" or i == "i" or i == "u"):
        Vowels.append(i)

print Vowels
#################################################################################
#Filtered Way
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


sequence = ["a","z","i","o","c","e"]

filtered = filter(fun, sequence)

print filtered
#################################################################################
#Mapping lists

Nums = [1,4,7,8,4,2,7,9,3,5]
Nums2 = []

for i in Nums:
    Nums2.append(pow(i,2))

print Nums2
#################################################################################
def Num(number):
    return (pow(number,2))

#=Can be range
squares = map(Num, range (1,10))
#Also an be array argument
square = map(Num, Nums)
print squares
print square
#################################################################################
#Reduing lists. Returns single value instead of whole list like everything else
def red(x,y):
    return x *y
fact = reduce(red, range(1,5))
print fact

#################################################################################
#List comprehension manual

NumList = []
for i in range (0,21):
    if i % 2 == 0:
        NumList.append(i)

print NumList
#################################################################################
#List comprehension implied

z = [i for i in range (10) if i % 2 == 0]
print z
       # function         #Lists             #condition
sums = [x + y for x in [1,2,3] for y in [3,1,4] if x != y]
print sums
#################################################################################
#cubed comprehension
cubes = [x**3 for x in range (11)]
print cubes
#################################################################################
#Set is another python sequence that comtains unordered collection or unique values
#Defining sets is as follows: Ex/: a = {1,2,3,4,5}
#Can convert lists to sets
#Examples
#c = [1,2,3,4,5,6,3]
#d = set(c)  <----- This will result in [1,2,3,4,5,6], without the extra 3 because it has to have unique individual values

#Union is the set of values that are memeber of A or B or both. Defined as A U B
#In Python, this can be declared with A|B (in other languages this is OR)

#Intersection is the set of values that are in both A and B. Defined as A ^ B
#In Python, this is declared with A & B

#Difference is the set of values that are in one set that is not found in another set
# In Python, this is defined as a - b
#################################################################################
#Dictionaries store elements so that they can be located quickly using keys
#Defined as <key, value> tuples. Keys are unique.

#Functions to edit dictionary key
#Deletion = del offices ["Smith"]
#Checking if key exits in dictionary = if ("Smith" in offices): Returns True or False statement
#Obtain a list of all keys in dictionary = keys = offices.keys()
#Retreives key value print offices ["Kennedy"]
#################################################################################
#Can use dictionaries with list comprehensions
#Example:// dict = { x: x**3 for i in range (1,6)}
#What is stored is x is value and x^3 would be value that is stored in dictionary
