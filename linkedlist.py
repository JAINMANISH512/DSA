class Node(object):
	def __init__(self,data):
		self.data=data
		self.next=None

	def __str__(self):
		return str(self.data)

class linkedlist(object):
	def __init__(self,head=None):
		self.head=head

	def __str__(self):
		curr=self.head
		arr=[]
		while curr:
			arr.append(curr.data)
			curr=curr.next
		return str(arr)

def insertfront(head,data):
	new=Node(data)
	new.next=head
	head=new
	return head

def insertafter(prev,data):
	if prev==None:
		print "Prev can't be none"
		return
	new=Node(data)
	new.next=prev.next
	prev.next=new
def insertend(head,data):
	if head==None:
		head=Node(data)
		return head
	curr=head
	while curr.next:
		curr=curr.next
	curr.next=Node(data)
	return head

def delete(head,key):
	if head.data==key:
		temp=head
		head=head.next
		del temp
		return head
	curr=head
	while curr:
		if curr.next.data==key:
			temp=curr.next
			curr.next=temp.next
			del temp
			break
		else:
			curr=curr.next
	return head


def getnnode(head,n):
	curr=head
	idx=1
	while curr:
		if idx==n:
			print curr
			return
		curr=curr.next
		idx+=1
	if idx <=n:
		print "List is shorter than n "	

def delnode(head,node):
	if head==node:
		head=head.next
		del node
		return head
	if node.next==None:
		curr=head
		while curr:
			if curr.next==node:
				curr.next=None
				del node
			curr=curr.next
	else:
		temp=node.next
		node.data=temp.data
		node.next=temp.next
		del temp
	return head
def printmid(head):
	if head==None:
		print"Empty list"
		return
	fast=slow=head
	while fast.next and fast.next.next:
		fast=fast.next.next
		slow=slow.next
	print slow

def nthfromend(head,n):
	ref=head
	main=head
	count=1
	while count<n and ref:
		ref=ref.next
		count+=1
	if ref==None:
		print "Short list"
		return None
	while ref.next:
		ref=ref.next
		main=main.next
	return main

def deletelist(head):
	curr=head
	while curr:
		nextn=curr.next
		del curr
		curr=nextn
	head=None
	return head
def xcount(head,x):
	count=0
	curr=head
	while curr:
		if curr.data==x:
			count+=1
		curr=curr.next
	return count

def reviter(head):
	curr=head
	prev=None
	while curr:
		nextn=curr.next
		curr.next=prev
		prev=curr
		curr=nextn
	head=prev
	return head

def revrec(head):
	first=head
	if first==None:
		return head
	rest=first.next
	if rest==None:
		return head
	rest=revrec(rest)
	first.next.next=first
	first.next=None
	head=rest
	return head

def detectloop(head):
	slow=head
	fast=head
	while fast.next and slow.next and fast.next.next:
		slow=slow.next
		fast=fast.next.next
		if slow==fast:
			return True
	return False

def checkpalin(head):
	stack=[]
	curr=head
	while curr:
		stack.append(curr.data)
		curr=curr.next
	curr=head
	while curr:
		s=stack.pop()
		if not s==curr.data:
			return Faxlse
		curr=curr.next
	return True

def inssorted(head,x):
	if head==None:
		return Node(x)
	if head.data>=x:
		new=Node(x)
		new.next=head
		return new
	curr=head
	while curr:
		if curr.next:
			if curr.data<x and curr.next.data>=x:
				new=Node(x)
				new.next=curr.next
				curr.next=new
				return head
		else:
			curr.next=Node(x)
			return head
		curr=curr.next
def countnodes(head):
	curr=head
	count=0
	while curr:
		count+=1
		curr=curr.next
	return count

def intersect(head1,head2):
	if head1==None or head2==None:
		return None
	c1=countnodes(head1)
	c2=countnodes(head2)
	
	diff=abs(c1-c2)
	if c1>c2:
		curr=head1
		count=1
		while count<diff:
			curr=curr.next
			count+=1
		curr2=head2
		while curr and curr2:
			if curr==curr2:
				return curr
			curr=curr.next
			curr2=curr2.next
	else:
		curr=head2
		count=0
		while count<diff:
			curr=curr.next
			count+=1
		curr2=head1
		while curr and curr2:
			if curr==curr2:
				return curr
			curr=curr.next
			curr2=curr2.next
