"""

Given an array nums of positive integers, return the longest possible length of an array prefix of nums, such that it is possible to remove exactly one element from this prefix so that every number that has appeared in it will have the same number of occurrences.

If after removing one element there are no remaining elements, it's still considered that every appeared number has the same number of ocurrences (0).



Example 1:

Input: nums = [2,2,1,1,5,3,3,5]
Output: 7
Explanation: For the subarray [2,2,1,1,5,3,3] of length 7, if we remove nums[4]=5, we will get [2,2,1,1,3,3], so that each number will appear exactly twice.
Example 2:

Input: nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
Output: 13
Example 3:

Input: nums = [1,1,1,2,2,2]
Output: 5
Example 4:

Input: nums = [10,2,8,9,3,8,1,5,2,3,7,6]
Output: 8


"""

import collections

class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt,freq,maxF,res = collections.defaultdict(int),\
                             collections.defaultdict(int),0,0

        for i,num in enumerate(nums):
            cnt[num]+=1
            freq[cnt[num]-1] -= 1
            freq[cnt[num]] += 1
            maxF = max(maxF,cnt[num])
            if maxF * freq[maxF] == i or (maxF - 1) * (
                freq[maxF - 1] + 1) == i or maxF == 1:
                res = i + 1
        return res

sol = Solution()
print(sol.maxEqualFreq([2,2,1,1,5,3,3,5]))