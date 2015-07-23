INT_MAX=float("inf")
INT_MIN=-1

class minheap(object):
	def __init__(self,capacity):
		self.capacity=capacity
		self.size=0
		self.array=[]
		for i in range(capacity):
			self.array.append(None)
	def __str__(self):
		return str(self.array[:self.size])

def parent(i):
	return ((i-1)/2 )
def left(i):
	return ((2*i)+1)
def right(i):
	return ((2*i)+2)
def getmin(heap):
	return heap.array[0]
def insert(heap,key):
	if heap.size==heap.capacity:
		print "O/F"
		return
	heap.array[heap.size]=key
	heap.size+=1
	i=heap.size-1
	while not (i==0) and heap.array[parent(i)]>heap.array[i]:
	
		heap.array[parent(i)],heap.array[i]=heap.array[i],heap.array[parent(i)]
		
		i=parent(i)
def decreasekey(heap,i,newval):
	heap.array[i]=newval
	while not (i==0) and heap.array[parent(i)]>heap.array[i]:
		
		heap.array[parent(i)],heap.array[i]=heap.array[i],heap.array[parent(i)]
		
		i = parent(i)

def replacemin(heap,x):
	root=heap.array[0]
	heap.array[0]=x
	if root<x:
		heapify(heap,0)
	return root
def extractmin(heap):
	if heap.size<=0:
		return INT_MAX
	if heap.size==1:
		heap.size-=1
		return heap.array[0]
	root=heap.array[0]
	heap.array[0]=heap.array[heap.size-1]
	heap.size-=1
	heapify(heap,0)
	return root
def delete(heap,i):
	decreasekey(heap,i,INT_MIN)
	
	extractmin(heap)
	

def heapify(heap,i):
	l=left(i)
	r=right(i)
	smallest=i
	if l<heap.size and heap.array[l]<heap.array[i]:
		smallest=l
	if r<heap.size and heap.array[r]<heap.array[smallest]:
		smallest=r
	if not smallest==i:
		heap.array[smallest],heap.array[i]=heap.array[i],heap.array[smallest]
		heapify(heap,smallest)

myheap=minheap(11)
#print myheap
insert(myheap,3)
insert(myheap,2)
delete(myheap,1)
insert(myheap,15)
insert(myheap,5)
insert(myheap,4)
insert(myheap,45)
#print myheap
#print extractmin(myheap)
#print myheap
#print getmin(myheap)
#decreasekey(myheap,2,1)
#print myheap
#print getmin(myheap)
def heapsort(inp):
	n=len(inp)
	myheap=minheap(n)
	for i in range(n):
		insert(myheap,inp[i])
	for i in range(n):
		print extractmin(myheap)

#heapsort([2,1,3,6,2,2,5,3,11,35,1])
def kthsmallest(inp,k):
	n=len(inp)
	myheap=minheap(n)
	for i in range(n):
		insert(myheap,inp[i])
	for i in range(k):
		x=extractmin(myheap)
	print x
#kthsmallest([2,1,3,6,2,2,5,3,11,35,1],10)

def ksorted(inp,k):
	n=len(inp)
	myheap=minheap(k+1)
	for i in range(k+1):
		insert(myheap,inp[i])
	for i in range(k+1,n):
		print replacemin(myheap,inp[i]),
	for i in range(k+1):
		print extractmin(myheap),

		
		
#ksorted([2, 6, 3, 12, 56, 8],3)


