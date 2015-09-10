from tree import Tree
import random

tree = Tree(random.sample(range(100), 100))

storage = []

# tree.inOrder(lambda x: storage.append(x))

# print "in-order works" if tree == Tree(storage) else "in-order fails"

# storage = []

# tree.preOrder(lambda x: storage.append(x))

# print "pre-order works" if tree == Tree(storage) else "pre-order fails"

# print tree.min(),' - ', tree.max()


# # for i in tree.preOrder():
# # 	print i

# f = open("test.tree", "w")

# tree.preOrder(lambda x: f.write(str(x)+' '))
# f.close()

# try:
# 	f = open("test.tree", "r")
# 	contents = f.read().strip()

# 	if contents : contents = map(lambda x: int(x), contents.split(' '))

# 	tree2 = Tree(contents)
# 	print "pre-order works" if tree == tree2 else "pre-order fails"

# except IOError:
# 	pass

for i in tree.root.inOrderGenerator():
	print(i)