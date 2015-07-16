class stack(object):
	def __init__(self,capacity):
		self.top=-1
		self.capacity=capacity
		self.arr=[None]*capacity
	def __str__(self):
		if self.top==-1:
			return str([])
		return str(self.arr[0:self.top+1])

def isfull(stack):
	return stack.top==stack.capacity-1

def isempty(stack):
	return stack.top==-1
def push(stack,x):
	if not isfull(stack):
		stack.top+=1
		stack.arr[stack.top]=x
	else:
		print "o/f"
def pop(stack):
	if not isempty(stack):
		s=stack.arr[stack.top]
		stack.top-=1
		return s
	else:
		print "o/f"
		return -1

def peek(stack):
	return stack.arr[stack.top]
	

mystack=stack(5)
#print mystack
push(mystack,1)
push(mystack,2)

#print mystack
#print pop(mystack)
#print mystack
#print pop(mystack)
print mystack
print peek(mystack)