import MillerRabin
import time
import sys

if __name__ == "__main__":
	
	# some primes
	lst = []
	for i in range(2, 30):
		if MillerRabin.miller_rabin(i):
			lst.append(i)
	print("{} are the primes up to 30".format(lst))
	
	# some bigger primes
	count = 0
	for i in range(2, 10000):
		if MillerRabin.miller_rabin(i):
			count += 1
	print("{} primes up to 10000 ({}%)".format(count, count/100))
	
	# some time expensive calculation (takes ~18 secs)
	t1 = time.time() 
	
	i = 2
	count = 0
	while i < 1000000:
		if MillerRabin.miller_rabin(i):
			count += 1
		i += 1
		if (i % 100000 == 0):
			print("{}%".format(i/10000))
	t2 = time.time()
	
	print("Calculation of primes from 1 to 1 million took {} "
			"seconds. Found {} primes.".format((t2-t1), count))
