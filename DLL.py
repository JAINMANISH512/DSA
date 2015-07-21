class Node(object):
	def __init__(self,data):
		self.data=data
		self.next=None
		self.prev=None
	def __str__(self):
		return str(self.data)

class DLL(object):
	def __init__(self,head=None):
		self.head=head
	def __str__(self):
		curr=self.head
		arr=[]
		while curr:
			arr.append(curr.data)
			curr=curr.next
		return str(arr)

def push(head,x):
	new=Node(x)
	if head==None:
		head=new
	else:
		new.next=head
		head.prev=new
		head=new
	return head

def insend(head,x):
	new=Node(x)
	if head==None:
		head=new
	else:
		curr=head
		while not curr.next==None:
			curr=curr.next
		curr.next=new
		new.prev=curr
	return head

def after(node1,x):
	if node1==None:
		return
	new=Node(x)
	new.next=node1.next
	new.prev=node1
	node1.next=new
	new.next.prev=new

def before(node1,x):
	if node1==None:
		return
	new=Node(x)
	new.next=node1
	new.prev=node1.prev
	node1.prev=new
	new.prev.next=new

def delete(head,node1):
	if head==None or node1== None:
		return head
	if head==node1:
		head=head.next
	if node1.next:
		node1.next.prev=node1.prev
	if node1.prev:
		node1.prev.next=node1.next
	del node1
	return head

mylist=DLL()
print mylist
mylist.head=push(mylist.head,2)
print mylist
mylist.head=push(mylist.head,1)
print mylist
mylist.head=insend(mylist.head,1)
print mylist
mylist.head=insend(mylist.head,6)
print mylist
after(mylist.head.next.next,9)
print mylist
after(mylist.head,9)
print mylist
before(mylist.head.next.next,8)
print mylist

mylist.head=delete(mylist.head,mylist.head.next)
print mylist
mylist.head=delete(mylist.head,mylist.head)
print mylist