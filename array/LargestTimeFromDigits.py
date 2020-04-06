"""

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.



Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""


Note:

A.length == 4
0 <= A[i] <= 9

"""

import itertools

class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """

        h=m=-float("inf")

        for a,b,c,d in itertools.permutations(A):
            hh,mm = a*10+b,c*10+d

            if 0 <= hh <= 23 and 0 <= mm <= 59 and (hh>h or hh==h and mm>m):
                h,m = hh,mm
        sh = str(h) if h > 9 else "0" + str(h)
        sm = str(m) if m > 9 else "0" + str(m)

        return 0 <= h <= 23 and 0 <= m <= 59 and sh + ":" + sm or ""

sol = Solution()
print(sol.largestTimeFromDigits([1,2,3,4]))
