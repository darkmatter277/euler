#!/bash/bin/dev/euler_problem/

n=range(0,1000)

truei_val=[]

for val in n:
	if val%3==0:
		truei_val.append(val)
	elif val%5==0:
		truei_val.append(val)


print sum(truei_val)
