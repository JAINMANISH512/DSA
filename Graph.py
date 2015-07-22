import random
class adjnode(object):
    def __init__(self,dest,weight=0,next=None):
        self.dest=dest
        self.next=next
        self.weight=weight
        
    def __str__(self):
        return str(self.dest)+str(self.weight)

class adjlist(object):
    def __init__(self,head=None,tail=None):
        self.head=head
        self.tail=tail
    
    def __str__(self):
        current=self.head
        a=[]
        while current:
            a.append(current.dest)
            current=current.next
        return str(a)
    
class graph(object):
    def __init__(self,v):
        self.v=v
        self.array=[]
        self.indeg=[]
        self.outdeg=[]
        for i in range(v):
            self.array.append(adjlist(None))
            self.indeg.append(0)
            self.outdeg.append(0)

    def __str__(self):
        return str(self.array)

class edge(object):
    def __init__(self,src,dest,weight):
        self.src=src
        self.dest=dest
        self.weight=weight
    
    def __str__(self):
        return str(self.src)+"---->"+str(self.weight)+"----->"+str(self.dest)
class newgraph(object):
    def __init__(self,v,e):
        self.v=v
        self.e=e
        self.edgelist=[]
        for i in range(self.e):
            self.edgelist.append(edge(None,None,None))
    def __str__(self):
    	res=[]
    	for i in range(self.e):
    		b=[]
    		b.append(self.edgelist[i].src)
    		b.append(self.edgelist[i].weight)
    		b.append(self.edgelist[i].dest)
    		res.append(b)
    	return str(res)
    def sortedges(self):
        for i in range(self.e-1):
            for j in range(i+1,self.e):
                if self.edgelist[i].weight>self.edgelist[j].weight:
                    temp=self.edgelist[i].weight
                    self.edgelist[i].weight=self.edgelist[j].weight
                    self.edgelist[j].weight=temp
                    temp=self.edgelist[i].src
                    self.edgelist[i].src=self.edgelist[j].src
                    self.edgelist[j].src=temp
                    temp=self.edgelist[i].dest
                    self.edgelist[i].dest=self.edgelist[j].dest
                    self.edgelist[j].dest=temp



class queue(object):
    def __init__(self,front=None,back=None):
		self.front=None
		self.back=None
    def __str__(self):
        current=self.front
        a=[]
        while current:
            a.append(current.dest)
            current=current.next
        return str(a)
    def isemp(self):
        return self.front==None
    def enq(self,data):
    	new=adjnode(data)
    	if self.front==None:
    		self.front=self.tail=new
    	else:
    		self.tail.next=new
    		self.tail=new
    def deq(self):
    	if not self.isemp():
    		temp=self.front
    		data=temp.dest
    		self.front=self.front.next
    		del temp

    		return data
    	else :
    		return -1
    def frontele(self):
    	if self.isemp():
    		return self.front.dest
    	else:
    		return -1
def printgraph(g):
    for src in range(g.v):
        print str(src)+ "->"+str(g.array[src])
        

def addedge(g,src,dest,weight=0):
	#print str(src)+"->"+str(dest)+"added"
	new=adjnode(dest,weight,g.array[src].head)
	g.array[src].head=new
	g.indeg[dest]+=1
	g.outdeg[src]+=1

	return g
def adduedge(g,src,dest,weight=0):
	addedge(g,src,dest,weight)
	addedge(g,dest,src,weight)
	return g
def addedgeend(g,src,dest,weight=0):
	#print str(src)+"->"+str(dest)+" added"
	new=adjnode(dest,weight)
	if g.array[src].tail==None:
		g.array[src].head=g.array[src].tail=new
	else:
		g.array[src].tail.next=new
		g.array[src].tail=new
	g.indeg[dest]+=1
	g.outdeg[src]+=1
	return g

def adduedgeend(g,src,dest,weight=0):
	addedgeend(g,src,dest,weight)
	addedgeend(g,dest,src,weight)
	return g

def bfs(g,src):
    visited=[]
    for i in range(g.v):
        visited.append(False)
    visited[src]=True
    myqueue=queue()
    myqueue.enq(src)
    while myqueue.isemp()==False:

        s=myqueue.deq()
        print s,
        curr=g.array[s].head
        while curr:
            if visited[curr.dest]==False:
                myqueue.enq(curr.dest)
                visited[curr.dest]=True
            curr=curr.next   
def dfs(g):
    visited=[]
    for i in range(g.v):
        visited.append(False)
    for i in range(g.v):
        if not visited[i]:
            visited=dfsutil(i,g,visited)
            
        
    #visited=dfsutil(3,g,visited)
def dfsutil(src,g,visited):
    visited[src]=True
    print src,
    curr=g.array[src].head
    
    while curr:
        if not visited[curr.dest]and curr.dest>=0 and not (curr.dest==9999):
            visited=dfsutil(curr.dest,g,visited)
        
        curr=curr.next
    
    return visited

