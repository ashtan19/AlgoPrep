# Leetcode: 437 Path Sum in BTree - Need to try again

# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Solving process:
# Problems Encountered: Did not know how to recurse while checking for sums

# Other Solutions: Need to Memoize


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.numPaths = 0

        self.dfs(root, sum)

        return self.numPaths

    def dfs(self, node, target):
        if node is None:
            return
        self.test(node, target)
        self.dfs(node.left, target)
        self.dfs(node.right, target)

    def test(self, node, target):
        if node is None:
            return
        if node.val == target:
            self.numPaths += 1
        self.test(node.left, target-node.val)
        self.test(node.right, target-node.val)
