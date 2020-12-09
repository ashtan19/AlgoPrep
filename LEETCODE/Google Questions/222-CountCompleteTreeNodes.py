"""
Leetcode:222. Count Complete Tree Nodes

Attempts:1
Completed: Y
Acheived Ideal: N
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: Tree Traversal
Technique: Used BFS but not good O(N) space and time. 
            Better: Use Binary search to find the last node in the last level

Problems Encountered:
Other Solutions:

"""


# Binary Search Solution O(logN), Space O(1)
class Solution:
    def compute_depth(self, node):
        """
        Return tree depth in O(d) time.
        """
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, idx, d, node):
        """
        Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        Return True if last level node idx exists. 
        Binary search with O(d) complexity.
        """
        left, right = 0, 2**d - 1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None

    def countNodes(self, root):
        # if the tree is empty
        if not root:
            return 0

        d = self.compute_depth(root)
        # if the tree contains 1 node
        if d == 0:
            return 1

        # Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        # Perform binary search to check how many nodes exist.
        left, right = 1, 2**d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1

        # The tree contains 2**d - 1 nodes on the first (d - 1) levels
        # and left nodes on the last level.
        return (2**d - 1) + left

# Recursive Soln


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return 1 + self.countNodes(root.right) + self.countNodes(root.left) if root else 0

# BFS Solution (My Solution )
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        from collections import deque

        if root == None:
            return 0

        queue = deque()
        level_count = 1
        queue.append(root)
        result = 0

        while queue:
            level = len(queue)
            result += level
            if level != level_count:
                break
            for i in range(level):
                node = deque.popleft(queue)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_count = level_count * 2

        return result