def dfscycle(g):
    visited=[]
    for i in range(g.v):
        visited.append(False)
    for i in range(g.v):
        #print "DFS from "+str(i)
        if not visited[i]:
            visited,status=dfsutilcycle(i,g,visited)
            if status==1:
                return
        
    
def dfsutilcycle(src,g,visited):
    visited[src]=True
    status=0
    
    curr=g.array[src].head
    
    while curr:
        if not visited[curr.dest]:
            visited,status=dfsutilcycle(curr.dest,g,visited)
            if status==1:
                #print src,visited,status
                break

        else:
            #print "src with cycle is "+str(src) +"to "+str(curr)
            print "A cycle detected "
            status=1
            break
        curr=curr.next
    visited[src]=False
    return visited,status

def find(parent,i):
    if parent[i]==-1:
        return i
    else:
        return find(parent,parent[i])

def union(parent,x,y):
    xset=find(parent,x)
    yset=find(parent,y)
    parent[xset]=yset

def isundircycle(g):
    parent=[]
    for i in range(g.v):
        parent.append(-1)
    for i in range(g.e):
        x=find(parent,g.edgelist[i].src)
        y=find(parent,g.edgelist[i].dest)
        if x==y:
            return True
        union(parent,x,y)

    return False

def undirecdfscycle(g):
    visited=[]
    for i in range(g.v):
        visited.append(False)
    for i in range(g.v):
        #print "DFS from "+str(i)
        if not visited[i]:
            visited,status=undirecddfsutilcycle(i,g,visited,-1)
            if status==1:
                return True
    return False
        
    
def undirecddfsutilcycle(src,g,visited,parent):
    visited[src]=True
    status=0
    
    curr=g.array[src].head
    
    while curr:
        if not visited[curr.dest]:
            visited,status=undirecddfsutilcycle(curr.dest,g,visited)
            if status==1:
                #print src,visited,status
                break

        else:
            #print "src with cycle is "+str(src) +"to "+str(curr)
            print "A cycle detected "
            status=1
            break
        curr=curr.next
    visited[src]=False
    return visited,status

def topo(g):
    visited=[]
    stack=[]
    for i in range(g.v):
        visited.append(False)
    for i in range(g.v):
        if not visited[i]:
            visited,stack=topoutil(i,g,visited,stack)
    res=[]
    while not len(stack)==0:
        res.append(stack.pop())
    return res

            
        
    #visited=dfsutil(3,g,visited)
def topoutil(src,g,visited,stack):
    visited[src]=True
    curr=g.array[src].head
    
    while curr:
        if not visited[curr.dest]:
            visited,stack=topoutil(curr.dest,g,visited,stack)
        
        curr=curr.next
    stack.append(src)
    return visited,stack


def longestpath(g,s):
    dist=[]
    for i in range(g.v):
        dist.append(-float("inf"))
    #print dist
    stack=topo(g)
    dist[s]=0
    #print dist
    for src in stack:
        if not dist[src]==-float("inf"):
            crawl=g.array[src].head
            while crawl:
                if dist[crawl.dest]<dist[src]+crawl.weight:
                    dist[crawl.dest]=dist[src]+crawl.weight 
                crawl=crawl.next
    print dist

def bipart(g):
    colored=[]
    for i in range(g.v):
        colored.append(-1)
    myqueue=queue()
    colored[0]=1
    myqueue.enq(0)
    while not myqueue.isemp():
        src=myqueue.deq()
        crawl=g.array[src].head
        while crawl:
            if colored[crawl.dest]==-1:
                colored[crawl.dest]=1-colored[src]
                myqueue.enq(crawl.dest)
            elif colored[crawl.dest]==colored[src]:
                return False
            crawl=crawl.next

    return True
def snakeladder(move,N):
    visited=[]
    dist=[]
    for i in range(N):
        visited.append(False)
        dist.append(float("inf"))
    visited[0]=True
    dist[0]=0
    myqueue=queue()
    myqueue.enq(0)
    while not myqueue.isemp():
        s=myqueue.deq()
        if s==N-1:
            break
        for i in range(s+1,s+7):
            if i<N:
                if not visited[i]:
                    visited[i]=True
                    if move[i]==-1:
                        adj=i
                    else:
                        adj=move[i]
                    dist[adj]=dist[s]+1
                    print s,adj,myqueue
                    myqueue.enq(adj)


    return dist
def maxidx(arr):
    maxx=arr[0]
    idx=0
    for i in range(1,len(arr)):

        if maxx<arr[i]:
            maxx=arr[i]
            idx=i
        
    return idx
def minidx(arr):
    minx=arr[0] 
    idx=0
    for i in range(1,len(arr)):
        if minx>arr[i]:
            minx=arr[i]
            idx=i
        
    return idx

