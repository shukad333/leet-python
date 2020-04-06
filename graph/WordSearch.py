"""

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


"""

class Solution:

    def exist(self, board, word):
        if not board:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board,word,i,j):
                    return True

        return False


    def dfs(self,board,word,i,j):

        if(len(word)==0):
            return True

        if i>=len(board) or i<0 or j>=len(board[0]) or j<0 or word[0]!=board[
            i][j]:
            return False

        temp = board[i][j]

        board[i][j] = "#"

        resp =  self.dfs(board,word[1:],i-1,j) or self.dfs(board,word[1:],i+1,
                                                      j) or self.dfs(board,
                                                                     word[
                                                                     1:],i,
                                                                     j-1) or \
                self.dfs(board,word[1:],i,j+1)

        board[i][j] = temp

        return resp



sol = Solution()
print(sol.exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']],
      "ABCCED"))