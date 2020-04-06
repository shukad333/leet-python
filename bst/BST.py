class TreeNode:
    def __init__(self,data):
        self.data = data;
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def push(self,data):
        self.root = self.pushRec(self.root,data)

    def pushRec(self,node,key):
        if node==None:
            node = TreeNode(key)
            return node
        if key<node.data:
            node.left = self.pushRec(node.left,key)
        else:
            node.right = self.pushRec(node.right,key)
        return node

    def preOrder(self,node):
        if node==None:
            return
        print(node.data)
        self.preOrder(node.left)
        self.preOrder(node.right)
b = BST()
b.push(10)
b.push(100)
b.push(1)
b.push(1000)
b.push(200)
b.preOrder(b.root)