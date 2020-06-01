# Leetcode: 226 Invert BTree

# Attempts: 2

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solving process:
# Problems Encountered:

# Other Solutions:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root

# Attempt 2


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.right, root.left = self.invertTree(
                root.left), self.invertTree(root.right)
        return root
