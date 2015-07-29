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

def fibtab(n): #DP dude!!! *_*
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
			elif i==0: #insertion
				dist[i][j]=j
			elif j==0:#deletion
				dist[i][j]=i
			else:
				replace=0
				if not X[i-1]==Y[j-1]: #replace
					replace=1
				dist[i][j]=min(dist[i-1][j]+1,dist[i][j-1]+1,dist[i-1][j-1]+replace)
	return dist[m-1][n-1]
#print editdist("SUNDAY","SATURDAY")

def mincostrec(cost,m,n):
	if m<0 or n<0:
		return 9999
	if m==0 and n==0:
		return cost[m][n]
	else:
		return cost[m][n]+min(mincostrec(cost,m,n-1),mincostrec(cost,m-1,n),mincostrec(cost,m-1,n-1))
def mincost(cost,r,c,m,n):
	tc=[]

	for i in range(r):
		b=[]
		for j in range(c):
			b.append(0)
		tc.append(b)
	tc[0][0]=cost[0][0]
	for i in range(1,m+1):
		tc[i][0]=tc[i-1][0]+cost[i][0]
	for i in range(1,n+1):
		tc[0][i]=tc[0][i-1]+cost[0][i]
	for i in range(1,m+1):
		for j in range(1,n+1):
			tc[i][j]=cost[i][j]+min(tc[i-1][j-1],tc[i][j-1],tc[i-1][j])
	return tc[m][n]

cost=[]
for i in range(3):
	b=[]
	for j in range(3):
		b.append(0)
	cost.append(b)
cost[0][0]=1
cost[0][1]=2
cost[0][2]=3
cost[1][0]=4
cost[1][1]=8
cost[1][2]=2
cost[2][0]=1
cost[2][1]=5
cost[2][2]=3

#print mincostrec(cost,2,2)
#print mincost(cost,3,3,2,2)

def coinchangerec(s,m,n):
	if n==0:
		return 1
	if n<0:
		return 0
	if m<=0 and n>0:
		return 0
	return coinchangerec(s,m-1,n)+coinchangerec(s,m,n-s[m-1])
#print coinchangerec([1,2,3],3,4)

def coinchange(s,m,n):
	arr=[]
	for i in range(n+1):
		arr.append(0)
	arr[0]=1
	for i in range(m):
		for j in range(s[i],n+1):
			arr[j]=arr[j]+arr[j-s[i]]
	
	return arr[n]
#print coinchange([1,2,3],3,4)

def binomialrec(n,k):
	if k==0 or k==n:
		return 1
	return binomialrec(n-1,k-1)+binomialrec(n-1,k)
#print binomialrec(5,2)

def binomial(n,k):
	res=[]
	for i in range(n+1):
		b=[]
		for j in range(k+1):
			b.append(0)
		res.append(b)
	for i in range(n+1):
	
		for j in range(min(i,k)+1):
			if j==0 or j==i:
				res[i][j]=1
			else:
				res[i][j]=res[i-1][j-1]+res[i-1][j]
	return res[n][k]
#sprint binomial(5,2)





def lismj(arr):
	n=len(arr)
	lis=[]
	for i in range(n):
		lis.append(1)
	for i in range(1,n):
		for j in range(i):
			
			if arr[j]<arr[i] and lis[i]<lis[j]+1:
				lis[i]=lis[j]+1
				
			
	print max(lis)
#lismj([10, 22, 9, 33, 21, 50, 41,55, 60 ])

def lcsmj(X,Y):
	m=len(X)
	n=len(Y)
	res=[]
	for i in range(m+1):
		col=[]
		for j in range(n+1):
			col.append(0)
		res.append(col)
	for i in range(m+1):
		for j in range(n+1):
			if i==0 or j==0:
				res[i][j]=0
			else:
				if X[i-1]==Y[j-1]:
					res[i][j]=res[i-1][j-1]+1
				else:
					res[i][j]=max(res[i][j-1],res[i-1][j])
		
	
	print max(max(res))
#lcsmj("Do you know what it feels like","yes i Know")

def editdistmj(X,Y):
	m=len(X)+1
	n=len(Y)+1
	res=[]
	for i in range(m):
		col=[]
		for j in range(n):
			col.append(0)
		res.append(col)

	
	for i in range(m):
		for j in range(n):
			if i==0 and j==0:
				res[i][j]=0
			elif i==0:
				res[i][j]=j
			elif j==0:
				res[i][j]=i
			else:
				replace=0
				if not X[i-1]==Y[j-1]:
					replace=1
				res[i][j]=min(res[i-1][j]+1,res[i][j-1]+1,res[i-1][j-1]+replace)
	print res[m-1][n-1]
#editdistmj("SUNDAY","SATURDAY")

def matrixchainorder(p):
	n=len(p)
	m=[]
	for i in range(n):
		beta=[]
		for j in range(n):
			beta.append(0)
		m.append(beta)

	for l in range(2,n):
		for i in range(1,(n-l+1)):
			j=i+l-1
			print i,j
			m[i][j]=float("inf")
			for k in range(i,(j-1)+1):
				q=m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
				if q <m[i][j]:
					m[i][j]=q
	return m[1][n-1]
#print matrixchainorder([1,2,3,4])
def zerooneknapsack(W,wt,val):
	n=len(val)
	K=[]
	for i in range(n+1):
		beta=[]
		for j in range(W+1):
			beta.append(0)
		K.append(beta)
	for i in range(n+1):
		for w in range(W+1):
			if i==0 or w==0:
				K[i][w]=0
			elif wt[i-1]<=W:
				K[i][w]=max(val[i-1]+K[i-1][w-wt[i-1]],K[i-1][w])
			else:
				K[i][w]=K[i-1][w]
	return K[n][W]
val = [60, 100, 120]
wt = [10, 20, 30]
#print zerooneknapsack(50,wt,val)

def eggdrop(n,k):
	eggfloor=[]
	for i in range(n+1):
		beta=[]
		for j in range(k+1):
			beta.append(0)
		eggfloor.append(beta)
	for i in range(1,n+1):
		eggfloor[i][1]=1
		eggfloor[i][0]=0
	for j in range(1,k+1):
		eggfloor[1][j]=j
	for i in range(2,n+1):
		for j in range(2,k+1):
			eggfloor[i][j]=float("inf")
			for x in range(1,j+1):
				res=1+max(eggfloor[i-1][x-1],eggfloor[i][j-x])
				if res<eggfloor[i][j]:
					eggfloor[i][j]=res

	return eggfloor[n][k]

#print eggdrop(2,36)

def lps(mystring):
	n=len(mystring)
	L=[]
	for i in range(n+1):
		beta=[]
		for j in range(n+1):
			beta.append(0)
		L.append(beta)
	for i in range(n):
		L[i][i]=1
	for cl in range(2,n+1):
		for i in range(0,n-cl+1):
			j=i+cl-1
			if mystring[i]==mystring[j] and cl==2:
				L[i][j]=2
			elif mystring[i]==mystring[j]:
				L[i][j]=L[i+1][j-1]+2
			else:
				L[i][j]=max(L[i][j-1],L[i+1][j])
	return L[0][n-1]

#print lps("GEEKS FOR GEEKS")


