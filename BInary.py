class Node(object):
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None    
    
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

print isbalanced(mytree4.root)