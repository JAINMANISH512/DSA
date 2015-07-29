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

def cutrod(price):
	n=len(price)
	val=[]
	for i in range(n+1):
		val.append(0)
	for i in range(1,n+1):
		maxval=-float("inf")
		for j in range(i):
			maxval=max(maxval,price[j]+val[i-j-1])
		val[i]=maxval
	return val[n]
#print cutrod([1, 5, 8, 9, 10, 17, 17, 20])

def maxincrsum(arr):
	n=len(arr)
	msis=[]
	for i in range(n):
		msis.append(arr[i])
	for i in range(1,n):
		for j in range(i):
			if arr[j]<arr[i] and msis[i]<msis[j]+arr[i]:
				msis[i]=msis[j]+arr[i]
	return max(msis)

#print maxincrsum([1, 101, 2, 3, 100,4,5])
def bitonic(arr):
	n=len(arr)
	lis=[]
	for i in range(n):
		lis.append(1)
	for i in range(1,n):
		for j in range(i):
			if arr[j]<arr[i] and lis[i]<lis[j]+1:
				lis[i]=lis[j]+1
	lds=[]
	for i in range(n):
		lds.append(1)
	for i in range(n-2,-1,-1):
		for j in range(n-1,i,-1):
			
			if arr[j]<arr[i] and lds[i]<lds[j]+1:
				lds[i]=lds[j]+1
	maxx=0
	for i in range(n):
		if maxx<lis[i]+lds[i]-1:
			maxx=lis[i]+lds[i]-1
	return maxx
#print bitonic([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])


def palindromepartition(str1):
	n=len(str1)
	C=[]
	P=[]
	for i in range(n): #i ->last j (i=j+1 repeat)
		b=[]
		for j in range(n):
			if i==j:
				b.append(True)
			else:
				b.append(False)
		P.append(b)
		C.append(float("inf"))
	for L in range(2,n+1):
		for i in range(0,n-L+1):
			j=i+L-1
			if L==2:
				if str1[i]==str1[j]:
					P[i][j]=True
			else:
				if str1[i]==str1[j] and P[i+1][j-1]:
					P[i][j]=True

	for i in range(n):
		if P[0][i]:
			C[i]=0
		else:
			for j in range(i):
				if P[j+1][i] and C[i]>C[j]+1:
					C[i]=1+C[j]
					
	
	return C[n-1]
#print palindromepartition("ababbbabbababa")

def sumpartition(arr):
	sumx=sum(arr)
	n=len(arr)
	if sumx%2:
		return False
	part=[]
	for i in range((sumx/2)+1):
		b=[]
		for j in range(n+1):
			b.append(False)
		part.append(b)
	for i in range(n+1):
		part[0][i]=True
	for i in range(1,(sumx/2)+1):
		part[i][0]=False

	for i in range((sumx/2)+1):
	
		for j in range(n+1):
			if i>=arr[j-1]:
				part[i][j]=part[i][j-1] or part[i-arr[j-1]][j-1]
			else:
				part[i][j]=part[i][j-1]
	return part[sumx/2][n]

#print sumpartition([3, 1, 1, 2, 2, 1])

def wordwrap(l,M):
	n=len(l)
	extras=[]
	lc=[]
	c=[]
	p=[]

	for i in range(n+1):
		b1=[]

		for j in range(n+1):
			b1.append(None)
		extras.append(b1)
		lc.append(b1)
		c.append(None)
		p.append(0)
	for i in range(1,n+1):
		extras[i][i]=M-l[i-1]
		for j in range(i+1,n+1):
			extras[i][j]=extras[i][j-1]-l[j-1]-1
	for i in range(1,n+1):
		for j in range(i,n+1):
			if extras[i][j]<0:
				lc[i][j]=float("inf")
			elif j==n and extras[i][j]>=0:
				lc[i][j]=0
			else:
				lc[i][j]=extras[i][j]*extras[i][j]
	c[0]=0
	for j in range(1,n+1):
		c[j]=float("inf")
		for i in range(1,j+1):
			if (not c[i-1]==float("inf")) and (not lc[i][j]==float("inf")) and (c[i-1]+lc[i][j]<c[j]):
				c[j]=c[i-1]+lc[i][j]
				p[j]=i
	
	prinsolution(p,n)

def prinsolution(p,n):
	if p[n]==1:
		k=1
	else:
		k= prinsolution(p,p[n]-1)+1
	print "Line no " +str(k)+ " from word "+str(p[n])+" to "+str(n)
	return k
#wordwrap([3,2,2,5],6)

def maxchainlength(arr):
	n=len(arr)
	mcl=[]
	for i in range(n):
		mcl.append(1)
	for i in range(1,n):
		for j in range(i):
			if arr[i][0]>arr[j][1] and mcl[i]<mcl[j]+1:
				mcl[i]=mcl[j]+1
	return max(mcl)
