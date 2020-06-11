# Leetcode:207. Course Schedule

# Attempts: 1
# Completed: N
# Acheived Ideal: N

# Time Complexity:
# Space Complexity:

# Solving process:
# Problems Encountered:

# Other Solutions: Use DFS and a visited Hashtable. Mark visiting, and visited

# DFS and cycle detection
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        # create graph
        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)
        # visit each node
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True

    def dfs(self, graph, visited, i):
        # if ith node is marked as being visited, then a cycle is found
        if visited[i] == -1:
            return False
        # if it is done visted, then do not visit again
        if visited[i] == 1:
            return True
        # mark as being visited
        visited[i] = -1
        # visit all the neighbours
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        # after visit all the neighbours, mark it as done visited
        visited[i] = 1
        return True


# First Attempt. Does not work. Can get correct ans if no cycles
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edgegraph = {}
        checkcycle = {}
        for edge in prerequisites:
            n1, n2 = edge
            if (n2, n1) in checkcycle:
                numCourses += 1
            else:
                checkcycle[n1, n2] = edge

        print(prerequisites)
        for n1, n2 in prerequisites:
            if n1 in edgegraph:
                edgegraph[n1].append(n2)
            else:
                edgegraph[n1] = [n2]
        visited = {}
        stack = []
        print(edgegraph)
        for node in edgegraph.keys():
            if node in visited:
                continue
            else:
                self.topsort(edgegraph, node, visited, stack)
        print(stack)
        print(visited)
        return len(stack) >= numCourses

    def topsort(self, edgegraph, node, visited, stack):
        print(stack)
        print(visited)
        visited[node] = True
        if node in edgegraph:
            for edge in edgegraph[node]:
                if edge in visited:
                    continue
                else:
                    self.topsort(edgegraph, edge, visited, stack)

        stack.append(node)
