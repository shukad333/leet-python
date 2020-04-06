"""

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        out = []
        for i in sorted(intervals,key  = lambda a: a[0]):

            if out and i[0]<=out[-1][-1]:
                out[-1][-1] = max(out[-1][-1],i[-1])
            else:
                out += [i]
        return out

sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
