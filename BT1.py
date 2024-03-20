class Node:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right= None
        
class BinarySearchTree:
    def __init__(self):
        self.root= None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        while current:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                else:
                    current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    return
                else:
                    current = current.right
            else:
                
                return

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.value)
            self.inorder_traversal(node.right)


bst = BinarySearchTree()


bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(7)
bst.insert(12)
bst.insert(20)


print("Contents of the binary search tree:")
bst.inorder_traversal(bst.root)
