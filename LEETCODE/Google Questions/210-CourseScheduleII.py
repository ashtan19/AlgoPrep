"""
Leetcode:210. Course Schedule II

Attempts:1
Completed: N
Acheived Ideal: Y
Under 30 Mins: N

Time Complexity: O(V+E)
Space Complexity: O(V+E)

Pattern: Topological Sort
Technique: Kahns Algorithm (BFS approach) => this approach checks for cycles as well

Problems Encountered:
Other Solutions: DFS approach is also possible and may be easier to implement but more work to check for cycles

"""


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict, deque

        nodes = set()
        adj = defaultdict(list)
        in_deg = [0 for i in range(numCourses)]
        queue = deque()
        result = []

        # Create ADJ matrix
        for course, pre in prerequisites:
            adj[pre].append(course)
            nodes.add(pre)
            in_deg[course] += 1

        # Push starting nodes into the queue
        for i in range(numCourses):
            if in_deg[i] == 0:
                queue.append(i)

        while queue:
            c = deque.popleft(queue)
            for req in adj[c]:
                in_deg[req] -= 1
                if in_deg[req] == 0:
                    queue.append(req)
            result.append(c)

        return result if numCourses == len(result) else []