#arr=[]
#for i in range(4):
#	pair=[]
#	for j in range(2):
#		pair.append(0)
#	arr.append(pair)
#arr[0][0]=5
#arr[0][1]=24
#arr[1][0]=15
#arr[1][1]=25
#arr[2][0]=27
#arr[2][1]=40
#arr[3][0]=50
#arr[3][1]=60

#print maxchainlength(arr)
class box(object):
	def __init__(self,l,b,h):
		self.l=l
		self.b=b
		self.h=h
	def __str__(self):
		return str(self.l)+str(self.b)+str(self.h)

def maxstackheight(arr):
	n=len(arr)
	rot=[]
	for i in range(n):
		rot.append(arr[i])
		rot.append(box(max(arr[i].b,arr[i].h),min(arr[i].b,arr[i].h),arr[i].l))
		rot.append(box(max(arr[i].l,arr[i].h),min(arr[i].l,arr[i].h),arr[i].b))
	#for i in range(3*n):
	#	print rot[i]
	n=3*n
	rot =sorted(rot, key=lambda rot:rot.l*rot.b,reverse=True)
	for i in range(n):
		print rot[i]
	msh=[]
	for i in range(n):
		msh.append(rot[i].h)
	print msh
	rot[6],rot[7]=rot[7],rot[6]
	for i in range(1,n):
		for j in range(i):
			#print (rot[i].l,rot[j].l) , (rot[i].b,rot[j].b) , (msh[i],msh[j]+rot[i].h)
			if (rot[i].l<rot[j].l) and (rot[i].b<rot[j].b) and (msh[i]<msh[j]+rot[i].h):
				#print i,j
				msh[i]=msh[j]+rot[i].h
	print msh
	return max(msh)
#array=[]
#array.append(box(7,6,4))
#array.append(box(3,2,1))
#array.append(box(6,5,4))
#array.append(box(32,12,10))
#print maxstackheight(array)

def minjumps(arr):
	n=len(arr)
	if n==0 or arr[0]==0:
		return float("inf")
	jumps=[]
	for i in range(n):
		jumps.append(float("inf"))
	jumps[0]=0
	for i in range(n):
		for j in range(i):
			if i<=j+arr[j] and (not jumps[j]==float("inf")):
				jumps[i]=min(jumps[i],jumps[j]+1)
				break
	#print jumps
	return jumps[n-1]
#print minjumps([1,2,6,1,0,9])

def maxsubsquare(M):
	m=len(M)
	n=len(M[0])
	S=[]
	for i in range(m):
		b=[]
		for j in range(n):
			b.append(0)
		S.append(b)
	for i in range(m):
		S[i][0]=M[i][0]
	for j in range(n):
		S[0][j]=M[0][j]
	for i in range(1,m):
		for j in range(1,n):
			if M[i][j]==1:
				S[i][j]=min(S[i-1][j-1],S[i][j-1],S[i-1][j])+1
			else:
				S[i][j]=0
	
	return max(max(S))

arr=[]
for i in range(6):
	b=[]
	for j in range(5):
		b.append(1)
	arr.append(b)
arr[0][0]=0
arr[0][3]=0
arr[1][2]=0
arr[2][0]=0
arr[2][4]=0
arr[3][4]=0
arr[5][0]=0
arr[5][1]=0
arr[5][2]=0
arr[5][3]=0
arr[5][4]=0


#print maxsubsquare(arr)

def nthugly(n):
	ugly=[]
	for i in range(n):
		ugly.append(None)
	ugly[0]=1
	i2=i3=i5=0
	nextmultipleof2=2
	nextmultipleof3=3
	nextmultipleof5=5
	for i in range(1,n):
		nextugly=min(nextmultipleof2,nextmultipleof3,nextmultipleof5)
		ugly[i]=nextugly
		if nextugly==nextmultipleof2:
			i2+=1
			nextmultipleof2=ugly[i2]*2
		if nextugly==nextmultipleof3:
			i3+=1
			nextmultipleof3=ugly[i3]*3
		if nextugly==nextmultipleof5:
			i5+=1
			nextmultipleof5=ugly[i5]*5
		
	return ugly[n-1]

#for i in range(1,151):
#	print nthugly(i)

def maxsumconti(a):
	size=len(a)
	currmax=a[0]
	maxsofar=a[0]
	for i in range(1,size):
		currmax=max(currmax+a[i],a[i])
		maxsofar=max(currmax,maxsofar)
	return maxsofar
#print maxsumconti([-2, -3, 4, -1, -2, 1, 5, -3])

