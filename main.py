def userName ():
  name = input("Please enter your name: ") #Prompts the user to enter name and store the name variable
  return name

def userAge (name):
  age = int(input("How old are you, " + name + "? ")) 
   #Displays the inputed name while asking user to enter age to store under "age" variable
  return age

def printInfo (name,age):
  print("Hi, "+name+". You are",age,"years old. Twice your age is "+str(age*2)+".")
  #ageTwice = (age * 2) #Does internal calculations of doubling the age to display for next output
  #return ageTwice


def main():
  name = userName()
  age = userAge(name)
  printInfo(name,age)

main ()