def mincashflow(g):
    amount=[]
    for i in range(len(g)):
        amount.append(0)
    for i in range(len(g)):
        for j in range(len(g)):
            amount[j]+=g[i][j]-g[j][i]#  For person j (Amt  to be returned from i )-(Amt to give to i )=net amount to be returned to j( to give finally)
    mincashrec(amount)
    return 
def mincashrec(amount):
    Giver=minidx(amount)
    Taker=maxidx(amount)
    if amount[Giver]==0 and amount[Taker]==0:
        return
    pay=min(-amount[Giver],amount[Taker])
    amount[Giver]+=pay
    amount[Taker]-=pay
    print str(Giver)+ " gives "+str(Taker)+"  amount "+str(pay)
    mincashrec(amount)

dict1=["GEEKS","FOR","QUIZ","GO"]
def checkstring(str1):
    for i in dict1:
        if i==str1:
            return True
    return False

def boggle(arr,M,N):
    visited=[]
    for i in range(M):
        b=[]
        for j in range(N):
            b.append(False)
        visited.append(b)
    
    str1=""
    for i in range(M):
        for j in range(N):
            visited,str1=boggleutil(arr,visited,M,N,i,j,str1)

def boggleutil(arr,visited,M,N,i,j,str1):
    visited[i][j]=True
    print str1
    str1=str1+arr[i][j]
    if checkstring(str1):
        print "Found: "+str1
    for k in range(i-1,i+2):
        for l in range(j-1,j+2):
            if k>=0 and k<M and l>=0 and l<N and (not visited[k][l]):
                visited,str1=boggleutil(arr,visited,M,N,k,l,str1)
    visited[i][j]=False
    
    str1=str1[:len(str1)-1]
    return visited,str1

def kruskal(g):
    result=[]
    for i in range(g.v-1):
        result.append(edge(None,None,None))
    
    e=0
    g.sortedges()
    parent=[]
    for i in range(g.v):
        parent.append(-1)
    
    i=0
    while e<(g.v)-1:
        x=find(parent,g.edgelist[i].src)
        y=find(parent,g.edgelist[i].dest)
        if not x==y:
            union(parent,x,y)
            result[e]=g.edgelist[i]
            e+=1
        i+=1

    for i in range(g.v-1):
        print result[i]

def minkey(key,mstset):
	minx=float("inf")
	minidx=-1
	for i in range(len(key)):
		if mstset[i]==False and key[i]<minx:
			minx=key[i]
			minidx=i
	return minidx   
def primadjmat(g):
	V=len(g)
	parent=[]
	mstset=[]
	key=[]

	for i in range(V):
		parent.append(None)
		key.append(float("inf"))
		mstset.append(False)

	key[0]=0
	parent[0]=-1
	for i in range(V-1):
		u=minkey(key,mstset)
		mstset[u]=True
		for v in range(V):
			if g[u][v] and mstset[v]==False and g[u][v]<key[v]:
				parent[v]=u
				key[v]=g[u][v]

	for i in range(1,V):
		print str(parent[i])+"----" +str(i)+"-==--"+str(g[parent[i]][i]) 
  
def borgukal(g):
	V=g.v
	E=g.e
	parent=[]
	cheapest=[]
	for i in range(V):
		parent.append(-1)


		cheapest.append(-1)
	numTrees=V
	while numTrees>1:
		for i in range(E):
			set1=find(parent,g.edgelist[i].src)
			set2=find(parent,g.edgelist[i].dest)

			if set1==set2:
				continue

			if cheapest[set1]==-1 or g.edgelist[cheapest[set1]].weight>g.edgelist[i].weight:
				cheapest[set1]=i
			if cheapest[set2]==-1 or g.edgelist[cheapest[set2]].weight>g.edgelist[i].weight:
				cheapest[set2]=i

		for i in range(V):
			if not cheapest[i]==-1:
				set1=find(parent,g.edgelist[cheapest[i]].src)
				set2=find(parent,g.edgelist[cheapest[i]].dest)
				if set1==set2:
					continue
				print str(g.edgelist[cheapest[i]].src)+"---"+str(g.edgelist[cheapest[i]].weight)+"---"+str(g.edgelist[cheapest[i]].dest)
				union(parent,set1,set2)
				numTrees-=1

def dijkstra(g,src,V):
	mstset=[]
	dist=[]

	for i in range(V):
		dist.append(float("inf"))
		mstset.append(False)

	dist[src]=0
	for i in range(V-1):
		u=minkey(dist,mstset)
		mstset[u]=True
		for v in range(V):
			if g[u][v] and mstset[v]==False and not (dist[u]==float("inf")) and dist[u]+g[u][v]<dist[v]:
				dist[v]=g[u][v]+dist[u]

	for i in range(0,V):
		print str(i)+"-==--"+str(dist[i]) 	

