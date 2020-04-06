"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

"""

class Solution:

    def postorderTraversal(self,root):

        resp , stack = [],[(root,False)]

        while stack:

            node,visited = stack.pop()
            if node:

                if visited:
                    resp.append(node.val)

                else:
                    stack.append((node,True))
                    stack.append((node.left, False))
                    stack.append((node.right, False))
        return resp


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

sol = Solution()
print(sol.postorderTraversal(root))
