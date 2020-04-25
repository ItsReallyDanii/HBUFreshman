###########################################################################################
# Name: Daniel Sleiman
# Date: 10/14/2019
# Description: A fantastically fabulous list
###########################################################################################
def getList ():
  global list
  list = []
  n = int(input("How many integers would you like to add to the list? "))

  for i in range (0,n):
    nums = int(input(("Enter an integer: " )))
    list.append(nums)


# function that:
# (1) prompts the user for a list size
# (2) prompts the user for the integers to store in the list (corresponding to the list size)
# (3) creates the list
# (4) returns the list



###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# create the list

getList()

# display information about the list using the list functions discussed in class
sort = sorted(list)
reverse = reversed(list)
print "The original list: {} ".format(list)
print "The length of the list is {} ".format(len(list))
print "The minimum value in the list is {} ".format(min(list))
print "The maximum value in the list is {} ".format(max(list))
print "The reversed list: {} ".format(list[::-1])
print "The sorted list: {} ".format(sort)


# there is no need to write/call your own functions here