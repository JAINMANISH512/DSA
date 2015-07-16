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
			return slow
	return None

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

def altersplit(head):###rev order
	
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


def sortedmerge(head1,head2):
	if head1==None:
		return head2
	elif head2==None:
		return head1
	elif head1.data < head2.data:
		result=head1
		result.next=sortedmerge(head1.next,head2)
	else:
		result=head2
		result.next=sortedmerge(head1,head2.next)
	return result
def sortedmerged(head1,head2):
	if head1==None:
		return head2
	elif head2==None:
		return head1
	elif head1.data > head2.data:
		result=head1
		result.next=sortedmerged(head1.next,head2)
	else:
		result=head2
		result.next=sortedmerged(head1,head2.next)
	return result
def isiden(head1,head2):
	if head1==None and head2==None:
		return True
	elif head1==None and head2:
		return False
	elif head1 and head2==None:
		return False
	elif not head1.data == head2.data:
		return False
	else:
		return isiden(head1.next,head2.next)
def frontbacksplit(head):
	if head==None or head.next==None:
		return head,None
	slow=head
	fast=head.next
	while fast:
		fast=fast.next
		if fast:
			fast=fast.next
			slow=slow.next
	front=head
	back=slow.next
	slow.next=None

	return front,back

def mergesort(head):
	if head==None or head.next==None:
		return head
	front,back=frontbacksplit(head)
	front=mergesort(front)
	back=mergesort(back)
	return sortedmerge(front,back)
def mergesortd(head):
	if head==None or head.next==None:
		return head
	front,back=frontbacksplit(head)
	front=mergesortd(front)
	back=mergesortd(back)
	return sortedmerged(front,back)

def reversek(head,k):
	if head==None:
		return head
	count=0
	curr=head
	prev=None
	while curr and count<k:
		nextn=curr.next
		curr.next=prev
		prev=curr
		curr=nextn
		count+=1

	if curr:
		head.next=reversek(curr,k)
	return prev

def revaltk(head,k,b):
	if head==None:
		return head
	count=0
	curr=head
	prev=None
	while curr and count<k:
		nextn=curr.next
		if b:
			curr.next=prev
		prev=curr
		curr=nextn
		count+=1
	if b:
		head.next=revaltk(curr,k,not b)
		return prev
	else:
		prev.next=revaltk(curr,k,not b)
		return head
def greatonright(head):
	if head==None or head.next==None:
		return
	rev=revrec(head)
	maxi=rev.data
	curr=rev.next
	while curr:
		if curr.data<maxi:
			delnode(rev,curr)
		else:
			maxi=curr.data
			curr=curr.next
	return revrec(rev)

def segoddeven(head):
	if head==None or head.next==None:
		return head
	oddstart=None
	oddend=None
	evenstart=None
	evenend=None
	curr=head
	while head:
		#print head,evenstart,evenend,oddstart,oddend
		if head.data%2==0:
			if evenend==None:#first node
				evenstart=evenend=head
				head=head.next
				evenend.next=None

			else:
				evenend.next=head
				evenend=head
				head=head.next
				evenend.next=None
			continue
		else:
			if oddend==None:#first node
				oddstart=oddend=head
				head=head.next
				oddend.next=None
			else:
				oddend.next=head
				oddend=head
				head=head.next
				oddend.next=None
	oddend.next=evenstart
	return oddstart

def removeloop(head):
	loopnode=detectloop(head)
	ptr=head

	ptr2=loopnode
	
	count=1
	while not ptr2.next==loopnode:
		count+=1
		ptr2=ptr2.next

	ptr2=head
	k=1
	while k<=count:
		k+=1
		ptr2=ptr2.next
	while not ptr==ptr2:
		ptr=ptr.next
		ptr2=ptr2.next
	k=1
	while k<count:
		ptr2=ptr2.next
		k+=1
	
	ptr2.next=None
	
	return head

def addlist(head1,head2):
	res=linkedlist()
	ptr1=head1
	ptr2=head2
	carry=0
	result=0
	while ptr1 or ptr2:
		if ptr1:
			val1=ptr1.data
			ptr1=ptr1.next
		else:
			val1=0
		if ptr2:
			val2=ptr2.data
			ptr2=ptr2.next
		else:
			val1=0
		result=val1+val2+carry
		if result>9:
			carry=int(result/10)
			result=result%10
		else:
			carry=0
		res.head=insertend(res.head,result)
	if not carry== 0:
		res.head=insertend(res.head,carry)
	return res

def checktriplet(head1,head2,head3,key):
	a=mergesort(head1)
	b=mergesortd(head2)
	c=head3
	while c:
		while a and b:
			num=a.data+b.data+c.data
			if num==key:
				print a,b,c
				return True
			elif num<key:
				a=a.next
			else:
				b=b.next
	c=c.next
	return False

def rotatebyk(head,k):
	if head==None:
		return head
	ptr=head
	realhead=head
	count=1
	while count<k:
		if ptr.next:
			ptr=ptr.next
		else:
			print "smaller list"
			return head
		count+=1
	newhead=ptr.next
	ptr.next=None
	ptr=newhead
	while ptr.next:
		ptr=ptr.next
	ptr.next=realhead
	return newhead

