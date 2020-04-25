from random import randint, seed
from time import sleep

seed(randint(0,1234))
for i in range(1, 101):
	print "{}\t".format(randint(0, 99)),
	if (i % 10 == 0):
		print
print
sleep(3)
seed(randint(0,1234))
for i in range(1, 101):
	print "{}\t".format(randint(0, 99)),
	if (i % 10 == 0):
		print
