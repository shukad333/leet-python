"""

In a 1 million by 1 million grid, the coordinates of each grid square are (x, y) with 0 <= x, y < 10^6.

We start at the source square and want to reach the target square.  Each move, we can walk to a 4-directionally adjacent square in the grid that isn't in the given list of blocked squares.

Return true if and only if it is possible to reach the target square through a sequence of moves.



Example 1:

Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
Output: false
Explanation:
The target square is inaccessible starting from the source square, because we can't walk outside the grid.
Example 2:

Input: blocked = [], source = [0,0], target = [999999,999999]
Output: true
Explanation:
Because there are no blocked cells, it's possible to reach the target square.


Note:

0 <= blocked.length <= 200
blocked[i].length == 2
0 <= blocked[i][j] < 10^6
source.length == target.length == 2
0 <= source[i][j], target[i][j] < 10^6
source != target


"""
import collections
class Solution:
    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """

        if not blocked: return True
        blocked = set(map(tuple,blocked))


        def check(blocked,source,targer):
            si,sj=source
            ti,tj = target

            level = 0

            q = collections.deque([(si,sj)])
            vis = set()

            while q:
                for _ in range(len(q)):
                    i,j = q.popleft()
                    if i==ti and j==tj:
                        return True
                    for x,y in ((i+1,j),(i,j+1),(i-1,j),(i,j-1)):
                        if 0<=x<=10**6 and 0<=y<=10**6 and (x,y) not in vis \
                                and (x,y) not in blocked:
                            vis.add((x,y))
                            q.append((x,y))
                level += 1
                if level == len(blocked):
                    break
                else:
                    return False

                return True

        return check(blocked,source,target) and check(blocked,target,source)