def palindromesubseq(string):
	n=len(string)
	table=[]
	for i in range(n):
		b=[]
		for j in range(n):
			b.append(False)
		table.append(b)
	maxlength=1
	for i in range(n):
		table[i][i]=True
	start=0
	for i in range(n-1):
		if string[i]==string[i+1]:
			start=i
			table[i][i+1]=True
			maxlength=2
	for k in range(3,n+1):
		for i in range(0,n-k+1):
			j=i+k-1
			if table[i+1][j-1] and string[i]==string[j]:
				table[i][j]=True
				if k>maxlength:
					maxlength=k
					start=i
	print "Longest substring is : "+ string[start:start+maxlength]
	return maxlength
#palindromesubseq("forgeeksskeegfor")

def optimalbinary(keys,freq):
	n=len(keys)
	cost=[]
	for i in range(n):
		b=[]
		for j in range(n):
			b.append(float("inf"))
		cost.append(b)
	for i in range(n):
		cost[i][i]=freq[i]
	for L in range(2,n+1):
		for i in range((n-L+1)+1):
			j-i+L-1
			cost[i][j]=float("inf")
			for r in range(i,j+1):
				if r>i:
					c=cost[i][r-1]
				else:
					c=0
				if r<j:
					c+=cost[r+1][j]
				else:
					c+=0
				c+=sum(freq[i:j+1])
				if c<cost[i][j]:
					cost[i][j]=c
	print cost
	return cost[0][n-1]
#print optimalbinary([10, 12, 20],[34, 8, 50]) # check 
class node(object):
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
		self.liss=0
	def __str__(self):
		return str(self.data)
def LISS(root):
	if not root:
		return 0
	if root.liss:
		return root.liss
	if root.left==None and root.right==None:
		root.liss=1
		return (root.liss)
	liss_excl=LISS(root.left)+LISS(root.right)
	liss_incl=1
	if root.left:
		liss_incl+=LISS(root.left.left)+LISS(root.left.right)
	if root.right:
		liss_incl+=LISS(root.right.left)+LISS(root.right.right)
	root.liss=max(liss_incl,liss_excl)
	return root.liss

#root=node(20);
#root.left= node(8)
#root.left.left= node(4)
#root.left.right= node(12)
#root.left.right.left= node(10)
#root.left.right.right= node(14)
#root.right= node(22)
#root.right.right= node(25)
#print LISS(root)

def issubsetsum(arr,sumx):
	subset=[]
	n=len(arr)
	for i in range(sumx+1):
		b=[]
		for j in range(n+1):
			b.append(False)
		subset.append(b)
	for i in range(n+1):
		subset[0][i]=True
	for j in range(1,sumx+1):
		subset[j][0]=False
	for i in range(1,sumx+1):
	
		for j in range(1,n+1):
			if i<arr[j-1]:
				subset[i][j]=subset[i][j-1]
			else:
				subset[i][j]=subset[i][j-1] or subset[i-arr[j-1]][j-1]
	return subset[sumx][n]
#print issubsetsum([3, 34, 4, 12, 5, 2],9)

def kadane(arr):
	n=len(arr)
	sumx=0
	maxsum=-float("inf")
	finish=-1
	start=0
	for i in range(n):
		sumx+=arr[i]
		if sumx<0:
			sumx=0
			start=i+1
		elif sumx>maxsum:
			maxsum=sumx
			start=start
			finish=i
	if not finish==-1:
		return maxsum,start,finish
	maxsum=arr[0]
	start=finish=0
	for i in range(1,n):
		if a[i]>maxsum:
			maxsum=a[i]
			start=finish=i
	return maxsum,start,finish
#maxsum,start,finish=kadane([2,3,1,-5,6,-4,2])

def findmaxrectsum(M):
	maxsum=-float("inf")
	m=len(M)
	n=len(M[0])
	temp=[]
	for i in range(m):
		temp.append(None)

	for left in range(n):
		for i in range(m):
			temp[i]=0

		for right in range(left,n):
			for i in range(m):
				temp[i]+=M[i][right]
			
			sumx,start,finish=kadane(temp)
			if sumx>maxsum:
				maxsum=sumx
				finalleft=left
				finalright=right
				finaltop=start
				finalbottom=finish

	print finaltop,finalleft,finalbottom,finalright
	print maxsum
M=[]
for i in range(4):
	b=[]
	for i in range(5):
		b.append(0)
	M.append(b)
M[0][0]=1
M[0][1]=2
M[0][2]=-1
M[0][3]=-4
M[0][4]=-20
M[1][0]=-8
M[1][1]=-3
M[1][2]=4
M[1][3]=2
M[1][4]=1
M[2][0]=3
M[2][1]=8
M[2][2]=10
M[2][3]=1
M[2][4]=3
M[3][0]=-4
M[3][1]=-1
M[3][2]=1
M[3][3]=7
M[3][4]=-6
#findmaxrectsum(M)

