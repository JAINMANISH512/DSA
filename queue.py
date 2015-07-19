class queue(object):
	def __init__(self,capacity):
		self.front=0
		self.rear=capacity-1
		self.size=0
		self.capacity=capacity
		self.array=[]
		for i in range(capacity):
			self.array.append(None)

	def __str__(self):
		return str(self.array)

def isfull(myqueue):
	return myqueue.size==myqueue.capacity

def isemp(myqueue):
	return myqueue.size==0

def enq(myqueue,x):
	if isfull(myqueue):
		return
	myqueue.rear=(myqueue.rear+1)%myqueue.capacity
	myqueue.array[myqueue.rear]=x
	myqueue.size+=1

def deq(myqueue):
	if isemp(myqueue):
		return -float("inf")
	myqueue.array[myqueue.front]=None
	myqueue.front=(myqueue.front+1)%myqueue.capacity
	x=myqueue.array[myqueue.front]
	myqueue.size-=1
	return x

def frontele(myqueue):
	if isemp(myqueue):
		return -float("inf")
	return myqueue.array[myqueue.front]

def rearele(myqueue):
	if isemp(myqueue):
		return -float("inf")
	return myqueue.array[myqueue.rear]

class queuelist(object):
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
#myqueue=queue(10)
#print myqueue
#enq(myqueue,5)
#enq(myqueue,10)
#enq(myqueue,5)
#enq(myqueue,25)
#print myqueue
#print frontele(myqueue)
#print rearele(myqueue)
#deq(myqueue)
#deq(myqueue)
#print myqueue




