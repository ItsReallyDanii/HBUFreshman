################################
# Name:Daniel Sleiman
# Date:02/05/2020
################################

#import timeit python library
import timeit
import math

#factorial recursive method
def fact_rec(n):
	if (n==1 or n ==0):
		return 1
	else:
		return n*fact_rec(n-1)
	pass

#factorial iterative method
def fact_iter(n):
	j = 1
	for i in range(1, n + 1):
		j *= i
	return j
	pass

#power iterative method
def pow_iter(x,y):
	z = pow(x,y)
	return z
	pass

#power recursive method
def pow_rec(x,y):
	if y == 0:
		return 1
	if y >= 1:
		return x * pow_rec(x, y - 1)
	pass

#fibonacci iterative
def fib_iter(n):
	a, b = 0, 1
	for i in range (0, n):
		a, b = b, a + b
	return a

#fibonacci recursive
def fib_rec(n):
	if n <= 1:
		return n
	else:
		return (fib_rec(n-1) + fib_rec(n-2))

#testing the methods
#Uncomment each line to test your method implementation
print (fact_iter(5))
print (fact_rec(5))
print (pow_rec(2,5))
print (pow_iter(2,5))
print (fib_iter(10))
print (fib_rec(10))


#Main program

time = timeit.repeat("fact_iter(5)", setup = "from __main__ import fact_iter", number = 10000, repeat = 3)
print "Execution time for Iterative factorial is: {} " .format(time)
time1 = timeit.repeat("fact_rec(5)", setup = "from __main__ import fact_rec", number = 10000, repeat = 3)
print "Execution time for Recursive factorial is: {} " .format(time1)
print "*******************************************"

time2 = timeit.repeat("pow_iter(2, 5)", setup = "from __main__ import pow_iter", number = 10000, repeat = 3)
print "Execution time for Iterative power is: {} " .format(time2)
time3 = timeit.repeat("pow_rec(2, 5)", setup = "from __main__ import pow_rec", number = 10000, repeat = 3)
print "Execution time for Recursive power is: {} " .format(time3)
print "*******************************************"

time4 = timeit.repeat("fact_iter(10)", setup = "from __main__ import fact_iter", number = 10000, repeat = 3)
print "Execution time for Iterative Fibonnaci is: {} " .format(time4)
time5 = timeit.repeat("fact_rec(10)", setup = "from __main__ import fact_rec", number = 10000, repeat = 3)
print "Execution time for Recursive Fibonnaci is: {} " .format(time5)
print "*******************************************"
#Call timeit.repeat for each method
#Print reported times
#See the program description for the sample output