def bellmanford(g,src):
	V=g.v
	E=g.e
	dist=[]
	for i in range(V):
		dist.append(float("inf"))
	dist[src]=0
	for i in range(V-1):
		for j in range(E):
			u=g.edgelist[j].src
			v=g.edgelist[j].dest
			if not (dist[u]==float("inf")) and dist[u]+g.edgelist[j].weight<dist[v]:
				dist[v]=dist[u]+g.edgelist[j].weight
	for j in range(E):
			u=g.edgelist[j].src
			v=g.edgelist[j].dest
			if not (dist[u]==float("inf")) and dist[u]+g.edgelist[j].weight<dist[v]:
				print "Negative Cycle!!!!!!"
				break
	for i in range(0,V):
		print str(i)+"-==--"+str(dist[i]) 


def floydwarshall(g):
	V=len(g)
	dist=[]
	for i in range(V):
		b=[]
		for j in range(V):
			b.append(g[i][j])
		dist.append(b)
	for k in range(V):
		for i in range(V):
			for j in range(V):
				if dist[i][k]+dist[k][j]<dist[i][j] and not (dist[i][k] == float("inf")) and  not (dist[k][j] == float("inf")):
					dist[i][j]=dist[i][k]+dist[k][j]

	print dist

def shortestpathklen(g,u,v,k):
	if k==0 and u==v:
		return 0
	if k==1 and not (g[u][v]==float("inf")):
		return g[u][v]
	if k<0:
		return float("inf")
	res=float("inf")

	for i in range(len(g)):
		if not (g[u][i]==float("inf")) and not(u==i) and not(v==i):
			res1=shortestpathklen(g,i,v,k-1)
			if not res1==float("inf"):
				res=min(res,g[u][i]+res1)
	return res

def transposegraphadjlist(mygraph):
	newgraph=graph(mygraph.v)
	for i in range(mygraph.v):
		curr=mygraph.array[i].head
		while curr:
			newgraph =addedgeend(newgraph,curr.dest,i)
			curr=curr.next
	return newgraph


def isSC(mygraph):
	visited=[]
	for i in range(mygraph.v):
		visited.append(False)
	visited=dfsutil(0,mygraph,visited)
	for i in range(mygraph.v):
		if visited[i]==False:
			return False
	mygraphtrans=transposegraphadjlist(mygraph)
	for i in range(mygraph.v):
		visited[i]=False
	print "\n"
	visited=dfsutil(0,mygraphtrans,visited)
	print "\n"
	for i in range(mygraph.v):
		if visited[i]==False:
			return False
	return True

def listsize(head):
	count=0
	curr=head
	while curr:
		count+=1
		curr=curr.next
	return count

def isConnected(mygraph):
	visited=[]
	V=mygraph.v
	for i in range(V):
		visited.append(False)
	flag=0
	for i in range(V):
		
		if listsize(mygraph.array[i].head):
			flag=1
			break
	if flag==0:
		return True
	visited=dfsutil(i,mygraph,visited)
	for i in range(V):
		if not visited[i] and listsize(mygraph.array[i].head)>0:
			return False
	return True

def iseuler(mygraph): #0:not 1:path 2:cycle 
	V=mygraph.v
	if not isConnected:
		return 0
	odd=0
	for i in range(V):
		if not  listsize(mygraph.array[i].head)%2==0:
			odd+=1
	if odd>2:
		return 0
	if odd==0:
		return 2
	if odd==2:
		return 1
def removeedge(mygraph,u,v): #flag=0  for del
	
	curr=mygraph.array[u].head
	while curr:
		if curr.dest==v:
			curr.dest=-1
			break
		curr=curr.next
	
	curr=mygraph.array[v].head
	while curr:
		if curr.dest==u:
			curr.dest=-1
			break
		curr=curr.next
	


	
def countreachable(mygraph,u):
	visited=[]
	for i in range(mygraph.v):
		visited.append(False)
	visited=dfsutil(u,mygraph,visited)
	count=0
	for i in range(mygraph.v):
		if visited[i] and not (i==u):
			count+=1
	return count

def isvalidedge(mygraph,u,v):
	count=0
	curr=mygraph.array[u].head
	while curr:
		if curr.dest>=0:
			count+=1
		curr=curr.next
	if count==1:
		return True
	count1=countreachable(mygraph,u)
	removeedge(mygraph,u,v)
	count2=countreachable(mygraph,u)
	mygraph=adduedgeend(mygraph,u,v)#add edge
	if count1>count2:
		return False
	return True

	count1=countreachable(mygraph,u)
def printeuler(mygraph):
	if not iseuler(mygraph):
		print "Not euler"
		return
	for i in range(mygraph.v):
		if not (listsize(mygraph.array[i].head)%2==0):
			break
	printeulerutil(mygraph,i)
def printeulerutil(mygraph,u):
	#print "util"
	curr=mygraph.array[u].head
	while curr:

		v=curr.dest
		#print "checking"+str(u)+"---"+str(v)
		if not (v<0) and isvalidedge(mygraph,u,v):
			print str(u)+"---"+str(v)
			removeedge(mygraph,u,v)
			
			printeulerutil(mygraph,v)

		curr=curr.next
	
