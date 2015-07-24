class Node(object):
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

	def __str__(self):
		return str(self.data)

class BST(object):
	def __init__(self,root=None):
		self.root=root

def inord(root):
	if root==None:
		return
	inord(root.left)
	print root.data
	inord(root.right)

def search(root,key):
	if root==None:
		return None
	if root.data==key:
		return root
	if root.data>key:
		return search(root.left,key)
	return search(root.right,key)

def insert(root,key):
	new=Node(key)
	if root==None:
		root=new
		return root
	if root.data>key:
		root.left= insert(root.left,key)
	else:
		root.right= insert(root.right,key)
	return root
def minval(root):
	curr=root
	while curr.left:
		curr=curr.left
	return curr
def maxval(root):
	curr=root
	while curr.right:
		curr=curr.right
	return curr

def delete(root,key):
	if root==None:
		return root
	if root.data<key:
		root.right=delete(root.right,key)
	elif root.data>key:
		root.left=delete(root.left,key)
	else:
		if root.left==None:
			temp=root.right
			del root
			return temp
		if root.right==None:
			temp=root.right
			del root
			return temp
		temp=minval(root.right)
		root.data=temp.data
		root.right=delete(root.right,temp.data)
	return root
def isbst(root):
	if root==None:
		return True
	if root.left:
		if maxval(root.left).data>root.data:
			return False
	if root.right:
		if minval(root.right).data<root.data:
			return False
	if (not isbst(root.left)) or (not isbst(root.right)):
		return False
	return True

def lca(root,n1,n2):
	if root==None:
		return None
	if root.data>n1 and root.data>n2:
		return lca(root.left,n1,n2)
	if root.data<n1 and root.data<n2:
		return lca(root.left,n1,n2)
	return root

def printsorted(arr,str,end):
	if str>end :
		return
	printsorted(arr,2*str+1,end)
	print arr[str]
	printsorted(arr,2*str+2,end)

def inordsucc(root,n):
	if n.right:
		return minval(n.right)
	succ=None
	while root:
		if n.data<root.data:
			succ=root
			root=root.left
		elif n.data>root.data:
			root=root.right
		else:
			break
	return succ
def kthnode(root):
	pass

def printrange(root,k1,k2):
	if root==None:
		return
	if k1<root.data:
		printrange(root.left,k1,k2)
	if k1 <= root.data and root.data <= k2:
		print root.data
	if root.data<k2:
		printrange(root.right,k1,k2)

def sortarrtobst(arr,strt,end):
	if strt>end:
		return None
	mid=(strt+end)/2
	root=Node(arr[mid])
	root.left=sortarrtobst(arr,strt,mid-1)
	root.right=sortarrtobst(arr,mid+1,end)
	return root
def size(root):
	if root==None:
		return 0
	return size(root.left)+size(root.right)+1
#def largestbst(root):
#	if isbst(root):
#		return size(root)
#	return max(largestbst(root.left),largestbst(root.right))
def largestbst(root):
	minref=float("inf")
	maxref=-float("inf")
	isbstref=False
	maxsizeref=0

	minref,maxref,isbstref,maxsizeref,size=largestbstutil(root,minref,maxref,isbstref,maxsizeref)
	return maxsizeref

def largestbstutil(root,minref,maxref,isbstref,maxsizeref):
	if root==None:
		#print"cond true"
		return minref,maxref,True,maxsizeref,0
	#print "after condition here"#+str(root.data)
	leftflag=False
	rightflag=False
	maxref=-float("inf")
	#print "b4 calling"
	minref,maxref,isbstref,maxsizeref,ls=largestbstutil(root.left,minref,maxref,isbstref,maxsizeref)
	if isbstref and root.data>maxref:
		leftflag=True
	minleft=minref

	minref=float("inf")
	minref,maxref,isbstref,maxsizeref,rs=largestbstutil(root.right,minref,maxref,isbstref,maxsizeref)
	if isbstref and root.data<minref:
		rightflag=True
	#print "b4 minmax"+str(root.data)
	if minleft<minref:
		minref=minleft
	if root.data<minref:
		minref=root.data
	if root.data>maxref:
		maxref=root.data
	#print "aftr minmax"+str(root.data)
	if leftflag and rightflag:
		if ls+rs+1>maxsizeref:
			maxsizeref=ls+rs+1
			isbstref=True
		return minref,maxref,isbstref,maxsizeref,ls+rs+1
	else:
		isbstref=False
		return minref,maxref,isbstref,maxsizeref,0
