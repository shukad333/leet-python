"""

There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room.

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0).

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

"""


class Solution(object):
    def _canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        dfs = [0]
        seen = set(dfs)

        while dfs:
            i = dfs.pop()
            for x in rooms[i]:
                if not x in seen:
                    seen.add(x)
                    dfs.append(x)
                    if len(seen) == len(rooms):
                        return True
        return len(seen) == len(rooms)

    def canVisitAllRooms(self, rooms):

        seen = set()

        #seen.add(0)

        def dfs(roomNo):
            if not roomNo in seen:
                seen.add(roomNo)
                for x in rooms[roomNo]:
                    dfs(x)

        dfs(0)
        return len(seen) == len(rooms)

inp = [[1],[2],[3],[]]
sol = Solution()
print(sol.canVisitAllRooms(inp))



