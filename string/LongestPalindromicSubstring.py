"""

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        resp = ""
        for i in range(len(s)):
            tmp = self.extend(i,i,s)
            if len(tmp) > len(resp):
                resp = tmp
            tmp = self.extend(i,i+1,s)
            if len(tmp) > len(resp):
                resp = tmp
        return resp

    def extend(self,start,end,s):
        while start>=0 and end<len(s) and s[start] == s[end]:
            start-=1
            end+=1
        return s[start+1:end]



sol = Solution()
print(sol.longestPalindrome("cbbd"))