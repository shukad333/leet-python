"""
Print the Diagonal view of a tree
"""


class Solution:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def diagonalUtil(self, map, level, root):

        if root is None:
            return
        try:
            map[level].append(root.data)
        except KeyError:
            map[level] = [root.data]

        self.diagonalUtil(map, level + 1, root.left)
        self.diagonalUtil(map, level, root.right)

    def print(self, root):

        map = dict()
        self.diagonalUtil(map, 0, root)

        print("Printing diagonal view")

        for i in map:
            for j in map[i]:
                print(j)
            print("------")


sol = Solution(12)
sol.left = Solution(5)
sol.right = Solution(20)
sol.left.right = Solution(7)

sol.print(sol)