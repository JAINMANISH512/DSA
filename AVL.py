class node(object):
	def __init__(self,key):
		self.key=key
		self.left=None
		self.right=None
		self.height=1
	def __str__(self):
		return str(self.key)

def height(root):
	if not root:
		return 0
	return root.height 
def updateheight(root):
	root.height=max(height(root.left),height(root.right))+1

def rrot(y):
	x=y.left
	t2=x.right

	x.right=y
	y.left=t2

	updateheight(y)
	updateheight(x)

	return x

def lrot(x):
	y=x.right
	t2=y.left

	y.left=x
	x.right=t2

	updateheight(x)
	updateheight(y)

	return y

def getbal(root):
	if not root:
		return 0
	return height(root.left)-height(root.right)

def insert(root,key):
	if not root:
		return node(key)
	if key<root.key:
		root.left=insert(root.left,key)
	else:
		root.right=insert(root.right,key)
	updateheight(root)
	balance=getbal(root)

	if balance>1 and key<root.left.key:
		return rrot(root)

	if balance<-1 and key>root.right.key:
		return lrot(root)

	if balance>1 and key>root.left.key:
		root.left=lrot(root.left)
		return rrot(root)

	if balance<-1 and key<root.right.key:
		root.right=rrot(root.right)
		return lrot(root)
	return root

def preorder(root):
	if root:
		print root
		preorder(root.left)
		preorder(root.right)
def minvalnode(root):
	curr=root
	while curr.left:
		curr=curr.left
	return curr

def delete(root,key):
	if not root:
		return root
	if key<root.key:
		root.left=delete(root.left,key)
	elif key>root.key:
		root.right=delete(root.right,key)
	else:
		if root.left==None or root.right==None:
			temp=None
			if root.left:
				temp=root.left
			else:
				temp=root.right
			del root
			root=temp
		else:
			temp=minvalnode(root.right)
			root.key=temp.key
			root.right=delete(root.right,temp.key)

	if root==None:
		return root

	updateheight(root)
	balance=getbal(root)

	if balance>1 and getbal(root.left)>=0:
		return rrot(root)

	if balance<-1 and getbal(root.right)<=0:
		return lrot(root)

	if balance>1 and getbal(root.left)<0:		
		root.left=lrot(root.left)
		return rrot(root)

	if balance<-1 and getbal(root.right)>0:
		root.right=rrot(root.right)
		return lrot(root)
	return root



root=None

root=insert(root,10)
root=insert(root,20)
root=insert(root,30)
root=insert(root,40)
root=insert(root,50)
root=insert(root,25)

root1=None
root1=insert(root1,9)
root1=insert(root1,5)
root1=insert(root1,10)
root1=insert(root1,0)
root1=insert(root1,6)
root1=insert(root1,11)
root1=insert(root1,-1)
root1=insert(root1,1)
root1=insert(root1,2)
preorder(root1)
root1=delete(root1,10)
preorder(root1)