def fill(src,g,visited,stack):
    visited[src]=True
    #print src,
    curr=g.array[src].head
    
    while curr:
        if not visited[curr.dest]:
        	fill(curr.dest,g,visited,stack)
            #visited,stack=fill(curr.dest,g,visited,stack)
        
        curr=curr.next
    stack.append(src)
    #return visited,stack

def printSCC(mygraph):
	visited=[]
	stack=[]
	for i in range(mygraph.v):
		visited.append(False)
	for i in range(mygraph.v):
		if visited[i]==False:
			#visited,stack=fill(i,mygraph,visited,stack)
			fill(i,mygraph,visited,stack)
	new = transposegraphadjlist(mygraph)
	#printgraph(new)
	#print stack
	for i in range(mygraph.v):
		visited[i]=False
	while len(stack):
		v=stack.pop()
		if visited[v]==False:
			visited=dfsutil(v,new,visited)
		print ""

def ireachesj(g):
	V=len(g)
	reach=[]
	for i in range(V):
		b=[]
		for j in range(V):
			b.append(g[i][j])
		reach.append(b)
	for k in range(V):
		for i in range(V):
			for j in range(V):
				if reach[i][k]and reach[k][j]:
					reach[i][j]=1

	print reach


def dfsmatrix(g,r,c,visited):
	visited[r][c]=True
	for i in range(r-1,r+2):
		for j in range(c-1,c+2):
			if i>=0 and i<len(g) and j>=0 and j<len(g) and g[i][j] and (not visited[i][j]):
				dfsmatrix(g,i,j,visited)


def countisland(g):
	visited=[]
	for i in range(len(g)):
		b=[]
		for j in range(len(g)):
			b.append(False)
		visited.append(b)
	count=0
	for i in range(len(g)):
		for j in range(len(g)):
			if g[i][j] and (not visited[i][j]):
				dfsmatrix(g,i,j,visited)
				count+=1
	return count

def countpathsk(g,u,v,k):
	if k==0 and u==v:
		return 1
	if k==1 and not (g[u][v]==float("inf")):
		return 1
	if k<=0:
		return 0
	count=0

	for i in range(len(g)):
		if g[u][i] and not(u==i) and not(v==i):
			count+=countpathsk(g,i,v,k-1)
			
	return count

def isSChelper(mygraph):
	visited=[]
	for i in range(mygraph.v):
		visited.append(False)

	for i in range(mygraph.v):
		 if mygraph.outdeg[i]>0:
		 	break
	k=i

	visited=dfsutil(k,mygraph,visited)
	for i in range(mygraph.v):
		if mygraph.outdeg[i]>0 and visited[i]==False:
			return False

	mygraphtrans=transposegraphadjlist(mygraph)
	
	for i in range(mygraph.v):
		visited[i]=False
	print "\n"
	visited=dfsutil(k,mygraphtrans,visited)
	for i in range(mygraph.v):
		if mygraph.outdeg[i]>0 and visited[i]==False:
			return False
	return True


def iseulercycledirec(mygraph):
	if not isSChelper(mygraph):
		return False
	for i in range(mygraph.v):
		if not mygraph.indeg[i]==mygraph.outdeg[i]:
			return False
	return True
def iscycleundirutil(mygraph,src,visited,parent):
	visited[src]=True
	curr=mygraph.array[src].head
	while curr:
		if not visited[curr.dest]:
			if iscycleundirutil(mygraph,curr.dest,visited,src):
				return True
		elif not (curr.dest==parent):
			return True
		curr=curr.next
	return False

def isTree(mygraph):
	visited=[]
	for i in range(mygraph.v):
		visited.append(False)
	print visited
	if iscycleundirutil(mygraph,0,visited,-1):
		return False
	print visited
	for i in range(mygraph.v):
		if not visited[i]:
			return False
	return True

def karger(g):
    parent=[]
    for i in range(g.v):
        parent.append(-1)
    noOfVertices=g.v
    while noOfVertices>2:
        i=random.randint(0,g.e-1)
        set1=find(parent,g.edgelist[i].src)
        set2=find(parent,g.edgelist[i].dest)
        if set1==set2:
            continue
        else:
            print "Contracting "+str(g.edgelist[i].src)+"-----"+str(g.edgelist[i].dest)
            union(parent,g.edgelist[i].src,g.edgelist[i].dest)
            noOfVertices-=1
    cutedges=0
    for i in range(g.e):

        set1=find(parent,g.edgelist[i].src)
        set2=find(parent,g.edgelist[i].dest)
        if not set1==set2:
            cutedges+=1
    return cutedges

