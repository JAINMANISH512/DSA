def fibrec(n):
	if n<=1:
		return n
	return fibrec(n-1)+fibrec(n-2)

#print fibrec(40)

fiblookup=[]
for i in range(100):
	fiblookup.append(None)
def fibmem(n):
	if fiblookup[n]==None:
		if n<=1:
			fiblookup[n]=n
		else:
			fiblookup[n]=fibmem(n-1)+fibmem(n-2)
	return fiblookup[n]
#print fibmem(40)

def fibtab(n):
	fibs=[]
	for i in range(n+1):
		fibs.append(None)
	fibs[0]=0
	fibs[1]=1
	for i in range(2,n+1):
		fibs[i]=fibs[i-1]+fibs[i-2]
	return fibs[n]
#print fibtab(40)

def lis(arr):
	n=len(arr)
	lis=[]
	for i in range(n):
		lis.append(1)
	for i in range(1,n):
		for j in range(i):
			if arr[j]<arr[i] and lis[i]<lis[j]+1:
				lis[i]=lis[j]+1
	return max(lis)
#print lis([10, 22, 9, 33, 21, 50, 41, 60 ])

def lcsrec(X,Y,m,n):
	if m==0 or n==0:
		return 0
	if X[m-1]==Y[n-1]:
		return 1+lcsrec(X,Y,m-1,n-1)
	else:
		return max(lcsrec(X,Y,m-1,n) ,lcsrec(X,Y,m,n-1))
#print lcsrec("MANISH","AXIDSH",6,6)

def lcs(X,Y,m,n):
	array=[]
	for i in range(m+1):
		b=[]
		for j in range(n+1):
			b.append(0)
		array.append(b)
	
	for i in range(m+1):
		for j in range(n+1):
			if i==0 or j==0:
				array[i][j]=0
			elif X[i-1]==Y[j-1]:
				array[i][j]=array[i-1][j-1]+1
			else:
				array[i][j]=max(array[i][j-1],array[i-1][j])
	
	
	return array
def printlcs(X,Y,m,n):
	array=lcs(X,Y,m,n)
	length=max(max(array))
	print length
	result=[]
	for i in range(length):
		result.append(None)
	i=m
	j=n
	index=length-1
	while i>0 and j>0:
		if X[i-1]==Y[j-1]:
			result[index]=X[i-1]
			index-=1
			i-=1
			j-=1
		elif array[i-1][j]>array[i][j-1]:
			i-=1
		else:
			j-=1
	return str(result)
#print printlcs("AGGTAB","GXTXAYB",6,7)

def editdistrec(X,Y,m,n):
	if m==0 and n==0:
		return 0
	if m==0:
			return n
	if n==0:
			return m
	left=editdistrec(X,Y,m-1,n)+1
	right=editdistrec(X,Y,m,n-1)+1
	corner=editdistrec(X,Y,m-1,n-1)
	if not X[m-1]==Y[n-1]:
		corner+=1
	return min(left,right,corner)
#print editdistrec("SUNDAY","SATURDAY",6,8)

def editdist(X,Y):
	m=len(X)+1
	n=len(Y)+1
	dist=[]
	for i in range(m):
		b=[]
		for j in range(n):
			b.append(0)
		dist.append(b)

	for i in range(m):
		for j in range(n):
			if i==0 and j==0:
				dist[i][j]=0
			elif i==0:
				dist[i][j]=j
			elif j==0:
				dist[i][j]=i
			else:
				replace=0
				if not X[i-1]==Y[j-1]:
					replace=1
				dist[i][j]=min(dist[i-1][j]+1,dist[i][j-1]+1,dist[i-1][j-1]+replace)
	return dist[m-1][n-1]
#print editdist("SUNDAY","SATURDAY")
			

	


