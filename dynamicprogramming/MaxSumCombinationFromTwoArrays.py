"""
 Given two arrays arr1[] and arr2[] each of size N. The task is to choose some elements from both the arrays such that no two elements have the same index and no two consecutive numbers can be selected from a single array. Find the maximum sum possible of above-chosen numbers.

Examples:

Input : arr1[] = {9, 3, 5, 7, 3}, arr2[] = {5, 8, 1, 4, 5}
Output : 29
Select first, third and fivth element from the first array.
Select the second and fourth element from the second array.

Input : arr1[] = {1, 2, 9}, arr2[] = {10, 1, 1}
Output : 19
Select last element from the first array and first element from the second array.
"""


class Solution:
    def maxSum(self,arr1,arr2):

        n = len(arr1)
        dp = [[0]*2 for i in range(n)]

        for i in range(0,n):

            if i==0:
                dp[i][0] = arr1[i]
                dp[i][1] = arr2[i]
                continue

            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+arr1[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]+arr2[i])

        return max(dp[n-1][0],dp[n-1][1])

sol = Solution()
print(sol.maxSum([9, 3, 5, 7, 3],[5, 8, 1, 4, 5]))
