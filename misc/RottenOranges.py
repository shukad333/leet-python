"""

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.



Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.

"""


import collections
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """


        n , m = len(grid),len(grid[0])
        Q = collections.deque([])
        cnt = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: cnt += 1
                if grid[i][j] == 2: Q.append((i,j))
        resp = 0
        while Q:
            for _ in range(len(Q)):
                i , j = Q.popleft()
                for x ,y in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                    if 0<=x<n and 0<=y<m and grid[x][y]==1:
                        grid[x][y] = 2
                        cnt -= 1
                        Q.append((x,y))
            resp += 1

        return max(0,resp-1) if cnt==0 else -1
