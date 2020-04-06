"""

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        start=0
        longest=0
        used_chars = {}
        for i in range(len(s)):

            if s[i] in used_chars and start<=used_chars[s[i]]:
                start = used_chars[s[i]]+1
            else:
                longest = max(longest,i-start+1)

            used_chars[s[i]] = i
        return longest


s = Solution()
s.lengthOfLongestSubstring("shu")