def printrev(head):
	if head==None:
		return
	printrev(head.next)
	print head
mylist=linkedlist()
mylist.head=Node(1)
mylist.head.next=Node(2)
mylist.head.next.next=Node(3)
print mylist

def deldupli(head):
	if head==None:
		return head
	if head.next==None:
		return head
	curr=head
	while curr and curr.next:
		if curr.data==curr.next.data:
			temp=curr.next
			curr.next=temp.next
			del temp
		curr=curr.next
	return head

def removedupliunsort(head):
	pass

def pairwiseswap(head):
	curr=head
	while curr and curr.next:
		curr.data,curr.next.data=curr.next.data,curr.data
		curr=curr.next.next
	return head

def movelast2front(head):
	curr=head
	while curr and curr.next:
		prev=curr
		curr=curr.next
	prev.next=None
	curr.next=head
	head=curr
	return head

def sortedintersect(head1,head2):
	
	if head1==None or head2==None:
		return None
	if head1.data<head2.data:
		return sortedintersect(head1.next,head2)
	elif head1.data>head2.data:
		return sortedintersect(head1,head2.next)
	else:
		temp=Node(head1.data)
		temp.next=sortedintersect(head1.next,head2.next)
	return temp

def altdel(head):
	if head==None:
		return head
	if head.next==None:
		return head
	node=head.next
	head.next=node.next
	del node
	head.next=altdel(head.next)
	return head

def altersplit(head):
	
	a=linkedlist()
	b=linkedlist()
	if head==None:
		return a,b
	if head.next==None:
		a.head=head
		return a,b
	curr=head
	currnext=curr.next
    
	while curr:
		print curr,currnext
		node=curr
		node.next=a.head
		a.head=node
		if currnext:
			curr=currnext.next
        	node=currnext
        	node.next=b.head
        	b.head=node
        	if curr:
        		currnext=curr.next
        

	return a, b

#mylist.head=insertfront(mylist.head,0)
#print mylist
#mylist.head=insertfront(mylist.head,7)
#print mylist

#insertafter(mylist.head.next.next,4)
#print mylist

#mylist.head=insertend(mylist.head,7)
#print mylist

#mylist.head=delete(mylist.head,3)
#print mylist

#getnnode(mylist.head,1)
#getnnode(mylist.head,4)

#mylist.head=delnode(mylist.head,mylist.head)
#print mylist

#printmid(mylist.head)
#mylist.head.next.next.next=Node(4)
#printmid(mylist.head)
#mylist.head.next.next.next.next=Node(5)
#printmid(mylist.head)

#mylist.head=deletelist(mylist.head)
#print mylist

#mylist.head.next.next.next=Node(3)
#print xcount(mylist.head,3)

#mylist.head=reviter(mylist.head)
#print mylist

#mylist.head=revrec(mylist.head)
#print mylist

#mylist.head.next.next.next=mylist.head
#print detectloop(mylist.head)

#print checkpalin(mylist.head)

#mylist.head=inssorted(mylist.head,2)
#print mylist

#print count(mylist.head)

#mylist2=linkedlist()
#mylist2.head=Node(4)
#mylist2.head.next=Node(5)
#mylist2.head.next.next=mylist.head.next.next
#print mylist,mylist2
#print intersect(mylist.head,mylist2.head)

#printrev(mylist.head)

mylist3=linkedlist()
mylist3.head=Node(1)
mylist3.head.next=Node(1)
mylist3.head.next.next=Node(2)
mylist3.head.next.next.next=Node(3)
mylist3.head.next.next.next.next=Node(3)
mylist3.head.next.next.next.next.next=Node(4)
#print mylist3

#mylist3.head=deldupli(mylist3.head)
#print mylist3

#removedupliunsort(mylist.head)
#mylist.head.next.next.next=Node(4)
#mylist.head=pairwiseswap(mylist.head)
#print mylist

#mylist.head.next.next.next=Node(4)
#mylist.head=movelast2front(mylist.head)
#print mylist

#mylistinter=linkedlist()
#mylistinter.head=sortedintersect(mylist.head,mylist3.head)
#print mylistinter

#print mylist3
#mylist3.head=altdel(mylist3.head)
#print mylist3

print mylist3
mylista,mylistb=altersplit(mylist3.head)
print mylista,mylistb