def flatten(head):# todo
	if head==None or head.right==None:
		return head
	return sortedmerge(root,flatten(root.right))

def addequallength(head1,head2):
	result=Node(None)
	
	if head1==None:
		return None,0
	result.next,carry=addequallength(head1.next,head2.next)
	sumx=head1.data+head2.data+carry
	carry=sumx/10
	sumx=sumx%10
	result.data=sumx
	return result,carry
def addremain(head1,curr,carry,result):
  
    if not head1==curr:
    	result,carry=addremain(head1.next,curr,carry,result)
    	sumx=head1.data+carry
    	carry=sumx/10
    	sumx=sumx%10
    	result=insertfront(result,sumx)
    	
    return result,carry

def addlistunequal(head1,head2):
	if head1==None:
		return head2
	if head2==None:
		return head1
	k1=countnodes(head1)
	k2=countnodes(head2)
	diff=abs(k1-k2)
	if k1==k2:
		result,carry=addequallength(head1,head2)
		result=insertfront(result,carry)
		return result
	elif k1<k2:
		head1,head2=head2,head1
	curr=head1
	while diff>0:
		diff-=1
		curr=curr.next
	result,carry=addequallength(curr,head2)
	
	result,carry=addremain(head1,curr,carry,result)
	if carry:
		result=insertfront(result,carry)
	return result

def sortzeroonetwo(head):
	if head==None:
		return head
	zero=one=two=0
	curr=head
	while curr:
		if curr.data==0:
			zero+=1
		elif curr.data==1:
			one+=1
		else:
			two+=1
		curr=curr.next
	curr=head
	
	while zero:
		curr.data=0
		curr=curr.next
		zero-=1
	while one:
		curr.data=1
		curr=curr.next
		one-=1
	while two:
		curr.data=2
		curr=curr.next
		two-=1
	return head
def flattenmultilevel(head):#todo
	pass

def skipmdeln(head,m,n):
	if head==None:
		return head
	curr=head
	for i in range(1,m):
		curr=curr.next
		if curr==None:
			print "m greater than length of list"
			return head
	if curr==None:
		return head
	ptr=curr
	for i in range(0,n):
		temp=curr.next
		if temp:
			curr.next=temp.next
			del temp
		else:
			return head
	curr.next=skipmdeln(curr.next,m,n)
	return head		

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

mylist5=linkedlist()
mylist5.head=Node(7)
mylist5.head.next=Node(3)
mylist5.head.next.next=Node(5)
mylist5.head.next.next.next=Node(2)
mylist5.head.next.next.next.next=Node(6)
mylist5.head.next.next.next.next.next=Node(2)


mylist4=linkedlist()
mylist4.head=Node(1)
mylist4.head.next=Node(3)
mylist4.head.next.next=Node(2)
mylist4.head.next.next.next=Node(5)
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

#print mylist3
#mylista,mylistb=altersplit(mylist3.head)
#print mylista,mylistb

#print mylist3,mylist4
#result=linkedlist()
#result.head=sortedmerge(mylist3.head,mylist4.head)
#print result

#print isiden(mylist3.head,mylist4.head)

#print mylist5
#lista=linkedlist()
#listb=linkedlist()
#lista.head,listb.head=frontbacksplit(mylist5.head)
#print lista,listb

#print mylist5
#res=linkedlist()
#res.head=mergesort(mylist5.head)
#print res

#print mylist3
#mylist3.head=reversek(mylist3.head,2)
#print mylist3

#print mylist3
#mylist3.head=revaltk(mylist3.head,3,True)
#print mylist3

#print mylist5
#mylist5.head=greatonright(mylist5.head)
#print mylist5

#print mylist3
#mylist3.head=segoddeven(mylist3.head)
#print mylist3

#print mylist3
#mylist3.head.next.next.next.next.next.next=mylist3.head.next.next
#print detectloop(mylist3.head)
#print mylist3
#mylist3.head=removeloop(mylist3.head)
#print mylist3

#print mylist,mylist3
#print addlist(mylist.head,mylist3.head)

#print mylist,mylist3,mylist
#print checktriplet(mylist.head,mylist3.head,mylist4.head,7)

#print mylist3
#mylist3.head=rotatebyk(mylist3.head,3)
#print mylist3

#print mylist,mylist3
#result=linkedlist()
#result.head=addlistunequal(mylist.head,mylist3.head)
#print result


#mylist6=linkedlist()
#mylist6.head=Node(0)
#mylist6.head.next=Node(1)
#mylist6.head.next.next=Node(2)
#mylist6.head.next.next.next=Node(2)
#mylist6.head.next.next.next.next=Node(1)
#mylist6.head.next.next.next.next.next=Node(0)
#print mylist6
#mylist6.head=sortzeroonetwo(mylist6.head)
#print mylist6

#mylist.head=flattenmultilevel(mylist.head)

#print mylist3
#mylist3.head=skipmdeln(mylist3.head,2,3)
#print mylist3