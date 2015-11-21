#!/usr/bin/bash/python

FactorList=[]

primeList= []

for num in range(2, int(600851475143**0.5+1)):
	if 600851475143%num==0:
		FactorList.append(num)


def prime(n):
	for i in range (2,n):
		if n%i==0:
			if n in FactorList:
				primeList.append(n)



for each in FactorList:
	prime(each)

for num in primeList:
	if num in FactorList:
		FactorList.remove(num)


print max(FactorList)
