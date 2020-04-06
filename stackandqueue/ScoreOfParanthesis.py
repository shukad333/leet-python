"""

Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6


Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50


"""


class Solution:


    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """

        global MY_CONS
        print(MY_CONS)
        stack=[]

        for i in S:
            if i=='(':
                stack.append(-1)

            else:
                local=0
                while stack and stack[-1]!=-1:
                    local+=stack.pop()
                stack.pop()
                if local==0:
                    stack.append(1)
                else:
                    stack.append(2*local)

        resp=0
        #print(stack)
        for x in stack:
            resp+=x
        return resp

MY_CONS="shuahil"
sol = Solution()
print(sol.scoreOfParentheses("(()(()))"))