"""
Leetcode: 124. Binary Tree Maximum Path Sum

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(N)
Space Complexity: O(H)

Pattern: Recursion
Technique: Keep track of the max sums of the left and right subtrees and compare it with the max path's

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def maxTreeSum(node):
            max_path, max_subtree_path = node.val, node.val
            left_path = 0
            right_path = 0
            if node.left:
                left_path, left_subtree_path = maxTreeSum(node.left)
                max_path = max(max_path, node.val + left_path)
                max_subtree_path = max(max_subtree_path, left_subtree_path)
            if node.right:
                right_path, right_subtree_path = maxTreeSum(node.right)
                max_path = max(max_path, node.val + right_path)
                max_subtree_path = max(max_subtree_path, right_subtree_path)
            max_subtree_path = max(
                max_subtree_path, left_path + right_path + node.val, max_path)

            return (max_path, max_subtree_path)

        max_path, max_subtree_path = maxTreeSum(root)
        return max_subtree_path
