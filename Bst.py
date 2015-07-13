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
		oot.data=temp.data
		root.right=delete(root.right,temp.data)
	return root
def isbst(root):
	if root==None:
		return True
	if root.left:
		if root.left.data>root.data:
			return False
	if root.right:
		if root.right.data<root.data:
			return False
	if (not isbst(root.left)) or (not isbst(root.right)):
		return False
	return True
mybst=BST()
mybst.root=insert(mybst.root,7)
mybst.root=insert(mybst.root,5)
mybst.root=insert(mybst.root,6)
mybst.root=insert(mybst.root,1)
mybst.root=insert(mybst.root,2)
mybst.root=insert(mybst.root,3)
mybst.root=insert(mybst.root,4)
inord(mybst.root)

#print search(mybst.root,5)

#delete(mybst.root,6)
#inord(mybst.root)

#print minval(mybst.root)

#mybst.root.data=0
#inord(mybst.root)
#print isbst(mybst.root)
