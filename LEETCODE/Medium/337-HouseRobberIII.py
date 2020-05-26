# Leetcode: 337. House Robber III


# Completed: Y
# Acheived Ideal: Y

# Time Complexity: O(n)
# Space Complexity: O(n)

# Solving process: Recursion and Memo
# Problems Encountered: Slow and solution is not clean

# Other Solutions: Decoupled Recursive Approach


# Cleaned up code of Recursion and Memo - Faster 36ms
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.hashtable = {}
        return self.maxrob(root)

    def maxrob(self, root):
        if root == None:
            return 0
        if not root.left and not root.right:
            return root.val
        if root in self.hashtable:
            return self.hashtable[root]
        else:
            sum = root.val
            if root.left:
                sum += self.maxrob(root.left.left) + \
                    self.maxrob(root.left.right)
            if root.right:
                sum += self.maxrob(root.right.left) + \
                    self.maxrob(root.right.right)
            self.hashtable[root] = max(sum, self.maxrob(
                root.left) + self.maxrob(root.right))
            return self.hashtable[root]

# Long Solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.hashtable = {}
        return self.maxrob(root)

    def maxrob(self, root):
        if root == None:
            return 0
        if not root.left and not root.right:
            return root.val
        if root in self.hashtable:
            return self.hashtable[root]
        else:
            sum = root.val
            if root.left:
                if root.left.left not in self.hashtable:
                    self.hashtable[root.left.left] = self.maxrob(
                        root.left.left)
                if root.left.right not in self.hashtable:
                    self.hashtable[root.left.right] = self.maxrob(
                        root.left.right)
                sum += self.hashtable[root.left.left] + \
                    self.hashtable[root.left.right]
            if root.right:
                if root.right.left not in self.hashtable:
                    self.hashtable[root.right.left] = self.maxrob(
                        root.right.left)
                if root.right.right not in self.hashtable:
                    self.hashtable[root.right.right] = self.maxrob(
                        root.right.right)
                sum += self.hashtable[root.right.left] + \
                    self.hashtable[root.right.right]
            self.hashtable[root] = max(sum, self.maxrob(
                root.left) + self.maxrob(root.right))
            return self.hashtable[root]
