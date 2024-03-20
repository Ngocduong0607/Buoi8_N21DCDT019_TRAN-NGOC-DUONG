class TreeNode:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children if children is not None else []

    def __str__(self, level=0):
        ret = "  " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self, data):
        new_child = TreeNode(data)
        self.children.append(new_child)

tree = TreeNode('Drinks')
cold = TreeNode('Cold')
hot = TreeNode('Hot')
tree.addChild(cold)
tree.addChild(hot)
print(tree)
