class Node(object):
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
        self.nextright=None #for connectig nodes at same level 
        self.succ=None
    
    def __str__(self):
        return str(self.data)
    
    #def __del__(self):
    #    print "deleting"

class ThreadNode(object):
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
        self.rightThread=None    
    
    def __str__(self):
        return str(self.data)
        
class Tree(object):
    def __init__(self, root=None):
        self.root = root

def preorder(root):
    if root==None:
        return 
    print root
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root==None:
        return 
    
    inorder(root.left)
    print root
    inorder(root.right)

def postorder(root):
    if root==None:
        return 
    
    postorder(root.left)
    postorder(root.right)
    print root

def leftmost(root):
    if root ==None:
        return None
    while root.left!=None:
        root=root.left
    return root
    
def threadinord(root):
    curr=leftmost(root)
    while curr!=None:
        print curr
        if curr.rightThread==True:
            curr=curr.right
        else:
            curr=leftmost(curr.right)

def size(root):
    if root==None:
        return 0
    return size(root.left)+size(root.right)+1

def isidentical(root1,root2):
    if root1==None and root2==None:
        return True
    if((not root1 == None) and (not root2 == None)):
        if root1.data==root2.data and isidentical(root1.left,root2.left) and isidentical(root1.right,root2.right):
            return True
    
    return False		
def isgreater(a,b):
    return a>b

def height(root):
    if root==None:
        return 0
    lheight=height(root.left)
    rheight=height(root.right)
    if isgreater(lheight,rheight):
        return lheight+1
    else:
        return rheight+1	

def deltreex(root):
    if root==None:
        return
    deltree(root.left)
    deltree(root.right)
    del root

def deltree(root):
    deltreex(root)
    root=None
    return root
def convertmirror(root):
    if root==None:
        return
    convertmirror(root.left)
    convertmirror(root.right)
    temp=root.left
    root.left=root.right
    root.right=temp
    
def printpaths(root,patharr,pathlen):
    if root==None:
        return
    patharr[pathlen]=root.data
    pathlen=pathlen+1
    if root.left == None and root.right ==None:
        print patharr[0:pathlen]
    else:
        printpaths(root.left,patharr,pathlen)
        printpaths(root.right,patharr,pathlen)

def levelorder(root):
    for i in range(height(root)):
        printgivenlevel(root,i+1)
        print "\n"

def printgivenlevel(root,level):
    if root==None:
        return
    if level==1:
        print root.data 
    else:
        printgivenlevel(root.left,level-1)
        printgivenlevel(root.right,level-1)

def leafcount(root):
    if root==None:
        return 0
    if root.left==None and root.right==None:
        return 1
    else:
        return leafcount(root.left)+leafcount(root.right)

def levelorderspiral(root):
    ltr=True
    for i in range(height(root)):
        printgivenlevelspiral(root,i+1,ltr)
        print "\n"
        ltr=not ltr

def printgivenlevelspiral(root,level,ltr):
    if root==None:
        return
    if level==1:
        print root.data 
    else:
        if ltr:
            printgivenlevelspiral(root.left,level-1,ltr)
            printgivenlevelspiral(root.right,level-1,ltr)
        else:
            
            printgivenlevelspiral(root.right,level-1,ltr)
            printgivenlevelspiral(root.left,level-1,ltr)

def childsum(root):
    if root==None:
        return True
    if root.left==None and root.right==None:
        return True
    leftval=0
    rightval=0
    if root.left:
        leftval=root.left.data
    if root.right:
        rightval=root.right.data
    if root.data==leftval+rightval and childsum(root.left) and childsum(root.right):
        return True
    else :
        return False

def convertchildsum(root):
    if root==None:
        return
    if root.left==None and root.right==None:
        return
    convertchildsum(root.left)
    convertchildsum(root.right)
    leftval=0
    rightval=0
    if root.left:
        leftval=root.left.data
    if root.right:
        rightval=root.right.data
    diff=leftval+rightval-root.data
    if diff>0:
        root.data+=diff
    else:
        increment(root,-diff)

def increment(node,diff):
    if node.left:
        node.left.data+=diff
        increment(node.left,diff)
    else:
        node.right.data+=diff
        increment(node.right,diff)
def diameter(root):
    if root==None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    
    ld=diameter(root.left)
    rd=diameter(root.right)
     
    return max(lh+rh+1,ld,rd)

def isbalanced(root):
    if root==None:
        return True
    lh=height(root.left)
    rh=height(root.right)
    
    if abs(lh-rh)<=1 and isbalanced(root.left) and isbalanced(root.right):
        return True
    else:
        return False


def inorditer(root):
    stack=[]
    curr=root
    done=False
    while not done:
        if curr:
            stack.append(curr)
            curr=curr.left
        else:
            if not len(stack) == 0:
                curr=stack.pop()
                print curr.data
                curr=curr.right
            else:
                done=True    

