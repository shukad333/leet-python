"""

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.



Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False


Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].


"""


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        A = [ord(x)-ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]

        window = target = [0] * 26

        for x in A:
            target[x] += 1

        for index,num in enumerate(B):
            window[num] += 1

            if index >= len(A):
                window[B[index-len(A)]] -= 1

            if window == target:
                return True

        return False

