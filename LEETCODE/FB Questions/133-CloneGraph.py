"""
Leetcode: 133 Clone Graph

Attempts: 1
Completed: Y
Acheived Ideal: Y but can also do a BFS 
Under 30 Mins: Y 

Time Complexity: O(n)
Space Complexity: O(n) hashtable and recursion stack

Pattern: Graph Traversal and Recursion
Technique: 

Problems Encountered:
Other Solutions: Can do it in BFS manner using a queue

"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""




from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        def deepClone(node, new_nodes):
            if not node:
                return None
            if node.val in new_nodes:
                return new_nodes[node.val]
            cloned_node = Node(node.val)
            new_nodes[node.val] = cloned_node
            if node.neighbors != []:
                for neighbor in node.neighbors:
                    if neighbor.val not in new_nodes:
                        new_nodes[neighbor.val] = deepClone(
                            neighbor, new_nodes)
                    cloned_node.neighbors.append(new_nodes[neighbor.val])
            return cloned_node
        new_nodes = {}
        return deepClone(node, new_nodes)


# BFS solution using a queue in lieu of the recursion stack


class Solution(object):

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return node

        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        visited = {}

        # Put the first node in the queue
        queue = deque([node])
        # Clone the node and put it in the visited dictionary.
        visited[node] = Node(node.val, [])

        # Start BFS traversal
        while queue:
            # Pop a node say "n" from the from the front of the queue.
            n = queue.popleft()
            # Iterate through all the neighbors of the node
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # Clone the neighbor and put in the visited, if not present already
                    visited[neighbor] = Node(neighbor.val, [])
                    # Add the newly encountered node to the queue.
                    queue.append(neighbor)
                # Add the clone of the neighbor to the neighbors of the clone node "n".
                visited[n].neighbors.append(visited[neighbor])

        # Return the clone of the node from visited.
        return visited[node]
