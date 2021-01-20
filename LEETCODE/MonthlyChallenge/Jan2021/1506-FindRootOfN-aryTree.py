"""
Leetcode:1506. Find Root of N-Ary Tree

Attempts: 1
Completed: Y
Acheived Ideal: N
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(n) but can be O(1)

Pattern: Tree
Technique: Hashtable to track in-degree/seen

Problems Encountered:
Other Solutions: Can do it in O(1) space. Since root will only be encountered once, 
                 we can add the node values when we see iterate and subtract the value
                when we see it as a child. the remaining value is the root node value

"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution(object):
    def findRoot(self, tree):
        """
        :type tree: List['Node']
        :rtype: 'Node'
        """

        table = {}

        for node in tree:
            if node not in table:
                table[node] = False
            for child in node.children:
                if child:
                    table[child] = True

        parent = None
        for node, status in table.items():
            if status == False:
                parent = node

        return parent

# O(1) space solution


class Solution(object):
    def findRoot(self, tree):
        """
        :type tree: List['Node']
        :rtype: 'Node'
        """

        value_sum = 0

        for node in tree:
            value_sum += node.val
            for child in node.children:
                if child:
                    value_sum -= child.val
        root = None
        for node in tree:
            if node.val == value_sum:
                root = node
                break

        return root
