"""

On an 8x8 chessboard, there can be multiple Black Queens and one White King.

Given an array of integer coordinates queens that represents the positions of
the Black Queens, and a pair of coordinates king that represent the position
of the White King, return the coordinates of all the queens (in any order)
that can attack the King.


Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
Output: [[0,1],[1,0],[3,3]]
Explanation:
The queen at [0,1] can attack the king cause they're in the same row.
The queen at [1,0] can attack the king cause they're in the same column.
The queen at [3,3] can attack the king cause they're in the same diagnal.
The queen at [0,4] can't attack the king cause it's blocked by the queen at [0,1].
The queen at [4,0] can't attack the king cause it's blocked by the queen at [1,0].
The queen at [2,4] can't attack the king cause it's not in the same row/column/diagnal as the king.


"""


class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """

        queens = {(x,y) for x,y in queens}
        resp = []
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                for k in range(1,8):
                    x,y = king[0] +i *k , king[1]+j*k
                    if (x,y) in queens:
                        resp.append([x,y])
                        break
        return resp

queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
king = [0,0]

sol = Solution()
print(sol.queensAttacktheKing(queens,king))