def vertexcolor(g):
    used=[]
    assigned=[]
    for i in range(g.v):
        used.append(False)
        assigned.append(-1)
    assigned[0]=0
    for u in range(1,g.v):
        curr=g.array[u].head
        while curr:
            if not assigned[curr.dest]==-1:
                used[assigned[curr.dest]]=True
            curr=curr.next
        for i in range(g.v):
            if used[i]==False:
                break
        assigned[u]=i
        curr=g.array[u].head
        while curr:
            if not assigned[curr.dest]==-1:
                used[assigned[curr.dest]]=False
            curr=curr.next
    for i in range(g.v):
        print i,assigned[i]
def issafe(v,g,path,pos):
    if not g[path[pos-1]][v]:
        return False
    for i in range(pos):
        if path[i]==v:
            return False
    return True

def hamrec(g,path,pos):
    if pos==len(g):
        if g[path[pos-1]][path[0]]:
            return True
        else:
            return False
    for i in range(len(g)):
        if issafe(i,g,path,pos):
            path[pos]=i
            if hamrec(g,path,pos+1):
                return True
            
            path[pos]=-1
    return False

def hamcycle(g):
    v=len(g)
    path=[]
    for i in range(v):
        path.append(-1)
    path[0]=0
    if not hamrec(g,path,1):
        print "NO solution exist"
    else:
        path.append(0)
        print path
        
def vertexcover(g):
    visited=[]
    for i in range(g.v):
        visited.append(False)
    for u in range(g.v):
        if not visited[u]:
            curr=g.array[u].head
            while curr:
                v=curr.dest
                if not visited[v]:
                    visited[u]=True
                    visited[v]=True
                    break
                curr=curr.next
    for i in range(g.v):
        if visited[i]:
            print i,
#mygraph=graph(5)
#printgraph(mygraph)
#mygraph=addedgeend(mygraph,0,1)
#mygraph=addedgeend(mygraph,0,4)
#mygraph=addedgeend(mygraph,1,2)
#mygraph=addedgeend(mygraph,3,1)
#mygraph=addedgeend(mygraph,1,4)
#mygraph=addedgeend(mygraph,2,3)
#mygraph=addedgeend(mygraph,3,4)
#printgraph(mygraph)

#mygraph=adduedgeend(mygraph,0,1)
#mygraph=adduedgeend(mygraph,1,4)
#mygraph=adduedgeend(mygraph,1,2)
#mygraph=adduedgeend(mygraph,1,3)
#mygraph=adduedgeend(mygraph,1,4)
#mygraph=adduedgeend(mygraph,2,3)
#mygraph=adduedgeend(mygraph,3,4)
#printgraph(mygraph)
#print "BFS:"
#bfs(mygraph,2)
#print "\nDFS:"
#dfs(mygraph)

#print "\nCycle:"
#dfscycle(mygraph)

#mygraph2=newgraph(3,2)
#mygraph2.edgelist[0].src=0
#mygraph2.edgelist[0].dest=1
#mygraph2.edgelist[1].src=1
#mygraph2.edgelist[1].dest=2
#mygraph2.edgelist[2].src=0
#mygraph2.edgelist[2].dest=2

#print isundircycle(mygraph2)

#mygraph3=graph(6)
#printgraph(mygraph3)
#mygraph3=addedgeend(mygraph3,5,2)
#mygraph3=addedgeend(mygraph3,5,0)
#mygraph3=addedgeend(mygraph3,4,0)
#mygraph3=addedgeend(mygraph3,4,1)
#mygraph3=addedgeend(mygraph3,2,3)
#mygraph3=addedgeend(mygraph3,3,1)
#mygraph3=addedgeend(mygraph3,3,4)
#printgraph(mygraph3)
#dfs(mygraph3)
#print"\n"
#topo(mygraph3)
#x=float("inf")

#mygraph4=graph(6)
#printgraph(mygraph4)
#mygraph4=addedgeend(mygraph4,0,1,5)
#mygraph4=addedgeend(mygraph4,0,2,3)
#mygraph4=addedgeend(mygraph4,1,3,6)
#mygraph4=addedgeend(mygraph4,1,2,2)
#mygraph4=addedgeend(mygraph4,2,4,4)
#mygraph4=addedgeend(mygraph4,2,5,2)
#mygraph4=addedgeend(mygraph4,2,3,7)
#mygraph4=addedgeend(mygraph4,3,5,1)
#mygraph4=addedgeend(mygraph4,3,4,-1)
#mygraph4=addedgeend(mygraph4,4,5,-2)
#printgraph(mygraph4)
#print topo(mygraph4)

#longestpath(mygraph4,1)

#mygraph4=graph(5)
#printgraph(mygraph4)
#mygraph4=adduedgeend(mygraph4,0,1)
#mygraph4=adduedgeend(mygraph4,0,3)
#mygraph4=adduedgeend(mygraph4,1,0)
#mygraph4=adduedgeend(mygraph4,1,2)
#mygraph4=adduedgeend(mygraph4,2,1)
#mygraph4=adduedgeend(mygraph4,2,3)
#mygraph4=adduedgeend(mygraph4,3,0)
#mygraph4=adduedgeend(mygraph4,3,2)
#mygraph4=adduedgeend(mygraph4,3,4)
#mygraph4=adduedgeend(mygraph4,4,0)
#printgraph(mygraph4)
#prin*t bipart(mygraph4)

