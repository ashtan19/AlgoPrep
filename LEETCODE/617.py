# Leetcode: 617 Merge two binary trees

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solving process:
# Problems Encountered: 

# Other Solutions:

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        #BaseCase is when both nodes are null
        if t1 == None and t2 == None:
            return None
        if t1 == None: 
            return t2
        elif t2 == None: 
            return t1
        else: 
            leftchild = self.mergeTrees(t1.left, t2.left)
            rightchild = self.mergeTrees(t1.right, t2.right)
            t1.left = leftchild
            t1.right = rightchild
            t1.val = t1.val + t2.val
            return t1
            