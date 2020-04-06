"""

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3


"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs(grid,x,y):
            if x>=0 and x<len(grid) and y>=0 and y<len(grid[0]) and grid[x][
                y]!='0':

                grid[x][y] = '0'

                for i,j in [[0,1],[0,-1],[1,0],[-1,0]]:
                    dfs(grid,x+i,y+j)

        resp = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    dfs(grid,i,j)
                    resp += 1
        return resp

sol = Solution()
print(sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1",
                                                                   "0","0","0"],["0","0","0","0","1"]]))