'''
CS 241 Lab 8

File:        fib.py

Description: Two types of Fibonacci Implementation: looping technique and
	     recursion.
	     

Created by:  Ulises Giacoman (ugiacoma)
'''

import time

def main():
	""" Prints dialogue to compare two different types of Fibonacci Sequence
	    Implementation. Then calls for a print of Histogram to double check
	    Sequence calculators are correct. 
	
	"""
    
	n = int(input("Enter n: "))
	print()
    
	t0 = time.time()
	f1 = fib1(n)
	print("fib1(%d) = %d" % (n, f1))
	t1 = time.time()
	print("fib1 elapsed time is %5.3f." % (t1-t0))
    
	print()

	t0 = time.time()
	f2 = fib2(n)
	print("fib2(%d) = %d" % (n, f2))
	t1 = time.time()
	print("fib2 elapsed time is %5.3f." % (t1-t0))
    
	print()

	if f1 != f2:
		print("Test failed!")

	print()
    
	printFibHistogram(10)

def fib1(n):
	""" Non-Recursive Version of Fibonacci Sequence using Looping 
	Technique
	
	Arguments:
	n - The nth term in the Fibonacci sequence.
	"""
	if n == 1 or n == 0:
		return n
	else:
		countOne, countTwo = 1,1
		for number in range(n - 1):
			countOne, countTwo = countTwo, (countOne + countTwo)
		return countOne
	
def fib2(n):
	""" Recursive Version of Fibonacci Sequence
	
	Arguments:
	n - The nth term in the Fibonacci sequence.
	"""
	assert n >= 0, 'Fibonacci not defined for n < 0'
	if n == 1 or n == 0:
		return n
	else:
		return fib2(n - 1) + fib2(n - 2)

def printFibHistogram(n):
	""" Prints Histogram check. If Histograms match, the algorithms are
	correct.
	
	"""
    
	for i in range(n):
    	    print('*' * fib1(i+1))
   	 
	print("\nCheck the above and below histogram to see if they are identical")
	print("Otherwise, something is wrong!\n")

	for i in range(n):
    	    print('*' * fib2(i+1))

main()