"""

Given a set of non-overlapping intervals, insert a new interval into the
intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their
start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to
default code definition to get new method signature.

"""


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        resp, i, n = [], 0, len(intervals)
        while i < n and intervals[i][-1] < newInterval[0]:
            resp += [intervals[i]]
            i += 1

        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0], newInterval[1] = min(intervals[i][0], newInterval[
                0]), max(intervals[i][1], newInterval[1])
            i += 1
        resp += [newInterval]

        while i < n:
            resp += [intervals[i]]
            i += 1

        return resp

    def _insert(self, intervals, newInterval):

        s, e = newInterval[0], newInterval[1]
        left = [i for i in intervals if i[1] < s]
        right = [i for i in intervals if i[0] > e]

        if left + right != intervals:
            s = min(s, intervals[len(left)][0])
            e = max(e, intervals[len(intervals) - len(right) - 1][1])

        return left + [[s, e]] + right


sol = Solution()
print(sol._insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
