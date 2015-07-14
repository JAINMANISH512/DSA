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
inord(mybst.root)

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