def countstring(n):
	a=[]
	b=[]
	for i in range(n):
		a.append(0)
		b.append(0)
	a[0]=b[0]=1
	for i in range(1,n):
		a[i]=a[i-1]+b[i-1]
		b[i]=a[i-1]
	return a[n-1]+b[n-1]
#print countstring(3)

def countparenthe(sym,oper):
	n=len(sym)
	F=[]
	T=[]
	for i in range(n):
		b=[]
		for j in range(n):
			b.append(None)
		F.append(b)
		T.append(b)
	for i in range(n):
		if sym[i]=='F':
			F[i][i]=1
			T[i][i]=0
		if sym[i]=='T':
			T[i][i]=1
			F[i][i]=0
	for gap in range(1,n):
		for i in range((n-gap)):
			j=i+gap
			T[i][j]=F[i][j]=0
			for g in range(gap):
				k=i+g
				tik=T[i][k]+F[i][k]
				tkj=T[k+1][j]+F[k+1][j]
				if oper[k]=='&':
					T[i][j]+=T[i][k]*T[k+1][j]
					F[i][j]+=tik*tkj-T[i][k]*T[k+1][j]
				if oper[k]=='|':
					F[i][j]+=F[i][k]*F[k+1][j]
					T[i][j]+=tik*tkj-F[i][k]*F[k+1][j]
				if oper[k]=='^':
					T[i][j]+=F[i][k]*T[k+1][j]+T[i][k]*F[k+1][j]
					F[i][j]+=T[i][k]*T[k+1][j]+F[i][k]*F[k+1][j]
	return T[0][n-1]
#symbols="TTFT"
#operators="|&^"
#print countparenthe(symbols,operators) #check

def nthchair(n,m):
	n+=1
	res=[]
	for i in range(n):
		res.append(0)
	res[0]=res[1]=1
	for i in range(2,n):
		for j in range(1,m+1):
			if j>i:
				break
			res[i]+=res[i-j]
	return res[n-1]
#print nthchair(4,2)


import math
class point(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __str__(self):
		return str(self.x)+" "+str(self.y)
def dist(p1,p2):
	return math.sqrt((p1.x-p2.x)*(p1.x-p2.x)+(p1.y-p2.y)*(p1.y-p2.y))
def cost(points,i,j,k):
	return dist(points[i],points[j])+dist(points[j],points[k])+dist(points[i],points[k])
def mtcdp(points):
	n=len(points)
	if n<3:
		return 0
	table=[]
	for i in range(n):
		b=[]
		for j in range(n):
			b.append(float("inf"))
		table.append(b)
	for gap in range(n):
		for i in range(n-gap):
			j=i+gap
			if j<i+2:
				table[i][j]=0
			else:
				for k in range(i+1,j):
					val=table[i][k]+table[k][j]+cost(points,i,j,k)
					if val<table[i][j]:
						table[i][j]=val
	return table[0][n-1]

#points=[]
#points.append(point(0,0))
#points.append(point(1,0))
#points.append(point(2,1))
#points.append(point(1,2))
#points.append(point(0,2))
#for pointa in points:
#	print pointa
#print mtcdp(points)

def getcount(keypad,n):
	if keypad==None or n<=0:
		return 0
	if n==1:
		return 10
	row=[0,0,-1,0,1]
	col=[0,-1,0,1,0]
	count=[]
	for i in range(10):
		b=[]
		for j in range(n+1):
			b.append(0)
		count.append(b)
	for i in range(10):
		count[i][0]=0
		count[i][1]=1
	for k in range(2,n+1):
		for i in range(4):
			for j in range(3):
				if not (keypad[i][j]=='*' or keypad[i][j]=='#'):
					num=int(keypad[i][j])
					for move in range(5):
						ro=i+row[move]
						co=j+col[move]
						if ro>=0 and ro<4 and co>=0 and co<3 and not (keypad[ro][co]=='*' or keypad[ro][co]=='#'):
							nextnum=int(keypad[ro][co])
							count[num][k]+=count[nextnum][k-1]
	tot=0
	for i in range(10):
		tot+=count[i][n]
	return tot
keypad=[]
for i in range(4):
		b=[]
		for j in range(4):
			b.append(None)
		keypad.append(b)
keypad[0][0]='1'
keypad[0][1]='2'
keypad[0][2]='3'
keypad[1][0]='4'
keypad[1][1]='5'
keypad[1][2]='6'
keypad[2][0]='7'
keypad[2][1]='8'
keypad[2][2]='9'
keypad[3][0]='*'
keypad[3][1]='0'
keypad[3][2]='#'

print getcount(keypad,1)
print getcount(keypad,2)
print getcount(keypad,3)
print getcount(keypad,4)
print getcount(keypad,5)









	
