#!/usr/bin/bash/python

numList=[]
yesList=[]
notList=[]
for each in range (1,21):
	numList.append(each)

def multpl(num):
	for i in range (1,num):
		for n in numList:
			if not i%n==0:
				notList.append(i)
		if i not in notList:
			yesList.append(i)


multpl(500000)

print numList

print yesList
