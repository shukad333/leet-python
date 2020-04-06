"""

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

"""


class Solution(object):
    def rightSideView(self, root):

        resp = []

        def rightView(root,depth):
            if not root:
                return
            if depth == len(resp):
                resp.append(root.val)
            rightView(root,depth+1)
            rightView(root,depth+1)

        rightView(root,0)
        return resp
