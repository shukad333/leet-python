class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def LCA(root,n1,n2):
    if root is None:
        return root
    if root.data<n1 and root.data<n2:
        return LCA(root.left,n1,n2)
    if root.data>n1 and root.data>n2:
        return LCA(root.right,n1,n2)
    return root

node = Node(100)
node.left = Node(50)
node.right = Node(200)
node.left.left = Node(25)
node.left.right = Node(75)

print(LCA(node,50,200).data)