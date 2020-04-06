class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None

class Solution:
    def invertTree(self, root):
        if root:
            #invert = self.invertTree
            root.left, root.right = self.invertTree(root.right), self.invertTree(
                root.left)
            return root


    def pre(self, root):

        if root:
            print(root.data)
            self.pre(root.left)
            self.pre(root.right)


node = TreeNode(12)
node.left = TreeNode(15)
node.right = TreeNode(25)

sol = Solution()
#sol.pre(node)
sol.invertTree(node)
sol.pre(node)
