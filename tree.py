
class Tree:

	def __init__(self, values = None):
	# {
		self.root = None
		self.count = 0
		if values: self.insertValues(values)
	# }

	def __iter__(self):
		return InOrderIterator(self)

	def __eq__(self, other):
	# {
		if self.count != other.count : return False
		
		i2 = iter(other.preOrder())
		try:
			for i1 in self.preOrder():
				if i1 != i2.next(): return False
			
			return True
		
		except StopIteration:
			return False
	# }

	def min(self):
	# {
		if self.root is None : return None

		step = self.root
		while step.left: step = step.left
		
		return step.value
	# }

	def max(self):
	# {
		if self.root is None : return None

		step = self.root
		while step.right: step = step.right
		
		return step.value
	# }

	def insert(self, value):
	# {
		if self.root is None:
			self.root = TreeNode(value)
			return

		step = self.root
		lastStep = self.root
		while step:
			if step.value < value:
				step = step.right
			elif step.value > value:
				step = step.left
			else:
				return

			if step:
				lastStep = step

		if lastStep.value < value:
			lastStep.right = TreeNode(value, lastStep)
		else:
			lastStep.left = TreeNode(value, lastStep)

		self.count += 1
	# }

	def insertValues(self, values):
	# {
		for value in values:
			self.insert(value)
	# }

	def inOrder(self, fn = None) :
		return Tree.InOrder(self) if fn is None else self.root.inOrder(fn)

	def preOrder(self, fn = None) :
		return Tree.PreOrder(self) if fn is None else self.root.preOrder(fn)

	
	class Iterator:
		def __init__(self, parent):
			self.parent = parent

	class InOrder(Iterator):
		def __iter__(self):
			return InOrderIterator(self.parent)

	class PreOrder(Iterator):
		def __iter__(self):
			return PreOrderIterator(self.parent)

# / Tree


class TreeNode:

	def __init__(self, value, parent = None):
		self.value = value
		self.parent = parent
		self.left = None
		self.right = None

	def inOrder(self, fn):
		if self.left:
			self.left.inOrder(fn)
		fn(self.value)
		if self.right:
			self.right.inOrder(fn)

	def preOrder(self, fn) :
		fn(self.value)
		if self.left:
			self.left.preOrder(fn)
		if self.right:
			self.right.preOrder(fn)

# / TreeNode	


class InOrderIterator:

	def __init__(self, tree):
	# {
		self.tree = tree
		self.current = self.seekLeft(tree.root)
	# }

	def seekLeft(self, step):
	# {
		while step and step.left: step = step.left

		return step
	# }

	def findNext(self):
	# {
		step = self.current
		if step.right :
			step = self.seekLeft(step.right)
		else :
			while self.current.value >= step.value and step.parent :
				step = step.parent

			if self.current.value >= step.value :
				step = None

		return step
	# }

	def next(self):
	# {
		if self.current is None:
			raise StopIteration()

		value = self.current.value

		# find next
		self.current = self.findNext()
		
		return value
	# }

# / InOrderIterator

class PreOrderIterator:

	def __init__(self, tree):
	# {
		self.tree = tree
		self.current = tree.root
	# }

	def findNextRightChild(self):
	# {
		last = self.current
		while self.current:
			last = self.current
			self.current = self.current.parent
			if self.current is None or not(self.current.right is None or self.current.right == last): break

		if self.current:
			self.current = self.current.right
	# }

	def next(self):
	# {
		if self.current is None:
			raise StopIteration()

		value = self.current.value

		# find next
		if self.current.left:
			self.current = self.current.left
		elif self.current.right:
			self.current = self.current.right
		else:
			self.findNextRightChild()
		
		return value
	# }

# / PreOrderIterator
