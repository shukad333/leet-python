"""

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Accepted
172,076
Submissions
386,406

"""

from itertools import combinations

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        #return list(combinations(range(1,n+1),k))

        if k==0:
            return [[]]
        return [pre + [i] for i in range(k,n+1) for pre in self.combine(
            i-1,k-1)]


sol = Solution()
print(sol.combine(5,2))