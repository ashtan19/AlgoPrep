"""
Leetcode: Amazon OA Power Grid

Attempts: 1
Completed: N and did not get idea
Acheived Ideal:
Under 30 Mins:

Time Complexity: O(n logV)
Space Complexity:

Pattern: Minimum Spanning Tree
Technique: Implement a disjoint set(union find) and use a heap for kruskral's algo 

Problems Encountered: Need to brush up on Prim's and Kruskrals Algorithm
Other Solutions:

"""


class DisjointSet:
    """
    Quick find implementation of Disjoint set data structure
    """

    def __init__(self, vertices):
        # vertices is any iterable (elements need to be hashable)
        self.adj = {v: v for v in vertices}
        print(self.adj)

    def __repr__(self):
        return str(self.adj)

    def connect(self, v1, v2):

        # Get root of a vertex
        def getRoot(v):
            while v != self.adj[v]:
                v = self.adj[v]
            return v

        # We change all root matching root of v1 to root of v2
        r1, r2 = getRoot(v1), getRoot(v2)
        for v in self.adj:
            if self.adj[v] == r1:
                self.adj[v] = r2

    def isConnected(self, v1, v2):
        return self.adj[v1] == self.adj[v2]


def power_grid(num, connection):

    # We implement Kruskal's with sorted array instead of heap
    # Both are equivalent in time complexity
    connection.sort(key=lambda x: x[2])
    result = []

    # Loop over edge list to get vertices
    vertices = set()
    for v1, v2, weight in connection:
        vertices.add(v1)
        vertices.add(v2)

    disjoint_set = DisjointSet(vertices)
    cost = 0
    for v1, v2, weight in connection:
        if not disjoint_set.isConnected(v1, v2):
            cost += weight
            result.append([v1, v2, weight])
            disjoint_set.connect(v1, v2)

    return result


if __name__ == "__main__":
    num = 5
    connection = [
        ["A", "B", 1],
        ["B", "C", 4],
        ["B", "D", 6],
        ["D", "E", 5],
        ["C", "E", 1],
    ]
    print(power_grid(num, connection))
