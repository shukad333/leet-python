"""
There are n computers numbered from 0 to n-1 connected by ethernet cables
connections forming a network where connections[i] = [a, b] represents a
connection between computers a and b. Any computer can reach any other
computer directly or indirectly through the network.

Given an initial computer network connections. You can extract certain cables
between two directly connected computers, and place them between any pair of
disconnected computers to make them directly connected. Return the minimum
number of times you need to do this in order to make all the computers
connected. If it's not possible, return -1.
"""

class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        if len(connections)<n-1: return -1
        G = [set() for i in range(n)]
        for i , j in connections:
            G[i].add(j)
            G[j].add(i)

        seen = [0] * n
        def dfs(i):
            if seen[i]: return 0
            seen[i] = 1
            for j in G[i]: dfs(j)
            return 1

        return sum(dfs(i) for i in range(n)) - 1
