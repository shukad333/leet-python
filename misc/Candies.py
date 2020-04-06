"""

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.

"""

class Solution:
    def candy(self, ratings):
        resp=[1]*len(ratings)
        n=len(ratings)
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                resp[i] = resp[i-1]+1

        for i in range(n-1,0,-1):
            if ratings[i-1]>ratings[i]:
                resp[i-1] = max(resp[i-1],resp[i]+1)

        r=0
        for i in range(0,n):
            r+=resp[i]

        return r


sol = Solution()
rat = [1,0,2]
print(sol.candy(rat))
