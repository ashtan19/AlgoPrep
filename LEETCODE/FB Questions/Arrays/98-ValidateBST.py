"""
Leetcode: 98. Validate Binary Search Tree

Attempts: 1
Completed: N
Acheived Ideal: N
Under 30 Mins: N

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: Recursion 
Technique: Pass the min and max values that a child node can have and check if it is in the range

Problems Encountered:
Other Solutions: Use a stack

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def isBST(root, l, r):
            if root == None:
                return True
            if root.val <= l or root.val >= r:
                return False
            return isBST(root.left, l, root.val) and isBST(root.right, root.val, r)

        left, right = -float("inf"), float("inf")

        return isBST(root, left, right)
