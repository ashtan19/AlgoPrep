"""
Leetcode: 938. Range Sum of BST

Attempts: 1
Completed: Y
Acheived Ideal: Y but not fast enough 

Time Complexity: O(R-L)
Space Complexity: O(H) -> Recursion stack 

Pattern: Binary Search 
Technique: 
        0) If null => return 
        1) check if node is >= L and node <= R
            - if yes add to sum
            - call recursive function on children
        2) if node < L: 
            - recursive on right child
        3) if node > R : 
            - recurse on left child 

Problems Encountered: Forgot to add root.val T.T
Other Solutions: Iterative Approach

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root == None: 
            return 0
        curSum = 0
        if root.val < L:
            curSum += self.rangeSumBST(root.right, L, R)
        elif root.val > R: 
            curSum += self.rangeSumBST(root.left, L, R)
        else: 
            curSum += root.val
            curSum += self.rangeSumBST(root.right, L, R)
            curSum += self.rangeSumBST(root.left, L, R)
        return curSum 


# Iterative Solution
class Solution(object):
    def rangeSumBST(self, root, L, R):
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return ans