def roottoleafsum(root,sum):
    if root==None:
        return sum==0
    sum=sum-root.data    
    if sum==0 and root.left==None and root.right== None:
        return True
    ans=False
    
    ans=roottoleafsum(root.left,sum) or roottoleafsum(root.right,sum)    
    return ans

preidx=0
def buildtree(ino,pre,str,end):
    global preidx
    print ino,pre,str,end,preidx
    if(str>end):
        return None
    new=Node(pre[preidx])
    print new.data
    preidx+=1
    if(str==end):
        return new
    inidx=search(ino,str,end,new.data)
    new.left=buildtree(ino,pre,str,inidx-1)
    new.right=buildtree(ino,pre,inidx+1,end)
    return new

def search(arr,str,end,val):
    i=str
    while i<=end:
        if arr[i]==val:
            print i
            return i
        i+=1
def printpaths(root):
    path=[None]*1000
    printpathutil(root,path,0)

def printpathutil(root,path,pathlen):
    if root==None:
        return
    path[pathlen]=root.data
    pathlen+=1
    if root.left==None and root.right==None:
        print path[:pathlen]
    else:
        printpathutil(root.left,path,pathlen)
        printpathutil(root.right,path,pathlen)

def doubletree(root):
    if root==None:
        return
    doubletree(root.left)
    doubletree(root.right)
    oldleft=root.left
    newleft=Node(root.data)
    root.left=newleft
    newleft.left=oldleft

def maxwidth(root):
    maxwidth=0
    for i in range(height(root)):
        width=treewidth(root,i+1)
        if width>maxwidth:
            maxwidth=width
    return maxwidth    

def treewidth(root,lev):
    if root==None:
        return 0
    if lev==1:
        return 1
    elif lev>1:
        return treewidth(root.left,lev-1)+treewidth(root.right,lev-1)
def isstructsame(root1,root2):
    if root1==None and root2==None:
        return True
    if root1 and root2 and isstructsame(root1.left,root2.left) and isstructsame(root1.right,root2.right):
        return True
    else:
        return False

def isfoldable(root):
    if root==None:
        return True
    convertmirror(root.left)
    res=isstructsame(root.left,root.right)
    convertmirror(root.left)
    return res

def printkdist(root,k):
    if root==None:
        return
    if k==0:
        print root.data
    else:
        printkdist(root.left,k-1)
        printkdist(root.right,k-1)

def getlevel(root,val,lev):
    if root==None:
        return 0
    if root.data==val:
        return lev
    res=getlevel(root.left,val,lev+1)
    if not res==0:
        return res
    else:
        return getlevel(root.right,val,lev+1)

def printances(root,tar):
    if root==None:
        return False
    if root.data==tar:
        return True

    if printances(root.left,tar) or printances(root.right,tar):
        print root.data
        return True    

def sumtree(root):
    if root==None:
        return 0
    else:
        return root.data+sumtree(root.left)+sumtree(root.right)

def issumtree(root):
    if root==None:
        return True
    if root.left==None and root.right==None:
        return True
    ls=sumtree(root.left)
    rs=sumtree(root.right)

    if root.data==ls+rs and issumtree(root.left) and issumtree(root.right):
        return True
    return False

def issubtree(root1,root2):
    if root2==None:
        return True
    if root1==None:
        return False
    if isidentical(root1,root2):
        return True
    return issubtree(root1.left,root2) or issubtree(root1.right,root2)

def connect(p):
	if not p:
		return
	if p.left:
		p.left.nextright=p.right
	if p.right:
		if p.nextright:
			p.right.nextright=p.nextright.left
	connect(p.left)
	connect(p.right)


def populateinordersucc(root):
	if root:
		populateinordersucc(root.right)
		root.succ=populateinordersucc.inordsucc
		populateinordersucc.inordsucc=root
		populateinordersucc(root.left)
populateinordersucc.inordsucc=None

def verticalsum(root):
	if not root:
		return
	mydict={}
	verticalsumutil(root,0,mydict)
	print mydict
def verticalsumutil(root,hd,mydict):
	if not root:
		return
	verticalsumutil(root.left,hd-1,mydict)
	prevsum=0
	if mydict.has_key(hd):
		prevsum=mydict[hd]
	mydict[hd]=prevsum+root.data
	verticalsumutil(root.right,hd+1,mydict)
def gettargetleaf(root,maxsum,currsum,target):
	if not root:
		return maxsum,target
	currsum+=root.data
	if root.left==None and root.right==None:
		if currsum>maxsum:
			maxsum=currsum
			target=root
	maxsum,target=gettargetleaf(root.left,maxsum,currsum,target)
	maxsum,target=gettargetleaf(root.right,maxsum,currsum,target)
	return maxsum,target
def printmaxsumpath(root,target):
	if root==None:
		return False
	if root==target or printmaxsumpath(root.left,target) or printmaxsumpath(root.right,target):
		print root.data
		return True
	return False