#moves=[]
#for i in range(30):
    #moves.append(-1)
#moves[1]=29

# Ladders
#moves[2] = 21
#moves[4] = 7
#moves[10] = 25
#moves[19] = 28
 
# Snakes
#moves[26] = 0
#moves[20] = 8
#moves[16] = 3
#moves[18] = 6

#print snakeladder(moves,30)


#g[i][j] amount i have to pay this to j
#g=[]
#for i in range(3):
#    b=[]
#    for j in range(3):
#        b.append(0)
#    g.append(b)
#print g
#g[0][1]=1000
#g[0][2]=2000
#g[1][2]=5000
#print g
#mincashflow(g)
#0 1000 2000
#0  0   5000
#0  0    0

#g=[]
#for i in range(3):
#    b=[]
#    for j in range(3):
#        b.append(None)
#    g.append(b)
#print g
#g[0][0]="G"
#g[0][1]="I"
#g[0][2]="Z"
#g[1][0]="U"
#g[1][1]="E"
#g[1][2]="K"
#g[2][0]="Q"
#g[2][1]="S"
#g[2][2]="E"
#print g

#boggle(g,3,3)

#mygraph2=newgraph(4,5)
#mygraph2.edgelist[0].src=0
#mygraph2.edgelist[0].dest=1
#mygraph2.edgelist[0].weight=10
#mygraph2.edgelist[1].src=0
#mygraph2.edgelist[1].dest=2
#mygraph2.edgelist[1].weight=6
#mygraph2.edgelist[2].src=0
#mygraph2.edgelist[2].dest=3
#mygraph2.edgelist[2].weight=5
#mygraph2.edgelist[3].src=1
#mygraph2.edgelist[3].dest=3
#mygraph2.edgelist[3].weight=15
#mygraph2.edgelist[4].src=2
#mygraph2.edgelist[4].dest=3
#mygraph2.edgelist[4].weight=4

#print mygraph2.edgelist[0]
#print mygraph2.edgelist[1]
#print mygraph2.edgelist[2]


#kruskal(mygraph2)

#print isundircycle(mygraph2)


g=[]
for i in range(5):
    b=[]
    for j in range(5):
        b.append(0)
    g.append(b)
#print g
g[0][1]=2
g[0][3]=6
g[1][0]=2
g[1][2]=3
g[1][3]=8
g[1][4]=5
g[2][1]=3
g[2][4]=7
g[3][0]=6
g[3][1]=8
g[3][4]=9
g[4][1]=5
g[4][2]=7
g[4][3]=9

#primadjmat(g)

#borgukal(mygraph2)

#dijkstra(g,0,4)

#print mygraph2
#bellmanford(mygraph2,0)

#print g
#floydwarshall(g)


g1=[]
for i in range(4):
    b=[]
    for j in range(4):
        b.append(0)
    g1.append(b)

g1[0][1]=10
g1[0][2]=3
g1[0][3]=2
g1[1][0]=float("inf")
g1[1][2]=float("inf")
g1[1][3]=7
g1[2][0]=float("inf")
g1[2][1]=float("inf")
g1[2][3]=6
g1[3][0]=float("inf")
g1[3][1]=float("inf")
g1[3][2]=float("inf")
#print g1
#print shortestpathklen(g1,0,3,2)



#mygraph=graph(5)
#printgraph(mygraph)
#mygraph=addedgeend(mygraph,0,1)
#mygraph=addedgeend(mygraph,1,2)
#mygraph=addedgeend(mygraph,2,3)
#mygraph=addedgeend(mygraph,3,0)
#mygraph=addedgeend(mygraph,2,4)
#mygraph=addedgeend(mygraph,4,2)

#printgraph(mygraph)
#print isSC(mygraph)


#mygraph2=graph(4)
#printgraph(mygraph2)
#mygraph2=addedgeend(mygraph2,0,1)
#mygraph2=addedgeend(mygraph2,1,2)
#mygraph2=addedgeend(mygraph2,2,3)


#printgraph(mygraph2)

#print isSC(mygraph2)


#mygraph2=graph(5)
#printgraph(mygraph2)
#mygraph2=adduedgeend(mygraph2,0,1)
#mygraph2=adduedgeend(mygraph2,1,2)
#mygraph2=adduedgeend(mygraph2,2,3)
#mygraph2=adduedgeend(mygraph2,3,0)
#mygraph2=adduedgeend(mygraph2,3,4)


#printgraph(mygraph2)
#print isConnected(mygraph2)
#print iseuler(mygraph2)
#printeuler(mygraph2)


