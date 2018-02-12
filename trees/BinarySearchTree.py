

class BinarySearchTree():
    PREORDER = 0
    POSTORDER = 1
    INORDER = 2

    def __init__(self):
        self.root = self.TreeNode.makeLeaf(None, None)
        self.size = 0


    class TreeNode():
        def __init__(self, leftChild, rightChild, parent, element):
            self.deleted = False;
            self.element = element;
            self.parent = parent;
            self.leftChild = leftChild;
            self.rightChild = rightChild;
    
        @classmethod
        def makeLeaf(cls, parent, element):
            return cls(None, None, parent, element)
  
  
    def find(self, key):
        root = self.root
        while root is not None:
            if key < root.element:
                root = root.leftChild
            elif key > root.element:
                root = root.rightChild
            else:
                if root.deleted:
                    return None
                else:
                    return root
        return None

  
    def findMin(self, root):
        while root.leftChild is not None:
            root = root.leftChild
        while root.deleted == True:
            root = root.parent
        return root


    def findMax(self, root):
        while root.rightChild is not None:
            root = root.rightChild
        while root.deleted == True:
            root = root.parent
        return root


    def insert(self, element):
        if self.size == 0:
            self.root.element = element
            self.size += 1
            return

        # Iteratively walk tree
        node = self.root
        while True:
            # check if node has been deleted previously
            if element == node.element:
                node.deleted = False
                return

            if element < node.element:
                if node.leftChild is None:
                    node.leftChild = self.TreeNode.makeLeaf(node, element)
                    self.size += 1
                    return
                else:
                    node = node.leftChild

            else:
                if node.rightChild is None:
                    node.rightChild = self.TreeNode.makeLeaf(node, element)
                    self.size += 1
                    return
                else:
                    node = node.rightChild


    def lazyDelete(self, element):
        node = self.find(element)
        if node != 'None':
            node.deleted = True
        else:
            pass


    def remove(self, element):
        return self._remove(self.root, element)

    def _remove(self, root, element):
        # Base / Escape Case
        if root is None:
            return root

        if element < root.element:
            root.leftChild = self._remove(root.leftChild, element)
        elif root.element > element:
            root.rightChild = self._remove(root.rightChild, element)
        else:
            if root.leftChild is None:
                newRoot = root.rightChild
                root = None
                return newRoot

            elif root.rightChild is None:
                newRoot = root.leftChild
                root = None
                return newRoot

        min = self.findMin(root.rightChild)
        root.element = min.element
        self._remove(root.rightChild, min.element)
        return root


    def _inOrderTraversal(self, nodes, root):
        if root.leftChild is not None:
            self._inOrderTraversal(nodes, root.leftChild)
        if root is not None:
            nodes.append(root.element)
        if root.rightChild is not None:
            self._inOrderTraversal(nodes, root.rightChild)
        return nodes


    def _preOrderTraversal(self, nodes, root):
        if root is not None:
            nodes.append(root.element)
        if root.leftChild is not None:
            self._preOrderTraversal(nodes, root.leftChild)
        if root.rightChild is not None:
            self._preOrderTraversal(nodes, root.rightChild)
        return nodes


    def _postOrderTraversal(self, nodes, root):
        if root.leftChild is not None:
            self._postOrderTraversal(nodes, root.leftChild)
        if root.rightChild is not None:
            self._postOrderTraversal(nodes, root.rightChild)
        if root.element is not None:
            nodes.append(root.element)
        return nodes


    def traversal(self, option):
        nodes = []
        if option == self.PREORDER:
            return self._preOrderTraversal(nodes, self.root)
        if option == self.POSTORDER:
            return self._postOrderTraversal(nodes, self.root)
        if option == self.INORDER:
            return self._inOrderTraversal(nodes, self.root)

