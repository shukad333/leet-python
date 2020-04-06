"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
Accepted
309,351
Submissions
597,911
"""

import itertools
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(itertools.permutations(nums))

        return [[n] + p
                for i,n in enumerate(nums)
                for p in self.permute(nums[:i]+nums[i+1:])] or [[]]

print(list(itertools.combinations([1,2,3,4],2)))