#mygraph=graph(5)
#printgraph(mygraph)
#mygraph=addedgeend(mygraph,1,0)
#mygraph=addedgeend(mygraph,0,2)
#mygraph=addedgeend(mygraph,2,1)
#mygraph=addedgeend(mygraph,0,3)
#mygraph=addedgeend(mygraph,3,4)
#printgraph(mygraph)
#printSCC(mygraph)

#g2=[]
#for i in range(4):
#    b=[]
#    for j in range(4):
#        b.append(0)
#    g2.append(b)
#g2[0][0]=1
#g2[0][1]=1
#g2[0][3]=1
#g2[1][1]=1
#g2[1][2]=1
#g2[2][3]=1
#g2[2][2]=1
#g2[3][3]=1

#ireachesj(g2)

g3=[]
for i in range(5):
    b=[]
    for j in range(5):
        b.append(0)
    g3.append(b)
g3[0][0]=1
g3[0][1]=1
g3[1][1]=1
g3[1][4]=1
g3[2][0]=1
g3[2][3]=1
g3[2][4]=1
g3[4][0]=1
g3[4][2]=1
g3[4][4]=1
#print countisland(g3)

g4=[]
for i in range(4):
    b=[]
    for j in range(4):
        b.append(0)
    g4.append(b)
g4[0][1]=1
g4[0][2]=1
g4[1][3]=1
g4[1][3]=1
g4[2][3]=1

#print countpathsk(g4,0,3,2)

#mygraph=graph(5)
#printgraph(mygraph)
#mygraph=addedgeend(mygraph,1,0)
#mygraph=addedgeend(mygraph,0,2)
#mygraph=addedgeend(mygraph,2,1)
#mygraph=addedgeend(mygraph,0,3)
#mygraph=addedgeend(mygraph,3,4)
#mygraph=addedgeend(mygraph,4,0)
#printgraph(mygraph)
#print iseulercycledirec(mygraph)


#mygraph=graph(5)
#printgraph(mygraph)
#mygraph=adduedgeend(mygraph,1,0)
#mygraph=adduedgeend(mygraph,0,2)
#mygraph=adduedgeend(mygraph,2,1)
#mygraph=adduedgeend(mygraph,0,3)
#mygraph=adduedgeend(mygraph,3,4)
#mygraph4=adduedgeend(mygraph4,2,3)
#mygraph4=adduedgeend(mygraph4,3,0)
#mygraph4=adduedgeend(mygraph4,3,2)
#mygraph4=adduedgeend(mygraph4,3,4)
#mygraph4=adduedgeend(mygraph4,4,0)
#printgraph(mygraph)
#print isTree(mygraph)

#mygraph2=newgraph(4,5)
#mygraph2.edgelist[0].src=0
#mygraph2.edgelist[0].dest=1
#mygraph2.edgelist[0].weight=10
#mygraph2.edgelist[1].src=0
#mygraph2.edgelist[1].dest=2
#mygraph2.edgelist[1].weight=6
#mygraph2.edgelist[2].src=0
#mygraph2.edgelist[2].dest=3
#mygraph2.edgelist[2].weight=5
#mygraph2.edgelist[3].src=1
#mygraph2.edgelist[3].dest=3
#mygraph2.edgelist[3].weight=15
#mygraph2.edgelist[4].src=2
#mygraph2.edgelist[4].dest=3
#mygraph2.edgelist[4].weight=4
#print karger(mygraph2)

mygraph4=graph(5)
#printgraph(mygraph4)
mygraph4=adduedgeend(mygraph4,0,1,5)
mygraph4=adduedgeend(mygraph4,0,2,3)
mygraph4=adduedgeend(mygraph4,1,2,6)
mygraph4=adduedgeend(mygraph4,1,3,2)
mygraph4=adduedgeend(mygraph4,2,3,4)
mygraph4=adduedgeend(mygraph4,3,4,2)

#printgraph(mygraph4)
#vertexcolor(mygraph4)

g5=[]
for i in range(5):
    b=[]
    for j in range(5):
        b.append(0)
    g5.append(b)
g5[0][1]=1
g5[0][3]=1
g5[1][0]=1
g5[1][2]=1
g5[1][3]=1
g5[1][4]=1
g5[2][1]=1
g5[2][4]=1
g5[3][0]=1
g5[3][1]=1
g5[3][4]=1
g5[4][1]=1
g5[4][2]=1
g5[4][3]=1
#hamcycle(g5)

mygraph7=graph(7)
printgraph(mygraph7)
mygraph7=adduedgeend(mygraph7,0,1,5)
mygraph7=adduedgeend(mygraph7,0,2,3)
mygraph7=adduedgeend(mygraph7,1,3,6)
mygraph7=adduedgeend(mygraph7,3,4,2)
mygraph7=adduedgeend(mygraph7,4,5,4)
mygraph7=adduedgeend(mygraph7,5,6,2)

printgraph(mygraph7)
vertexcover(mygraph7)