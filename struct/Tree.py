
import random

listBool = []
sizeVar = 7

class Tree:
	def __init__(self,value,operator):
		self.value = value
		self.operator = operator
		self.sons = []
		self.father = None

	def addSon(self, son):
		self.sons.append(son)
		son.father = self


	#if not defined then value will be returned as false since not of bool is false.
	def returnValue(self):
		if not self.sons:
			if self.value[1] == 1:
				return listBool[self.value[0]-1]
			else:
				return not listBool[self.value[0]-1]
		else:
			return self.value


	def printTree(self):
		print("Value : %s , operator: %s " %(Tree.returnValue(self),self.operator))
		for son in self.sons:
			Tree.printTree(son)

	def solveTree(self):
		if not self.sons:
			return Tree.returnValue(self)
		else:
			Tree.solveTree(self.sons[0])
			result = Tree.returnValue(self.sons[0])
			for son in self.sons[1:]:
				if self.operator == "^":
					result = Tree.solveTree(son) and result
				else:
					result = Tree.solveTree(son) or result
			self.value = result
			return result

	def updateValues(self):
		if not self.father:
			return self.value
		else:
			result = Tree.returnValue(self.father.sons[0].value)
			for son in self.father.sons[1:]:
				if self.father.operator == "^":
					result =  Tree.returnValue(son) and result
				else:
					result =  Tree.returnValue(son)  or result
				self.father.value = result
			return Tree.updateValues(self.father)


	def toDot(self):
		if not self.sons:
			return ("" + str(self) + "[label=\"%s , %s\"]; \n" %(Tree.returnValue(self),self.value[0]))
		else:
			dotStr = ""
			dotStr += str(self)+"[label=\"(%s,%s)\"]; \n" %(self.operator,self.value)
			for son in self.sons:
				dotStr += str(self) + " -> " + str(son) + " ; \n"
				dotStr += Tree.toDot(son)
		return dotStr

#to be moved in a different file maybe ?? .
def generateLeaf():
	k = random.randint(0,len(listBool))
	if random.random() >= 0.5 :
		x = 1
	else:
		x = 0
	return Tree((k,x),"")

def generateNode():
	if random.random() >= 0.5 :
		return Tree(False,"^")
	else:
		return Tree(False,"v")

def fillList(size):
	i = 0
	length = 2**(size)
	while(i < length):
		listBool.append(bool)
		i = i + 1



def generateBinaryTree( size ):
	# generating list of possible values for the leafs, size of 2^$size * 2 for negitive and positive.
	# generate the tree with a height of $size where the first level is considered 1
	# Nodes have 1:1 chance of having an operater of AND , OR
	# Afterwards fill each leaf with a boolean randomly picked from the list.
	fillList(size)  
	i = 0
	pere = generateNode()
	currentGen = []
	currentGen.append(pere)
	while(i < size):
		j = 0
		length = len(currentGen)
		while(j < length):
			tmp = currentGen.pop(0)
			if i == size - 1:		# we have a leaf therefore needs to contain a value from the list.
				Tree.addSon(tmp,generateLeaf())
				Tree.addSon(tmp,generateLeaf())
			else:
				son1 = generateNode()
				Tree.addSon(tmp,son1)
				currentGen.append(son1)
				son2 = generateNode()
				Tree.addSon(tmp,son2)
				currentGen.append(son2)
			j = j + 1
		i = i + 1
	return pere
	 			


# x =  False
# y = not(x)

# tr2 = Tree(True,"")
# tr3 = Tree(False,"")
# Tree.addSon(tr,tr2)
# Tree.addSon(tr,tr3)
# print("========")
# Tree.solveTree(tr)
# Tree.printTree(tr)
# tr3.value = True
# Tree.updateValues(tr3)
# Tree.printTree(tr)




# generateBinaryTree(2)
# print(listBool)

# tr = Tree(False,"and")
# tr2 = Tree((0,0),"")
# tr3 = Tree((0,0),"")
# Tree.addSon(tr,tr2)
# Tree.addSon(tr,tr3)
# print("=========")
# Tree.printTree(tr)
# print("=========")
# listBool[0] = False
# #listBool[1] = False
# Tree.printTree(tr)

# print("=========")

# Tree.solveTree(tr)

tr = generateBinaryTree(sizeVar)


i = 0 
while i < 2**(sizeVar):
	if random.random() >= 0.5:
		listBool[i] = True
	else:
		listBool[i] = False
	i = i + 1

print(Tree.toDot(tr))
Tree.solveTree(tr)
print("============")

print(Tree.toDot(tr))

# listBool[0]=True
# Tree.printTree(tr)