def issamebstutil(a,b,n,i1,i2,minx,maxx):
	j=i1
	for j in range(i1,n):
		if a[j]>minx and a[j]<maxx:
			break
	
	k=i2
	for k in range(i2,n):
		if b[k]>minx and b[k]<maxx:
			break
	
	if j==n and k==n:
		return True
	if (j==n and not (k==n)) or (k==n and not (j==n))or not( a[j]==b[k]):
		return False
	return issamebstutil(a,b,n,j+1,k+1,minx,a[j]) and issamebstutil(a,b,n,j+1,k+1,a[j],maxx)
def addgreater(root,sumx):
	if root==None:
		return sumx
	sumx=addgreater(root.right,sumx)
	sumx=sumx+root.data
	root.data=sumx
	sumx=addgreater(root.left,sumx)

	return sumx
def removeoutsiderange(root,minx,maxx):
	if root==None:
		return None
	root.left=removeoutsiderange(root.left,minx,maxx)
	root.right=removeoutsiderange(root.right,minx,maxx)
	if root.data<minx:
		rchild=root.right
		del root
		return rchild
	if root.data>maxx:
		lchild=root.left
		del root
		return lchild
	return root

def hasonlyonechild(pre):
	for i in range(len(pre)-1):
		if (pre[i]-pre[i+1])*(pre[i]-pre[len(pre)-1])<0:
			return False
	return True
def convertbsttodll(root,head,tail):
	if root==None:
		return head,tail
	if root.left:
		head,tail=convertbsttodll(root.left,head,tail)
	root.left=tail
	if tail:
		tail.right=root
	else:
		head=root
	tail=root

	if root.right:
		head,tail=convertbsttodll(root.right,head,tail)
	return head,tail

def ispresentindll(head,tail,sumx):
	while not (head==tail):
		curr=head.data+tail.data
		if curr==sumx:
			#print str(head.data)+" " +str(tail.data)
			return True
		elif curr>sumx:
			tail=tail.left
		else:
			head=head.right
	return False

def istripletpresent(root):
	if not root:
		return False
	head,tail=convertbsttodll(root,None,None)
	while not (head.right==tail) and (head.data<0):
		if ispresentindll(head.right,tail,-head.data):
			#print str(head.data)
			return True
		else:
			head=head.right
	return False

def correctbstutil(root,prev,first,middle,last):
	if root:
		prev,first,middle,last=correctbstutil(root.left,prev,first,middle,last)
		if prev and root.data<prev.data:#violet ion
			if not first:
				first=prev
				middle=root
			else:
				last=root
		prev=root
		prev,first,middle,last=correctbstutil(root.right,prev,first,middle,last)
	return prev,first,middle,last


def correctbst(root):
	prev=first=middle=last=None
	prev,first,middle,last=correctbstutil(root,prev,first,middle,last)
	if first and last:
		first.data,last.data=last.data,first.data
		print "swapped :(("
	elif first and middle:
		first.data,middle.data=middle.data,first.data
		print "swapped :("
	else:
		print "No swap :D"

def constructtreefromprerec(pre,idx,minx,maxx,size):
	if idx>=size:
		return None,idx
	root=None
	key=pre[idx]
	if key>minx and key<maxx:
		root=Node(key)
		idx+=1
		if idx<size:
			root.left,idx=constructtreefromprerec(pre,idx,minx,key,size)
			root.right,idx=constructtreefromprerec(pre,idx,key,maxx,size)
	return root,idx

def constructtreefrompreiter(pre,size):
	stack=[]
	root=Node(pre[0])
	stack.append(root)
	for i in range(1,size):
		temp=None
		while len(stack) and pre[i]>stack[-1].data:
			temp=stack.pop()
		if temp:
			temp.right=Node(pre[i])
			stack.append(temp.right)
		else:
			stack[-1].left=Node(pre[i])
			stack.append(stack[-1].left)
	return root

