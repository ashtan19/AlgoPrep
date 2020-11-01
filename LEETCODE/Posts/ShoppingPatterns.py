"""
Leetcode: Amazon OA 2020 Shopping Patterns

Attempts:1
Completed: N
Acheived Ideal:
Under 30 Mins: 

Time Complexity: O(V*E)
Space Complexity:

Pattern: 
Technique: 

Problems Encountered:
Other Solutions:

"""


import unittest
import collections
from collections import defaultdict
from typing import List
import math


class Graph(object):
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.edges = defaultdict(set)
        self.degrees = defaultdict(int)

    def addEdge(self, u: int, v: int) -> None:
        self.edges[u].add(v)
        self.edges[v].add(u)

        self.degrees[u] += 1
        self.degrees[v] += 1

    def getDegree(self, u: int) -> int:
        return self.degrees[u]


class Solution:
    def getMinScore(self, products_nodes: int, products_edges: int, products_from: List[int], products_to: List[int]) -> int:
        # Base case
        if products_nodes == 0:
            return 0

        # Construct graph
        graph = Graph(products_nodes)
        for i, u in enumerate(products_from):
            v = products_to[i]
            graph.addEdge(u, v)

        minScore = math.inf

        def standardize(u: int, v: int, w: int) -> str:
            return ':'.join([str(x) for x in sorted([u, v, w])])

        # Find trios and get min score.
        visited = set()
        # For every edge, (u,v) find another node w such that (u,w)
        # and (v,w) edges exist; then (u,v,w) is a trio.
        for u, u_edges in graph.edges.items():
            for v in u_edges:
                for w, w_edges in graph.edges.items():
                    if w == u or w == v or standardize(u, v, w) in visited:
                        continue
                    if u in w_edges and v in w_edges:
                        minScore = min(minScore, sum(
                            [graph.getDegree(x) for x in [u, v, w]]) - 6)
                        visited.add(standardize(u, v, w))
        return -1 if minScore == math.inf else minScore


# Another Solution that is easier to understand


class Solution:
    def getMinScore(self, products_nodes, products_edges, products_from, products_to):
        # Create edge list
        edges = set()
        vertices = set(range(1, products_nodes + 1))
        for f, t in zip(products_from, products_to):
            edges.add((f, t))
            edges.add((t, f))

        # Create adjacency list
        adj = collections.defaultdict(set)
        for e in edges:
            adj[e[0]].add(e[1])
            adj[e[1]].add(e[0])

        # Keep a set of trios
        # For each edge in (products_from, products_to): loop over all vertices and check for trios not seen before (use the set of trios)
        # Once a trio is identified: record it in the set,
        # then construct a sub-adjacency list of trio vertices (keys) and remove trio vertices (from values) to get outside products.
        # Finally, record the number of outside products and keep track of its minimum
        # Time complexity O(|V|x|E|) - first loop over edges and second loop over vertices
        trios = set()
        mincounter = math.inf
        for f, t in zip(products_from, products_to):
            for v in vertices - {f, t}:
                if (
                    (v, f) in edges
                    and (v, t) in edges
                    and ":".join(sorted([str(v), str(f), str(t)], key=int))
                    not in trios  # last one checks if we have already seen this trio
                ):
                    trios.add(
                        ":".join(sorted([str(v), str(f), str(t)], key=int)))
                    trio = {v, f, t}
                    # make a sub-adjacency list for elements only in a given trio
                    subadj = {vs: adj[vs] for vs in trio}
                    subadj[v] = subadj[v] - {f, t}
                    subadj[f] = subadj[f] - {v, t}
                    subadj[t] = subadj[t] - {f, v}
                    # print(":".join( sorted([str(v),str(f),str(t)], key = int) ), subadj)
                    mincounter = min(mincounter, sum(
                        len(subadj[v]) for v in trio))
        return mincounter if mincounter != math.inf else -1


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test1(self):
        products_nodes = 5
        products_edges = 6
        products_from = [1, 1, 2, 2, 3, 4]
        products_to = [2, 3, 3, 4, 4, 5]
        self.assertEqual(
            self.solution.getMinScore(
                products_nodes, products_edges, products_from, products_to
            ),
            2,
        )

    def test2(self):
        products_nodes = 6
        products_edges = 6
        products_from = [1, 2, 2, 3, 4, 5]
        products_to = [2, 4, 5, 5, 5, 6]

        self.assertEqual(
            self.solution.getMinScore(
                products_nodes, products_edges, products_from, products_to
            ),
            3,
        )


if __name__ == "__main__":
    unittest.main()
