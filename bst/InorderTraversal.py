"""
Inorder Tree Traversal

"""


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        resp = []
        self.helper(root,resp)
        return resp

    def helper(self,root,resp):
        if not root:
            return
        self.helper(root.left,resp)
        resp.append(root.val)
        self.helper(root.right, resp)

    def iterative(self,root):
        stack,resp=[],[]
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return resp
            node = stack.pop()
            resp.append(node.val)
            root.node.right

        return resp