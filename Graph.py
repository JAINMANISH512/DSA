from collections import deque
class adjnode(object):
    def __init__(self,dest,next=None):
        self.dest=dest
        self.next=next
        
    def __str__(self):
        return str(self.dest)

class adjlist(object):
    def __init__(self,head=None):
        self.head=head
    
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
        for i in range(v):
            self.array.append(adjlist(None))

    def __str__(self):
        return str(self.array)

def printgraph(g):
    for src in range(g.v):
        print str(src)+ "->"+str(g.array[src]) 
        

def adduedgeatstart(g,src,dest):
    new=adjnode(dest,g.array[src].head)
    g.array[src].head=new
 
    
    new=adjnode(src,g.array[dest].head)
    g.array[dest].head=new

def addedgeatstart(g,src,dest):
    new=adjnode(dest,g.array[src].head)
    g.array[src].head=new

def adduedge(g,src,dest):
    addedge(g,src,dest)
    addedge(g,dest,src)

def addedge(g,src,dest):
    new=adjnode(dest)
    crawl=g.array[src].head
    if crawl:
    	while crawl.next:
    		crawl=crawl.next
    	crawl.next=new
    else:
    	g.array[src].head=new

def bfs(g,src):
	print "Bfs"
	visited=[]
	for i in range(g.v):
		visited.append(False)
	
 	visited[src]=True
 	
	queue=deque([])
 	queue.append(src)

 	while not len(queue) == 0:
 		s=queue.popleft()
 		print s
 		crawl=g.array[s].head
 		while crawl:
 			if not visited[crawl.dest]:
 				queue.append(crawl.dest)
 				visited[crawl.dest]=True
 			crawl=crawl.next	

def dfs(g,src):
	print "Dfs"
	visited=[]
	for i in range(g.v):
		visited.append(False)
	dfsutil(g,src,visited)

def dfsutil(g,src,visited):	
 	visited[src]=True
 	print src
 	
	crawl=g.array[src].head
 	while crawl:
 		if not visited[crawl.dest]:
 			visited[crawl.dest]=True
 			dfsutil(g,crawl.dest,visited)
 		crawl=crawl.next			


mygraph=graph(4)
addedge(mygraph,0,1)
addedge(mygraph,0,2)
addedge(mygraph,1,2)
addedge(mygraph,2,0)
addedge(mygraph,2,3)
addedge(mygraph,3,3)

printgraph(mygraph)
dfs(mygraph,2)