#!bash/bin/dev/python
list1=[]
var = raw_input("Run Matrix?")

for each in range(1,200):
	for num in range(1,200):
		list1.append(each*num)
		print list1	
