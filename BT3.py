class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def contains(self, target):
        temp = self.root
        
        while temp:
            if target < temp.value:
                temp = temp.left
            elif target > temp.value:
                temp = temp.right
            else:
                return True
        
        return False


bst = BinarySearchTree()
bst.root = Node(10)
bst.root.left = Node(5)
bst.root.right = Node(15)
bst.root.left.right = Node(7)
bst.root.right.left = Node(12)

print(bst.contains(7))  
print(bst.contains(20))  