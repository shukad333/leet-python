"""

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.

"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        while i < len(nums):
            if nums[i] == i + 1 or nums[i] < 0 or nums[i] > len(nums):
                i += 1
            elif nums[i] > 0 and nums[nums[i] - 1] != nums[i]:
                self.swap(nums, i, nums[i] - 1)
            else:
                i += 1

        i = 0

        while i < len(nums) and nums[i] == i + 1:
            i += 1

        return i + 1

    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]


sol = Solution()
print(sol.firstMissingPositive([3, 4, -1, 1]))
