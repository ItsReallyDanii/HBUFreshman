###########################################################################################
# Name: Daniel Sleiman
# Date: 09/23/2019
# Description: Easy Does it Reloaded
###########################################################################################

# function that prompts the user for a name and returns it

def userName ():
  name = input("Please enter your name: ") #Prompts the user to enter name and store the name variable
  return name

# function that receives the user's name as a parameter, and prompts the user for an age and returns it

def userAge (name):
  age = int(input("How old are you, " + name + "? ")) 
   #Displays the inputed name while asking user to enter age to store under "age" variable
  return age

# function that receives the user's name and age as parameters and displays the final output

def printInfo (name,age):
  print("Hi, "+name+". You are",age,"years old. Twice your age is "+str(age*2)+".")
  #ageTwice = (age * 2) #Does internal calculations of doubling the age to display for next output
  #return ageTwice

###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################

def main():

# get the user's name

name = userName()

# get the user's age

age = userAge(name)

# display the final output

printInfo(name,age)

main ()
