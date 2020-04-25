##########################################################################################
# Name: Daniel Sleiman
# Date: 10/10/2019
# Description: Search Comparison Table
##########################################################################################
import math


# a function that displays the table
def tablePrint(Min, Max, Inter):
      print('    n     |   Seq   |   bin   |   Perf  ')
      print('______________________________________________________')
      while(Min <= Max):
        if(binary(Min) == 0 ):
            print("   {}            {}          {}         {} ".format(int(Min),int(linear(Min)),int(binary(Min)),0))
        else:
            print("   {}            {}          {}         {} ".format(int(Min),int(linear(Min)),int(binary(Min)),int(linear(Min)/binary(Min))))
               # print('______________________________________________________')  
        Min = Min + Inter
      print('______________________________________________________')


# a function that calculates the maximum number of comparisons of a binary search on a list of size n
def binary(Min):
     if(Min == 0):
       return 0
     return math.ceil(math.log(Min,2))

# a function that calculates the average number of comparisons of a sequential search on a list of size n
def linear(Min): 
     return math.ceil((0+Min)/2)


###############################################
# MAIN PART OF THE PROGRAM
###############################################

# get user input for the minimum (make sure that it is >= 0)
print('Minimum number of list items (>=0)?')
Min = input()
if (Min < 0):
      print('*ERROR: Minimum must be >= 0!')

# get user input for the maximum (make sure that is is >= minimum)
print('Maximum number of list items (>= min ({}))?').format(Min)
Max = input()
if (Max < Min or Max <0):
      print('*ERROR: Maximum must be >= minimum (100)!')

# get user input for the interval (make sure that it is >= 1)
print('The interval between each row of the table (>= 1)?')
Inter = input()
if (Inter < 1):
      print('*ERROR: Interval must be >= 1!')


# generate the table
tablePrint(Min, Max, Inter)