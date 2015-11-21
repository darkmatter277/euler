#!/bash/bin/dev/euler/python

notPrime=[]     							#make list for mubers that aren't prime

prime=[]								#make list for prime numbers

def primefunc(n):							#create function to find prime numbers
	for num in range(2, n):						#define each number between 2 and the last number
		for denom in range(2, num-1):				#define all numbers to divide by
			if num%denom==0:				#test all numerators divided by denominators
				notPrime.append(num)			#put all failing numerators in list notPrime
		if num not in notPrime:					#check notPrime for all numerators
			prime.append(num)				#put all numerators not in notPrime in prime


primefunc(2000000)							#call prime function

print sum(prime)							#print sum of prime

