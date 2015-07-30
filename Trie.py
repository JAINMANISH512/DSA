ALPHA=26
class node(object):
	def __init__(self):
		self.val=0
		self.children=[]
		for i in range(ALPHA):
			self.children.append(None)
	def __str__(self):
		return str(self.val)
class trie(object):
	def __init__(self):
		self.root=node()
		self.count=0

def insert(mytrie,key):
	length=len(key)
	crawl=mytrie.root
	mytrie.count+=1
	for level in range(length):
		index=ord(key[level])-ord('a')
		if not crawl.children[index]:
			crawl.children[index]=node()
		crawl=crawl.children[index]
	crawl.val=mytrie.count

def search(mytrie,key):
	length=len(key)
	crawl=mytrie.root
	for level in range(length):
		index=ord(key[level])-ord('a')
		if not crawl.children[index]:
			return False
		crawl=crawl.children[index]
	crawl.val=mytrie.count
	if crawl and crawl.val:
		return True
	return False

def leafnode(pnode):
	return not (pnode.val==0)

def isfreenode(pnode):
	for i in range(ALPHA):
		if pnode.children[i]:
			return 0
	return 1

def delhelp(pnode,key,level,length):
	if pnode:
		if level==length:
			if pnode.val:
				pnode.val=0
				if isfreenode(pnode):
					return True
				return False
		else:
			index=ord(key[level])-ord('a')
			if delhelp(pnode.children[index],key,level+1,length):
				del pnode.children[index]
				pnode.children[index]=None
				return not leafnode(pnode) and isfreenode(pnode)
	return False


mytrie=trie()
insert(mytrie,"the")
insert(mytrie,"a")
insert(mytrie,"there")
insert(mytrie,"answer")
insert(mytrie,"any")
insert(mytrie,"by")
insert(mytrie,"bye")
insert(mytrie,"their")
print search(mytrie,"the")
delhelp(mytrie.root,"their",0,len("their"))
print search(mytrie,"these")
print search(mytrie,"their")
print search(mytrie,"thaw")


