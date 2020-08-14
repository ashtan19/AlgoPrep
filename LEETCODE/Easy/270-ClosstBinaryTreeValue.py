"""
Leetcode: 270. Closest Binary Search Tree Value

Attempts: 1
Completed: Y
Acheived Ideal: Y

Time Complexity: O(H)
Space Complexity: O(1)

Pattern: Binary Search
Technique: Keep the current closest num and its diff

Problems Encountered:
Other Solutions:

"""


'''
Given: 
    -Non Empty BT
    - Floating point target value => could be negative
Req:    Find the node value that is closest to the target

Process:

- Min Number and a min Difference
-  Start Min Diff of the root 
- If target < root => left child 
- If Target > root => right child
- Continue until target == root or root == None: 


'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        result = root.val
        resultDiff = float("inf")
        while root:
            diff = abs(float(root.val) - target)
            if diff < resultDiff:
                result = root.val
                resultDiff = diff
            if target < float(root.val):
                root = root.left
            elif target > float(root.val):
                root = root.right
            else:
                return root.val

        return result