def maxsumpath(root):
	if root==None:
		return 0
	target=None
	maxsum=-float("inf")
	maxsum,target=gettargetleaf(root,maxsum,0,target)
	print maxsum,target
	printmaxsumpath(root,target)
	return maxsum
def arraytobinary(array,start,end):
	if start>end:
		return None
	maxi=-float("inf")
	idx=-1
	for i in range(start,end+1):
		if array[i]>maxi:
			maxi=array[i]
			idx=i
	root= Node(array[idx])
	if start==end:
		return root
		
	root.left=arraytobinary(array,start,idx-1)
	root.right=arraytobinary(array,idx+1,end)
	return root


mytree=Tree()
mytree.root=Node(1)
mytree.root.left=Node(2)
mytree.root.right=Node(3)
mytree.root.left.left=Node(4)
mytree.root.left.right=Node(5)

mytree2=Tree()
mytree2.root=Node(1)
mytree2.root.left=Node(2)
mytree2.root.right=Node(3)
mytree2.root.left.left=Node(4)
mytree2.root.left.right=Node(5)

mytree3=Tree()
mytree3.root=Node(1)
mytree3.root.left=Node(3)
mytree3.root.left.left=Node(4)
mytree3.root.left.right=Node(5)

mytree4=Tree()
mytree4.root=Node(12)
mytree4.root.left=Node(9)
mytree4.root.right=Node(3)
mytree4.root.left.left=Node(4)
mytree4.root.left.right=Node(5)

mytree5=Tree()
mytree5.root=Node(26)
mytree5.root.left=Node(9)
mytree5.root.right=Node(8)
mytree5.root.left.left=Node(4)
mytree5.root.left.right=Node(5)

mytree6=Tree()
mytree6.root=Node(2)
mytree6.root.left=Node(4)
mytree6.root.right=Node(5)

#print mytree.root,mytree.root.left,mytree.root.right,mytree.root.left.left

#preorder(mytree.root)
#inorder(mytree.root)
#postorder(mytree.root)

#print leftmost(mytree.root)

#threadedinord(mytree.root)

#print size(mytree.root)

#print isidentical(mytree.root,mytree2.root)
#print isidentical(mytree2.root,mytree2.root)
#print isidentical(mytree2.root,mytree3.root)

#print height(mytree.root)
#print height(mytree3.root)

#print inorder(mytree.root)
#deltreex(mytree.root)
#mytree.root=deltree(mytree.root)
#print inorder(mytree.root)

#convertmirror(mytree.root)
#inorder(mytree.root)

#patharr=[None]*1000
#pathlen=0
#printpaths(mytree.root,patharr,pathlen)

#levelorder(mytree.root)

#print leafcount(mytree.root)

#levelorderspiral(mytree.root)

#print childsum(mytree1.root)
#print childsum(mytree4.root)

#levelorder(mytree.root)
#convertchildsum(mytree.root)
#levelorder(mytree.root)

#print diameter(mytree.root)

#print isbalanced(mytree4.root)

#inorditer(mytree.root)

#print roottoleafsum(mytree.root,3)

#ino=['D', 'B', 'E', 'A', 'F', 'C']
#pre=['A', 'B', 'D', 'E', 'C', 'F']
#length=len(pre)
#root = buildtree(ino,pre,0,length-1)
#inorder(root)

#printpaths(mytree.root)

#doubletree(mytree.root)
#inorder(mytree.root)

#print maxwidth(mytree.root)

#print isfoldable(mytree4.root)

#printkdist(mytree.root,0)
#printkdist(mytree.root,1)
#printkdist(mytree.root,2)
#printkdist(mytree.root,3)

#print getlevel(mytree.root,5,1)

#printances(mytree.root,5)

#print issumtree(mytree5.root)

#print issubtree(mytree.root,mytree2.root)
#print issubtree(mytree2.root,mytree6.root)

#connect(mytree.root)
#print mytree.root,mytree.root.nextright
#print mytree.root.left,mytree.root.left.nextright
#print mytree.root.right,mytree.root.right.nextright
#print mytree.root.left.left,mytree.root.left.left.nextright
#print mytree.root.left.right,mytree.root.left.right.nextrigh0

#populateinordersucc(mytree.root)
#print mytree.root,mytree.root.succ
#print mytree.root.left,mytree.root.left.succ
#print mytree.root.right,mytree.root.right.succ
#print mytree.root.left.left,mytree.root.left.left.succ
#print mytree.root.left.right,mytree.root.left.right.succ

#verticalsum(mytree.root)

#maxsumpath(mytree.root)

#mytree.root=arraytobinary([5,20,35,10,15,30],0,5)
#print mytree.root,mytree.root.left,mytree.root.left.left
#print mytree.root.right,mytree.root.right.left,mytree.root.right.left.left