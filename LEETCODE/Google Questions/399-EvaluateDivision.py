"""
Leetcode: 399. Evaluate Division

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: N

Time Complexity: O(m * n)
Space Complexity: O(n^2)

Pattern: Graph Question. Finding if nodes are connected
Technique: Use hashtable to store adjacency and edges

Problems Encountered:
Other Solutions: Use DFS to find if nodes are connected 

"""


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        from collections import defaultdict, deque
        e = len(equations)
        graph = defaultdict(set)
        edges = {}
        result = []

        # Create graph and edge hashtable
        for i in range(e):
            a, b = equations[i]
            value = values[i]
            graph[a].add(b)
            graph[b].add(a)
            edges[(a, b)] = value
            edges[(b, a)] = 1 / value

        def search_value(query, graph, edges):
            n = len(graph)  # number of nodes

            x, y = query
            if x not in graph or y not in graph:
                return -1.0
            if x == y:
                return 1.0
            if (x, y) in edges:
                return edges[(x, y)]

            visited = set()
            queue = deque()
            cur_value = 1
            queue.append((x, cur_value))

            while queue and len(visited) < n:
                node, cur_value = deque.popleft(queue)
                if node in visited:
                    continue
                if node == y:
                    edges[(x, y)] = cur_value
                    edges[(y, x)] = 1/cur_value
                    graph[x].add(y)
                    graph[y].add(x)
                    return cur_value
                visited.add(node)
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        neighbour_value = edges[(node, neighbour)] * cur_value
                        edges[(x, neighbour)] = neighbour_value
                        edges[(neighbour, x)] = 1/neighbour_value
                        graph[x].add(neighbour)
                        graph[neighbour].add(x)
                        queue.append((neighbour, neighbour_value))
            if not queue and y not in visited:
                return -1.0

        for query in queries:
            result.append(search_value(query, graph, edges))

        return result


# DFS solution
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Step 1. Build the Graph
        graph = collections.defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0 / val
        print(graph)

        # Step 2. DFS function
        def dfs(x, y, visited):
            # neither x not y exists
            if x not in graph or y not in graph:
                return -1.0

            # x points to y
            if y in graph[x]:
                return graph[x][y]

            # x maybe connected to y through other nodes
            # use dfs to see if there is a path from x to y
            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i, y, visited)
                    if temp == -1:
                        continue
                    else:
                        return graph[x][i] * temp
            return -1

        # go through each of the queries and find the value
        res = []
        for query in queries:
            res.append(dfs(query[0], query[1], set()))
        return res
