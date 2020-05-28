# Leetcode: 114. Flatten Binary Tree to Linked List

# Completed: Y
# Acheived Ideal: Time Y but not good space

# Time Complexity: O(n^2)
# Space Complexity: O(n)

# Solving process:
# Problems Encountered:

# Other Solutions: Could use a stack but it would be space expensive as well


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        if root.left is None:
            return
        if root.right is None:
            root.right = root.left
            root.left = None
            return
        pointer = root.left
        while pointer.right != None:
            pointer = pointer.right
        pointer.right = root.right
        root.right = root.left
        root.left = None

        return


# Cleaner Solution but same process
def __init__(self):
    self.prev = None


def flatten(self, root):
    if not root:
        return None
    self.flatten(root.right)
    self.flatten(root.left)

    root.right = self.prev
    root.left = None
    self.prev = root