def ceiling(root,ip):
	if root==None:
		return -1
	if root.data==ip:
		return root.data
	if root.data<ip:
		return ceiling(root.right,ip)
	leftceil=ceiling(root.left,ip)
	if leftceil>=ip:
		return leftceil
	else:
		return root.data
mybst=BST()
mybst.root=Node(20)
mybst.root.left=Node(8)
mybst.root.right=Node(22)
mybst.root.left.left=Node(4)
mybst.root.left.right=Node(12)
mybst.root.right.left=Node(21)
mybst.root.right.right=Node(26)

#mybst.root=insert(mybst.root,7)
#mybst.root=insert(mybst.root,5)
#mybst.root=insert(mybst.root,6)
#mybst.root=insert(mybst.root,1)
#mybst.root=insert(mybst.root,2)
#mybst.root=insert(mybst.root,3)
#mybst.root=insert(mybst.root,4)
#inord(mybst.root)

#print search(mybst.root,21)

#delete(mybst.root,20)
#inord(mybst.root)

#print minval(mybst.root)

#mybst.root.data=0
#inord(mybst.root)
#print isbst(mybst.root)

#print lca(mybst.root,4,12)
#print lca(mybst.root,4,26)

#arr=[4,2,5,1,3]
#printsorted(arr,0,len(arr)-1)

#print inordsucc(mybst.root,mybst.root.left)

#kthnode(mybst.root,k)

#printrange(mybst.root,5,23)

#arr=[1,3,5,6,7]
#root=sortarrtobst(arr,0,len(arr)-1)
#inord(root)
#print root,root.left,root.right

#print largestbst(mybst.root)

#a=[8, 3, 6, 1, 4, 7, 10, 14, 13]
#b=[8, 10, 14, 3, 6, 4, 1, 7, 13]
#print issamebstutil(a,b,len(a),0,0,-float("inf"),float("inf"))

#inord(mybst.root)
#addgreater(mybst.root,0)
#print "\n"
#inord(mybst.root)

#inord(mybst.root)
#mybst.root=removeoutsiderange(mybst.root,10,18)
#print "\n"
#inord(mybst.root)

#print hasonlyonechild([8,3,5,7,6,10])

#inord(mybst.root)
#head,tail=convertbsttodll(mybst.root,None,None)
#curr=head
#while curr:
#	print curr
#	curr=curr.right
#curr=tail
#while curr:
#	print curr
#	curr=curr.left

#mybst1=BST()
#mybst1.root=Node(6)
#mybst1.root.left=Node(-13)
#mybst1.root.right=Node(14)
#mybst1.root.left.right=Node(-8)
#mybst1.root.right.left=Node(13)
#mybst1.root.right.right=Node(15)
#mybst1.root.right.left.left=Node(7)
#print istripletpresent(mybst1.root)

#inord(mybst.root)
#correctbst(mybst.root)
#print "\n\nAfter correction"
#inord(mybst.root)
#print "\n\nTrial 2"
#mybst.root.left.data=12
#mybst.root.left.right.data=8
#inord(mybst.root)
#correctbst(mybst.root)
#print "\n\nAfter correction"
#inord(mybst.root)
#print "\n\nTrial3"
#mybst.root.left.data=20
#mybst.root.data=8
#inord(mybst.root)
#correctbst(mybst.root)
#print "\n\nAfter correction"
#inord(mybst.root)


#pre=[10 ,5 ,1 ,7 ,40 ,50]
#mybst.root,idx=constructtreefromprerec(pre,0,-float("inf"),float("inf"),len(pre))
#inord(mybst.root)
#print mybst.root,mybst.root.left,mybst.root.right,mybst.root.left.left,mybst.root.left.right,mybst.root.right.right

#pre=[10 ,5 ,1 ,7 ,40 ,50]
#mybst.root,idx=constructtreefromprerec(pre,0,-float("inf"),float("inf"),len(pre))
#inord(mybst.root)
#print mybst.root,mybst.root.left,mybst.root.right,mybst.root.left.left,mybst.root.left.right,mybst.root.right.right

#pre=[10 ,5 ,1 ,7 ,40 ,50]
#mybst.root=constructtreefrompreiter(pre,len(pre))
#inord(mybst.root)

#for i in range(30):
#	print i,ceiling(mybst.root,i)