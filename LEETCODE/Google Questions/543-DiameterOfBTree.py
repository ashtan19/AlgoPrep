"""
Leetcode: 543. Diameter of Binary Tree

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(h)

Pattern: Tree   
Technique: 

Problems Encountered:
Other Solutions:

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def find_diameter(node):
            if not node:
                return (0, 0)

            max_diameter = 1

            left_max, left_branch = find_diameter(node.left)
            right_max, right_branch = find_diameter(node.right)

            max_diameter = max(left_branch + right_branch, left_max, right_max)

            return (max_diameter, max(left_branch, right_branch) + 1)

        d, b = find_diameter(root)
        return d
