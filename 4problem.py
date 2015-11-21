#!/usr/bin/bash/python

numList=[]
def prdct():
	for a in range (100,999):
		for b in range(100,999):
			num=a*b
		  	if str(num)[::-1]==str(num):
		 		numList.append(num)

prdct()
print max(numList)
