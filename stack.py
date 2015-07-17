class stack(object):
	def __init__(self,capacity):
		self.top=-1
		self.capacity=capacity
		self.arr=[None]*capacity
	def __str__(self):
		if self.top==-1:
			return str([])
		return str(self.arr[0:self.top+1])

class twostack(object):
	def __init__(self,capacity):
		self.top1=-1
		self.top2=capacity
		self.capacity=capacity
		self.arr=[None]*capacity
	def __str__(self):
		if self.top1==-1 and self.top2==self.capacity:
			return str([])
		return str(self.arr[0:self.top1+1])+"---"+str(self.arr[self.top2:])

def push1(stack,x):
	if stack.top1<stack.top2-1:
		stack.top1+=1
		stack.arr[stack.top1]=x
	else:
		print "O/F"

def push2(stack,x):
	if stack.top1<stack.top2-1:
		stack.top2-=1
		stack.arr[stack.top2]=x
	else:
		print "O/F"
def pop1(stack):
	if stack.top1>=0:
		s=stack.arr[stack.top1]
		stack.top1-=1
		return s
	else:
		print "U/F"

def pop2(stack):
	if stack.top2<stack.capacity:
		s=stack.arr[stack.top2]
		stack.top2+=1
		return s
	else:
		print "U/F"

def isfull(stack):
	return stack.top==stack.capacity-1

def isemp(stack):
	return stack.top==-1
def push(stack,x):
	if not isfull(stack):
		stack.top+=1
		stack.arr[stack.top]=x
	else:
		print "o/f"
def pop(stack):
	if not isemp(stack):
		s=stack.arr[stack.top]
		stack.top-=1
		return s
	else:
		print "o/f"
		return -1

def peek(stack):
	return stack.arr[stack.top]

def isoperand(a):
	if (a>='a' and a<='z') or (a>='A' and a<='Z'):
		return True
	else :
		return False
def isdigit(a):
	if (a>='0' and a<='9') :
		return True
	else :
		return False

def prec(a):
	if a=='+' or a=='-':
		return 1
	elif a=="*" or a=="/":
		return 2
	elif a=="^":
		return 3
	else:
		return -1

def infixtoprefix(infix):
	print infix
	pfix=""
	mystack=stack(len(infix))
	for i in range(len(infix)):
		if isoperand(infix[i]):
			#pfix.append(infix[i])
			pfix=pfix+infix[i]
		elif infix[i]=='(':
			push(mystack,infix[i])
		elif infix[i]==')':
			while (not isemp(mystack)) and (not peek(mystack)=='('):
				#pfix.append(pop(mystack))
				pfix=pfix+pop(mystack)
			if (not isemp(mystack)) and (not peek(mystack)=='('):
				print"Inval expression"
				return pfix
			pop(mystack)
		else:
			while (not isemp(mystack)) and prec(infix[i])<=prec(peek(mystack)):
				#pfix.append(pop(mystack))
				pfix=pfix+pop(mystack)
			push(mystack,infix[i])

	while not isemp(mystack):
		#pfix.append(pop(mystack))
		pfix=pfix+pop(mystack)
	
	return pfix

def evalpost(pfix):
	mystack=stack(len(pfix))
	for i in range(len(pfix)):
		if isdigit(pfix[i]):
			push(mystack,float(pfix[i]))
		else:
			a=pop(mystack)
			b=pop(mystack)
			if pfix[i]=='+':
				push(mystack,b+a)
			elif pfix[i]=='-':
				push(mystack,b-a)
			elif pfix[i]=='*':
				push(mystack,b*a)
			else :
				push(mystack,b/a)

	return pop(mystack)

def revstr(inp):
	out=""
	mystack=stack(len(inp))
	for i in range(len(inp)):
		push(mystack,inp[i])
	while (not isemp(mystack)):
		out=out+pop(mystack)
	return out

def parencheck(inp):
	mystack=stack(len(inp))
	for i in range(len(inp)):
		if inp[i]=='(' or inp[i]=='[' or inp[i]=='{':
			push(mystack,inp[i]) 
		else:
			if isemp(mystack):
				return False
			elif inp[i]==')' and pop(mystack)=='(':
				continue
			elif inp[i]=='}' and pop(mystack)=='{':
				continue
			elif inp[i]==']' and pop(mystack)=='[':
				continue
			else:
				return False
	if isemp(mystack):
		return True
	else:
		return False

def nge(inp):
	mystack=stack(len(inp))
	push(mystack,inp[0])
	for i in range(1,len(inp)):
		next=inp[i]
		if not isemp(mystack):
			curr=pop(mystack)
			while curr <next:
				print str(curr)+"->"+str(next)
				if isemp(mystack):
					break
				curr=pop(mystack)
			if curr>next:
				push(mystack,curr)
		push(mystack,next)

	while not isemp(mystack):
		print str(pop(mystack))+"->-1"


def insertatbot(mystack,x):
	if isemp(mystack):
		push(mystack,x)
	else:
		temp=pop(mystack)
		insertatbot(mystack,x)
		push(mystack,temp)
def stackreverse(mystack):
	if isemp(mystack):
		return
	temp=pop(mystack)
	stackreverse(mystack)
	insertatbot(mystack,temp)

def stockspan(price):
	span=[]
	mystack=stack(len(price))
	for i in range(len(price)):
		span.append(0)
	span[0]=1
	push(mystack,0)
	for i in range(1,len(price)):
		curr=price[i]
		while not isemp(mystack) and curr>price[peek(mystack)]:
			pop(mystack)
		if isemp(mystack):
			span[i]=i+1
		else:
			span[i]=i-peek(mystack)
		push(mystack,i)
	return span

def specialpush(mystack,spclstack,x):
	if isemp(mystack):
		push(mystack,x)
		push(spclstack,x)
	else:
		push(mystack,x)
		s=peek(spclstack)
		if x<s:
			push(spclstack,x)
		else:
			push(spclstack,s)

def specialpop(mystack,spclstack):
	s=pop(mystack)
	pop(spclstack)
	return s

def getmin(spclstack):
	return peek(spclstack)


#mystack=stack(5)
#print mystack
#push(mystack,1)
#push(mystack,2)

#print mystack
#print pop(mystack)
#print mystack
#print pop(mystack)
#print mystack
#print peek(mystack)

#print infixtoprefix("a+b*(c^d-e)^(f+g*h)-i")
#print evalpost("8231*+9-/")

#print revstr("MANISH")

#mystack2=twostack(10)
#print mystack2
#push1(mystack2,10)
#push1(mystack2,20)
#ush1(mystack2,15)
#push2(mystack2,1)
#push2(mystack2,19)
#print mystack2
#print pop1(mystack2)
#print pop2(mystack2)
#print pop2(mystack2)
#print mystack2

#print parencheck("[(({[]})])")

#arr1=[4,2,5,20,2]
#nge(arr1)

#mystack=stack(5)
#push(mystack,2)
#push(mystack,3)
#print mystack
#insertatbot(mystack,4)
#print mystack
#stackreverse(mystack)
#print mystack

#print stockspan([10, 4, 5, 90, 120, 80])

#mystack=stack(5)
#spclstack=stack(5)
#print mystack,spclstack
#specialpush(mystack,spclstack,5)
#print mystack,spclstack
#specialpush(mystack,spclstack,10)
#print mystack,spclstack
#specialpush(mystack,spclstack,2)
#print mystack,spclstack
#specialpush(mystack,spclstack,1)
#print mystack,spclstack
#print specialpop(mystack,spclstack)
#print mystack,spclstack
#print specialpop(mystack,spclstack)
#print mystack,spclstack


