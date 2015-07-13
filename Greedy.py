#ACTIVITY SELECTION PROBLEM
def activityselect(s,f,n):
	i=0
	print i
	for j in range(1,n):
		if s[j]>=f[i]:
			print j
			i=j

#s=[1,3,0,5,8,5]
#f=[2,4,6,7,9,9]
#activityselect(s,f,len(s))

