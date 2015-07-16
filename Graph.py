from collections import deque
class adjnode(object):
    def __init__(self,dest,next=None):
        self.dest=dest
        self.next=next
        
    def __str__(self):
        return str(self.dest)

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
        for i in range(v):
            self.array.append(adjlist(None))

    def __str__(self):
        return str(self.array)
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
        

def addedge(g,src,dest):
	#print str(src)+"->"+str(dest)+"added"
	new=adjnode(dest,g.array[src].head)
	g.array[src].head=new
	return g
def adduedge(g,src,dest):
	addedge(g,src,dest)
	addedge(g,dest,src)
	return g
def addedgeend(g,src,dest):
	#print str(src)+"->"+str(dest)+" added"
	new=adjnode(dest)
	if g.array[src].tail==None:
		g.array[src].head=g.array[src].tail=new
	else:
		g.array[src].tail.next=new
		g.array[src].tail=new
	return g

def adduedgeend(g,src,dest):
	addedgeend(g,src,dest)
	addedgeend(g,dest,src)
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


mygraph=graph(5)
#printgraph(mygraph)
#mygraph=adduedge(mygraph,0,1)
#mygraph=adduedge(mygraph,0,4)
#mygraph=adduedge(mygraph,1,2)
#mygraph=adduedge(mygraph,1,3)
#mygraph=adduedge(mygraph,1,4)
#mygraph=adduedge(mygraph,2,3)
#mygraph=adduedge(mygraph,3,4)
#printgraph(mygraph)

mygraph=adduedgeend(mygraph,0,1)
mygraph=adduedgeend(mygraph,0,4)
mygraph=adduedgeend(mygraph,1,2)
mygraph=adduedgeend(mygraph,1,3)
mygraph=adduedgeend(mygraph,1,4)
mygraph=adduedgeend(mygraph,2,3)
mygraph=adduedgeend(mygraph,3,4)
printgraph(mygraph)

bfs(mygraph,2)