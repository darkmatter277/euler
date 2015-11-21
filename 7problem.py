#!/bash/bin/python/euler


notprimeList=[]

primeList=[]

def prime(n):
	for each in range(2, n):
		for num in range(2, each-1):
			if each%num==0:
				notprimeList.append(each)
		if each not in notprimeList:
			primeList.append(each)
	



prime(100)
print primeList
