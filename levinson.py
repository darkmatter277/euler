#!/usr/bin/bash/python

list1=[]
list2=[50]
#list3=[]

#def bahra(n):
#	list1.append(range(1,n+1))
#	if min(list1) < min(list2):
#		list2.append(min(list1))
#	else:
#		list3.append(min(list1))
#	if len(list3)<n:
#		bahra(n)
#bahra(200)

#print list

for each in range (1,200):
	for n in range (1,200):
		if not n%each==0:
			list1.append(n)
			list2.append(each)
		print list1
