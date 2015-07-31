def permute(str1,l,r):
	if l==r:
		print str1
		print "\n"
	else:
		for i in range(l,r+1):
			str1[i],str1[l]=str1[l],str1[i]
			permute(str1,l+1,r)
			str1[i],str1[l]=str1[l],str1[i]
mystring="MANISH"
#permute(list(mystring),0,len(mystring)-1)


def solvektutil(x,y,movei,sol,xmove,ymove):
	if movei==len(sol)*len(sol):
		return True
	for k in range(8):
		nx=x+xmove[k]
		ny=y+ymove[k]
		if nx>=0 and nx<len(sol) and ny>=0 and ny<len(sol)and sol[nx][ny]==-1:
			sol[nx][ny]=movei
			if solvektutil(nx,ny,movei+1,sol,xmove,ymove):
				return True
			else:
				sol[nx][ny]=-1
	return False
def solvekt(N):
	sol=[]
	for i in range(N):
		b=[]
		for j in range(N):
			b.append(-1)
		sol.append(b)
	xmove=[ 2, 1, -1, -2, -2, -1,  1,  2]
	ymove=[1, 2,  2,  1, -1, -2, -2, -1]
	sol[0][0]=0
	if solvektutil(0,0,1,sol,xmove,ymove):
		print sol
	else:
		print "NO sol"

#solvekt(6)
def ratutil(maze,sol,x,y):
	if x==len(sol)-1 and y==len(sol)-1:
		sol[x][y]=1
		return True
	if x>=0 and x<len(sol) and y>=0 and y<len(sol)and maze[x][y]==1:
		sol[x][y]=1
		if ratutil(maze,sol,x+1,y):
			return True
		if ratutil(maze,sol,x,y+1):
			return True
		sol[x][y]=0
		return False
	return False

	
	return False
def ratmaze(maze):
	N=len(maze)
	
	sol=[]
	for i in range(N):
		b=[]
		for j in range(N):
			b.append(0)
		sol.append(b)
	#sol[0][0]=1
	if ratutil(maze,sol,0,0):
		print sol
	else:
		print "NO sol"
maze=[]
maze.append([1,0,0,0])
maze.append([1,1,0,1])
maze.append([0,1,0,0])
maze.append([1,1,1,1])
print maze
ratmaze(maze)


