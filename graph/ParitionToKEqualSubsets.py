"""
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.



Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.


Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if len(nums)<k:
            return False
        numSum = sum(nums)
        nums.sort(reverse=True)
        if numSum%k!=0:
            return False

        target = [numSum/k] * k

        def dfs(pos):
            if pos == len(nums):
                return True

            for i in range(k):
                if target[i] >= nums[pos]:
                    target[i]-=nums[pos]
                    if dfs(pos+1):
                        return True
                    target[i]+=nums[pos]
            return False

        return dfs(0)

sol = Solution()
print(sol.canPartitionKSubsets([4,3,2,3,5,2,1],4))



