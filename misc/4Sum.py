"""

Given an array nums of n integers and an integer target, are there elements
a, b, c, and d in nums such that a + b + c + d = target? Find all unique
quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:
a
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""


class Solution:
    def theeSum(self, nums, target):

        results = []
        nums.sort()
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            t = target - nums[i]
            if i == 0 or nums[i] != nums[i - 1]:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == t:
                        results.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]: l += 1
                        while r > l and nums[r] == nums[r - 1]: r -= 1
                        l += 1;
                        r -= 1
                    elif s < t:
                        l += 1
                    else:
                        r -= 1
        return results

    def fourSum(self, nums, target):
        results = []
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i - 1]:
                threeRes = self.theeSum(nums[i + 1:], target - nums[i])
                for item in threeRes:
                    results.append(item+[nums[i]])
        return results


sol = Solution()
print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))
