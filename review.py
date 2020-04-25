letters = ["a","z", "i", "o", "c", "e"]

def FilteredWay(variable):
    letters = ['a','e','i','o','u']
    if (variable in letters):
        return True
    else:
        return False

filtered = filter(FilteredWay, letters)
print filtered

#Difference is that you create a function to isolate variables to return True or False
#then is called with new variable that applies filtered condition with first parameter
#as the function created and second as the list

Nums = [1,4,7,8,4,2,7,9,3,5]

def Num(variable):
    return (pow(variable,2))

squares = map(Num, range(1,10))
print squares

#Creates a function for a specific action and then creates a new variable to
