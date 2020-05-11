# Leetcode: 101 Symmetric Tree

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solving process:
# Problems Encountered:

# Other Solutions: Can also do iteratively in a queue with same complexity


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)

    def isMirror(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:  # When only one is null, we know its not symmetric
            return False
        return t1.val == t2.val and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)

# Definition for a binary tree node.

# First Attempt  - Tried to construct mirror pre-order traversals - works on VS code but not in leetcode


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        leftTreeArr = []
        rightTreeArr = []

        self.preOrderLeft(root.left, leftTreeArr)
        self.preOrderRight(root.right, rightTreeArr)
        print(leftTreeArr)
        print(rightTreeArr)

        if leftTreeArr == rightTreeArr:
            return True
        else:
            return False

    def preOrderLeft(self, root, arr):
        if root:
            arr.append(root.val)
            self.preOrderLeft(root.left, arr)
            self.preOrderLeft(root.right, arr)

    def preOrderRight(self, root, arr):
        if root:
            arr.append(root.val)
            self.preOrderRight(root.right, arr)
            self.preOrderRight(root.left, arr)


testTree = TreeNode(1)
testTree.left = TreeNode(2)
testTree.left.left = TreeNode(3)
testTree.left.right = TreeNode(None)

testTree.right = TreeNode(2)
testTree.right.left = TreeNode(None)
testTree.right.right = TreeNode(3)

testSolution = Solution()
print(testSolution.isSymmetric(testTree))
