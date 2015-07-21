class Node(object):
	def __init__(self,data):
		self.data=data
		self.next=None
	def __str__(self):
		return str(self.data)

class CLL(object):
	def __init__(self,head=None):
		self.head=head

	def __str__(self):
		res=[]
		ptr=self.head
		if self.head:
			res.append(ptr.data)
			ptr=ptr.next
			while not ptr==self.head:
				res.append(ptr.data)
				ptr=ptr.next
		return str(res)

def push(head,data):
	new=Node(data)
	if head:
		ptr=head
		while not ptr.next==head:
			ptr=ptr.next
		ptr.next=new
		new.next=head
	else:
		new.next=new
	head=new

	return head

def splitin2(head):
	if head==None:
		return None,None
	if head.next==head:
		return head,None
	fast=slow=head
	while not (fast.next==head) and not (fast.next.next==head):
		slow=slow.next
		fast=fast.next.next
	if fast.next.next==head:
		fast=fast.next
	head1=head
	head2=slow.next
	slow.next=head1
	fast.next=head2
	return head1,head2

def sortedinsert(head,data):
	new=Node(data)
	if head==None:
		new.next=new
		head=new
		return head
	if head.data>=new.data:
		curr=head
		while not (curr.next== head):
			curr=curr.next
		curr.next=new
		new.next=head
		head=new
		return head
	curr=head
	while not (curr.next== head) and curr.next.data<new.data:
			curr=curr.next
	new.next=curr.next
	curr.next=new


	return head
#mylist=CLL()
#print mylist
#mylist.head=push(mylist.head,2)
#mylist.head=push(mylist.head,4)
#mylist.head=push(mylist.head,3)
#mylist.head=push(mylist.head,6)
#mylist.head=push(mylist.head,3)
#print mylist

#mylist1=CLL()
#mylist2=CLL()
#mylist1.head,mylist2.head=splitin2(mylist.head)
#print mylist1,mylist2

mylist=CLL()
print mylist
mylist.head=sortedinsert(mylist.head,1)
mylist.head=sortedinsert(mylist.head,3)
mylist.head=sortedinsert(mylist.head,0)
mylist.head=sortedinsert(mylist.head,2)
print mylist