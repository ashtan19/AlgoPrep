# Leetcode: 104 Max Depth of BTree

# Time Complexity: O(n)
# Space Complexity: 
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
    def maxDepth(self, root: TreeNode) -> int:
        if root == None: return 0
        
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        return max(leftMax, rightMax) +1