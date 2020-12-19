"""
Leetcode: 947. Most Stones Removed with Same Row or Column

Attempts: 1
Completed: N
Acheived Ideal: N
Under 30 Mins: N

Time Complexity: O(N^2)
Space Complexity: O(n)

Pattern: Graph Question
Technique: FOr this question, you need to realize that the solution is len(stones) - number islands
            Where an island is a group of stones that are connected. There will be one left over stone
            in every island so the number of stones that you can remove is ( len(stones) - number islands)

            You can use DFS to find the Islands or Union find to find the islands 

Problems Encountered:
Other Solutions:

"""


class Solution:
    def removeStones(self, stones):
        def dfs(i, j):
            points.discard((i, j))
            for y in rows[i]:
                if (i, y) in points:
                    dfs(i, y)
            for x in cols[j]:
                if (x, j) in points:
                    dfs(x, j)
        points, island, rows, cols = {(i, j) for i, j in stones}, 0, collections.defaultdict(
            list), collections.defaultdict(list)
        for i, j in stones:
            rows[i].append(j)
            cols[j].append(i)
        for i, j in stones:
            if (i, j) in points:
                dfs(i, j)
                island += 1
        return len(stones) - island

    def removeStones(self, points):
        UF = {}

        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]

        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)

        for i, j in points:
            union(i, ~j)
        return len(points) - len({find(x) for x in UF})
