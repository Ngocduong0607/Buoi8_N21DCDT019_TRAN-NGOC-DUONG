class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.leftChild is None:
                    self.leftChild = BSTNode(data)
                else:
                    self.leftChild.insert(data)
            elif data > self.data:
                if self.rightChild is None:
                    self.rightChild = BSTNode(data)
                else:
                    self.rightChild.insert(data)
        else:
            self.data = data

    def inorder_traversal(self):
        result = []
        if self.leftChild:
            result.extend(self.leftChild.inorder_traversal())
        result.append(self.data)
        if self.rightChild:
            result.extend(self.rightChild.inorder_traversal())
        return result


newBST = BSTNode(None) 
newBST.insert(5)        
newBST.insert(3)
newBST.insert(7)

print(newBST.inorder_traversal())
