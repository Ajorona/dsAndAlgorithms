import BinarySearchTree
from time import sleep

nodes = [7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14]

print("\n")
sleep(.5)
print("Testing the BinarySearchTree class\n")
sleep(.5)

BST = BinarySearchTree.BinarySearchTree()
for node in nodes:
  BST.insert(node)
  
for node in nodes:
  print("We have found node number: {}".format(BST.find(node).element))

print("\n")
print("The min element is: {}".format(BST.findMin(BST.root).element))
print("The max element is: {}\n".format(BST.findMax(BST.root).element))
print("")

print("In order traversal: {}".format(BST.traversal(BST.INORDER)))
print("Pre order traversal: {}".format(BST.traversal(BST.PREORDER)))
print("Post order traversal: {}".format(BST.traversal(BST.POSTORDER)))

print("\n\n")
for node in nodes:
	print("Lazy delete node number: {}".format(node))
	BST.lazyDelete(node)

print("\n\n")
sleep(.5)

for node in nodes:
	if BST.find(node) == None:
		print("Node number: {} is not visible".format(node))

print("\n\n")
for node in nodes:
  print("Inserting node number {}".format(node))
  BST.insert(node)

print("\n\n")
for node in nodes:
	if BST.find(node) != None:
		print("Node number {} has been reinserted".format(node))


print("\n\n")
for node in nodes:
	print("Attempting to hard delete node number: {}".format(node))
	BST.remove(node)

print("\n\n")
for node in nodes:
	if BST.find(node) is None:
		print("Node number {} has been deleted".format(node))

print("\n\n")
print("Testing of Basic BST complete")